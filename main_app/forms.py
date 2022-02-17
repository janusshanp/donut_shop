from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
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

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name= forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')