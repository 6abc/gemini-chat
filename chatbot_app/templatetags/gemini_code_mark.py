import markdown

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def gemini_code_mark(value):
  return markdown.markdown(value, extensions=['markdown.extensions.codehilite','markdown.extensions.fenced_code'])