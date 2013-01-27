from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Bidder(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

    def purchase_total(self):
        return sum(map(lambda x: x.unit_price * x.quantity, self.purchases.all()))

    def get_absolute_url(self):
        return reverse('bidder', args=(self.id,))

class Item(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    unit_price = models.FloatField(null=True)
    max_quantity = models.IntegerField(default=-1)
    fixed_price = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

    def get_absolute_url(self):
        return reverse('item', args=(self.id,))
        
    def quantity_sold(self):
        return sum(map(lambda p: p.quantity, self.purchases.all()))

    def quantity_remaining(self):
        if self.max_quantity == -1:
            return -1
        return max(0, self.max_quantity - self.quantity_sold())

    def quantity_remaining_str(self):
        qr = self.quantity_remaining()
        return 'unlimited' if qr == -1 else "%s / %s" % (qr, self.max_quantity)

class Purchase(models.Model):
    bidder = models.ForeignKey(Bidder, related_name='purchases')
    item = models.ForeignKey(Item, related_name='purchases')
    quantity = models.IntegerField(default=1)
    unit_price = models.FloatField(null=True)
    paid = models.BooleanField(default=False)
