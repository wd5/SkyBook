# encoding: utf-8
import os
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."

        comments = open(os.path.join(os.path.dirname(__file__), 'data', 'comments.txt'))
        for comment in comments:            
            code, text = comment.strip().decode('utf8').split('.', 1)
            for paragraph in orm.Paragraph.objects.filter(content__contains=code):
                paragraph.content = paragraph.content.replace(u"((%s))" % code, 
                                        u'''<span class="comment-link js-comment-link" data-comment="%s">*</span>
                                        <span id="comment_%s" class="comment js-comment">%s</span>''' 
                                        % (paragraph.pk, paragraph.pk, text.strip())
                )
                paragraph.save()
        

    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'core.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.paragraph': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Paragraph'},
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Chapter']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['core']
