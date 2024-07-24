from django.shortcuts import render, redirect
from bien_immobiliers.models import Bien
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        quantity = cart_items.count()
        total = quantity * 1000
    except ObjectDoesNotExist():
        pass
            
    context = {
        'quantity': quantity,
        'total': total,
        'cart_items': cart_items
    }
    return render(request, 'cart/cart.html', context)


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
   

def add_cart(request, id):
    bien = Bien.objects.get(id=id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()
    
    try:
        cart_item = CartItem.objects.get(bien=bien, cart=cart)
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            bien = bien,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')
        
        