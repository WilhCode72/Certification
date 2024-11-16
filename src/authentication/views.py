from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CustomUser
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)  # Connecte automatiquement l'utilisateur après l'inscription
            return redirect('blog-index')  # Remplacez 'home' par la vue ou l'URL de votre choix
    else:
        form = RegistrationForm()

    return render(request, 'authentication/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('blog-index')  # Redirigez vers la page souhaitée
            else:
                return render(request, 'authentication/login.html', {
                    'form': form,
                    'error': "Nom d'utilisateur ou mot de passe incorrect."
                })
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirigez vers la page de connexion