# myshop/coupons/forms.py
# Django modules
from django import forms

class CouponApplyForm(forms.Form):
    code = forms.CharField()