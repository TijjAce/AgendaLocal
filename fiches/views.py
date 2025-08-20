from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.conf import settings
from datetime import datetime, time
from urllib.parse import urljoin, urlparse
import json
import logging
import re
from io import BytesIO
from django.contrib import messages
from .models import Fiche, Phase, Annexe
from .forms import FicheForm, AnnexeForm, PhaseFormSet, AnnexeFormSet, FicheWithPhasesForm

from django.core.paginator import Paginator
from django.db.models import Q


# Initialize logger
logger = logging.getLogger(__name__)

# Models imports
from .models import Fiche, Phase, Annexe
from pages.models import Page
from sequences.models import Sequence
from main.models import UserDisciplineColorPreference

# Forms imports

# PDF libraries - WeasyPrint supprimé pour corriger les failles de sécurité
from xhtml2pdf import pisa


def process_images_for_pdf(html_content, request):
    """
    Traite les images dans le contenu HTML pour l'export PDF de manière sécurisée.
    Convertit uniquement les URLs relatives vers les médias autorisés.
    """
    import os.path
    from urllib.parse import urlparse
    
    def replace_img_src(match):
        img_tag = match.group(0)
        src_match = re.search(r'src=["\']([^"\'>]+)["\']', img_tag)
        
        if not src_match:
            return img_tag
        
        src = src_match.group(1)
        
        # Validation de sécurité : rejeter les URLs suspectes
        if any(dangerous in src.lower() for dangerous in ['../', '..\\', 'file://', 'javascript:', 'data:']):
            # Supprimer l'image dangereuse
            return '<!-- Image supprimée pour sécurité -->'
        
        # Si c'est déjà une URL absolue HTTP/HTTPS, la garder telle quelle
        if src.startswith(('http://', 'https://')):
            # Validation supplémentaire de l'URL
            try:
                parsed = urlparse(src)
                if parsed.scheme in ['http', 'https'] and parsed.netloc:
                    return img_tag
            except:
                return '<!-- URL invalide supprimée -->'
        
        # Si c'est une URL relative vers les médias de l'application
        if src.startswith(settings.MEDIA_URL):
            # Extraire le chemin relatif
            relative_path = src[len(settings.MEDIA_URL):]
            
            # Validation de sécurité : vérifier que le chemin ne sort pas du dossier media
            normalized_path = os.path.normpath(relative_path)
            if normalized_path.startswith('../') or '\\' in normalized_path:
                return '<!-- Chemin dangereux supprimé -->'
            
            # Construire le chemin absolu
            absolute_path = os.path.join(settings.MEDIA_ROOT, normalized_path)
            
            # Vérifier que le fichier existe et est dans le dossier autorisé
            if (os.path.exists(absolute_path) and 
                os.path.commonpath([absolute_path, settings.MEDIA_ROOT]) == settings.MEDIA_ROOT):
                
                # Vérifier l'extension du fichier
                _, ext = os.path.splitext(absolute_path.lower())
                if ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                    # Remplacer le src par le chemin absolu sécurisé
                    safe_path = absolute_path.replace(os.sep, "/")
                    new_img_tag = re.sub(
                        r'src=["\']([^"\'>]+)["\']',
                        f'src="file:///{safe_path}"',
                        img_tag
                    )
                    return new_img_tag
        
        # Pour les autres URLs relatives, les ignorer par sécurité
        return '<!-- Image non autorisée supprimée -->'
    
    # Remplacer toutes les balises img de manière sécurisée
    try:
        processed_html = re.sub(r'<img[^>]*>', replace_img_src, html_content)
        return processed_html
    except Exception as e:
        # En cas d'erreur, retourner le HTML original sans images
        return re.sub(r'<img[^>]*>', '<!-- Image supprimée suite à erreur -->', html_content)


# Créer une nouvelle fiche avec ses phases
@login_required
def fiche_create_view(request):
    discipline_id = request.GET.get('discipline_id')
    competence_id = request.GET.get('competence_id')
    date_param = request.GET.get('date')  # Paramètre de date depuis le calendrier
    sequence_param = request.GET.get('sequence')  # Paramètre de séquence
    initial = {}
    initial_competences = []

    # Préremplir la date si fournie depuis le calendrier
    if date_param:
        try:
            from datetime import datetime
            parsed_date = datetime.strptime(date_param, '%Y-%m-%d').date()
            initial['date'] = parsed_date
        except ValueError:
            pass  # Ignorer si le format de date est invalide

    if discipline_id:
        discipline = Page.objects.filter(id=discipline_id).first()
        if discipline:
            initial['discipline'] = discipline
            # Récupérer la couleur personnalisée de l'utilisateur pour cette discipline
            user_color = UserDisciplineColorPreference.get_user_discipline_color(request.user, discipline)
            initial['couleur'] = user_color
    
    if competence_id:
        competence = Page.objects.filter(id=competence_id).first()
        if competence:
            initial_competences.append(competence.id)
    
    # Pré-remplir la séquence si fournie depuis une séquence
    if sequence_param:
        try:
            # Vérifier que sequence_param est un entier valide
            sequence_id = int(sequence_param)
            sequence = Sequence.objects.get(id=sequence_id, user=request.user)
            initial['sequence'] = sequence
            # Récupérer le niveau de classe depuis la séquence
            if sequence.niveau:
                initial['niveau'] = sequence.niveau
            # Récupérer la discipline depuis la séquence
            if sequence.discipline:
                initial['discipline'] = sequence.discipline
                # Récupérer la couleur personnalisée de l'utilisateur pour cette discipline
                user_color = UserDisciplineColorPreference.get_user_discipline_color(request.user, sequence.discipline)
                initial['couleur'] = user_color
        except (ValueError, Sequence.DoesNotExist):
            pass  # Ignorer si sequence_param n'est pas un entier valide ou si la séquence n'existe pas

    if request.method == 'POST':
        fiche_form = FicheForm(request.POST)
        phase_formset = PhaseFormSet(request.POST)
        annexe_formset = AnnexeFormSet(request.POST, request.FILES)

        if fiche_form.is_valid() and phase_formset.is_valid() and annexe_formset.is_valid():
            fiche = fiche_form.save(commit=False)
            fiche.user = request.user  # Associe la fiche à l'utilisateur connecté
            fiche.save()  # Enregistre la fiche d'abord
            
            # Gestion manuelle des compétences ManyToMany
            competences = fiche_form.cleaned_data.get('competences', [])
            fiche.competences.set(competences)
            
            # Sauvegarde des phases
            phases = phase_formset.save(commit=False)
            for phase in phases:
                phase.fiche = fiche  # Associe la phase à la fiche
                phase.save()
            # Supprime les phases marquées pour suppression
            for phase in phase_formset.deleted_objects:
                phase.delete()
            
            # Sauvegarde des annexes
            annexes = annexe_formset.save(commit=False)
            for annexe in annexes:
                annexe.fiche = fiche  # Associe l'annexe à la fiche
                annexe.save()
            # Supprime les annexes marquées pour suppression
            for annexe in annexe_formset.deleted_objects:
                annexe.delete()
            
            messages.success(request, 'Fiche créée avec succès !')
            return redirect('fiche_detail', fiche_id=fiche.id)
        else:
            # Debug: Afficher les erreurs spécifiques du formulaire
            if fiche_form.errors:
                for field, errors in fiche_form.errors.items():
                    for error in errors:
                        messages.error(request, f'Erreur dans le champ "{field}": {error}')
            if phase_formset.errors:
                for i, form_errors in enumerate(phase_formset.errors):
                    if form_errors:
                        for field, errors in form_errors.items():
                            for error in errors:
                                messages.error(request, f'Erreur dans la phase {i+1}, champ "{field}": {error}')
            if annexe_formset.errors:
                for i, form_errors in enumerate(annexe_formset.errors):
                    if form_errors:
                        for field, errors in form_errors.items():
                            for error in errors:
                                messages.error(request, f'Erreur dans l\'annexe {i+1}, champ "{field}": {error}')
    else:
        fiche_form = FicheForm(initial=initial)
        # Préremplir les compétences si spécifiées
        if initial_competences:
            fiche_form.fields['competences'].initial = initial_competences
        phase_formset = PhaseFormSet()
        annexe_formset = AnnexeFormSet()

    return render(request, 'fiches/fiche_create.html', {
        'fiche_form': fiche_form,
        'phase_formset': phase_formset,
        'annexe_formset': annexe_formset
    })


# === Modifier une fiche existante + ses phases ===
@login_required
def fiche_edit_view(request, fiche_id):
    fiche = get_object_or_404(Fiche, id=fiche_id, user=request.user)

    if request.method == 'POST':
        fiche_form = FicheForm(request.POST, instance=fiche)
        phase_formset = PhaseFormSet(request.POST, instance=fiche)
        annexe_formset = AnnexeFormSet(request.POST, request.FILES, instance=fiche)

        if fiche_form.is_valid() and phase_formset.is_valid() and annexe_formset.is_valid():
            try:
                # Sauvegarder la fiche avec tous les champs
                fiche = fiche_form.save(commit=False)
                fiche.save()
                
                # Gestion manuelle des compétences ManyToMany
                competences = fiche_form.cleaned_data.get('competences', [])
                fiche.competences.set(competences)
                
                # Sauvegarder les phases
                phases = phase_formset.save(commit=False)
                for phase in phases:
                    phase.fiche = fiche
                    phase.save()
                
                # Supprimer les phases marquées pour suppression
                for phase in phase_formset.deleted_objects:
                    phase.delete()
                
                # Sauvegarder les annexes
                annexes = annexe_formset.save(commit=False)
                for annexe in annexes:
                    annexe.fiche = fiche
                    annexe.save()
                
                # Supprimer les annexes marquées pour suppression
                for annexe in annexe_formset.deleted_objects:
                    annexe.delete()
                
                messages.success(request, 'Fiche modifiée avec succès!')
                return redirect('fiche_detail', fiche_id=fiche.id)
            except Exception as e:
                messages.error(request, f'Erreur lors de la sauvegarde: {str(e)}')
        else:
            # Debug: Afficher les erreurs spécifiques du formulaire
            if fiche_form.errors:
                for field, errors in fiche_form.errors.items():
                    for error in errors:
                        messages.error(request, f'Erreur dans le champ "{field}": {error}')
            if phase_formset.errors:
                for i, form_errors in enumerate(phase_formset.errors):
                    if form_errors:
                        for field, errors in form_errors.items():
                            for error in errors:
                                messages.error(request, f'Erreur dans la phase {i+1}, champ "{field}": {error}')
            if annexe_formset.errors:
                for i, form_errors in enumerate(annexe_formset.errors):
                    if form_errors:
                        for field, errors in form_errors.items():
                            for error in errors:
                                messages.error(request, f'Erreur dans l\'annexe {i+1}, champ "{field}": {error}')
            if not fiche_form.errors and not phase_formset.errors and not annexe_formset.errors:
                messages.error(request, 'Erreur de validation inconnue.')
    else:
        # Préparer les données initiales pour l'affichage
        initial = {}
        if fiche.heure_debut:
            initial['heure_debut'] = fiche.heure_debut.strftime('%H:%M')
        if fiche.heure_fin:
            initial['heure_fin'] = fiche.heure_fin.strftime('%H:%M')

        fiche_form = FicheForm(instance=fiche, initial=initial)
        phase_formset = PhaseFormSet(instance=fiche)
        annexe_formset = AnnexeFormSet(instance=fiche)

    return render(request, 'fiches/fiche_edit.html', {
        'fiche_form': fiche_form,
        'phase_formset': phase_formset,
        'annexe_formset': annexe_formset,
        'fiche': fiche,
    })



# === Dupliquer une fiche existante + ses phases ===






@login_required
def dupliquer_fiche(request, fiche_id):
    fiche = get_object_or_404(Fiche, id=fiche_id, user=request.user)

    # --- Dupliquer la fiche ---
    fiche.pk = None
    fiche.titre = f"{fiche.titre} (copie)"
    fiche.date = timezone.now().date()
    fiche.save()

    # --- Copier les compétences (relation M2M) ---
    fiche.competences.set(
        get_object_or_404(Fiche, id=fiche_id).competences.all()
    )

    # --- Dupliquer les phases ---
    phases = Phase.objects.filter(fiche_id=fiche_id)
    for phase in phases:
        phase.pk = None
        phase.fiche = fiche
        phase.save()

    # --- Dupliquer les annexes ---
    annexes = Annexe.objects.filter(fiche_id=fiche_id)
    for annexe in annexes:
        old_file = annexe.fichier
        annexe.pk = None
        annexe.fiche = fiche
        if old_file:
            # Crée une nouvelle entrée fichier (copie logique, pas physique)
            annexe.fichier.save(old_file.name, old_file.file, save=False)
        annexe.save()

    return redirect('fiche_detail', fiche_id=fiche.id)







@login_required
def fiche_detail_view(request, fiche_id):
    fiche = get_object_or_404(Fiche, id=fiche_id, user=request.user)
    phases = fiche.phases.all().order_by('ordre')
    annexes = fiche.annexes.all().order_by('ordre', 'date_ajout')

    return render(request, 'fiches/fiche_detail.html', {
        'fiche': fiche,
        'phases': phases,
        'annexes': annexes,
    })

# Lister toutes les fiches avec tri dynamique

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Fiche

def fiche_list_view(request):
    fiches = Fiche.objects.all()

    # --- Recherche ---
    query = request.GET.get("q", "")
    if query:
        fiches = fiches.filter(
            Q(titre__icontains=query) |
            Q(discipline__title__icontains=query) |
            Q(groupes__icontains=query)  # CharField -> icontains direct
        ).distinct()

    # --- Tri ---
    sort = request.GET.get("sort", "date")
    order = request.GET.get("order", "asc")
    sort_mapping = {
        "titre": "titre",
        "discipline": "discipline__title",
        "date": "date",
        "heure": "heure_debut",
    }
    sort_field = sort_mapping.get(sort, "date")
    if order == "desc":
        sort_field = f"-{sort_field}"
    fiches = fiches.order_by(sort_field)

    # --- Pagination ---
    paginator = Paginator(fiches, 10)
    page_number = request.GET.get("page")
    fiches_page = paginator.get_page(page_number)

    # --- Bulk delete ---
    if request.method == "POST":
        to_delete = request.POST.getlist("delete")
        if to_delete:
            Fiche.objects.filter(id__in=to_delete).delete()
            return redirect("fiche_list")  # adapter selon ton urls.py

    return render(request, "fiches/fiche_list.html", {
        "fiches": fiches_page,
        "query": query,
        "sort": sort,
        "order": order,
    })









@login_required
def fiche_multi_create_view(request):
    if request.method == "POST":
        form = MultiFicheForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            discipline = form.cleaned_data['discipline']
            sequence = form.cleaned_data['sequence']
            niveau = form.cleaned_data['niveau']
            bilan = form.cleaned_data['bilan']
            heure_debut = datetime.strptime(form.cleaned_data['heure_debut'], "%H:%M").time()
            heure_fin = datetime.strptime(form.cleaned_data['heure_fin'], "%H:%M").time()
            dates = form.cleaned_data['dates'].split(',')

            for date_str in dates:
                try:
                    date_obj = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
                except ValueError:
                    continue

                Fiche.objects.create(
                    user=request.user,  # Associe la fiche à l'utilisateur connecté
                    titre=titre,
                    discipline=discipline,
                    sequence=sequence,
                    niveau=niveau,
                    bilan=bilan,
                    date=date_obj,
                    heure_debut=heure_debut,
                    heure_fin=heure_fin
                )

            return redirect('fiche_list')
    else:
        form = MultiFicheForm()

    return render(request, 'fiches/fiche_multi_create.html', {'form': form})


@login_required
def fiche_delete_view(request, fiche_id):
    """Supprimer une fiche (séance)"""
    fiche = get_object_or_404(Fiche, id=fiche_id, user=request.user)
    
    if request.method == 'POST':
        fiche_titre = fiche.titre
        fiche_discipline = fiche.discipline.title if fiche.discipline else 'Aucune discipline'
        
        # Supprimer la fiche
        fiche.delete()
        
        messages.success(
            request, 
            f'La séance "{fiche_titre}" ({fiche_discipline}) a été supprimée définitivement.'
        )
        
        return redirect('fiche_list')
    
    # Afficher la page de confirmation
    return render(request, 'fiches/fiche_delete.html', {
        'fiche': fiche,
    })


# Exporter une fiche en PDF
@login_required
def fiche_export_pdf(request, fiche_id):
    """Export sécurisé d'une fiche en PDF."""
    import re
    from django.utils.text import slugify
    
    # Vérification de sécurité : s'assurer que l'utilisateur possède la fiche
    fiche = get_object_or_404(Fiche, id=fiche_id, user=request.user)
    
    try:
        # Rendu du template HTML pour le PDF avec échappement sécurisé
        html_string = render_to_string('fiches/fiche_pdf.html', {
            'fiche': fiche,
            'export_date': timezone.now(),
            'request': request,
        })
        
        # Nettoyage sécurisé du nom de fichier
        safe_title = slugify(fiche.titre)[:50]  # Limiter à 50 caractères
        safe_date = fiche.date.strftime('%Y-%m-%d')
        filename = f"fiche_{safe_title}_{safe_date}.pdf"
        
        # Validation du nom de fichier
        if not re.match(r'^[a-zA-Z0-9_-]+\.pdf$', filename):
            filename = f"fiche_{fiche.id}_{safe_date}.pdf"
        
        # Traitement sécurisé des images
        html_string = process_images_for_pdf(html_string, request)
        
        # Génération du PDF avec xhtml2pdf
        pdf_buffer = BytesIO()
        
        # Configuration sécurisée de pisa
        pisa_status = pisa.CreatePDF(
            html_string, 
            dest=pdf_buffer,
            encoding='utf-8',
            # Désactiver les liens externes pour la sécurité
            link_callback=None
        )
        
        # Vérification des erreurs
        if pisa_status.err:
            logger.error(f"Erreur lors de la génération PDF pour fiche {fiche_id}: {pisa_status.err}")
            return HttpResponse('Erreur lors de la génération du PDF', status=500)
        
        pdf_buffer.seek(0)
        pdf_content = pdf_buffer.getvalue()
        
        # Validation de la taille du PDF (max 50MB pour éviter les attaques DoS)
        if len(pdf_content) > 50 * 1024 * 1024:  # 50MB
            return HttpResponse('Le PDF généré est trop volumineux', status=413)
        
        # Création de la réponse HTTP sécurisée
        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        
        return response
        
    except Exception as e:
        logger.error(f"Erreur lors de l'export PDF de la fiche {fiche_id}: {str(e)}")
        return HttpResponse('Erreur lors de la génération du PDF', status=500)
    
    finally:
        # Nettoyage du buffer
        if 'pdf_buffer' in locals():
            pdf_buffer.close()


@login_required
@require_POST
def toggle_completion(request, fiche_id):
    """Vue AJAX pour marquer/démarquer une séance comme réalisée"""
    try:
        fiche = get_object_or_404(Fiche, id=fiche_id, user=request.user)
        
        # Basculer l'état de réalisation
        fiche.is_completed = not fiche.is_completed
        
        if fiche.is_completed:
            fiche.completed_at = timezone.now()
        else:
            fiche.completed_at = None
            
        fiche.save()
        
        return JsonResponse({
            'success': True,
            'is_completed': fiche.is_completed,
            'completed_at': fiche.completed_at.isoformat() if fiche.completed_at else None,
            'message': 'Séance marquée comme réalisée' if fiche.is_completed else 'Séance marquée comme non réalisée'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


# === Vue pour télécharger/visualiser les annexes ===
@login_required
def annexe_view(request, annexe_id):
    """
    Vue pour télécharger ou visualiser une annexe.
    Vérifie que l'utilisateur est propriétaire de la fiche associée.
    """
    annexe = get_object_or_404(Annexe, id=annexe_id, fiche__user=request.user)
    
    try:
        # Ouvrir le fichier
        response = HttpResponse(annexe.fichier.read(), content_type='application/octet-stream')
        
        # Déterminer le type de contenu selon l'extension
        import os
        extension = os.path.splitext(annexe.fichier.name)[1].lower()
        
        if extension in ['.jpg', '.jpeg']:
            response['Content-Type'] = 'image/jpeg'
        elif extension == '.png':
            response['Content-Type'] = 'image/png'
        elif extension == '.gif':
            response['Content-Type'] = 'image/gif'
        elif extension == '.webp':
            response['Content-Type'] = 'image/webp'
        elif extension == '.pdf':
            response['Content-Type'] = 'application/pdf'
        else:
            response['Content-Type'] = 'application/octet-stream'
        
        # Pour les images et PDF, afficher dans le navigateur
        if annexe.est_image or annexe.est_pdf:
            response['Content-Disposition'] = f'inline; filename="{annexe.fichier.name}"'
        else:
            # Pour les autres fichiers, forcer le téléchargement
            response['Content-Disposition'] = f'attachment; filename="{annexe.fichier.name}"'
        
        return response
        
    except Exception as e:
        messages.error(request, f'Erreur lors de l\'accès au fichier: {str(e)}')
        return redirect('fiche_detail', fiche_id=annexe.fiche.id)


# === Vue pour supprimer une annexe ===
@login_required
def annexe_delete_view(request, annexe_id):
    """
    Vue pour supprimer une annexe.
    Vérifie que l'utilisateur est propriétaire de la fiche associée.
    """
    annexe = get_object_or_404(Annexe, id=annexe_id, fiche__user=request.user)
    fiche_id = annexe.fiche.id
    
    if request.method == 'POST':
        try:
            annexe.delete()  # Le fichier sera supprimé automatiquement grâce à la méthode delete() du modèle
            messages.success(request, f'Annexe "{annexe.nom}" supprimée avec succès.')
        except Exception as e:
            messages.error(request, f'Erreur lors de la suppression: {str(e)}')
        
        return redirect('fiche_detail', fiche_id=fiche_id)
    
    return render(request, 'fiches/annexe_delete.html', {
        'annexe': annexe,
        'fiche': annexe.fiche
    })


# === API pour la mise en cache PWA ===
@login_required
def api_recent_fiches_cache(request):
    """
    API pour récupérer les 10 dernières séances avec leurs annexes
    pour la mise en cache PWA et l'accès hors ligne.
    """
    try:
        # Récupérer les 10 dernières fiches de l'utilisateur
        recent_fiches = Fiche.objects.filter(
            user=request.user
        ).select_related(
            'discipline', 'sequence_obj'
        ).prefetch_related(
            'phases', 'annexes', 'competences'
        ).order_by('-date', '-id')[:10]
        
        fiches_data = []
        
        for fiche in recent_fiches:
            # Préparer les données de la fiche
            fiche_data = {
                'id': fiche.id,
                'titre': fiche.titre,
                'date': fiche.date.isoformat(),
                'heure_debut': fiche.heure_debut.strftime('%H:%M') if fiche.heure_debut else None,
                'heure_fin': fiche.heure_fin.strftime('%H:%M') if fiche.heure_fin else None,
                'duree': fiche.duree,
                'niveau': fiche.niveau,
                'effectif': fiche.effectif,
                'objectifs': fiche.objectifs,
                'materiel': fiche.materiel,
                'bilan': fiche.bilan,
                'is_completed': fiche.is_completed,
                'discipline': {
                    'id': fiche.discipline.id if fiche.discipline else None,
                    'title': fiche.discipline.title if fiche.discipline else None,
                    'couleur': fiche.discipline.couleur if fiche.discipline else None,
                } if fiche.discipline else None,
                'sequence': {
                    'id': fiche.sequence_obj.id if fiche.sequence_obj else None,
                    'nom': fiche.sequence_obj.nom if fiche.sequence_obj else None,
                } if fiche.sequence_obj else None,
                'phases': [],
                'annexes': [],
                'competences': []
            }
            
            # Ajouter les phases
            for phase in fiche.phases.all().order_by('ordre'):
                fiche_data['phases'].append({
                    'id': phase.id,
                    'phase': phase.phase,
                    'duree': phase.duree,
                    'ce': phase.ce,
                    'deroulement': phase.deroulement,
                    'posture': phase.posture,
                    'ordre': phase.ordre
                })
            
            # Ajouter les annexes avec URLs pour le cache
            for annexe in fiche.annexes.all().order_by('ordre', 'date_ajout'):
                annexe_data = {
                    'id': annexe.id,
                    'nom': annexe.nom,
                    'description': annexe.description,
                    'type_fichier': annexe.type_fichier,
                    'taille_fichier': annexe.taille_fichier,
                    'taille_lisible': annexe.taille_lisible,
                    'date_ajout': annexe.date_ajout.isoformat(),
                    'est_image': annexe.est_image,
                    'est_pdf': annexe.est_pdf,
                    'url': request.build_absolute_uri(f'/fiches/annexe/{annexe.id}/'),
                    'filename': annexe.fichier.name if annexe.fichier else None
                }
                fiche_data['annexes'].append(annexe_data)
            
            # Ajouter les compétences
            for competence in fiche.competences.all():
                fiche_data['competences'].append({
                    'id': competence.id,
                    'title': competence.title,
                    'objectifs_generaux': competence.objectifs_generaux,
                    'competence_generale': competence.competence_generale
                })
            
            fiches_data.append(fiche_data)
        
        # Informations supplémentaires pour le cache
        cache_info = {
            'timestamp': timezone.now().isoformat(),
            'user_id': request.user.id,
            'total_fiches': len(fiches_data),
            'cache_version': '1.0'
        }
        
        return JsonResponse({
            'success': True,
            'cache_info': cache_info,
            'fiches': fiches_data
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


@login_required
@require_POST
def fiche_bulk_delete(request):
    """
    Vue pour supprimer plusieurs fiches en une seule fois.
    Sécurisée : seules les fiches de l'utilisateur connecté peuvent être supprimées.
    """
    try:
        # Récupérer les IDs des fiches à supprimer
        fiche_ids_str = request.POST.get('fiche_ids', '')
        
        if not fiche_ids_str:
            messages.error(request, 'Aucune fiche sélectionnée pour la suppression.')
            return redirect('fiche_list')
        
        # Parser les IDs
        try:
            fiche_ids = [int(id.strip()) for id in fiche_ids_str.split(',') if id.strip()]
        except ValueError:
            messages.error(request, 'IDs de fiches invalides.')
            return redirect('fiche_list')
        
        if not fiche_ids:
            messages.error(request, 'Aucune fiche valide sélectionnée.')
            return redirect('fiche_list')
        
        # Sécurité : récupérer uniquement les fiches appartenant à l'utilisateur
        fiches_to_delete = Fiche.objects.filter(
            id__in=fiche_ids,
            user=request.user
        )
        
        # Vérifier qu'on a trouvé des fiches
        if not fiches_to_delete.exists():
            messages.error(request, 'Aucune fiche trouvée ou vous n\'avez pas les permissions nécessaires.')
            return redirect('fiche_list')
        
        # Compter les fiches trouvées
        count = fiches_to_delete.count()
        
        # Supprimer les fiches (les annexes seront supprimées automatiquement grâce à CASCADE)
        fiches_to_delete.delete()
        
        # Message de confirmation
        if count == 1:
            messages.success(request, '1 fiche a été supprimée avec succès.')
        else:
            messages.success(request, f'{count} fiches ont été supprimées avec succès.')
        
        return redirect('fiche_list')
        
    except Exception as e:
        logger.error(f"Erreur lors de la suppression multiple de fiches: {str(e)}")
        messages.error(request, 'Une erreur s\'est produite lors de la suppression. Veuillez réessayer.')
        return redirect('fiche_list')


@login_required
@require_POST
def update_session_time(request, fiche_id):
    """
    Met à jour les horaires d'une séance via AJAX (drag & drop)
    """
    try:
        # Récupérer la fiche
        fiche = get_object_or_404(Fiche, id=fiche_id, user=request.user)
        
        # Parser les données JSON
        data = json.loads(request.body)
        heure_debut_str = data.get('heure_debut')
        heure_fin_str = data.get('heure_fin')
        
        if not heure_debut_str or not heure_fin_str:
            return JsonResponse({
                'success': False,
                'error': 'Horaires manquants'
            })
        
        # Convertir les chaînes en objets time
        try:
            heure_debut = datetime.strptime(heure_debut_str, '%H:%M').time()
            heure_fin = datetime.strptime(heure_fin_str, '%H:%M').time()
        except ValueError:
            return JsonResponse({
                'success': False,
                'error': 'Format d\'horaire invalide'
            })
        
        # Vérifier que l'heure de fin est après l'heure de début
        if heure_fin <= heure_debut:
            return JsonResponse({
                'success': False,
                'error': 'L\'heure de fin doit être après l\'heure de début'
            })
        
        # Mettre à jour la fiche
        fiche.heure_debut = heure_debut
        fiche.heure_fin = heure_fin
        
        # Recalculer la durée en minutes
        debut_minutes = heure_debut.hour * 60 + heure_debut.minute
        fin_minutes = heure_fin.hour * 60 + heure_fin.minute
        duree_minutes = fin_minutes - debut_minutes
        
        # Convertir en format "XhYY" pour la durée
        heures = duree_minutes // 60
        minutes = duree_minutes % 60
        if heures > 0:
            fiche.duree = f"{heures}h{minutes:02d}" if minutes > 0 else f"{heures}h"
        else:
            fiche.duree = f"{minutes}min"
        
        fiche.save()
        
        logger.info(f"Horaires mis à jour pour la fiche {fiche_id}: {heure_debut_str}-{heure_fin_str}")
        
        return JsonResponse({
            'success': True,
            'message': 'Horaires mis à jour avec succès',
            'new_duration': fiche.duree
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Données JSON invalides'
        })
    except Exception as e:
        logger.error(f"Erreur lors de la mise à jour des horaires pour la fiche {fiche_id}: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Erreur interne du serveur'
        })
