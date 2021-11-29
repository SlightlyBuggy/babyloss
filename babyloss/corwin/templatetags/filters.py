
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = template.Library()

LINK_START_DELIM = '['
LINK_END_DELIM = ']'


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


@register.filter(needs_autoescape=False)
def db_links_to_html(text, autoescape=False):

    link_pattern = re.compile('(\\[link ".+" http.*?\\])')
    link_matches = link_pattern.findall(text)

    for link_match in link_matches:
        link_spl = link_match.replace(LINK_START_DELIM, '').replace(LINK_END_DELIM, '').split('"')
        new_link_text = mark_safe('<a href="{0}" target="_blank">{1}</a>'.format(link_spl[2], link_spl[1].replace('"', '')))
        text = text.replace(link_match, new_link_text)

    return mark_safe(text)


db_links_to_html.needs_autoescape = True
register.filter(db_links_to_html)