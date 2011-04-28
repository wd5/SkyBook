# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.views import password_reset

from views import *

urlpatterns = patterns('core.views',       
    url(r'^(?P<chapter_id>\d+)/$', chapter, name='chapter'),
    url(r'^(?P<chapter_id>\d+)/(?P<paragraph_id>\d+)/$', paragraph, name='paragraph'),
    )