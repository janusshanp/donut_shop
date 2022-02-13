from django.forms import ModelForm
from .models import Delivery_Address

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
        
