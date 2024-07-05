from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, 'Thank you for registering with us. We have sent you a verification email to your email address. Please verify it.')
            #return redirect('/accounts/login/?command=verification&email='+email)
            return redirect('/home')
    return redirect('/home') 