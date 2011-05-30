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

@register.simple_tag
def VK_API_ID():
    return settings.VK_API_ID


@register.inclusion_tag('book/b_chapters.html')
def navigation(current_chapter):
    chapters = list(Chapter.objects.all())
    chapters[4].padding = True
    chapters[8].padding = True
    return {'chapters': chapters, 'current_chapter': current_chapter}


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
