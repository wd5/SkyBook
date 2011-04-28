# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Chapter'
        db.create_table('core_chapter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('core', ['Chapter'])

        # Adding model 'Paragraph'
        db.create_table('core_paragraph', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chapter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Chapter'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Paragraph'])


    def backwards(self, orm):
        
        # Deleting model 'Chapter'
        db.delete_table('core_chapter')

        # Deleting model 'Paragraph'
        db.delete_table('core_paragraph')


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
