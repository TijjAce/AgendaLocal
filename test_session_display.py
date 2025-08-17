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
from datetime import datetime, time

def test_session_position_calculation():
    """Tester le calcul de position des séances comme dans la vue Django"""
    
    print("=== TEST CALCUL POSITION SÉANCES ===")
    
    # Prendre une séance récente pour tester
    session = Fiche.objects.filter(heure_debut__isnull=False).first()
    
    if not session:
        print("❌ Aucune séance trouvée avec des heures définies")
        return
    
    print(f"Test avec la séance: {session.titre}")
    print(f"  - Date: {session.date}")
    print(f"  - heure_debut: {session.heure_debut}")
    print(f"  - heure_fin: {session.heure_fin}")
    
    # Simuler le calcul de la vue Django
    if session.heure_debut and session.heure_fin:
        start_hour = session.heure_debut.hour
        start_minute = session.heure_debut.minute
        
        # Calcul total des minutes depuis 8h00
        total_minutes_from_8am = (start_hour - 8) * 60 + start_minute
        
        print(f"  - start_hour: {start_hour}")
        print(f"  - start_minute: {start_minute}")
        print(f"  - Calcul offset: ({start_hour} - 8) * 60 + {start_minute} = {total_minutes_from_8am}")
        
        # Calculer la position Y comme dans le JavaScript
        config_topMargin = 30
        config_hourHeight = 60
        position_y = config_topMargin + (total_minutes_from_8am / 60) * config_hourHeight
        
        print(f"  - Position Y calculée: {config_topMargin} + ({total_minutes_from_8am} / 60) * {config_hourHeight} = {position_y}")
        
        # Vérifier la cohérence
        expected_y_for_hour = config_topMargin + (start_hour - 8) * config_hourHeight
        print(f"  - Position Y attendue pour {start_hour}h: {expected_y_for_hour}")
        
        if abs(position_y - expected_y_for_hour) < 1:  # Tolérance d'1 pixel
            print("✅ Le calcul de position est correct !")
        else:
            print("❌ Problème dans le calcul de position")
    else:
        print("❌ La séance n'a pas d'heures définies")

if __name__ == "__main__":
    test_session_position_calculation()
