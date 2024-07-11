# myapp/signals.py
from django.dispatch import Signal
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

reset_password_signal = Signal()


def send_reset_password_email(sender, **kwargs):
    request = RequestMiddleware.get_request()
    current_site = get_current_site(request)
    
    user = Account.objects.filter(email=kwargs['email']).first()    
   
    uid, token = create_token(instance)
        
    print("----------------------- uid: "+ uid)
    print("----------------------- token: "+ token)
    email_context = {
        'user': instance,
        'uid': uid,
        'token': token,
        'current_site': current_site
    }
    email_subject = "Chez Laurent: Changement de votre compte"
    email_html_message = render_to_string('users/emails/user_password_reset_email.html', email_context)
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

reset_password_signal.connect(send_reset_password_email)
    
























