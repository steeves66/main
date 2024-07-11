from django import forms
from .models import Account
from django.forms.fields import CharField, EmailField


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField()

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'phone_number', 'email', 'password']

        def clean_email(self):
            email = self.cleaned_data['email']
            """ if email is None:
                raise forms.ValidationError('Vous devez avoir un email, veuillez saisir un email') """
            user = Accounts.objects.filter(email= email).exists()
            if(user):
                raise forms.ValidationError('Cet email est utilisé, veuillez saisir un email non utilisé.')
            regex = '^[a-z0-9]+[\.-_]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if not (re.fullmatch(regex, email)):
                raise forms.ValidationError("Votre email n'a pas le bon format, veuillez saisir un email valide")
            return email
        
        def clean_username(self):
            username = self.cleaned_data['username']
            user_name = Accounts.objects.filter(username=username).exists()
            if user_name:
                raise forms.ValidationError('Ce surnom est utilisé, veuillez saisir un surnom non utilisé.')
            if len(username) < 3:
                raise forms.ValidationError('Votre surnom doir contenir au moins 3 caractères.')
            return username
        
        def clean_phone_numbers(self):
            phone_numbers = self.cleaned_data['phone_numbers']
            if len(phone_numbers) < 10:
                raise forms.ValidationError('Votre numero doit être ne doit pas inferieur à 10 chiffres')
            if len(phone_numbers) > 15:
                raise forms.ValidationError('Votre numero doit être ne doit pas superieur à 15 chiffres')
            regex = '^[0-9]{10,15}$'
            if not (re.fullmatch(regex, phone_numbers)):
                raise forms.ValidationError('Le numero ne doit pas contenir des lettres')
            return phone_numbers
        
        def clean(self):
            password = self.cleaned_data.get('password')
            confirm_password = self.cleaned_data.get('confirm_password')
            
            if password and len(password) < 8:
                self.add_error('password', 'Votre mot de passe doit avoir au moins 8 caractères')
                
            if confirm_password and len(confirm_password) < 8:
                self.add_error('confirm_password', 'Votre mot de passe doit avoir au moins 8 caractères')
                
            if(password != confirm_password):
                raise forms.ValidationError('Votre mot de passe et sa confirmation ne correspondent pas')
            
        # def save(self, commit=True):
        #     user = Account()
        #     user.first_name = self.cleaned_data['first_name']
        #     user.last_name = self.cleaned_data['last_name']
        #     user.username = self.cleaned_data['username'],
        #     user.phone_number = self.cleaned_data['phone_number'],
        #     user.email = self.cleaned_data['email'],
        #
        #     user = super().save(commit=False)
        #     user.set_password(self.cleaned_data["password"])
        #     print("########################################")
        #     print(" password hashed")
        #     print("########################################")
        #     user.is_active = False
        #     user.save()
        #     return user
        
        
            
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = ('email', 'password')
#
#     def clean(self):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#
#         if not email and not password:
#             self.add_error('email', "L'email ne doit pas être vide")  
#             self.add_error('password', "Le mot de passe ne doit pas être vide")
#         if email and not password:
#             user = Accounts.objects.filter(email=email).first()
#             if not user:
#                 self.add_error('email', "L'email est incorrect")  
#                 self.add_error('password', "Le mot de passe ne doit pas être vide")
#             else:
#                 self.add_error('password', "Le mot de passe ne doit pas être vide")
#         if email and password:
#             user = Accounts.objects.filter(email=email).first()
#             if not user:
#                 self.add_error('email', "L'email est incorrect")
#             else: 
#                 if not user.check_password(password):
#                     self.add_error('password', "Mot de passe incorrect")
#         if not email and password:
#             self.add_error('email', "L'email ne doit pas être vide")  
#
from django.core.validators import validate_email
            
class ResetUserPasswordForm(forms.Form):
    email = forms.EmailField()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not Account.objects.filter(email="email").first():
            self.add_error('email', "Cet email n'existe pas")  
        return email
            
class PasswordChangeForm(forms.Form): 
    password = forms.CharField()
    confirm_password = forms.CharField()   
    
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
            
        if password and len(password) < 8:
            self.add_error('password', 'Votre mot de passe doit avoir au moins 8 caractères')
                
        if confirm_password and len(confirm_password) < 8:
            self.add_error('confirm_password', 'Votre mot de passe doit avoir au moins 8 caractères')
                
        if(password != confirm_password):
            raise forms.ValidationError('Votre mot de passe et sa confirmation ne correspondent pas')
                    
            
            
            
            
            
            
            
            
            
            
             