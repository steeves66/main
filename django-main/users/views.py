from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserRegistrationForm
from .services import create_user, active_user
from .models import Account
from django.contrib import messages

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        result = create_user(request.POST)
        if isinstance(result, dict):  # If result is the form with errors
            return render(request, 'users/register_user_page.html', {'form': result})
        return redirect('registration_success')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register_user_page.html', {'form': form})


def registration_success(request):
    return render(request, 'users/verification_email_sended_page.html')


def activate_user(request, uidb64, token):
    active_user(uidb64, token)
    messages.success(request, 'Congratulations! Your account is activated.')
    return redirect('home')

# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('home')  # Redirect to a success page.
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})
