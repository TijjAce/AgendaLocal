from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from .models import UserProfile, Friendship, SharedSequence, SharedFiche
from sequences.models import Sequence
from fiches.models import Fiche
from .avatar_generator import AvatarGenerator
import json

@login_required
def friends_dashboard(request):
    """Tableau de bord principal des amis"""
    # Créer le profil utilisateur s'il n'existe pas
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Récupérer les amis
    friends = Friendship.get_friends(request.user)
    
    # Récupérer les demandes d'amitié en attente
    pending_requests = Friendship.objects.filter(
        addressee=request.user, 
        status='pending'
    ).select_related('requester')
    
    # Récupérer les séquences et fiches partagées récemment
    recent_shared_sequences = SharedSequence.objects.filter(
        shared_with=request.user
    ).select_related('sequence', 'shared_by')[:5]
    
    recent_shared_fiches = SharedFiche.objects.filter(
        shared_with=request.user
    ).select_related('fiche', 'shared_by')[:5]
    
    context = {
        'profile': profile,
        'friends': friends,
        'pending_requests': pending_requests,
        'recent_shared_sequences': recent_shared_sequences,
        'recent_shared_fiches': recent_shared_fiches,
    }
    
    return render(request, 'friends/dashboard.html', context)

@login_required
def add_friend(request):
    """Ajouter un ami par identifiant"""
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        
        if not username:
            messages.error(request, "Veuillez entrer un identifiant utilisateur.")
            return redirect('friends:dashboard')
        
        if username == request.user.username:
            messages.error(request, "Vous ne pouvez pas vous ajouter vous-même comme ami.")
            return redirect('friends:dashboard')
        
        try:
            friend_user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, f"L'utilisateur '{username}' n'existe pas.")
            return redirect('friends:dashboard')
        
        # Vérifier si une demande d'amitié existe déjà
        existing_friendship = Friendship.objects.filter(
            Q(requester=request.user, addressee=friend_user) |
            Q(requester=friend_user, addressee=request.user)
        ).first()
        
        if existing_friendship:
            if existing_friendship.status == 'accepted':
                messages.info(request, f"Vous êtes déjà ami avec {username}.")
            elif existing_friendship.status == 'pending':
                messages.info(request, f"Une demande d'amitié avec {username} est déjà en attente.")
            elif existing_friendship.status == 'blocked':
                messages.error(request, f"Impossible d'ajouter {username} comme ami.")
            else:
                # Renouveler la demande si elle avait été refusée
                existing_friendship.status = 'pending'
                existing_friendship.requester = request.user
                existing_friendship.addressee = friend_user
                existing_friendship.save()
                messages.success(request, f"Demande d'amitié envoyée à {username}.")
        else:
            # Créer une nouvelle demande d'amitié
            Friendship.objects.create(
                requester=request.user,
                addressee=friend_user,
                status='pending'
            )
            messages.success(request, f"Demande d'amitié envoyée à {username}.")
    
    return redirect('friends:dashboard')

@login_required
def respond_friend_request(request, friendship_id):
    """Répondre à une demande d'amitié"""
    friendship = get_object_or_404(
        Friendship, 
        id=friendship_id, 
        addressee=request.user, 
        status='pending'
    )
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'accept':
            friendship.status = 'accepted'
            friendship.save()
            messages.success(request, f"Vous êtes maintenant ami avec {friendship.requester.username}.")
        elif action == 'decline':
            friendship.status = 'declined'
            friendship.save()
            messages.info(request, f"Demande d'amitié de {friendship.requester.username} refusée.")
    
    return redirect('friends:dashboard')

@login_required
def france_map(request):
    """Afficher la carte de France avec les amis"""
    # Créer le profil utilisateur s'il n'existe pas
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Récupérer tous les amis avec leur localisation
    friends = Friendship.get_friends(request.user)
    friends_with_location = []
    
    for friend in friends:
        friend_profile, _ = UserProfile.objects.get_or_create(user=friend)
        if friend_profile.has_location and friend_profile.is_public:
            friends_with_location.append({
                'username': friend.username,
                'first_name': friend.first_name,
                'last_name': friend.last_name,
                'latitude': friend_profile.latitude,
                'longitude': friend_profile.longitude,
                'ville': friend_profile.ville,
                'departement': friend_profile.departement,
                'bitmoji_url': friend_profile.bitmoji_url,
                'bio': friend_profile.bio,
            })
    
    context = {
        'profile': profile,
        'friends_with_location': json.dumps(friends_with_location),
        'user_location': {
            'latitude': profile.latitude,
            'longitude': profile.longitude,
            'ville': profile.ville,
            'departement': profile.departement,
        } if profile.has_location else None,
    }
    
    return render(request, 'friends/france_map.html', context)

@login_required
def update_profile(request):
    """Mettre à jour le profil utilisateur"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Mettre à jour les informations du profil
        profile.bitmoji_url = request.POST.get('bitmoji_url', '').strip()
        profile.ville = request.POST.get('ville', '').strip()
        profile.departement = request.POST.get('departement', '').strip()
        profile.bio = request.POST.get('bio', '').strip()
        profile.is_public = request.POST.get('is_public') == 'on'
        
        # Mettre à jour les champs d'avatar
        profile.avatar_type = request.POST.get('avatar_type', 'generated')
        if profile.avatar_type == 'generated':
            profile.avatar_skin_color = request.POST.get('avatar_skin_color', '#FDBCB4')
            profile.avatar_hair_style = request.POST.get('avatar_hair_style', 'short')
            profile.avatar_hair_color = request.POST.get('avatar_hair_color', '#8B4513')
            profile.avatar_eye_color = request.POST.get('avatar_eye_color', '#4A90E2')
            profile.avatar_clothing_color = request.POST.get('avatar_clothing_color', '#2E86AB')
            profile.avatar_accessories = request.POST.get('avatar_accessories', 'none')
        
        # Mettre à jour la localisation si fournie
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        if latitude and longitude:
            try:
                profile.latitude = float(latitude)
                profile.longitude = float(longitude)
            except ValueError:
                messages.error(request, "Coordonnées invalides.")
                return redirect('friends:update_profile')
        
        profile.save()
        messages.success(request, "Profil mis à jour avec succès.")
        return redirect('friends:dashboard')
    
    return render(request, 'friends/update_profile.html', {'profile': profile})

@login_required
def share_sequence(request, sequence_id):
    """Partager une séquence avec un ami"""
    sequence = get_object_or_404(Sequence, id=sequence_id, user=request.user)
    friends = Friendship.get_friends(request.user)
    
    if request.method == 'POST':
        friend_username = request.POST.get('friend_username')
        message = request.POST.get('message', '').strip()
        can_edit = request.POST.get('can_edit') == 'on'
        
        try:
            friend = User.objects.get(username=friend_username)
            if friend not in friends:
                messages.error(request, "Vous ne pouvez partager qu'avec vos amis.")
                return redirect('friends:share_sequence', sequence_id=sequence_id)
            
            # Vérifier si déjà partagée
            existing_share = SharedSequence.objects.filter(
                sequence=sequence,
                shared_by=request.user,
                shared_with=friend
            ).first()
            
            if existing_share:
                messages.info(request, f"Cette séquence est déjà partagée avec {friend.username}.")
            else:
                # Créer le partage de la séquence
                SharedSequence.objects.create(
                    sequence=sequence,
                    shared_by=request.user,
                    shared_with=friend,
                    message=message,
                    can_edit=can_edit
                )
                
                # Partager automatiquement toutes les fiches (séances) associées à la séquence
                fiches_associees = sequence.seances.all()
                fiches_partagees = 0
                
                for fiche in fiches_associees:
                    # Vérifier si la fiche n'est pas déjà partagée avec cet ami
                    existing_fiche_share = SharedFiche.objects.filter(
                        fiche=fiche,
                        shared_by=request.user,
                        shared_with=friend
                    ).first()
                    
                    if not existing_fiche_share:
                        SharedFiche.objects.create(
                            fiche=fiche,
                            shared_by=request.user,
                            shared_with=friend,
                            message=f"Fiche partagée automatiquement avec la séquence '{sequence.name}'",
                            can_edit=can_edit  # Même permission que la séquence
                        )
                        fiches_partagees += 1
                
                # Message de succès avec détails
                if fiches_partagees > 0:
                    messages.success(request, f"Séquence partagée avec {friend.username}. {fiches_partagees} fiche(s) associée(s) ont aussi été partagées automatiquement.")
                else:
                    messages.success(request, f"Séquence partagée avec {friend.username}.")
            
            return redirect('friends:dashboard')
            
        except User.DoesNotExist:
            messages.error(request, "Ami introuvable.")
    
    context = {
        'sequence': sequence,
        'friends': friends,
    }
    return render(request, 'friends/share_sequence.html', context)

@login_required
def share_fiche(request, fiche_id):
    """Partager une fiche avec un ami"""
    fiche = get_object_or_404(Fiche, id=fiche_id, user=request.user)
    friends = Friendship.get_friends(request.user)
    
    if request.method == 'POST':
        friend_username = request.POST.get('friend_username')
        message = request.POST.get('message', '').strip()
        can_edit = request.POST.get('can_edit') == 'on'
        
        try:
            friend = User.objects.get(username=friend_username)
            if friend not in friends:
                messages.error(request, "Vous ne pouvez partager qu'avec vos amis.")
                return redirect('friends:share_fiche', fiche_id=fiche_id)
            
            # Vérifier si déjà partagée
            existing_share = SharedFiche.objects.filter(
                fiche=fiche,
                shared_by=request.user,
                shared_with=friend
            ).first()
            
            if existing_share:
                messages.info(request, f"Cette fiche est déjà partagée avec {friend.username}.")
            else:
                SharedFiche.objects.create(
                    fiche=fiche,
                    shared_by=request.user,
                    shared_with=friend,
                    message=message,
                    can_edit=can_edit
                )
                messages.success(request, f"Fiche partagée avec {friend.username}.")
            
            return redirect('friends:dashboard')
            
        except User.DoesNotExist:
            messages.error(request, "Ami introuvable.")
    
    context = {
        'fiche': fiche,
        'friends': friends,
    }
    return render(request, 'friends/share_fiche.html', context)

@login_required
def shared_content(request):
    """Afficher le contenu partagé avec l'utilisateur"""
    shared_sequences = SharedSequence.objects.filter(
        shared_with=request.user
    ).select_related('sequence', 'shared_by').order_by('-created_at')
    
    shared_fiches = SharedFiche.objects.filter(
        shared_with=request.user
    ).select_related('fiche', 'shared_by').order_by('-created_at')
    
    context = {
        'shared_sequences': shared_sequences,
        'shared_fiches': shared_fiches,
    }
    
    return render(request, 'friends/shared_content.html', context)

@login_required
def update_location_ajax(request):
    """Mettre à jour la localisation via AJAX"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latitude = float(data.get('latitude'))
            longitude = float(data.get('longitude'))
            
            # Vérifier que les coordonnées sont dans les limites de la France
            if not (41.0 <= latitude <= 51.5 and -5.5 <= longitude <= 10.0):
                return JsonResponse({'success': False, 'error': 'Coordonnées hors de France'})
            
            profile, created = UserProfile.objects.get_or_create(user=request.user)
            profile.latitude = latitude
            profile.longitude = longitude
            profile.save()
            
            return JsonResponse({'success': True})
            
        except (ValueError, json.JSONDecodeError):
            return JsonResponse({'success': False, 'error': 'Données invalides'})
    
    return JsonResponse({'success': False, 'error': 'Méthode non autorisée'})

@login_required
def simple_map(request):
    """Carte simple pour test Leaflet"""
    return render(request, 'friends/simple_map.html')

@login_required
def shared_fiche_detail(request, fiche_id):
    """Afficher une fiche partagée avec l'utilisateur connecté"""
    # Vérifier que la fiche est bien partagée avec l'utilisateur connecté
    try:
        shared_fiche = SharedFiche.objects.get(
            fiche_id=fiche_id,
            shared_with=request.user
        )
    except SharedFiche.DoesNotExist:
        # Afficher une page d'erreur personnalisée au lieu d'une 404 générique
        return render(request, 'friends/shared_fiche_not_found.html', {
            'fiche_id': fiche_id,
        }, status=404)
    
    fiche = shared_fiche.fiche
    phases = fiche.phases.all().order_by('ordre')
    
    context = {
        'fiche': fiche,
        'phases': phases,
        'shared_fiche': shared_fiche,
        'is_shared_view': True,  # Pour adapter le template
        'can_edit': shared_fiche.can_edit,
    }
    
    return render(request, 'friends/shared_sequence_detail.html', {
        'shared_sequence': shared_sequence,
        'sequence': shared_sequence.sequence,
    })


@login_required
def generate_avatar_svg(request):
    """Génère un avatar SVG pour l'utilisateur connecté"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Générer le SVG de l'avatar
    svg_content = AvatarGenerator.generate_svg_avatar(profile)
    
    # Retourner le SVG avec le bon content-type
    response = HttpResponse(svg_content, content_type='image/svg+xml')
    response['Cache-Control'] = 'no-cache'  # Pas de cache pour voir les changements immédiatement
    return response


@login_required
@require_http_methods(["POST"])
def update_avatar_config(request):
    """Met à jour la configuration de l'avatar de l'utilisateur"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    try:
        data = json.loads(request.body)
        
        # Mettre à jour les champs de configuration de l'avatar
        if 'avatar_type' in data:
            profile.avatar_type = data['avatar_type']
        if 'avatar_skin_color' in data:
            profile.avatar_skin_color = data['avatar_skin_color']
        if 'avatar_hair_style' in data:
            profile.avatar_hair_style = data['avatar_hair_style']
        if 'avatar_hair_color' in data:
            profile.avatar_hair_color = data['avatar_hair_color']
        if 'avatar_eye_color' in data:
            profile.avatar_eye_color = data['avatar_eye_color']
        if 'avatar_clothing_color' in data:
            profile.avatar_clothing_color = data['avatar_clothing_color']
        if 'avatar_accessories' in data:
            profile.avatar_accessories = data['avatar_accessories']
        
        profile.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Avatar mis à jour avec succès'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Données JSON invalides'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Erreur lors de la mise à jour: {str(e)}'
        }, status=500)


@login_required
@require_http_methods(["POST"])
def randomize_avatar(request):
    """Génère une configuration aléatoire pour l'avatar"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    try:
        # Générer une configuration aléatoire
        random_config = AvatarGenerator.get_random_config()
        
        # Appliquer la configuration au profil
        for key, value in random_config.items():
            setattr(profile, key, value)
        
        profile.avatar_type = 'generated'
        profile.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Avatar aléatoire généré avec succès',
            'config': random_config
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Erreur lors de la génération: {str(e)}'
        }, status=500)


@login_required
def shared_sequence_detail(request, sequence_id):
    """Afficher une séquence partagée avec l'utilisateur connecté"""
    # Vérifier que la séquence est bien partagée avec l'utilisateur connecté
    shared_sequence = get_object_or_404(
        SharedSequence,
        sequence_id=sequence_id,
        shared_with=request.user
    )
    
    sequence = shared_sequence.sequence
    seances = sequence.seances.all().order_by('date')
    
    context = {
        'sequence': sequence,
        'seances': seances,
        'shared_sequence': shared_sequence,
        'is_shared_view': True,  # Pour adapter le template
        'can_edit': shared_sequence.can_edit,
    }
    
    return render(request, 'friends/shared_sequence_detail.html', context)
