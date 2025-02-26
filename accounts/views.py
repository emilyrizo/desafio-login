from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from .email_utils import send_registration_email
from .models import User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "E-mail inexistente!")
                return render(request, 'accounts/login.html', {'form': form})

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('menu')
            else:
                messages.error(request, "Senha inválida!")        
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()

            name = form.cleaned_data['name']
            send_registration_email(user.email, name)

            messages.success(request, "Registro realizado com sucesso!")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def menu_view(request):
    return render(request, 'accounts/menu.html')

def logout_view(request):
    logout(request)
    return redirect('login')