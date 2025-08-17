from django.http import Http404, JsonResponse, HttpResponse, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Page, PageAnnexe
from .forms import PageAnnexeFormSet
from main.models import UserDisciplineColorPreference
import mimetypes
import os

def page_view(request, path=''):
    slugs = [slug for slug in path.strip('/').split('/') if slug]
    page = None
    parent = None

    for slug in slugs:
        try:
            page = Page.objects.get(slug=slug, parent=parent, published=True)
            parent = page
        except Page.DoesNotExist:
            page = None
            break

    if not slugs:
        page = Page.objects.filter(parent=None, published=True).first()

    if page is None:
        raise Http404("Page non trouvée")

    # Gérer la mise à jour de couleur personnalisée si formulaire POST et page racine
    if request.method == "POST" and page.is_discipline_root():
        couleur = request.POST.get('couleur')
        if couleur:
            # Sauvegarder la couleur personnalisée pour cet utilisateur uniquement
            UserDisciplineColorPreference.set_user_discipline_color(request.user, page, couleur)
            messages.success(request, "Votre couleur personnalisée a été sauvegardée.")
            return redirect(page.get_absolute_url())
        else:
            messages.error(request, "Veuillez sélectionner une couleur valide.")

    descendants = Page.objects.filter(
        tree_id=page.tree_id,
        lft__gt=page.lft,
        rght__lt=page.rght,
        published=True
    )

    hierarchy = {}

    for comp in descendants:
        if not comp.get_children():  # compétence simple
            objectifs = comp.get_heritable_field('objectifs_generaux') or "Sans objectif"
            comp_gen = comp.get_heritable_field('competence_generale') or "Sans compétence générale"
            hierarchy.setdefault(objectifs, {}).setdefault(comp_gen, []).append(comp)

    # Ajouter la couleur personnalisée de l'utilisateur pour les disciplines racines
    if page.is_discipline_root():
        page.user_couleur = UserDisciplineColorPreference.get_user_discipline_color(request.user, page)
    
    # Récupérer les annexes de la page si l'utilisateur est connecté
    annexes = []
    if request.user.is_authenticated:
        annexes = page.annexes.all().order_by('ordre', 'date_ajout')
    
    context = {
        'page': page,
        'hierarchy': hierarchy,
        'annexes': annexes,
    }
    return render(request, 'pages/page.html', context)


# === Gestion des annexes des compétences ===

@login_required
@require_http_methods(["GET"])
def page_annexe_view(request, page_id, annexe_id):
    """
    Vue pour visualiser/télécharger une annexe d'une compétence.
    Seuls les utilisateurs connectés peuvent accéder aux annexes.
    """
    page = get_object_or_404(Page, id=page_id, published=True)
    annexe = get_object_or_404(PageAnnexe, id=annexe_id, page=page)
    
    try:
        # Ouvrir le fichier
        if not os.path.exists(annexe.fichier.path):
            messages.error(request, "Le fichier n'existe plus.")
            return redirect('page_view', path=page.get_absolute_url().strip('/'))
        
        # Déterminer le type MIME
        mime_type, _ = mimetypes.guess_type(annexe.fichier.path)
        if not mime_type:
            mime_type = annexe.type_fichier or 'application/octet-stream'
        
        # Utiliser FileResponse pour une gestion sécurisée des fichiers
        response = FileResponse(
            annexe.fichier.open('rb'),
            content_type=mime_type,
            filename=annexe.nom
        )
        
        # Pour les images, affichage inline, pour les autres fichiers, téléchargement
        if annexe.est_image:
            response['Content-Disposition'] = f'inline; filename="{annexe.nom}"'
        else:
            response['Content-Disposition'] = f'attachment; filename="{annexe.nom}"'
        
        return response
        
    except Exception as e:
        messages.error(request, f"Erreur lors de l'accès au fichier: {str(e)}")
        return redirect('page_view', path=page.get_absolute_url().strip('/'))


@login_required
@require_http_methods(["GET", "POST"])
def page_annexe_delete_view(request, page_id, annexe_id):
    """
    Vue pour supprimer une annexe d'une compétence.
    Seuls les superusers peuvent supprimer les annexes.
    """
    if not request.user.is_superuser:
        messages.error(request, "Vous n'avez pas les permissions pour supprimer cette annexe.")
        return redirect('page_view', path='')
    
    page = get_object_or_404(Page, id=page_id, published=True)
    annexe = get_object_or_404(PageAnnexe, id=annexe_id, page=page)
    
    if request.method == 'POST':
        try:
            annexe.delete()  # Supprime aussi le fichier physique grâce à la méthode delete() personnalisée
            messages.success(request, f'Annexe "{annexe.nom}" supprimée avec succès.')
        except Exception as e:
            messages.error(request, f'Erreur lors de la suppression: {str(e)}')
        
        return redirect('page_view', path=page.get_absolute_url().strip('/'))
    
    return render(request, 'pages/page_annexe_delete.html', {
        'annexe': annexe,
        'page': page
    })


@login_required
@require_http_methods(["GET", "POST"])
def page_manage_annexes_view(request, page_id):
    """
    Vue pour gérer les annexes d'une compétence (ajout/modification).
    Seuls les superusers peuvent gérer les annexes.
    """
    if not request.user.is_superuser:
        messages.error(request, "Vous n'avez pas les permissions pour gérer les annexes.")
        return redirect('page_view', path='')
    
    page = get_object_or_404(Page, id=page_id, published=True)
    
    if request.method == 'POST':
        formset = PageAnnexeFormSet(request.POST, request.FILES, instance=page)
        
        if formset.is_valid():
            try:
                annexes = formset.save(commit=False)
                for annexe in annexes:
                    annexe.page = page
                    annexe.save()
                
                # Supprimer les annexes marquées pour suppression
                for annexe in formset.deleted_objects:
                    annexe.delete()
                
                messages.success(request, 'Annexes mises à jour avec succès!')
                return redirect('page_view', path=page.get_absolute_url().strip('/'))
            except Exception as e:
                messages.error(request, f'Erreur lors de la sauvegarde: {str(e)}')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    else:
        formset = PageAnnexeFormSet(instance=page)
    
    return render(request, 'pages/page_manage_annexes.html', {
        'page': page,
        'formset': formset
    })
