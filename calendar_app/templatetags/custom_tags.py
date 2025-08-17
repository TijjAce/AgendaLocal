from django import template

register = template.Library()

@register.filter
def to(start, end):
    return range(start, end)

@register.filter
def mul(value, arg):
    try:
        return int(value) * int(arg)
    except:
        return ''