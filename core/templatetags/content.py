# -*- coding: utf-8 -*-
import re

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from core.models import Chapter

register = template.Library()

@register.simple_tag
def MEDIA_URL():
    return settings.MEDIA_URL


@register.inclusion_tag('b_chapters.html')
def navigation(current_chapter):
    return {'chapters': Chapter.objects.all(), 'current_chapter': current_chapter}


@register.filter
def linked_content(paragraph):
    content = paragraph.content
    first, other = content.split('.', 1)
    if len(first) > 60:
        first, separator, other = re.split('([:.,])', content, 1)
        other = separator + other
    else:
        other = u'.' + other
    return mark_safe(u'<a href="%s">%s</a>%s' % (paragraph.get_absolute_url(), first, other))
    