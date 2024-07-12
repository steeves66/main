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

# def password_reset(request):
#     if request.method == "POST":
#         form = ResetUserPasswordForm(data=request.POST)
#         if form.is_valid():
#             email = request.POST['email']
#             print(f"************* {email}******************")
#             pdb.set_trace()
#             reset_password_signal.send(sender=None, email=email)
#             # update_session_auth_hash(request, form.user)
#             messages.success(request, 'change password link send to your email')
#             return render(request, 'users/password_reset_page.html', {'form': form})
#         else:
#             # return HttpResponse('OK')
#             return render(request, 'test.html')
#             # return render(request, 'users/password_reset_page.html', {'form': form})
#     else:
#         form = ResetUserPasswordForm()
#         return render(request, 'users/password_reset_page.html', {form: form})


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            #Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('login')

    return render(request, 'accounts/forgotPassword.html')


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















