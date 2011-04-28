# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        
        db.execute("INSERT INTO django_flatpage SET url='/', title='Index', content='', template_name='flatpages/index.html', enable_comments=0, registration_required=0")
        db.execute("INSERT INTO django_flatpage_sites VALUES (NULL, 1, 1)")
        db.execute("INSERT INTO django_flatpage SET url='/book/', title='Book', content='', template_name='flatpages/book.html', enable_comments=0, registration_required=0")
        db.execute("INSERT INTO django_flatpage_sites VALUES (NULL, 2, 1)")


    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'core.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.paragraph': {
            'Meta': {'ordering': "('chapter', 'order')", 'object_name': 'Paragraph'},
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Chapter']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['core']
