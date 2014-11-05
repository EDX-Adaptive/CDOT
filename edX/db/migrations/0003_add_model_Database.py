# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Database'
        db.create_table(u'db_database', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('engine', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('port', self.gf('django.db.models.fields.IntegerField')(max_length=8)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'db', ['Database'])


    def backwards(self, orm):
        # Deleting model 'Database'
        db.delete_table(u'db_database')


    models = {
        u'db.database': {
            'Meta': {'object_name': 'Database'},
            'engine': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'port': ('django.db.models.fields.IntegerField', [], {'max_length': '8'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['db']