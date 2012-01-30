from django import template

register = template.Library()

@register.filter(name='chars')
def chars(value, num):
    value = value.lower()
    if len(value) > num:
        return (value[0:num-3] + '...')
    else:
        return value
