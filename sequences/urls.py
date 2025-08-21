from django.urls import path
from . import views
from . import views_periods

app_name = 'sequences'

urlpatterns = [
    # Liste et création des séquences
    path('', views.sequences_list, name='sequences_list'),
    path('create/', views.sequences_create, name='sequences_create'),
    
    # Gestion des séquences individuelles
    path('<int:sequence_id>/', views.sequences_detail, name='sequences_detail'),
    path('<int:sequence_id>/edit/', views.sequences_edit, name='sequences_edit'),
    path('<int:sequence_id>/delete/', views.sequences_delete, name='sequences_delete'),
    
    # Actions sur les séquences
    path('<int:sequence_id>/add-seance/', views.add_seance_to_sequence, name='add_seance_to_sequence'),
    path('<int:sequence_id>/remove-sessions/', views.remove_sessions, name='remove_sessions'),
    path('<int:sequence_id>/recalculate-progression/', views.recalculate_progression, name='recalculate_progression'),
    path('create-multiple-sessions/', views.create_multiple_sessions, name='create_multiple_sessions'),
    
    # API endpoints
    path('api/by-discipline/<int:discipline_id>/', views.sequences_by_discipline, name='sequences_by_discipline'),
    path('api/move-to-period/', views.move_sequence_to_period, name='move_sequence_to_period'),
    
    # Périodes scolaires
    path('periods/', views_periods.periods_list, name='periods_list'),
    path('periods/create-default/', views_periods.create_default_periods, name='create_default_periods'),
    path('periods/<int:period_id>/', views_periods.period_detail, name='period_detail'),
    path('periods/calendar/', views_periods.period_calendar_view, name='period_calendar'),
    path('periods/assign-sequence/', views_periods.assign_sequence_to_period, name='assign_sequence_to_period'),
    
    # Test de déploiement
    path('test-deployment/', views_periods.test_deployment_feature, name='test_deployment'),
]
