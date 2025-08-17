from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('disciplines/', views.disciplines_view, name='disciplines'),
    path('competences/<int:discipline_id>/', views.competences_view, name='competences'),
    # path('access-logs/', views.access_logs_view, name='access_logs'),  # Temporairement commenté
]