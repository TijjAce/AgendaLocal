from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from pages.models import Page
from .models import UserDisciplineColorPreference
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from fiches.models import Fiche
import json

def main_view(request):
    return render(request, 'main/main.html')

def disciplines_view(request):
    from fiches.models import Fiche
    
    # Récupérer toutes les pages racines (disciplines)
    pages = Page.objects.filter(parent=None, published=True)
    
    # Ajouter le nombre de séances et la couleur personnalisée pour chaque discipline
    for page in pages:
        page.nb_seances = Fiche.objects.filter(discipline=page, user=request.user).count()
        # Récupérer la couleur personnalisée de l'utilisateur pour cette discipline
        page.user_couleur = UserDisciplineColorPreference.get_user_discipline_color(request.user, page)
    
    # Gérer la modification de couleur personnalisée
    if request.method == 'POST':
        discipline_id = request.POST.get('discipline_id')
        couleur = request.POST.get('couleur')
        if discipline_id and couleur:
            discipline = get_object_or_404(Page, id=discipline_id)
            # Sauvegarder la couleur personnalisée pour cet utilisateur
            UserDisciplineColorPreference.set_user_discipline_color(request.user, discipline, couleur)
            return redirect('disciplines_view')
    
    return render(request, 'main/disciplines.html', {'pages': pages})

def competences_view(request, discipline_id):
    # Récupérer la discipline et ses compétences (enfants)
    discipline = get_object_or_404(Page, id=discipline_id, parent=None)
    competences = discipline.get_children().filter(published=True)
    
    # Récupérer la couleur personnalisée de l'utilisateur pour cette discipline
    discipline.user_couleur = UserDisciplineColorPreference.get_user_discipline_color(request.user, discipline)
    
    # Gérer la modification de couleur personnalisée de la discipline
    if request.method == 'POST':
        couleur = request.POST.get('couleur')
        if couleur:
            # Sauvegarder la couleur personnalisée pour cet utilisateur
            UserDisciplineColorPreference.set_user_discipline_color(request.user, discipline, couleur)
            return redirect('competences_view', discipline_id=discipline.id)
    
    return render(request, 'main/competences.html', {
        'discipline': discipline,
        'competences': competences
    })

@login_required
def access_logs_view(request):
    """
    Vue pour afficher les logs d'accès (monitoring des IPs et User-Agents)
    Accessible uniquement aux superutilisateurs
    """
    # Vérifier que l'utilisateur est superutilisateur
    if not request.user.is_superuser:
        messages.error(request, "Accès refusé. Cette page est réservée aux administrateurs.")
        return redirect('disciplines')
    
    from .models import AccessLog
    from django.db.models import Count, Q
    from django.utils import timezone
    from datetime import timedelta
    
    # Filtres
    filter_type = request.GET.get('filter', 'all')  # all, bots, suspicious, recent
    
    # Base queryset
    logs = AccessLog.objects.all()
    
    # Appliquer les filtres
    if filter_type == 'bots':
        logs = logs.filter(is_bot=True)
    elif filter_type == 'suspicious':
        logs = logs.filter(is_suspicious=True)
    elif filter_type == 'recent':
        # Dernières 24 heures
        yesterday = timezone.now() - timedelta(days=1)
        logs = logs.filter(timestamp__gte=yesterday)
    
    # Pagination
    from django.core.paginator import Paginator
    paginator = Paginator(logs, 50)  # 50 logs par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Statistiques
    total_logs = AccessLog.objects.count()
    bot_logs = AccessLog.objects.filter(is_bot=True).count()
    suspicious_logs = AccessLog.objects.filter(is_suspicious=True).count()
    
    # Top IPs
    top_ips = AccessLog.objects.values('ip_address').annotate(
        count=Count('id')
    ).order_by('-count')[:10]
    
    # Top User Agents suspects
    suspicious_agents = AccessLog.objects.filter(
        Q(is_bot=True) | Q(is_suspicious=True)
    ).values('user_agent').annotate(
        count=Count('id')
    ).order_by('-count')[:10]
    
    context = {
        'page_obj': page_obj,
        'filter_type': filter_type,
        'total_logs': total_logs,
        'bot_logs': bot_logs,
        'suspicious_logs': suspicious_logs,
        'top_ips': top_ips,
        'suspicious_agents': suspicious_agents,
    }
    
    return render(request, 'main/access_logs.html', context)