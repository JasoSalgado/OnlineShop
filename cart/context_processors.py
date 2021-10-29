# myshop/cart/context_processors.py
# Django modules

# my modules
from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}