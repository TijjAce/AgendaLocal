from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from fiches import upload_views
from calendar_app import analytics_views
from pages import views as pages_views
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),

    # Applications principales
    path('', include('main.urls')),                # Page d'accueil et disciplines
    path('fiches/', include('fiches.urls')),       # Gestion des fiches de préparation
    path('sequences/', include('sequences.urls')), # Gestion des séquences pédagogiques
    path('calendar/', include('calendar_app.urls')), # Calendrier
    # URLs spécifiques pour les annexes des compétences (avant pages/ pour éviter les conflits)
    path('page/<int:page_id>/annexe/<int:annexe_id>/', pages_views.page_annexe_view, name='page_annexe_view'),
    path('page/<int:page_id>/annexe/<int:annexe_id>/delete/', pages_views.page_annexe_delete_view, name='page_annexe_delete'),
    path('page/<int:page_id>/manage-annexes/', pages_views.page_manage_annexes_view, name='page_manage_annexes'),
    
    path('friends/', include('friends.urls')),     # Système d'amis avec carte de France

    # Route directe pour la page d'analyse
    path('Analyse/', analytics_views.radar_analytics, name='radar_analytics_direct'),
    path('api/competencies-radar/', analytics_views.competencies_radar_api, name='competencies_radar_api_direct'),
    path('api/fiches-radar/', analytics_views.fiches_radar_api, name='fiches_radar_api_direct'),
    path('api/hours-radar/', analytics_views.hours_radar_api, name='hours_radar_api_direct'),
    path('api/discipline-competencies-radar/', analytics_views.discipline_competencies_radar_api, name='discipline_competencies_radar_api_direct'),
    


    # CKEditor (upload d'images)
    path('ckeditor/upload/', upload_views.ckeditor_upload, name='global_ckeditor_upload'),
    
    # Pages et compétences - URL catch-all (doit être en dernier)
    path('', pages_views.page_view, name='home'),  # Page d'accueil
    re_path(r'^(?P<path>.*)/$', pages_views.page_view, name='page'),  # Toutes les autres pages
]

# ✅ Configuration pour servir les médias (upload CKEditor)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
