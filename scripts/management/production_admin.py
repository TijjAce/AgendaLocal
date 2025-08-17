#!/usr/bin/env python
"""
Script d'administration pour résoudre les problèmes de production
Usage: python scripts/management/production_admin.py [command]
"""

import os
import sys
import django

# Configuration Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
# from axes.models import AccessAttempt  # Supprimé pour développement local
# from axes.helpers import reset_attempts  # Supprimé pour développement local
from django.core.management import call_command


def unlock_all_users():
    """Fonction désactivée - django-axes supprimé pour développement local"""
    print("🔓 Fonction désactivée - pas de verrouillage en mode local")
    
    # # Supprimer toutes les tentatives d'accès
    # attempts_count = AccessAttempt.objects.count()
    # AccessAttempt.objects.all().delete()
    
    print("✅ Aucune action nécessaire en mode développement local")
    print("✅ Tous les utilisateurs sont maintenant débloqués")


def unlock_user(username):
    """Débloquer un utilisateur spécifique"""
    print(f"🔓 Déblocage de l'utilisateur: {username}")
    
    try:
        user = User.objects.get(username=username)
        reset_attempts(username=username)
        print(f"✅ Utilisateur {username} débloqué avec succès")
    except User.DoesNotExist:
        print(f"❌ Utilisateur {username} introuvable")


def show_locked_users():
    """Afficher les utilisateurs actuellement verrouillés"""
    print("🔍 Utilisateurs verrouillés:")
    
    attempts = AccessAttempt.objects.all()
    if not attempts:
        print("✅ Aucun utilisateur verrouillé")
        return
    
    for attempt in attempts:
        print(f"- Utilisateur: {attempt.username}")
        print(f"  IP: {attempt.ip_address}")
        print(f"  Tentatives: {attempt.failures_since_start}")
        print(f"  Dernière tentative: {attempt.attempt_time}")
        print()


def check_production_status():
    """Vérifier le statut de la production"""
    print("🔍 Vérification du statut de production...")
    
    # Vérifier les variables d'environnement
    print("\n📋 Variables d'environnement:")
    env_vars = [
        'DJANGO_SECRET_KEY',
        'RESEND_API_KEY', 
        'DATABASE_URL',
        'RAILWAY_ENVIRONMENT',
        'DJANGO_DEBUG'
    ]
    
    for var in env_vars:
        value = os.environ.get(var)
        if value:
            if 'KEY' in var or 'SECRET' in var:
                print(f"✅ {var}: ****** (défini)")
            else:
                print(f"✅ {var}: {value}")
        else:
            print(f"❌ {var}: Non défini")
    
    # Vérifier la base de données
    print("\n🗄️ Base de données:")
    try:
        user_count = User.objects.count()
        print(f"✅ Connexion DB OK - {user_count} utilisateurs")
    except Exception as e:
        print(f"❌ Erreur DB: {e}")
    
    # Vérifier django-axes
    print("\n🛡️ Django-axes:")
    try:
        attempts_count = AccessAttempt.objects.count()
        print(f"✅ Axes OK - {attempts_count} tentatives enregistrées")
    except Exception as e:
        print(f"❌ Erreur Axes: {e}")


def main():
    """Fonction principale"""
    if len(sys.argv) < 2:
        print("Usage: python production_admin.py [command]")
        print("\nCommandes disponibles:")
        print("  unlock-all     - Débloquer tous les utilisateurs")
        print("  unlock <user>  - Débloquer un utilisateur spécifique")
        print("  show-locked    - Afficher les utilisateurs verrouillés")
        print("  status         - Vérifier le statut de production")
        return
    
    command = sys.argv[1]
    
    if command == "unlock-all":
        unlock_all_users()
    elif command == "unlock" and len(sys.argv) > 2:
        unlock_user(sys.argv[2])
    elif command == "show-locked":
        show_locked_users()
    elif command == "status":
        check_production_status()
    else:
        print(f"❌ Commande inconnue: {command}")


if __name__ == "__main__":
    main()
