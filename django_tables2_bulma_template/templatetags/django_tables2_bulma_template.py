from django import template

register = template.Library()

@register.simple_tag()
def is_descending(obj):
    import django_tables2
    if obj is not None:
        if type(obj) == django_tables2.utils.OrderByTuple:
            return obj[0].is_descending
            if len(obj) > 0:
                if obj[0] == "-":
                    return True

    return False
