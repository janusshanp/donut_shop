from django.forms import ModelForm
from django import forms
from .models import *

class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery_Address
        fields = [
            'email',
            'address',
            'apartment',
            'city',
            'country',
            'Province',
            'postal_code' 
        ]
