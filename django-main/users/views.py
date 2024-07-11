from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .models import Account
from .forms import UserRegistrationForm, PasswordChangeForm
from .services import create_user, active_user, login_service
from .signals import reset_password_signal
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


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in .')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login_user')
    return render(request, 'users/login_user_page.html')



def logout_user(request):
    logout(request)
    return redirect('home')



import pdb
from .forms import ResetUserPasswordForm

def password_reset(request):
    if request.method == "POST":
        form = ResetUserPasswordForm(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
            print(f"************* {email}******************")
            pdb.set_trace()
            reset_password_signal.send(sender=None, email=email)
            # update_session_auth_hash(request, form.user)
            messages.success(request, 'change password link send to your email')
            return render(request, 'users/password_reset_page.html', {'form': form})
        else:
            # return HttpResponse('OK')
            return render(request, 'test.html')
            # return render(request, 'users/password_reset_page.html', {'form': form})
    else:
        form = ResetUserPasswordForm()
        return render(request, 'users/password_reset_page.html', {form: form})


def password_reset_done(request, uidb64, token):
    redirect('password_change')


def password_change(request):
    if request.method == "POST":
        pass
        form = PasswordChangeForm(data=request.POST)
        if form.is_valid():
            pass
        #     reset_password_signal.send(sender=None, email=email)
        #     update_session_auth_hash(request, form.user)
        #     messages.success(request, 'change password link send to your email')
        #     return render(request, 'users/password_reset_page.html', {'form': form})
        # else:
        #     return render(request, 'users/password_reset_page.html', {'form': form})
    else:
        form = ()
        return render(request, 'users/password_reset_page.html', {form: form})















