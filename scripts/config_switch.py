#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour basculer entre configuration locale et PythonAnywhere
Gere automatiquement les fichiers .env et settings.py
"""

import os
import sys
import shutil
import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent

class ConfigSwitcher:
    def __init__(self):
        self.project_root = PROJECT_ROOT
        self.env_file = self.project_root / '.env'
        self.env_local = self.project_root / '.env.local'
        self.env_pythonanywhere = self.project_root / '.env.pythonanywhere'
        self.settings_file = self.project_root / 'config' / 'settings.py'
        self.current_config_file = self.project_root / '.current_config'
        
    def log(self, message, level="INFO"):
        """Affiche un message avec timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        try:
            print(f"[{timestamp}] {level}: {message}")
        except UnicodeEncodeError:
            # Fallback pour les systemes avec encodage limite
            print(f"[{timestamp}] {level}: {message.encode('ascii', 'ignore').decode('ascii')}")
    
    def get_current_config(self):
        """Détermine la configuration actuelle"""
        if self.current_config_file.exists():
            with open(self.current_config_file, 'r') as f:
                return f.read().strip()
        
        # Détecter automatiquement basé sur le contenu du .env
        if self.env_file.exists():
            with open(self.env_file, 'r') as f:
                content = f.read()
                if 'pythonanywhere.com' in content.lower():
                    return 'pythonanywhere'
                elif 'localhost' in content or '127.0.0.1' in content:
                    return 'local'
        
        return 'unknown'
    
    def save_current_config(self, config_type):
        """Sauvegarde la configuration actuelle"""
        with open(self.current_config_file, 'w') as f:
            f.write(config_type)
    
    def backup_current_env(self):
        """Sauvegarde le fichier .env actuel"""
        if not self.env_file.exists():
            return
        
        current_config = self.get_current_config()
        
        if current_config == 'local':
            backup_file = self.env_local
        elif current_config == 'pythonanywhere':
            backup_file = self.env_pythonanywhere
        else:
            # Sauvegarde générique avec timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = self.project_root / f'.env.backup_{timestamp}'
        
        shutil.copy2(self.env_file, backup_file)
        self.log(f"Configuration actuelle sauvegardée dans: {backup_file.name}")
    
    def create_local_config(self):
        """Crée une configuration locale"""
        local_config = """# Configuration LOCALE pour développement
DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de données locale
DATABASE_URL=sqlite:///db.sqlite3

# URLs et domaines
SITE_URL=http://127.0.0.1:8000
DOMAIN=localhost:8000

# Sécurité (développement)
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False

# Email (développement - console backend)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Médias et statiques
MEDIA_URL=/media/
STATIC_URL=/static/

# Configuration spécifique locale
ENVIRONMENT=local
"""
        return local_config
    
    def create_pythonanywhere_config(self):
        """Crée une configuration PythonAnywhere"""
        pythonanywhere_config = """# Configuration PYTHONANYWHERE pour production
DEBUG=False
SECRET_KEY=your-production-secret-key-here-CHANGE-THIS
ALLOWED_HOSTS=VOTRE_USERNAME.pythonanywhere.com,www.VOTRE_USERNAME.pythonanywhere.com

# Base de données PythonAnywhere (MySQL optionnel)
# DATABASE_URL=mysql://username:password@username.mysql.pythonanywhere-services.com/username$dbname
DATABASE_URL=sqlite:///db.sqlite3

# URLs et domaines
SITE_URL=https://VOTRE_USERNAME.pythonanywhere.com
DOMAIN=VOTRE_USERNAME.pythonanywhere.com

# Sécurité (production)
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_BROWSER_XSS_FILTER=True
SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True

# Email (production)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=votre-email@gmail.com
EMAIL_HOST_PASSWORD=votre-mot-de-passe-app

# Médias et statiques
MEDIA_URL=/media/
STATIC_URL=/static/
STATIC_ROOT=/home/VOTRE_USERNAME/mysite/staticfiles

# Configuration spécifique PythonAnywhere
ENVIRONMENT=production
PYTHONANYWHERE_USERNAME=VOTRE_USERNAME
"""
        return pythonanywhere_config
    
    def switch_to_local(self):
        """Bascule vers la configuration locale"""
        self.log("[LOCAL] Basculement vers la configuration LOCALE")
        
        # Sauvegarder la config actuelle
        self.backup_current_env()
        
        # Utiliser la config locale existante ou en créer une nouvelle
        if self.env_local.exists():
            self.log("Utilisation de la configuration locale existante")
            shutil.copy2(self.env_local, self.env_file)
        else:
            self.log("Création d'une nouvelle configuration locale")
            with open(self.env_file, 'w', encoding='utf-8') as f:
                f.write(self.create_local_config())
            # Sauvegarder aussi comme template
            shutil.copy2(self.env_file, self.env_local)
        
        # Marquer la configuration actuelle
        self.save_current_config('local')
        
        self.log("[OK] Configuration locale activee")
        self.log("Serveur de developpement: python manage.py runserver")
        self.log("URL: http://127.0.0.1:8000")
    
    def switch_to_pythonanywhere(self):
        """Bascule vers la configuration PythonAnywhere"""
        self.log("[CLOUD] Basculement vers la configuration PYTHONANYWHERE")
        
        # Sauvegarder la config actuelle
        self.backup_current_env()
        
        # Utiliser la config PythonAnywhere existante ou en créer une nouvelle
        if self.env_pythonanywhere.exists():
            self.log("Utilisation de la configuration PythonAnywhere existante")
            shutil.copy2(self.env_pythonanywhere, self.env_file)
        else:
            self.log("Création d'une nouvelle configuration PythonAnywhere")
            with open(self.env_file, 'w', encoding='utf-8') as f:
                f.write(self.create_pythonanywhere_config())
            # Sauvegarder aussi comme template
            shutil.copy2(self.env_file, self.env_pythonanywhere)
        
        # Marquer la configuration actuelle
        self.save_current_config('pythonanywhere')
        
        self.log("[OK] Configuration PythonAnywhere activee")
        self.log("[ATTENTION] N'oubliez pas de modifier les valeurs dans .env:")
        self.log("   - VOTRE_USERNAME (remplacer par votre nom d'utilisateur)")
        self.log("   - SECRET_KEY (générer une nouvelle clé secrète)")
        self.log("   - Paramètres email si nécessaire")
    
    def show_status(self):
        """Affiche le statut actuel de la configuration"""
        current = self.get_current_config()
        
        self.log("[STATUS] STATUT DE LA CONFIGURATION")
        self.log("=" * 40)
        
        if current == 'local':
            self.log("Configuration actuelle: [LOCAL] LOCALE (developpement)")
        elif current == 'pythonanywhere':
            self.log("Configuration actuelle: [CLOUD] PYTHONANYWHERE (production)")
        else:
            self.log("Configuration actuelle: [?] INCONNUE")
        
        # Vérifier les fichiers de configuration
        configs_available = []
        if self.env_local.exists():
            configs_available.append("[LOCAL] Locale")
        if self.env_pythonanywhere.exists():
            configs_available.append("[CLOUD] PythonAnywhere")
        
        if configs_available:
            self.log(f"Configurations disponibles: {', '.join(configs_available)}")
        else:
            self.log("Aucune configuration sauvegardée trouvée")
        
        # Afficher quelques paramètres clés du .env actuel
        if self.env_file.exists():
            self.log("\nParamètres actuels:")
            with open(self.env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if any(key in line for key in ['DEBUG', 'ALLOWED_HOSTS', 'SITE_URL', 'ENVIRONMENT']):
                            self.log(f"  {line}")
    
    def interactive_menu(self):
        """Menu interactif pour choisir la configuration"""
        while True:
            print("\n" + "="*50)
            print("[CONFIG] GESTIONNAIRE DE CONFIGURATION")
            print("="*50)
            
            current = self.get_current_config()
            if current == 'local':
                print("Configuration actuelle: [LOCAL] LOCALE")
            elif current == 'pythonanywhere':
                print("Configuration actuelle: [CLOUD] PYTHONANYWHERE")
            else:
                print("Configuration actuelle: [?] INCONNUE")
            
            print("\nOptions disponibles:")
            print("1. [LOCAL] Basculer vers LOCAL (developpement)")
            print("2. [CLOUD] Basculer vers PYTHONANYWHERE (production)")
            print("3. [STATUS] Afficher le statut detaille")
            print("4. [EXIT] Quitter")
            
            try:
                choice = input("\nVotre choix (1-4): ").strip()
                
                if choice == '1':
                    self.switch_to_local()
                elif choice == '2':
                    self.switch_to_pythonanywhere()
                elif choice == '3':
                    self.show_status()
                elif choice == '4':
                    print("[EXIT] Au revoir!")
                    break
                else:
                    print("[ERREUR] Choix invalide, veuillez reessayer.")
                    
            except KeyboardInterrupt:
                print("\n[EXIT] Au revoir!")
                break
            except Exception as e:
                print(f"[ERREUR] Erreur: {e}")

def main():
    """Point d'entrée principal"""
    switcher = ConfigSwitcher()
    
    if len(sys.argv) > 1:
        # Mode ligne de commande
        command = sys.argv[1].lower()
        
        if command in ['local', 'l']:
            switcher.switch_to_local()
        elif command in ['pythonanywhere', 'pa', 'prod']:
            switcher.switch_to_pythonanywhere()
        elif command in ['status', 's']:
            switcher.show_status()
        else:
            print("Usage: python config_switch.py [local|pythonanywhere|status]")
            print("Ou lancez sans argument pour le menu interactif")
            sys.exit(1)
    else:
        # Mode interactif
        switcher.interactive_menu()

if __name__ == "__main__":
    main()
