# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

    
class GenericManager(models.Manager):
    """
    Filters query set with given selectors
    """
    def __init__(self, **kwargs):
        super( GenericManager, self ).__init__()
        self.selectors = kwargs

    def get_query_set(self):
        return super( GenericManager, self ).get_query_set().filter( **self.selectors )


class Chapter(models.Model):
    title = models.CharField(verbose_name=u"Название", max_length=200)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('chapter', args=[self.pk])
        
    class Meta:
        verbose_name = u"Глава"
        verbose_name_plural = u"Главы"


class Paragraph(models.Model):
    chapter = models.ForeignKey(Chapter, verbose_name=u"Глава")
    order = models.IntegerField(default=100, verbose_name=u"Порядок")
    content = models.TextField(verbose_name=u"Содержание")

    def __unicode__(self):
        return u"%s: параграф %s" % (self.chapter.title, self.order)

    def get_absolute_url(self):
        return reverse('paragraph', args=[self.chapter_id, self.pk])        
   
    class Meta:
        verbose_name = u"Параграф"
        verbose_name_plural = u"Параграфы"
        ordering = ('chapter', 'order',)