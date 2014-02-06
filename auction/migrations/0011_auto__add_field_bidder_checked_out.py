# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Bidder.checked_out'
        db.add_column('auction_bidder', 'checked_out',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Bidder.checked_out'
        db.delete_column('auction_bidder', 'checked_out')


    models = {
        'auction.bidder': {
            'Meta': {'object_name': 'Bidder'},
            'checked_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'credit': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'})
        },
        'auction.item': {
            'Meta': {'object_name': 'Item'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fixed_price': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_quantity': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'unit_price': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        'auction.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'bidder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchases'", 'to': "orm['auction.Bidder']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchases'", 'to': "orm['auction.Item']"}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'unit_price': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        }
    }

    complete_apps = ['auction']