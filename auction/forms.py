from django import forms

from models import Item, Bidder

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('deleted')

class BidderForm(forms.ModelForm):
    class Meta:
        model = Bidder
        exclude = ('deleted')

class PurchaseForm(forms.Form):
    bidder = forms.ModelChoiceField(queryset=Bidder.objects.order_by('name'))
    unit_price = forms.FloatField(required=False) 
    quantity = forms.IntegerField(initial=1)

    def __init__(self, *args, **kwargs):
        hide_price = kwargs.pop('hide_price', False)
        super(PurchaseForm, self).__init__(*args, **kwargs)
        if hide_price:
            del self.fields['unit_price']
     
class CheckoutForm(forms.Form):
    email = forms.CharField()
