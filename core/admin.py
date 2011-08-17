# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('id', 'chapter', 'order')
    ordering = ('id',)
    search_fields = ('content',)

admin.site.register(Chapter)
admin.site.register(Paragraph, ParagraphAdmin)