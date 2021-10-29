# myshop/orders/forms.py
# Djando modules
from django import forms
# My modules
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city']
                    