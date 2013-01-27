# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.fixed_price'
        db.add_column('auction_item', 'fixed_price',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.fixed_price'
        db.delete_column('auction_item', 'fixed_price')


    models = {
        'auction.bidder': {
            'Meta': {'object_name': 'Bidder'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'auction.item': {
            'Meta': {'object_name': 'Item'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fixed_price': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_quantity': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'unit_price': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        'auction.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'bidder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchases'", 'to': "orm['auction.Bidder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auction.Item']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'unit_price': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        }
    }

    complete_apps = ['auction']