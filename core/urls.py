# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.views import password_reset

from views import *

urlpatterns = patterns('',    
   
    url(r'^(?P<chapter>\d+)/$', chapter, name='chapter'),
    url(r'^(?P<chapter>\d+)/(?P<paragraph>\d+)', paragraph, name='paragraph'),
    )