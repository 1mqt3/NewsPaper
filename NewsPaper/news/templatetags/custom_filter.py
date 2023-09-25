from django import template

register = template.Library()

@register.filter()
def censor(value):
    censored_value = value.replace("едис", "****")
    return censored_value