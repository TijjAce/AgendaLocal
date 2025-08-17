from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count, Q
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from datetime import datetime, timedelta, time
from .models import Sequence, PeriodeScolaire
from .forms import SequenceForm
from pages.models import Page
from fiches.models import Fiche
from main.models import UserDisciplineColorPreference
import logging
from datetime import date

logger = logging.getLogger(__name__)


@login_required
def sequences_list(request):
    """Affiche la liste des séquences organisées par années scolaires et périodes"""
    # Récupérer l'année scolaire sélectionnée (par défaut: année actuelle)
    current_year = date.today().year
    if date.today().month >= 9:  # Septembre = début année scolaire
        default_year = f"{current_year}-{current_year + 1}"
    else:
        default_year = f"{current_year - 1}-{current_year}"
    
    selected_year = request.GET.get('year', default_year)
    
    # Récupérer ou créer les périodes pour l'année sélectionnée
    periodes = PeriodeScolaire.objects.filter(
        user=request.user,
        annee_scolaire=selected_year
    ).order_by('numero')
    
    # Si aucune période n'existe pour cette année, les créer
    if not periodes.exists():
        PeriodeScolaire.create_default_periods(request.user, selected_year)
        periodes = PeriodeScolaire.objects.filter(
            user=request.user,
            annee_scolaire=selected_year
        ).order_by('numero')
    
    # Récupérer toutes les séquences de l'utilisateur
    sequences = Sequence.objects.filter(user=request.user)
    
    # Organiser les séquences par période
    sequences_by_period = {}
    sequences_without_period = []
    
    # Calculer les heures par période et totales
    total_hours_year = 0
    
    for periode in periodes:
        periode_sequences = sequences.filter(periode_scolaire=periode)
        
        # Calculer les heures pour cette période
        period_total_minutes = 0
        for sequence in periode_sequences:
            sequence.seances_count = sequence.get_seances_count()
            sequence.total_duration_str = sequence.get_total_duration_str()
            sequence.total_hours = sequence.total_duration_minutes / 60 if sequence.total_duration_minutes > 0 else 0
            period_total_minutes += sequence.total_duration_minutes
        
        period_total_hours = period_total_minutes / 60 if period_total_minutes > 0 else 0
        total_hours_year += period_total_hours
        
        sequences_by_period[periode.id] = {
            'periode': periode,
            'sequences': periode_sequences,
            'total_hours': round(period_total_hours, 1)
        }
    
    # Séquences sans période assignée
    sequences_without_period = sequences.filter(periode_scolaire__isnull=True)
    unassigned_total_minutes = 0
    
    for sequence in sequences_without_period:
        sequence.seances_count = sequence.get_seances_count()
        sequence.total_duration_str = sequence.get_total_duration_str()
        sequence.total_hours = sequence.total_duration_minutes / 60 if sequence.total_duration_minutes > 0 else 0
        unassigned_total_minutes += sequence.total_duration_minutes
    
    unassigned_total_hours = unassigned_total_minutes / 60 if unassigned_total_minutes > 0 else 0
    total_hours_year += unassigned_total_hours
    
    # Récupérer les disciplines pour les filtres
    disciplines = Page.objects.filter(parent__isnull=True).order_by('title')
    
    # Générer les années disponibles (3 années: précédente, actuelle, suivante)
    available_years = [
        f"{current_year - 1}-{current_year}",
        f"{current_year}-{current_year + 1}",
        f"{current_year + 1}-{current_year + 2}"
    ]
    
    context = {
        'sequences_by_period': sequences_by_period,
        'sequences_without_period': sequences_without_period,
        'periodes': periodes,
        'disciplines': disciplines,
        'selected_year': selected_year,
        'available_years': available_years,
        'total_sequences': sequences.count(),
        'total_hours_year': round(total_hours_year, 1),
        'unassigned_total_hours': round(unassigned_total_hours, 1),
    }
    
    return render(request, 'sequences/sequences_list.html', context)


@login_required
def sequences_create(request):
    """Créer une nouvelle séquence"""
    disciplines = Page.objects.filter(parent__isnull=True).order_by('title')
    
    # Récupérer la discipline pré-sélectionnée depuis les paramètres GET
    selected_discipline_id = request.GET.get('discipline_id')
    selected_discipline = None
    if selected_discipline_id:
        try:
            selected_discipline = Page.objects.get(id=selected_discipline_id, parent__isnull=True)
        except Page.DoesNotExist:
            pass
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        discipline_id = request.POST.get('discipline')
        description = request.POST.get('description', '').strip()
        duree_estimee = request.POST.get('duration')
        niveau = request.POST.get('level')
        
        # Validation
        if not name:
            messages.error(request, 'Le nom de la séquence est obligatoire.')
            return render(request, 'sequences/sequences_create.html', {
                'disciplines': disciplines,
                'selected_discipline': selected_discipline,
            })
        
        if not discipline_id:
            messages.error(request, 'Veuillez sélectionner une discipline.')
            return render(request, 'sequences/sequences_create.html', {
                'disciplines': disciplines,
                'selected_discipline': selected_discipline,
            })
        
        try:
            discipline = Page.objects.get(id=discipline_id, parent__isnull=True)
        except Page.DoesNotExist:
            messages.error(request, 'Discipline invalide.')
            return render(request, 'sequences/sequences_create.html', {
                'disciplines': disciplines,
                'selected_discipline': selected_discipline,
            })
        
        # Vérifier l'unicité du nom pour cette discipline/utilisateur
        if Sequence.objects.filter(user=request.user, name=name, discipline=discipline).exists():
            messages.error(request, f'Une séquence nommée "{name}" existe déjà pour cette discipline.')
            return render(request, 'sequences/sequences_create.html', {
                'disciplines': disciplines,
                'selected_discipline': selected_discipline,
            })
        
        try:
            # Créer la séquence
            sequence = Sequence.objects.create(
                user=request.user,
                name=name,
                discipline=discipline,
                description=description,
                duree_estimee=int(duree_estimee) if duree_estimee else None,
                niveau=niveau if niveau else '',
            )
            
            messages.success(request, f'La séquence "{name}" a été créée avec succès!')
            return redirect('sequences:sequences_detail', sequence_id=sequence.id)
            
        except Exception as e:
            logger.error(f"Erreur lors de la création de la séquence: {e}")
            messages.error(request, 'Erreur lors de la création de la séquence.')
    
    return render(request, 'sequences/sequences_create.html', {
        'disciplines': disciplines,
        'selected_discipline': selected_discipline,
    })


@login_required
def sequences_detail(request, sequence_id):
    """Afficher les détails d'une séquence avec gestion intégrée des séances"""
    sequence = get_object_or_404(Sequence, id=sequence_id, user=request.user)
    
    # Traitement POST pour ajouter des séances à la séquence
    if request.method == 'POST':
        selected_fiches = request.POST.getlist('selected_fiches')
        
        if selected_fiches:
            updated_count = 0
            
            for fiche_id in selected_fiches:
                try:
                    fiche = Fiche.objects.get(
                        id=fiche_id, 
                        user=request.user,
                        discipline=sequence.discipline
                    )
                    # Utiliser la nouvelle relation ForeignKey
                    fiche.sequence_obj = sequence
                    fiche.save()
                    updated_count += 1
                except Fiche.DoesNotExist:
                    continue
            
            if updated_count > 0:
                messages.success(
                    request, 
                    f'{updated_count} séance(s) ajoutée(s) à la séquence "{sequence.name}"'
                )
            else:
                messages.warning(request, 'Aucune séance n\'a pu être ajoutée')
        else:
            messages.warning(request, 'Veuillez sélectionner au moins une séance')
        
        return redirect('sequences:sequences_detail', sequence_id=sequence.id)
    
    # Récupérer toutes les séances (fiches) de cette séquence
    seances = sequence.get_seances()
    
    # Utiliser les champs persistants pour les statistiques
    stats = {
        'total_seances': seances.count(),
        'total_duration': sequence.get_total_duration_str(),
        'total_minutes': sequence.total_duration_minutes,
        'progression': sequence.get_progression_percentage(),
        'competences_count': sequence.get_competences().count(),
        'prochaine_seance': sequence.get_next_seance_number(),
    }
    
    # Récupérer les séances disponibles pour cette discipline (pas encore dans une séquence)
    available_fiches = Fiche.objects.filter(
        user=request.user,
        discipline=sequence.discipline,
        sequence_obj__isnull=True
    ).order_by('-created_at')  # Plus récentes en premier
    
    # Calculer le pourcentage de progression pour l'affichage
    completion_percentage = stats['progression'] if stats['progression'] is not None else 0
    
    return render(request, 'sequences/sequences_detail.html', {
        'sequence': sequence,
        'seances': seances,
        'sessions': seances,  # Compatibilité avec le template
        'stats': stats,
        'available_fiches': available_fiches,
        'completion_percentage': completion_percentage,
    })


@login_required
def recalculate_progression(request, sequence_id):
    """Vue AJAX pour recalculer la progression d'une séquence"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
    
    sequence = get_object_or_404(Sequence, id=sequence_id, user=request.user)
    
    try:
        # Mettre à jour la durée totale
        sequence.update_total_duration()
        
        # Recalculer les statistiques
        seances = sequence.get_seances()
        stats = {
            'total_seances': seances.count(),
            'total_duration': sequence.get_total_duration_str(),
            'total_minutes': sequence.total_duration_minutes,
            'progression': sequence.get_progression_percentage(),
            'competences_count': sequence.get_competences().count(),
            'prochaine_seance': sequence.get_next_seance_number(),
        }
        
        completion_percentage = stats['progression'] if stats['progression'] is not None else 0
        
        return JsonResponse({
            'success': True,
            'stats': {
                'total_seances': stats['total_seances'],
                'total_duration': stats['total_duration'],
                'progression': stats['progression'],
                'completion_percentage': completion_percentage,
                'competences_count': stats['competences_count'],
            },
            'message': 'Progression recalculée avec succès !'
        })
        
    except Exception as e:
        logger.error(f"Erreur lors du recalcul de la progression: {e}")
        return JsonResponse({
            'success': False,
            'error': 'Erreur lors du recalcul de la progression'
        }, status=500)


@login_required
def sequences_edit(request, sequence_id):
    """Modifier une séquence"""
    sequence = get_object_or_404(Sequence, id=sequence_id, user=request.user)
    disciplines = Page.objects.filter(parent__isnull=True).order_by('title')
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        discipline_id = request.POST.get('discipline')
        description = request.POST.get('description', '').strip()
        duree_estimee = request.POST.get('duration')
        niveau = request.POST.get('level')
        
        # Validation
        if not name:
            messages.error(request, 'Le nom de la séquence est obligatoire.')
        elif not discipline_id:
            messages.error(request, 'Veuillez sélectionner une discipline.')
        else:
            try:
                discipline = Page.objects.get(id=discipline_id, parent__isnull=True)
                
                # Vérifier l'unicité du nom (sauf pour la séquence actuelle)
                existing = Sequence.objects.filter(
                    user=request.user, 
                    name=name, 
                    discipline=discipline
                ).exclude(id=sequence.id)
                
                if existing.exists():
                    messages.error(request, f'Une séquence nommée "{name}" existe déjà pour cette discipline.')
                else:
                    # Mettre à jour la séquence
                    old_name = sequence.name
                    sequence.name = name
                    sequence.discipline = discipline
                    sequence.description = description
                    sequence.duree_estimee = int(duree_estimee) if duree_estimee else None
                    sequence.niveau = niveau if niveau else ''
                    sequence.save()
                    
                    # Mettre à jour le champ sequence dans les fiches associées
                    if old_name != name:
                        Fiche.objects.filter(
                            user=request.user,
                            sequence=old_name,
                            discipline=discipline
                        ).update(sequence=name)
                    
                    messages.success(request, f'La séquence "{name}" a été modifiée avec succès!')
                    return redirect('sequences:sequences_detail', sequence_id=sequence.id)
                    
            except Page.DoesNotExist:
                messages.error(request, 'Discipline invalide.')
            except Exception as e:
                logger.error(f"Erreur lors de la modification de la séquence: {e}")
                messages.error(request, 'Erreur lors de la modification de la séquence.')
    
    return render(request, 'sequences/sequences_edit.html', {
        'sequence': sequence,
        'disciplines': disciplines,
    })


@login_required
def sequences_delete(request, sequence_id):
    """Supprimer une séquence"""
    sequence = get_object_or_404(Sequence, id=sequence_id, user=request.user)
    
    if request.method == 'POST':
        sequence_name = sequence.name
        
        # Supprimer la référence de séquence dans les fiches associées
        # (on ne supprime pas les fiches, juste la référence)
        updated_count = Fiche.objects.filter(
            user=request.user,
            sequence=sequence.name,
            discipline=sequence.discipline
        ).update(sequence='')
        
        # Supprimer la séquence
        sequence.delete()
        
        messages.success(
            request, 
            f'La séquence "{sequence_name}" a été supprimée. '
            f'{updated_count} séance(s) ont été détachée(s) de cette séquence.'
        )
        
        return redirect('sequences:sequences_list')
    
    # Afficher la page de confirmation
    seances_count = sequence.get_seances_count()
    
    return render(request, 'sequences/sequences_delete.html', {
        'sequence': sequence,
        'seances_count': seances_count,
    })


@login_required
def sequences_by_discipline(request, discipline_id):
    """API pour récupérer les séquences d'une discipline (pour AJAX)"""
    try:
        discipline = Page.objects.get(id=discipline_id, parent__isnull=True)
        
        sequences = Sequence.objects.filter(
            user=request.user,
            discipline=discipline
        ).order_by('ordre', 'name')
        
        sequences_data = []
        for sequence in sequences:
            sequences_data.append({
                'id': sequence.id,
                'name': sequence.name,
                'description': sequence.description,
                'seances_count': sequence.get_seances_count(),
                'progression': sequence.get_progression_percentage(),
                'niveau': sequence.get_niveau_display() if sequence.niveau else None,
                'created_at': sequence.created_at.strftime('%d/%m/%Y'),
                'updated_at': sequence.updated_at.strftime('%d/%m/%Y'),
            })
        
        return JsonResponse({
            'success': True,
            'sequences': sequences_data,
            'discipline_name': discipline.title,
        })
        
    except Page.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Discipline non trouvée'
        })
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des séquences: {e}")
        return JsonResponse({
            'success': False,
            'error': 'Erreur serveur'
        })


@login_required
def add_seance_to_sequence(request, sequence_id):
    """Afficher les séances existantes de la discipline pour les ajouter à la séquence"""
    sequence = get_object_or_404(Sequence, id=sequence_id, user=request.user)
    
    if request.method == 'POST':
        # Traitement de l'ajout de séances à la séquence
        selected_fiches = request.POST.getlist('selected_fiches')
        
        if selected_fiches:
            # Mettre à jour les fiches sélectionnées avec le nom de la séquence
            from fiches.models import Fiche
            updated_count = 0
            
            for fiche_id in selected_fiches:
                try:
                    fiche = Fiche.objects.get(
                        id=fiche_id, 
                        user=request.user,
                        discipline=sequence.discipline
                    )
                    # Utiliser la nouvelle relation ForeignKey
                    fiche.sequence_obj = sequence
                    fiche.save()
                    updated_count += 1
                except Fiche.DoesNotExist:
                    continue
            
            if updated_count > 0:
                messages.success(
                    request, 
                    f'{updated_count} séance(s) ajoutée(s) à la séquence "{sequence.name}"'
                )
            else:
                messages.warning(request, 'Aucune séance n\'a pu être ajoutée')
        else:
            messages.warning(request, 'Veuillez sélectionner au moins une séance')
        
        return redirect('sequences:sequences_detail', sequence_id=sequence.id)
    
    # GET: Afficher les séances disponibles
    from fiches.models import Fiche
    from django.db.models import Q
    
    # Récupérer toutes les fiches de l'utilisateur pour cette discipline
    # qui ne sont pas encore dans une séquence (sequence_obj null)
    available_fiches = Fiche.objects.filter(
        user=request.user,
        discipline=sequence.discipline,
        sequence_obj__isnull=True
    ).order_by('created_at', 'id')  # Ordre de création (plus anciennes en premier)
    
    # Récupérer aussi les séances déjà dans cette séquence
    current_fiches = Fiche.objects.filter(
        user=request.user,
        discipline=sequence.discipline,
        sequence_obj=sequence
    ).order_by('created_at', 'id')  # Ordre de création (plus anciennes en premier)
    
    context = {
        'sequence': sequence,
        'available_fiches': available_fiches,
        'current_fiches': current_fiches,
    }
    
    return render(request, 'sequences/add_seance_to_sequence.html', context)


@login_required
def move_sequence_to_period(request):
    """API pour déplacer une séquence vers une période via drag-and-drop"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Méthode non autorisée'})
    
    try:
        sequence_id = request.POST.get('sequence_id')
        period_id = request.POST.get('period_id')  # None si on retire de la période
        
        # Vérifier que la séquence appartient à l'utilisateur
        sequence = get_object_or_404(Sequence, id=sequence_id, user=request.user)
        
        # Si period_id est fourni, vérifier que la période appartient à l'utilisateur
        if period_id:
            periode = get_object_or_404(PeriodeScolaire, id=period_id, user=request.user)
            sequence.periode_scolaire = periode
            message = f'Séquence "{sequence.name}" déplacée vers {periode.nom}'
        else:
            sequence.periode_scolaire = None
            message = f'Séquence "{sequence.name}" retirée de sa période'
        
        sequence.save()
        
        return JsonResponse({
            'success': True,
            'message': message
        })
        
    except Exception as e:
        logger.error(f'Erreur lors du déplacement de séquence: {e}')
        return JsonResponse({
            'success': False,
            'error': 'Erreur lors du déplacement de la séquence'
        })


@login_required
@require_http_methods(["POST"])
def create_multiple_sessions(request):
    """
    Créer plusieurs séances d'un coup avec des paramètres similaires
    """
    try:
        data = json.loads(request.body)
        
        # Validation des données
        title = data.get('title', '').strip()
        count = int(data.get('count', 0))
        duration = int(data.get('duration', 60))
        interval = int(data.get('interval', 7))
        start_date_str = data.get('startDate', '')
        start_time_str = data.get('startTime', '08:00')
        description = data.get('description', '').strip()
        sequence_id = int(data.get('sequenceId', 0))
        
        # Validation
        if not title or count < 1 or count > 20:
            return JsonResponse({
                'success': False,
                'message': 'Données invalides. Vérifiez le titre et le nombre de séances (1-20).'
            })
        
        # Vérifier que la séquence appartient à l'utilisateur
        try:
            sequence = Sequence.objects.get(id=sequence_id, user=request.user)
            logger.info(f"Sequence found: {sequence.name} (ID: {sequence.id})")
        except Sequence.DoesNotExist:
            logger.error(f"Sequence not found: ID {sequence_id} for user {request.user.id}")
            return JsonResponse({
                'success': False,
                'message': f'Séquence introuvable (ID: {sequence_id}).'
            })
        
        try:
            # Récupérer la discipline depuis la séquence plutôt que par ID séparé
            discipline = sequence.discipline
            if not discipline:
                logger.error(f"No discipline associated with sequence {sequence.id}")
                return JsonResponse({
                    'success': False,
                    'message': 'Aucune discipline associée à cette séquence.'
                })
            logger.info(f"Discipline found: {discipline.title} (ID: {discipline.id})")
        except Exception as e:
            logger.error(f"Error getting discipline: {e}")
            return JsonResponse({
                'success': False,
                'message': f'Erreur lors de la récupération de la discipline: {str(e)}'
            })
        
        # Parser la date et l'heure de début
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
        except ValueError:
            return JsonResponse({
                'success': False,
                'message': 'Format de date ou d\'heure invalide.'
            })
        
        # Calculer l'heure de fin
        start_datetime = datetime.combine(start_date, start_time)
        end_datetime = start_datetime + timedelta(minutes=duration)
        end_time = end_datetime.time()
        
        # Récupérer la couleur personnalisée de l'utilisateur pour cette discipline
        couleur = UserDisciplineColorPreference.get_user_discipline_color(request.user, discipline)
        
        created_sessions = []
        
        # Créer les séances
        for i in range(1, count + 1):
            # Calculer la date de cette séance
            session_date = start_date + timedelta(days=(i - 1) * interval)
            
            # Créer la fiche (séance)
            fiche = Fiche.objects.create(
                user=request.user,
                titre=f"{title} {i}",
                discipline=discipline,
                date=session_date,
                heure_debut=start_time,
                heure_fin=end_time,
                couleur=couleur,
                # sequence_obj=sequence,  # Ne pas assigner automatiquement - laisser dans "Séances disponibles"
                bilan=description if description else f"Séance {i} de la séquence {sequence.name}"
            )
            
            created_sessions.append({
                'id': fiche.id,
                'title': fiche.titre,
                'date': session_date.strftime('%d/%m/%Y'),
                'time': f"{start_time_str} - {end_time.strftime('%H:%M')}"
            })
        
        # Recalculer les statistiques de la séquence
        sequence.recalculate_stats()
        
        return JsonResponse({
            'success': True,
            'message': f'{count} séances créées avec succès!',
            'created_count': count,
            'sessions': created_sessions
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Données JSON invalides.'
        })
    except ValueError as e:
        return JsonResponse({
            'success': False,
            'message': f'Erreur de validation: {str(e)}'
        })
    except Exception as e:
        logger.error(f"Erreur lors de la création de plusieurs séances: {e}")
        return JsonResponse({
            'success': False,
            'message': 'Une erreur inattendue s\'est produite.'
        })
