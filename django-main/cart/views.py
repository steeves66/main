from django.shortcuts import render
from bien_immobiliers.models import Bien
from .models import Cart, CartItem

# Create your views here.


def cart(request):
    return render(request, 'cart/cart.html')


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
   

def add_cart(request, bien_id):
    bien = Bien.objects.get(id=bien_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()
    
    try:
        cart_item = CartItem.objects.get(bien=bien, cart=cart)
        cart_item.quantity += 1
        cart_item = save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        