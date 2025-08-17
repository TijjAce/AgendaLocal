from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from fiches.models import Fiche
from pages.models import Page
from datetime import datetime, date
from collections import defaultdict
import json
import re


def clean_competence_title(title):
    """
    Nettoie le titre d'une compétence en décodant les caractères Unicode
    et en normalisant les espaces. Gère les problèmes de double encodage UTF-8.
    """
    if not title:
        return title
    
    try:
        # Étape 1: Décoder les caractères Unicode échappés (ex: \u00e9 -> é)
        cleaned_title = title.encode().decode('unicode_escape')
        
        # Étape 2: Gérer le double encodage UTF-8 (ex: gÃ© -> gé)
        if 'Ã©' in cleaned_title or 'Ã ' in cleaned_title or 'Ã¨' in cleaned_title:
            try:
                cleaned_title = cleaned_title.encode('latin-1').decode('utf-8')
            except (UnicodeDecodeError, UnicodeEncodeError):
                pass
        
        # Étape 3: Normaliser les espaces
        cleaned_title = re.sub(r'\s+', ' ', cleaned_title).strip()
        
        return cleaned_title
        
    except (UnicodeDecodeError, UnicodeEncodeError):
        # Fallback: corriger le double encodage directement
        try:
            if 'Ã©' in title or 'Ã ' in title or 'Ã¨' in title:
                corrected = title.encode('latin-1').decode('utf-8')
                return re.sub(r'\s+', ' ', corrected.strip())
        except:
            pass
        
        return re.sub(r'\s+', ' ', title.strip())


@login_required
def radar_analytics(request):
    """Page d'analyse avec graphiques radar pour compétences et fiches par discipline"""
    # Récupérer toutes les disciplines disponibles (pas seulement celles avec des fiches)
    disciplines = Page.objects.filter(
        parent=None  # Disciplines racines
    ).order_by('title')
    
    # Années scolaires disponibles (basées sur les fiches existantes)
    fiches_dates = Fiche.objects.filter(user=request.user).values_list('date', flat=True)
    school_years = set()
    
    for fiche_date in fiches_dates:
        if fiche_date.month >= 9:  # Septembre à Décembre
            school_years.add(f"{fiche_date.year}-{fiche_date.year + 1}")
        else:  # Janvier à Août
            school_years.add(f"{fiche_date.year - 1}-{fiche_date.year}")
    
    school_years = sorted(list(school_years), reverse=True)
    current_year = school_years[0] if school_years else None
    
    context = {
        'disciplines': disciplines,
        'school_years': school_years,
        'current_year': current_year,
    }
    
    return render(request, 'calendar_app/radar_analytics.html', context)


@login_required
def competencies_radar_api(request):
    """API pour les données du radar des compétences par discipline"""
    school_year = request.GET.get('school_year')
    
    if not school_year:
        return JsonResponse({'error': 'Année scolaire requise'}, status=400)
    
    # Calculer les dates de début et fin de l'année scolaire
    try:
        start_year, end_year = map(int, school_year.split('-'))
        start_date = date(start_year, 9, 1)  # 1er septembre
        end_date = date(end_year, 8, 31)    # 31 août
    except ValueError:
        return JsonResponse({'error': 'Format d\'année scolaire invalide'}, status=400)
    
    # Récupérer les disciplines de l'utilisateur
    disciplines = Page.objects.filter(
        parent=None,
        fiches__user=request.user,
        fiches__date__gte=start_date,
        fiches__date__lte=end_date
    ).distinct().order_by('title')
    
    labels = []
    data = []
    
    for discipline in disciplines:
        # Compter les compétences uniques mobilisées dans cette discipline
        # Récupérer toutes les fiches de cette discipline dans la période
        fiches_discipline = Fiche.objects.filter(
            user=request.user,
            discipline=discipline,
            date__gte=start_date,
            date__lte=end_date
        )
        
        # Compter les compétences uniques associées à ces fiches
        competences_uniques = set()
        for fiche in fiches_discipline:
            competences_uniques.update(fiche.competences.values_list('id', flat=True))
        
        competences_count = len(competences_uniques)
        
        labels.append(discipline.title)
        data.append(competences_count)
    
    return JsonResponse({
        'labels': labels,
        'datasets': [{
            'label': 'Compétences mobilisées',
            'data': data,
            'backgroundColor': 'rgba(54, 162, 235, 0.2)',
            'borderColor': 'rgba(54, 162, 235, 1)',
            'borderWidth': 2,
            'pointBackgroundColor': 'rgba(54, 162, 235, 1)',
            'pointBorderColor': '#fff',
            'pointHoverBackgroundColor': '#fff',
            'pointHoverBorderColor': 'rgba(54, 162, 235, 1)'
        }]
    })


@login_required
def fiches_radar_api(request):
    """API pour les données du radar du nombre de fiches par discipline"""
    school_year = request.GET.get('school_year')
    
    if not school_year:
        return JsonResponse({'error': 'Année scolaire requise'}, status=400)
    
    # Calculer les dates de début et fin de l'année scolaire
    try:
        start_year, end_year = map(int, school_year.split('-'))
        start_date = date(start_year, 9, 1)  # 1er septembre
        end_date = date(end_year, 8, 31)    # 31 août
    except ValueError:
        return JsonResponse({'error': 'Format d\'année scolaire invalide'}, status=400)
    
    # Récupérer les disciplines de l'utilisateur avec le nombre de fiches
    disciplines_data = Fiche.objects.filter(
        user=request.user,
        date__gte=start_date,
        date__lte=end_date
    ).values('discipline__title').annotate(
        fiches_count=Count('id')
    ).order_by('discipline__title')
    
    labels = []
    data = []
    
    for item in disciplines_data:
        labels.append(item['discipline__title'])
        data.append(item['fiches_count'])
    
    return JsonResponse({
        'labels': labels,
        'datasets': [{
            'label': 'Nombre de fiches',
            'data': data,
            'backgroundColor': 'rgba(255, 99, 132, 0.2)',
            'borderColor': 'rgba(255, 99, 132, 1)',
            'borderWidth': 2,
            'pointBackgroundColor': 'rgba(255, 99, 132, 1)',
            'pointBorderColor': '#fff',
            'pointHoverBackgroundColor': '#fff',
            'pointHoverBorderColor': 'rgba(255, 99, 132, 1)'
        }]
    })


@login_required
def hours_radar_api(request):
    """API pour les données du radar des heures par discipline"""
    school_year = request.GET.get('school_year')
    
    if not school_year:
        return JsonResponse({'error': 'Année scolaire requise'}, status=400)
    
    try:
        # Parser l'année scolaire (format: "2023-2024")
        start_year, end_year = map(int, school_year.split('-'))
        
        # Définir les dates de début et fin de l'année scolaire
        start_date = date(start_year, 9, 1)  # 1er septembre
        end_date = date(end_year, 8, 31)    # 31 août
        
    except ValueError:
        return JsonResponse({'error': 'Format d\'année scolaire invalide'}, status=400)
    
    # Récupérer les heures par discipline pour l'année scolaire
    from django.db.models import Sum
    
    disciplines_data = Fiche.objects.filter(
        user=request.user,
        date__gte=start_date,
        date__lte=end_date,
        duration_minutes__isnull=False,
        duration_minutes__gt=0
    ).values(
        'discipline__title'
    ).annotate(
        total_minutes=Sum('duration_minutes')
    ).order_by('discipline__title')
    
    labels = []
    data = []
    
    for item in disciplines_data:
        labels.append(item['discipline__title'])
        # Convertir les minutes en heures (arrondi à 1 décimale)
        hours = round(item['total_minutes'] / 60, 1)
        data.append(hours)
    
    return JsonResponse({
        'labels': labels,
        'datasets': [{
            'label': 'Heures d\'enseignement',
            'data': data,
            'backgroundColor': 'rgba(54, 162, 235, 0.2)',
            'borderColor': 'rgba(54, 162, 235, 1)',
            'borderWidth': 2,
            'pointBackgroundColor': 'rgba(54, 162, 235, 1)',
            'pointBorderColor': '#fff',
            'pointHoverBackgroundColor': '#fff',
            'pointHoverBorderColor': 'rgba(54, 162, 235, 1)'
        }]
    })


@login_required
def discipline_competencies_radar_api(request):
    """API pour les données du radar des compétences les plus mobilisées dans une discipline"""
    school_year = request.GET.get('school_year')
    discipline_id = request.GET.get('discipline_id')
    
    if not school_year:
        return JsonResponse({'error': 'Année scolaire requise'}, status=400)
    
    if not discipline_id:
        return JsonResponse({'error': 'ID de discipline requis'}, status=400)
    
    # Calculer les dates de début et fin de l'année scolaire
    try:
        start_year, end_year = map(int, school_year.split('-'))
        start_date = date(start_year, 9, 1)  # 1er septembre
        end_date = date(end_year, 8, 31)    # 31 août
    except ValueError:
        return JsonResponse({'error': 'Format d\'année scolaire invalide'}, status=400)
    
    # Vérifier que la discipline existe et appartient à l'utilisateur
    try:
        discipline = Page.objects.get(id=discipline_id, parent=None)
    except Page.DoesNotExist:
        return JsonResponse({'error': 'Discipline non trouvée'}, status=404)
    
    # Récupérer les compétences les plus mobilisées dans cette discipline
    from django.db.models import Count
    
    # Récupérer toutes les fiches de l'utilisateur pour cette discipline et année scolaire
    fiches_discipline = Fiche.objects.filter(
        user=request.user,
        discipline=discipline,
        date__gte=start_date,
        date__lte=end_date
    )
    
    # Parcourir toutes les fiches et compter les compétences mobilisées
    competences_count = {}
    
    for fiche in fiches_discipline:
        # Parcourir toutes les compétences de cette fiche
        for competence in fiche.competences.all():
            if competence.title:
                # Nettoyer le titre de la compétence
                cleaned_title = clean_competence_title(competence.title)
                if cleaned_title in competences_count:
                    competences_count[cleaned_title] += 1
                else:
                    competences_count[cleaned_title] = 1
    
    # Trier par nombre d'utilisations (décroissant) et prendre le top 10
    competencies_data = sorted(
        competences_count.items(), 
        key=lambda x: x[1], 
        reverse=True
    )[:10]
    
    labels = []
    data = []
    
    # Traiter les données (maintenant sous forme de tuples (titre, count))
    for competence_title, usage_count in competencies_data:
        if competence_title:  # S'assurer que le titre n'est pas None
            labels.append(competence_title)
            data.append(usage_count)
    
    # Si aucune compétence trouvée, retourner un message explicatif
    if not labels:
        return JsonResponse({
            'labels': ['Aucune compétence'],
            'datasets': [{
                'label': f'Compétences mobilisées - {discipline.title}',
                'data': [0],
                'backgroundColor': 'rgba(200, 200, 200, 0.2)',
                'borderColor': 'rgba(200, 200, 200, 1)',
                'borderWidth': 2,
                'pointBackgroundColor': 'rgba(200, 200, 200, 1)',
                'pointBorderColor': '#fff',
                'pointHoverBackgroundColor': '#fff',
                'pointHoverBorderColor': 'rgba(200, 200, 200, 1)'
            }],
            'message': 'Aucune compétence associée aux fiches de cette discipline pour l\'année sélectionnée.'
        })
    
    return JsonResponse({
        'labels': labels,
        'datasets': [{
            'label': f'Compétences mobilisées - {discipline.title}',
            'data': data,
            'backgroundColor': 'rgba(75, 192, 192, 0.2)',
            'borderColor': 'rgba(75, 192, 192, 1)',
            'borderWidth': 2,
            'pointBackgroundColor': 'rgba(75, 192, 192, 1)',
            'pointBorderColor': '#fff',
            'pointHoverBackgroundColor': '#fff',
            'pointHoverBorderColor': 'rgba(75, 192, 192, 1)'
        }]
    })
