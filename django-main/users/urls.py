
from django.contrib import admin 
from django.urls import path, include 
from .views import *


urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('register-success/', registration_success, name='registration_success'),
    path('activate/<uidb64>/<token>/', activate_user, name='activate_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    
    path('password_reset/', password_reset, name='password_reset'),
    path('resetpassword_validate/<uidb64>/<token>/', reset_password_validate, name='reset_password_validate'),
    path('change_password/', change_password, name='change_password'),
    # path('password_change/', password_change, name='password_change')
]
