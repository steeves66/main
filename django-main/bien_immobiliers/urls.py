
from django.contrib import admin 
from django.urls import path, include 
from .views import *


urlpatterns = [
    path('products/<type>/<filter>/', product_list, name='product_list'),
    path('product_details/<product_id>/', product_details, name='product_details'),
    path('test/', test),
]