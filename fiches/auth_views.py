from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

def signup_view(request):
    """Vue d'inscription standard pour les nouveaux utilisateurs"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Créer l'utilisateur et l'activer immédiatement
            user = form.save()
            user.is_active = True
            user.save()
            
            # Connecter l'utilisateur automatiquement
            login(request, user)
            
            messages.success(request, f'Compte créé avec succès ! Bienvenue {user.username} !')
            return redirect('fiche_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    """Vue de connexion Django standard"""
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return '/fiches/'

def logout_view(request):
    """Vue de déconnexion standard"""
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('/')

@login_required
def profile_view(request):
    """Vue du profil utilisateur"""
    return render(request, 'registration/profile.html', {'user': request.user})
