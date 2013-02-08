from django.core.urlresolvers import reverse
from django.db import models

class NonDeletedManager(models.Manager):
    def get_query_set(self):
        return super(NonDeletedManager, self).get_query_set().filter(deleted=False)

class DeletedManager(models.Manager):
    def get_query_set(self):
        return super(DeletedManager, self).get_query_set().filter(deleted=True)

# Create your models here.
class Bidder(models.Model):
    objects = NonDeletedManager() # Custom manager only returns non deleted items
    deleted_objects = DeletedManager() # Extra manager to get deleted objects

    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, blank=True)
    email = models.CharField(max_length=100, blank=True)
    credit = models.FloatField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

    def purchase_total(self):
        return sum(map(lambda x: x.unit_price * x.quantity, self.purchases.all())) - (self.credit or 0)

    def get_absolute_url(self):
        return reverse('bidder', args=(self.id,))

    @classmethod
    def search(cls, query=None):
        if query:
            return cls.objects.filter(models.Q(code__icontains=query) | models.Q(name__icontains=query)).order_by('code')
        else:
            return cls.objects.order_by('code')

class Item(models.Model):
    objects = NonDeletedManager() # Custom manager only returns non deleted items
    deleted_objects = DeletedManager() # Extra manager to get deleted objects

    code = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    unit_price = models.FloatField(null=True, help_text="For non fixed-price items, this is the fair market price")
    max_quantity = models.IntegerField(default=-1, help_text="Maximum number to be sold, -1 means unlimited")
    fixed_price = models.BooleanField(default=False, help_text="If price is fixed, all buyers will get same price")
    description = models.TextField(blank=True)
    deleted = models.BooleanField(default=False)

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

    @classmethod
    def search(cls, query=None):
        if query and query != '':
            return cls.objects.filter(models.Q(code__icontains=query) | models.Q(description__icontains=query) | models.Q(name__icontains=query)).order_by('code')
        else:
            return cls.objects.order_by('code')

class Purchase(models.Model):
    objects = NonDeletedManager() # Custom manager only returns non deleted items
    deleted_objects = DeletedManager() # Extra manager to get deleted objects

    bidder = models.ForeignKey(Bidder, related_name='purchases')
    item = models.ForeignKey(Item, related_name='purchases')
    quantity = models.IntegerField(default=1)
    unit_price = models.FloatField(null=True)
    paid = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('purchase', args=(self.bidder_id, self.id))
        
