from django import forms
from .models import Account


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField()

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'phone_number', 'email', 'password']
        
        def save(self, request):
            user = Account()
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.username = self.cleaned_data['username'],
            user.phone_number = self.cleaned_data['phone_number'],
            user.email = self.cleaned_data['email'],
            
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])
            
            # user.set_password(password)
            # user.password = make_password(self.cleaned_data['password'])
            # user.save(commit=False)
            
            user.is_active = False
            user.save()
            return user