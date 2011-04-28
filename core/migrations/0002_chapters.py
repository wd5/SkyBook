# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        
        numbers = [u'первой', u'второй', u'третьей', u'четвертой', 
                   u'пятой', u'шестой', u'седьмой', u'восьмой', 
                   u'девятой', u'десятой', u'одиннадцатой']
        
        for n in xrange(1, 12):
            orm.Chapter.objects.create(id=n, title=u"Из книги %s" % numbers[n-1])


    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'core.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.paragraph': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Paragraph'},
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Chapter']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['core']
