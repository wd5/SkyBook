# -*- coding: utf-8 -*-

from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def MEDIA_URL():
    return settings.MEDIA_URL