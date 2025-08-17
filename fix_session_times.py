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
from datetime import time

def fix_session_times():
    """Corriger les séances avec des heures manquantes"""
    
    print("=== CORRECTION DES HEURES DE SÉANCES ===")
    
    # Trouver les séances avec des heures manquantes
    sessions_without_start = Fiche.objects.filter(heure_debut__isnull=True)
    sessions_without_end = Fiche.objects.filter(heure_fin__isnull=True)
    
    print(f"Séances sans heure de début: {sessions_without_start.count()}")
    print(f"Séances sans heure de fin: {sessions_without_end.count()}")
    
    # Corriger les séances sans heure de début
    for session in sessions_without_start:
        print(f"Correction de '{session.titre}' (ID: {session.id})")
        print(f"  - Avant: heure_debut={session.heure_debut}, heure_fin={session.heure_fin}")
        
        # Définir une heure de début par défaut (9h00)
        session.heure_debut = time(9, 0)
        
        # Si pas d'heure de fin non plus, définir à 10h00
        if not session.heure_fin:
            session.heure_fin = time(10, 0)
        
        session.save()
        print(f"  - Après: heure_debut={session.heure_debut}, heure_fin={session.heure_fin}")
        print("---")
    
    # Corriger les séances sans heure de fin
    for session in sessions_without_end:
        if session.heure_debut:  # Si on a une heure de début
            print(f"Correction de '{session.titre}' (ID: {session.id})")
            print(f"  - Avant: heure_debut={session.heure_debut}, heure_fin={session.heure_fin}")
            
            # Ajouter 1 heure à l'heure de début
            start_hour = session.heure_debut.hour
            start_minute = session.heure_debut.minute
            end_hour = start_hour + 1
            
            if end_hour > 23:
                end_hour = 23
                end_minute = 59
            else:
                end_minute = start_minute
            
            session.heure_fin = time(end_hour, end_minute)
            session.save()
            
            print(f"  - Après: heure_debut={session.heure_debut}, heure_fin={session.heure_fin}")
            print("---")
    
    print("=== VÉRIFICATION POST-CORRECTION ===")
    
    # Vérifier qu'il n'y a plus de séances sans heures
    sessions_without_start_after = Fiche.objects.filter(heure_debut__isnull=True)
    sessions_without_end_after = Fiche.objects.filter(heure_fin__isnull=True)
    
    print(f"Séances sans heure de début (après): {sessions_without_start_after.count()}")
    print(f"Séances sans heure de fin (après): {sessions_without_end_after.count()}")
    
    if sessions_without_start_after.count() == 0 and sessions_without_end_after.count() == 0:
        print("✅ Toutes les séances ont maintenant des heures définies !")
    else:
        print("❌ Il reste des séances sans heures définies.")

if __name__ == "__main__":
    fix_session_times()
