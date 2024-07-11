from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django import dispatch
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import AuthenticationForm
from .middlewares import RequestMiddleware

from .models import Account
from .forms import UserRegistrationForm
from .utilitaires import create_token


def active_user(uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True
    
    
def create_user(data):
    form = UserRegistrationForm(data)
    # if form.is_valid():
    #     return user
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return user
    
    
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_service(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return True
        else:
            return False
    else:
         return False
                
                

def send_welcome_email(user):
    subject = 'Welcome to Our Site'
    message = f'Hi {user.username}, thank you for registering at our site.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    
    send_mail(subject, message, from_email, recipient_list)
    
    
@receiver(post_save, sender=Account)
def send_email_confirmation(sender, instance, created, **kwargs):
    if created:
        request = RequestMiddleware.get_request()
        current_site = get_current_site(request)
        
        uid, token = create_token(instance)
        
        print("----------------------- uid: "+ uid)
        print("----------------------- token: "+ token)
        email_context = {
            'user': instance,
            'uid': uid,
            'token': token,
            'current_site': current_site
        }
        email_subject = "Chez Laurent: Activation de votre compte"
        email_html_message = render_to_string('users/emails/register_user_verification_email.html', email_context)
        email_text_message = strip_tags(email_html_message)
        to_email = instance.email
        email = EmailMultiAlternatives(email_subject, email_text_message, to=[to_email])
        email.attach_alternative(email_html_message, "text/html")
        email.content_subtype = "html"  # Main content is now 
        email.send()
        print("******************************************************")
        print("email sended")
        print("******************************************************")
        return True


# @receiver(email_validated)
# def send_email_on_validation(sender, email, **kwargs):
#     subject = 'Validation de l\'email'
#     message = f"""
#     Bonjour,
#
#     Votre adresse e-mail {email} a été validée avec succès.
#
#     Merci de vous être inscrit(e) sur notre site. Si vous avez des questions, n'hésitez pas à nous contacter.
#
#     Cordialement,
#     L'équipe de support
#     """
#     send_mail(
#         subject,
#         message,
#         'votre-email@example.com',
#         [email],
#         fail_silently=False,
#     )


    
    
    
    
    
    
    
    
    
    
    
    
    