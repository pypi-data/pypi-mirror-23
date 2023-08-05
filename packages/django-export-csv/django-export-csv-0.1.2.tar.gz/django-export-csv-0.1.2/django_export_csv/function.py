import datetime
import unicodecsv as csv
import codecs

from django.http import StreamingHttpResponse

from .utils import generate_filename, attach_datestamp, clean_filename, get_uncontain_field_names
from .utils import Echo


def render_csv_response(queryset, filename=None, add_datestamp=False, **kwargs):
    """
    entry function, making a CSV streaming http response, take a queryset
    """
    if filename:
        filename = clean_filename(filename)
        if add_datestamp:
            filename = attach_datestamp(filename)
    else:
        filename = generate_filename(queryset, add_datestamp)

    response_args = {'content_type': 'text/csv'}

    response = StreamingHttpResponse(
        _iter_csv(queryset, Echo(), **kwargs), **response_args)

    # support chinese filename
    response['Content-Disposition'] = b'attachment; filename=%s;' % filename.encode(encoding='utf-8')
    response['Cache-Control'] = 'no-cache'

    return response


def _iter_csv(queryset, file_obj, **kwargs):
    """
    Writes CSV data to a file object based on the
    contents of the queryset and yields each row.
    """
    csv_kwargs = {'encoding': 'utf-8'}

    # add BOM to support MS Excel (for Windows only)
    yield file_obj.write(codecs.BOM_UTF8)

    if type(queryset).__name__ == 'ValuesQuerySet':
        queryset_values = queryset
    else:
        queryset_values = queryset.values()

    fields = kwargs.get('fields', [])
    exclude = kwargs.get('exclude', [])
    extra_field = kwargs.get('extra_field', [])

    if fields:
        uncontain_field_names = get_uncontain_field_names(
            fields, queryset_values.field_names
        )
        if uncontain_field_names:
            raise Exception(','.join(uncontain_field_names) + " aren't in default field names")

        field_names = fields
    elif exclude:
        field_names = [
            field_name
            for field_name in queryset_values.field_names
            if field_name not in exclude
        ]
    else:
        field_names = queryset_values.field_names

    field_names += extra_field

    field_order = kwargs.get('field_order', [])

    if field_order:
        field_names = [field_name for field_name in field_names if field_name in field_order] + \
                      [field_name for field_name in field_names if field_name not in field_order]

    # support extra
    # Sometimes, the Django query syntax by itself can't easily express a complex WHERE clause.
    # For these edge cases, Django provides the extra() QuerySet modifier
    # a hook for injecting specific clauses into the SQL generated by a QuerySet.
    extra_columns = list(queryset_values.query.extra_select)
    if extra_columns:
        field_names += extra_columns

    # support annotate
    # Annotates each object in the QuerySet with the provided list of query expressions.
    # An expression may be a simple value, a reference to a field on the model (or any related models),
    # or an aggregate expression (averages, sums, etc) that
    # has been computed over the objects that are related to the objects in the QuerySet.
    annotation_columns = list(queryset_values.query.annotation_select)
    if annotation_columns:
        field_names += annotation_columns

    writer = csv.DictWriter(file_obj, field_names, **csv_kwargs)

    header_map = dict((field, field) for field in field_names)

    use_verbose_names = kwargs.get('use_verbose_names', True)

    if use_verbose_names:
        for field in queryset.model._meta.get_fields():
            if field.name in field_names:
                try:
                    header_map[field.name] = field.verbose_name
                except AttributeError:
                    header_map[field.name] = field.name

    header_map.update(kwargs.get('field_header_map', {}))

    yield writer.writerow(header_map)

    if extra_field:
        model = queryset_values.model
        for item in queryset_values:
            item = _sanitize_related_item(item, model, **kwargs)
            item = _sanitize_item(item, **kwargs)
            yield writer.writerow(item)
    else:
        for item in queryset_values:
            item = _sanitize_item(item, **kwargs)
            yield writer.writerow(item)


def _sanitize_item(item, **kwargs):
    def _serialize_value(value):
        if isinstance(value, datetime.datetime):
            return value.isoformat()
        else:
            return str(value)

    obj = {}
    field_names = kwargs.get('field_names', [])
    exclude = kwargs.get('exclude', [])
    extra_field = kwargs.get('extra_field', [])
    field_serializer_map = kwargs.get('field_serializer_map', {})

    for key, val in item.items():
        if key in exclude:
            continue
        if key in field_names or key in extra_field:
            if key in extra_field:
                obj[key] = val
                continue
            if val is not None:
                serializer = field_serializer_map.get(key, _serialize_value)
                newval = serializer(val)
                if not isinstance(newval, str):
                    newval = str(newval)
                obj[key] = newval
    return obj


def _sanitize_related_item(item, model, **kwargs):
    obj = model.objects.get(id=item['id'])
    extra_field = kwargs.get('extra_field', [])
    field_serializer_map = kwargs.get('field_serializer_map', {})

    for field_name in extra_field:
        serializer = field_serializer_map.get(field_name)
        item[field_name] = serializer(obj)
    return item