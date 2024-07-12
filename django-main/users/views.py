from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

from .models import Account
from .forms import UserRegistrationForm, PasswordChangeForm
from .services import create_user, active_user, login_service, send_email_service
from .signals import reset_password_signal
from django.core.mail.message import EmailMessage
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


def password_reset(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            #Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('users/emails/user_password_reset_email.html', {
                'user': user,
                'current_site': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return render(request, 'users/password_reset_page.html')
        else:
            messages.error(request, 'Account does not exist!')
            return render(request, 'users/password_reset_page.html')

    return render(request, 'users/password_reset_page.html')



def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('change_password')
        # return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('password_reset')
    
    

# def resetPassword(request):
#     if request.method == 'POST':
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#
#         if password == confirm_password:
#             uid = request.session.get('uid')
#             user = Account.objects.get(pk=uid)
#             user.set_password(password)
#             user.save()
#             messages.success(request, 'Password reset successful')
#             return redirect('home')
#         else:
#             messages.error(request, 'Password do not match!')
#             return redirect('resetPassword')
#     else:
#         return render(request, 'accounts/resetPassword.html')




    
def change_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('home')
        else:
            messages.error(request, 'Password do not match!')
            return render(request, 'users/change_password_page.html')
    else:
        return render(request, 'users/change_password_page.html')












