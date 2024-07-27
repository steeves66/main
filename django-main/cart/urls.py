
from django.contrib import admin 
from django.urls import path, include 
from .views import *


urlpatterns = [
    
    path('', cart, name='cart'),
    path('add_cart/<product_id>/', add_cart, name='add_cart')
]