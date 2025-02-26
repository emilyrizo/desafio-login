from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User
import re

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="E-mail",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'}),
        error_messages={
            'invalid': "Por favor, insira um endereço de e-mail válido."
        }
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': '•••••••••••••••'}) 
    )

class RegisterForm(UserCreationForm):
    name = forms.CharField(
        label="Nome", 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nome completo', 'autofocus': True})
    )
    email = forms.EmailField(
        label="E-mail", 
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail válido'}),
        error_messages={
            'invalid': "Por favor, insira um endereço de e-mail válido."
        }
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        required=True,
        help_text='A senha deve ter pelo menos 8 caracteres, 1 caractere especial, 1 número e 1 letra maiúscula.'
    )
    password2 = forms.CharField(
        label="Confirmar Senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        required=True,
        error_messages={'invalid': 'As senhas não coincidem.'}
    )

    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.is_active = True
        if commit:
            user.save()
        return user

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s\'-]+$', name):
            raise ValidationError("O nome deve conter apenas letras, espaços e caracteres comuns.")
        if len(name) < 4:
            raise forms.ValidationError("Digite um nome válido.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está registrado.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            raise forms.ValidationError("A senha deve conter pelo menos 1 caractere especial.")
        if not re.search(r'\d', password1):
            raise forms.ValidationError("A senha deve conter pelo menos 1 número.")
        if not re.search(r'[A-Z]', password1):
            raise forms.ValidationError("A senha deve conter pelo menos 1 letra maiúscula.")
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")      
        if len(password2) < 8:
            raise forms.ValidationError("As senhas não coincidem.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password2):
            raise forms.ValidationError("As senhas não coincidem.")
        if not re.search(r'\d', password2):
            raise forms.ValidationError("As senhas não coincidem.")
        if not re.search(r'[A-Z]', password2):
            raise forms.ValidationError("As senhas não coincidem.")
        return password2      
        