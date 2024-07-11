
from django.contrib import admin 
from django.urls import path, include 
from .views import *

from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)



urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('register-success/', registration_success, name='registration_success'),
    path('activate/<uidb64>/<token>/', activate_user, name='activate_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    # path('password_reset/', password_reset, name='password_reset'),
    # path('password_reset_done/<uidb64>/<token>/', password_reset_done, name='password_reset_done'),
    # path('password_change/', password_change, name='password_change')
    
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_page.html'),name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done_page.html'),name='password_reset_done'),
]
