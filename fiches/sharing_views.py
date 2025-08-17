from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.db import transaction
from django.db import models
from django.contrib.auth.models import User
from .models import Fiche, Phase
from pages.models import Page
import json
import copy

def my_fiches_to_share(request):
    """API pour récupérer les fiches de l'utilisateur connecté avec leur statut de partage"""
    # Vérifier l'authentification pour les requêtes AJAX
    if not request.user.is_authenticated:
        return JsonResponse({
            'success': False,
            'error': 'Authentification requise',
            'redirect': '/fiches/login/'
        }, status=401)
    
    try:
        fiches = Fiche.objects.filter(user=request.user).select_related('discipline').order_by('-created_at')
        
        fiches_data = []
        for fiche in fiches:
            fiches_data.append({
                'id': fiche.id,
                'titre': fiche.titre,
                'discipline_nom': fiche.discipline.title if fiche.discipline else 'Sans discipline',
                'date': fiche.date.strftime('%d/%m/%Y'),
                'niveau': fiche.get_niveau_display() if fiche.niveau else '',
                'is_shared': fiche.is_shared,
                'import_count': fiche.import_count,
                'shared_at': fiche.shared_at.strftime('%d/%m/%Y %H:%M') if fiche.shared_at else None
            })
        
        return JsonResponse({
            'success': True,
            'fiches': fiches_data
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

def community_fiches(request):
    """API pour récupérer les fiches partagées par la communauté (autres utilisateurs)"""
    # Vérifier l'authentification pour les requêtes AJAX
    if not request.user.is_authenticated:
        return JsonResponse({
            'success': False,
            'error': 'Authentification requise',
            'redirect': '/fiches/login/'
        }, status=401)
    
    try:
        # Récupérer toutes les fiches partagées sauf celles de l'utilisateur connecté
        fiches = Fiche.objects.filter(
            is_shared=True
        ).exclude(
            user=request.user
        ).select_related('user', 'discipline').order_by('-shared_at')
        
        fiches_data = []
        for fiche in fiches:
            # Déterminer l'auteur original
            auteur = fiche.original_author.username if fiche.original_author else fiche.user.username
            
            fiches_data.append({
                'id': fiche.id,
                'titre': fiche.titre,
                'discipline_nom': fiche.discipline.title if fiche.discipline else 'Sans discipline',
                'date': fiche.date.strftime('%d/%m/%Y'),
                'niveau': fiche.get_niveau_display() if fiche.niveau else 'Tous niveaux',
                'auteur': auteur,
                'import_count': fiche.import_count,
                'shared_at': fiche.shared_at.strftime('%d/%m/%Y') if fiche.shared_at else None
            })
        
        return JsonResponse({
            'success': True,
            'fiches': fiches_data
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

@login_required
@require_http_methods(["POST"])
def toggle_share(request):
    """API pour basculer le statut de partage d'une fiche"""
    # Vérifier l'authentification pour les requêtes AJAX
    if not request.user.is_authenticated:
        return JsonResponse({
            'success': False,
            'error': 'Authentification requise',
            'redirect': '/fiches/login/'
        }, status=401)
    
    try:
        data = json.loads(request.body)
        fiche_id = data.get('fiche_id')
        is_shared = data.get('is_shared', False)
        
        # Vérifier que la fiche appartient à l'utilisateur
        fiche = Fiche.objects.get(id=fiche_id, user=request.user)
        
        fiche.is_shared = is_shared
        if is_shared:
            fiche.shared_at = timezone.now()
        else:
            fiche.shared_at = None
            
        fiche.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Statut de partage mis à jour avec succès'
        })
        
    except Fiche.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Fiche non trouvée ou non autorisée'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

@login_required
@require_http_methods(["POST"])
def import_fiche(request):
    """API pour importer une fiche partagée dans l'espace personnel de l'utilisateur"""
    # Vérifier l'authentification pour les requêtes AJAX
    if not request.user.is_authenticated:
        return JsonResponse({
            'success': False,
            'error': 'Authentification requise',
            'redirect': '/fiches/login/'
        }, status=401)
    
    try:
        data = json.loads(request.body)
        fiche_id = data.get('fiche_id')
        
        # Récupérer la fiche originale (doit être partagée et pas de l'utilisateur connecté)
        original_fiche = Fiche.objects.get(
            id=fiche_id, 
            is_shared=True
        )
        
        # Vérifier que l'utilisateur n'importe pas sa propre fiche
        if original_fiche.user == request.user:
            return JsonResponse({
                'success': False,
                'error': 'Vous ne pouvez pas importer votre propre fiche'
            })
        
        # Vérifier si l'utilisateur a déjà importé cette fiche
        existing_import = Fiche.objects.filter(
            user=request.user,
            titre=f"[Importé] {original_fiche.titre}",
            original_author=original_fiche.user
        ).exists()
        
        if existing_import:
            return JsonResponse({
                'success': False,
                'error': 'Vous avez déjà importé cette fiche'
            })
        
        with transaction.atomic():
            # Créer une copie de la fiche pour l'utilisateur connecté
            new_fiche = Fiche.objects.create(
                user=request.user,
                titre=f"[Importé] {original_fiche.titre}",
                discipline=original_fiche.discipline,
                date=original_fiche.date,
                heure_debut=original_fiche.heure_debut,
                heure_fin=original_fiche.heure_fin,
                duree=original_fiche.duree,
                sequence=original_fiche.sequence,
                niveau=original_fiche.niveau,
                bilan=original_fiche.bilan,
                couleur=original_fiche.couleur,
                is_shared=False,  # Les fiches importées ne sont pas partagées par défaut
                original_author=original_fiche.user  # Référence vers l'auteur original
            )
            
            # Copier les compétences associées
            new_fiche.competences.set(original_fiche.competences.all())
            
            # Copier les phases associées
            for phase in original_fiche.phases.all():
                Phase.objects.create(
                    fiche=new_fiche,
                    phase=phase.phase,
                    duree=phase.duree,
                    ce=phase.ce,
                    deroulement=phase.deroulement,
                    posture=phase.posture,
                    ordre=phase.ordre
                )
            
            # Incrémenter le compteur d'importations de la fiche originale
            original_fiche.import_count += 1
            original_fiche.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Fiche importée avec succès',
            'new_fiche_id': new_fiche.id
        })
        
    except Fiche.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Fiche non trouvée ou non partagée'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

def sharing_stats(request):
    """API pour récupérer les statistiques de partage de l'utilisateur"""
    # Vérifier l'authentification pour les requêtes AJAX
    if not request.user.is_authenticated:
        return JsonResponse({
            'success': False,
            'error': 'Authentification requise',
            'redirect': '/fiches/login/'
        }, status=401)
    
    try:
        user_stats = {
            'total_fiches': Fiche.objects.filter(user=request.user).count(),
            'shared_fiches': Fiche.objects.filter(user=request.user, is_shared=True).count(),
            'total_imports': Fiche.objects.filter(user=request.user, is_shared=True).aggregate(
                total=models.Sum('import_count')
            )['total'] or 0,
            'imported_fiches': Fiche.objects.filter(user=request.user, original_author__isnull=False).count()
        }
        
        return JsonResponse({
            'success': True,
            'stats': user_stats
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
