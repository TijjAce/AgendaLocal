#!/usr/bin/env python
import os
import sys
import django

# Ajouter le répertoire du projet au path
sys.path.append('c:/Users/clemt/Desktop/Agenda')

# Configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from fiches.models import Fiche
from datetime import datetime

def debug_session_data():
    """Debug pour comprendre le problème de position des séances"""
    
    # Récupérer toutes les sessions récentes
    sessions = Fiche.objects.all().order_by('-date', '-id')[:5]
    
    print("=== DEBUG SESSION DATA ===")
    print(f"Nombre total de sessions: {sessions.count()}")
    print()
    
    for i, session in enumerate(sessions):
        print(f"Session {i+1}: {session.titre}")
        print(f"  - ID: {session.id}")
        print(f"  - Date: {session.date}")
        print(f"  - heure_debut: {session.heure_debut} (type: {type(session.heure_debut)})")
        print(f"  - heure_fin: {session.heure_fin} (type: {type(session.heure_fin)})")
        print(f"  - Utilisateur: {session.user}")
        
        if session.heure_debut:
            print(f"  - heure_debut.hour: {session.heure_debut.hour}")
            print(f"  - heure_debut.minute: {session.heure_debut.minute}")
            
            # Calcul comme dans la vue
            start_hour = session.heure_debut.hour
            start_minute = session.heure_debut.minute
            total_minutes_from_8am = (start_hour - 8) * 60 + start_minute
            
            print(f"  - Calcul offset: ({start_hour} - 8) * 60 + {start_minute} = {total_minutes_from_8am}")
        
        print("---")

if __name__ == "__main__":
    debug_session_data()
