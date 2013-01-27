# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bidder'
        db.create_table('auction_bidder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('auction', ['Bidder'])

        # Adding model 'Item'
        db.create_table('auction_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('unit_price', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('auction', ['Item'])

        # Adding model 'Purchase'
        db.create_table('auction_purchase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bidder', self.gf('django.db.models.fields.related.ForeignKey')(related_name='purchases', to=orm['auction.Bidder'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auction.Item'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('auction', ['Purchase'])


    def backwards(self, orm):
        # Deleting model 'Bidder'
        db.delete_table('auction_bidder')

        # Deleting model 'Item'
        db.delete_table('auction_item')

        # Deleting model 'Purchase'
        db.delete_table('auction_purchase')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'unit_price': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        'auction.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'bidder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchases'", 'to': "orm['auction.Bidder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auction.Item']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['auction']