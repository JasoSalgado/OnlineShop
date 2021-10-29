# myshop/orders/urls.py
# Django modules
from django.urls import path
# My modules
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]
