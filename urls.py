# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/(.*)', admin.site.root, name="admin"),
    (r'^book', include('core.urls')),
)

