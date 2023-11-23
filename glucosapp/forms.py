from django import forms
from users.models import User

from decouple import config

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                               min_length=4, max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'username',
                                   'placeholder': 'Nombre de usuario'
                               }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
                                   'class': 'form-control',
                                   'id': 'email',
                                   'placeholder': 'Tu correo electrónico'
                               }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'id': 'password',
                                   'placeholder':'Tu password'
                               }))
    confirm_password = forms.CharField(label="Confirmar Password",
                                    required=True, widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'id': 'password',
                                   'placeholder':'Tu password'
                               }))
    private_key = forms.CharField(required=True, widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'private-key',
                                   'placeholder': 'Tu clave privada'
                               }))
    

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya está registrado')
        
        return username
    

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya está registrado')
        
        return email
    

    def clean_private_key(self):
        private_key = self.cleaned_data.get('private_key')
        pk_list = [config('PRIVATE_KEY_NUMBER')]

        if private_key not in pk_list:
            raise forms.ValidationError('Consigue tu private key en fer@fermavec.com')
        
        return private_key
    
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('confirm_password') != cleaned_data.get('password'):
            self.add_error('confirm_password', 'El password no coincide')
        
    
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )