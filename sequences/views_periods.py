from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from datetime import date, datetime
from .models import PeriodeScolaire, Sequence
from django.core.exceptions import ValidationError


@login_required
def periods_list(request):
    """Affiche la liste des périodes scolaires de l'utilisateur"""
    # Récupérer l'année scolaire actuelle
    current_year = date.today().year
    if date.today().month >= 9:  # Après septembre = nouvelle année scolaire
        annee_scolaire_actuelle = f"{current_year}-{current_year + 1}"
    else:
        annee_scolaire_actuelle = f"{current_year - 1}-{current_year}"
    
    # Récupérer toutes les périodes de l'utilisateur
    periodes = PeriodeScolaire.objects.filter(user=request.user)
    
    # Grouper par année scolaire
    periodes_by_year = {}
    for periode in periodes:
        if periode.annee_scolaire not in periodes_by_year:
            periodes_by_year[periode.annee_scolaire] = []
        periodes_by_year[periode.annee_scolaire].append(periode)
    
    # Période actuelle
    periode_actuelle = PeriodeScolaire.get_current_period(request.user)
    
    context = {
        'periodes_by_year': periodes_by_year,
        'annee_scolaire_actuelle': annee_scolaire_actuelle,
        'periode_actuelle': periode_actuelle,
        'total_periodes': periodes.count(),
    }
    
    return render(request, 'sequences/periods_list.html', context)


@login_required
def create_default_periods(request):
    """Crée les 5 périodes par défaut pour une année scolaire"""
    if request.method == 'POST':
        annee_scolaire = request.POST.get('annee_scolaire')
        
        if not annee_scolaire:
            messages.error(request, "Veuillez spécifier une année scolaire.")
            return redirect('sequences:periods_list')
        
        try:
            # Vérifier si des périodes existent déjà pour cette année
            existing_periods = PeriodeScolaire.objects.filter(
                user=request.user,
                annee_scolaire=annee_scolaire
            ).count()
            
            if existing_periods > 0:
                messages.warning(request, f"Des périodes existent déjà pour l'année {annee_scolaire}.")
                return redirect('sequences:periods_list')
            
            # Créer les périodes par défaut
            created_periods = PeriodeScolaire.create_default_periods(request.user, annee_scolaire)
            
            messages.success(request, f"✅ {len(created_periods)} périodes créées avec succès pour l'année {annee_scolaire}!")
            
        except Exception as e:
            messages.error(request, f"Erreur lors de la création des périodes : {str(e)}")
    
    return redirect('sequences:periods_list')


@login_required
def period_detail(request, period_id):
    """Affiche le détail d'une période et ses séquences associées"""
    periode = get_object_or_404(PeriodeScolaire, id=period_id, user=request.user)
    
    # Récupérer les séquences associées à cette période
    sequences = Sequence.objects.filter(
        user=request.user,
        periode_scolaire=periode
    ).select_related('discipline').order_by('discipline__title', 'ordre')
    
    # Statistiques
    total_sequences = sequences.count()
    total_duration = sum(seq.total_duration_minutes for seq in sequences)
    total_duration_hours = round(total_duration / 60, 1) if total_duration > 0 else 0
    
    # Séquences par discipline
    sequences_by_discipline = {}
    for sequence in sequences:
        discipline = sequence.discipline.title
        if discipline not in sequences_by_discipline:
            sequences_by_discipline[discipline] = []
        sequences_by_discipline[discipline].append(sequence)
    
    context = {
        'periode': periode,
        'sequences': sequences,
        'sequences_by_discipline': sequences_by_discipline,
        'total_sequences': total_sequences,
        'total_duration_hours': total_duration_hours,
        'is_current_period': periode.est_active,
    }
    
    return render(request, 'sequences/period_detail.html', context)


@login_required
@require_http_methods(["POST"])
def assign_sequence_to_period(request):
    """Assigne une séquence à une période via AJAX"""
    sequence_id = request.POST.get('sequence_id')
    period_id = request.POST.get('period_id')
    
    try:
        sequence = get_object_or_404(Sequence, id=sequence_id, user=request.user)
        
        if period_id and period_id != 'null':
            periode = get_object_or_404(PeriodeScolaire, id=period_id, user=request.user)
            sequence.periode_scolaire = periode
            success_message = f"Séquence '{sequence.name}' assignée à la période '{periode.nom}'"
        else:
            sequence.periode_scolaire = None
            success_message = f"Séquence '{sequence.name}' retirée de sa période"
        
        sequence.save()
        
        return JsonResponse({
            'success': True,
            'message': success_message
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f"Erreur : {str(e)}"
        })


@login_required
def period_calendar_view(request):
    """Vue calendrier des périodes scolaires"""
    # Récupérer l'année scolaire actuelle
    current_year = date.today().year
    if date.today().month >= 9:
        annee_scolaire = f"{current_year}-{current_year + 1}"
    else:
        annee_scolaire = f"{current_year - 1}-{current_year}"
    
    # Permettre de changer d'année via GET
    selected_year = request.GET.get('year', annee_scolaire)
    
    # Récupérer les périodes pour l'année sélectionnée
    periodes = PeriodeScolaire.objects.filter(
        user=request.user,
        annee_scolaire=selected_year
    ).order_by('numero')
    
    # Préparer les données pour le calendrier
    periods_data = []
    for periode in periodes:
        periods_data.append({
            'id': periode.id,
            'title': periode.nom,
            'start': periode.date_debut.isoformat(),
            'end': (periode.date_fin).isoformat(),
            'color': periode.couleur,
            'description': periode.description,
            'sequences_count': periode.sequences.count(),
        })
    
    # Années disponibles
    available_years = PeriodeScolaire.objects.filter(
        user=request.user
    ).values_list('annee_scolaire', flat=True).distinct().order_by('-annee_scolaire')
    
    context = {
        'periods_data': periods_data,
        'selected_year': selected_year,
        'available_years': available_years,
        'current_period': PeriodeScolaire.get_current_period(request.user),
    }
    
    return render(request, 'sequences/period_calendar.html', context)


@login_required
def test_deployment_feature(request):
    """Vue de test pour vérifier que le déploiement fonctionne"""
    # Cette vue sert à tester visuellement le déploiement
    
    # Statistiques rapides
    total_periods = PeriodeScolaire.objects.filter(user=request.user).count()
    total_sequences = Sequence.objects.filter(user=request.user).count()
    sequences_with_periods = Sequence.objects.filter(
        user=request.user,
        periode_scolaire__isnull=False
    ).count()
    
    # Période actuelle
    current_period = PeriodeScolaire.get_current_period(request.user)
    
    # Dernière mise à jour
    last_update = timezone.now()
    
    context = {
        'total_periods': total_periods,
        'total_sequences': total_sequences,
        'sequences_with_periods': sequences_with_periods,
        'current_period': current_period,
        'last_update': last_update,
        'deployment_test': True,
        'test_message': "🚀 Fonctionnalité des périodes scolaires déployée avec succès !",
    }
    
    return render(request, 'sequences/test_deployment.html', context)
