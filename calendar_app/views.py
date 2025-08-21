from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from fiches.models import Fiche
from pages.models import Page
from datetime import datetime, time, date, timedelta
from django.utils import timezone
from .school_holidays_service import SchoolHolidaysService
import logging

from django.utils.dateparse import parse_date

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

logger = logging.getLogger(__name__)

@login_required
def calendar_view(request):
    return render(request, 'calendar_app/calendar.html')


@login_required
def get_events(request):
    try:
        year = int(request.GET.get('year', datetime.now().year))
    except ValueError:
        year = datetime.now().year
    
    # Récupérer la zone scolaire depuis les paramètres ou les préférences utilisateur
    zone = request.GET.get('zone', 'A')  # Zone A par défaut

    # Filtrer les fiches par année et par utilisateur
    fiches = Fiche.objects.filter(date__year=year, user=request.user)

    events = []
    
    # Ajouter les fiches de l'utilisateur
    for fiche in fiches:
        events.append({
            'type': 'fiche',
            'title': fiche.titre,
            'description': fiche.discipline.title if fiche.discipline else "",
            'date': fiche.date.isoformat(),
            'color': fiche.couleur if hasattr(fiche, 'couleur') and fiche.couleur else '#0d6efd'
        })
    
    # Ajouter les vacances scolaires
    try:
        holidays = SchoolHolidaysService.get_school_holidays(year, zone)
        
        for holiday in holidays:
            # Créer un événement pour chaque jour de vacances
            # Note: Nous excluons le jour de début car il y avait un décalage d'un jour en trop
            from datetime import timedelta
            current_date = holiday['start_date'] + timedelta(days=1)  # Commencer au lendemain du jour de début
            while current_date <= holiday['end_date']:  # Inclure le jour de fin
                events.append({
                    'type': 'holiday',
                    'title': holiday['description'],
                    'description': f"Vacances scolaires - {holiday['zone']}",
                    'date': current_date.isoformat(),
                    'color': '#28a745',  # Vert pour les vacances
                    'zone': holiday['zone']
                })
                # Passer au jour suivant
                from datetime import timedelta
                current_date += timedelta(days=1)
                
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des vacances scolaires: {e}")
        # Continue sans les vacances en cas d'erreur

    return JsonResponse(events, safe=False)



def assign_columns(sessions):
    # Trie par heure de début
    sorted_sessions = sorted(sessions, key=lambda s: s.heure_debut)
    active = []

    for session in sorted_sessions:
        # Enlève les sessions déjà terminées
        active = [s for s in active if s.heure_fin > session.heure_debut]

        # Attribue une colonne disponible
        used_columns = {s.column_index for s in active if hasattr(s, 'column_index')}
        column = 0
        while column in used_columns:
            column += 1

        session.column_index = column
        active.append(session)

        # Met à jour le nombre total de colonnes pour les sessions actives
        for s in active:
            s.total_columns = max(getattr(s, 'total_columns', 1), len(active))

    return sorted_sessions



# daily_schedule_canvas view in your Django app

@login_required
def daily_schedule_canvas(request, year, month, day):
    """
    Version Canvas du daily schedule - plus robuste et sans bugs de positionnement CSS
    """
    selected_date = datetime(year, month, day).date()
    sessions = (
        Fiche.objects
        .filter(date=selected_date, user=request.user)
        .select_related('discipline')
        .order_by('heure_debut')
    )

    start_of_day = time(8, 0)

    for session in sessions:
        if session.heure_debut and session.heure_fin:
            start_hour = session.heure_debut.hour
            start_minute = session.heure_debut.minute
            
            total_minutes_from_8am = (start_hour - 8) * 60 + start_minute
            session.offset_minutes = total_minutes_from_8am
            
            delta_duration = datetime.combine(selected_date, session.heure_fin) - datetime.combine(selected_date, session.heure_debut)
            session.duration_minutes = int(delta_duration.total_seconds() // 60)
        else:
            session.offset_minutes = 0
            session.duration_minutes = 60
            if not session.heure_debut:
                session.heure_debut = start_of_day
            if not session.heure_fin:
                session.heure_fin = time(session.heure_debut.hour + 1, session.heure_debut.minute)
        
        session.page_url = f"/fiches/{session.id}/"
        session.couleur = session.couleur if session.couleur else '#CCCCCC'

    sessions = assign_columns(list(sessions))
    
    # Calculer les dates précédente et suivante pour la navigation
    previous_date = selected_date - timedelta(days=1)
    next_date = selected_date + timedelta(days=1)

    return render(request, 'calendar_app/daily_schedule_canvas.html', {
        'sessions': sessions,
        'selected_date': selected_date,
        'previous_date': previous_date,
        'next_date': next_date,
    })


@login_required
def toggle_session_completion(request, session_id):
    """
    Vue pour basculer l'état de completion d'une séance (réalisée/non réalisée).
    Met à jour automatiquement la progression de la séquence associée.
    """
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Méthode non autorisée'})
    
    try:
        # Récupérer la fiche (séance)
        fiche = get_object_or_404(Fiche, id=session_id, user=request.user)
        
        # Basculer l'état de completion
        fiche.is_completed = not fiche.is_completed
        
        if fiche.is_completed:
            fiche.completed_at = timezone.now()
        else:
            fiche.completed_at = None
        
        fiche.save()
        
        # Recalculer la progression de la séquence si elle existe
        progression_info = None
        if fiche.sequence_obj:
            sequence = fiche.sequence_obj
            total_seances = sequence.seances.count()
            completed_seances = sequence.seances.filter(is_completed=True).count()
            
            if total_seances > 0:
                progression_percentage = round((completed_seances / total_seances) * 100)
            else:
                progression_percentage = 0
            
            progression_info = {
                'sequence_id': sequence.id,
                'sequence_nom': sequence.name,  # Correction: utiliser 'name' au lieu de 'nom'
                'total_seances': total_seances,
                'completed_seances': completed_seances,
                'progression_percentage': progression_percentage
            }
        
        return JsonResponse({
            'success': True,
            'is_completed': fiche.is_completed,
            'completed_at': fiche.completed_at.isoformat() if fiche.completed_at else None,
            'message': f'Séance marquée comme {"réalisée" if fiche.is_completed else "non réalisée"}',
            'progression': progression_info
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })






# ===== VUE HEBDOMADAIRE =====




@login_required
def weekly_schedule(request, year=None, week=None):
    """
    Vue hebdomadaire affichant les cours de lundi à dimanche.
    """
    # Déterminer la semaine
    today = datetime.now()
    if year and week:
        try:
            year = int(year)
            week = int(week)
        except ValueError:
            year = today.year
            week = today.isocalendar()[1]
    else:
        year = today.year
        week = today.isocalendar()[1]

    # Premier lundi de l'année
    jan_1 = date(year, 1, 1)
    days_to_monday = (7 - jan_1.weekday()) % 7 if jan_1.weekday() != 0 else 0
    first_monday = jan_1 + timedelta(days=days_to_monday)

    # Lundi de la semaine demandée
    week_start = first_monday + timedelta(weeks=week - 1)
    week_days = [week_start + timedelta(days=i) for i in range(7)]

    # Récupérer les fiches de la semaine
    week_sessions = Fiche.objects.filter(
        user=request.user,
        date__range=[week_days[0], week_days[6]]
    ).order_by('date', 'heure_debut')

    # Organisation par jour
    day_names = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    week_data = []

    for i, day in enumerate(week_days):
        day_sessions = [s for s in week_sessions if s.date == day]
        processed_sessions = []

        for session in day_sessions:
            if session.heure_debut and session.heure_fin:
                start_hour = max(7, session.heure_debut.hour + session.heure_debut.minute / 60)
                end_hour = min(19, session.heure_fin.hour + session.heure_fin.minute / 60)
                top_position = max(0, (start_hour - 7) * (400 / 12))
                height = max(20, (end_hour - start_hour) * (400 / 12))
                session.top_position = int(top_position)
                session.height = int(height)
                processed_sessions.append(session)

        week_data.append((day_names[i], day, processed_sessions))

    # Semaine précédente et suivante
    prev_week, next_week = week - 1, week + 1
    prev_year, next_year = year, year
    if week == 1:
        prev_week = 52
        prev_year = year - 1
    if week == 52:
        next_week = 1
        next_year = year + 1

    context = {
        'year': year,
        'week': week,
        'week_days': week_days,
        'week_data': week_data,
        'prev_year': prev_year,
        'prev_week': prev_week,
        'next_year': next_year,
        'next_week': next_week,
        'week_start': week_start,
        'week_end': week_days[6],
    }
    return render(request, 'calendar_app/weekly_schedule.html', context)


@csrf_exempt
def update_session_date(request):
    """
    Met à jour la date d’une fiche après drag & drop.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            session_id = data.get("session_id")
            new_date = data.get("new_date")
            fiche = Fiche.objects.get(id=session_id)
            fiche.date = parse_date(new_date)
            fiche.save()
            return JsonResponse({"success": True})
        except Fiche.DoesNotExist:
            return JsonResponse({"success": False, "error": "Fiche introuvable"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Méthode non autorisée"})





@csrf_exempt
def update_session_position(request):
    """
    Met à jour la date ou la position d'une fiche après drag & drop.
    """
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Méthode non autorisée"})

    try:
        data = json.loads(request.body)
        session_id = data.get("session_id")
        new_date = data.get("new_date")  # si tu veux aussi déplacer de jour
        new_top = data.get("new_top")    # position verticale en px ou autre

        fiche = Fiche.objects.get(id=session_id)

        if new_date:
            fiche.date = parse_date(new_date)
        if new_top is not None:
            fiche.top_position = int(new_top)  # si tu as ce champ

        fiche.save()

        return JsonResponse({"success": True})

    except Fiche.DoesNotExist:
        return JsonResponse({"success": False, "error": "Fiche introuvable"})
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "error": "JSON invalide"})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})
    




   