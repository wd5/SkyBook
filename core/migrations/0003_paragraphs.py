# encoding: utf-8
import datetime
import os
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        
        path = os.path.join(os.path.dirname(__file__), 'data')
        for n in xrange(1, 12):
            content = open(os.path.join(path, '%s.txt' % n)).read()
            chapter = orm.Chapter.objects.get(pk=n)
            order = 1
            for paragraph in content.split('---'):
                orm.Paragraph.objects.create(chapter=chapter,
                                             order=order,
                                             content=paragraph.strip()
                                             )
                order += 1    


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
