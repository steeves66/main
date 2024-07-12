
from django.contrib import admin 
from django.urls import path, include 
from .views import *
from .views import forgot_password


urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('register-success/', registration_success, name='registration_success'),
    path('activate/<uidb64>/<token>/', activate_user, name='activate_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    
    # path('password_reset/', password_reset, name='password_reset'),
    # path('password_reset_done/<uidb64>/<token>/', password_reset_done, name='password_reset_done'),
    # path('password_change/', password_change, name='password_change')
]
