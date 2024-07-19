
from django.contrib import admin 
from django.urls import path, include 
from .views import *


urlpatterns = [
    
    path('product_by/<action>/', product_list, name='product_list'),
    path('product_details/<id>/', product_details, name='product_details')
]