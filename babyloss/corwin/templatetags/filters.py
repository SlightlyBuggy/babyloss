
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter(needs_autoescape=True)
def spacify(text, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        def esc(x):
            return x

    return mark_safe(re.sub('  ', ' &' + 'nbsp', esc(text)))


spacify.needs_autoescape = True
register.filter(spacify)