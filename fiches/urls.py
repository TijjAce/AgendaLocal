from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import upload_views
from . import auth_views as custom_auth_views
from . import sharing_views

urlpatterns = [
    # URLs d'authentification standard
    path('login/', custom_auth_views.CustomLoginView.as_view(), name='login'),
    path('logout/', custom_auth_views.logout_view, name='logout'),
    path('signup/', custom_auth_views.signup_view, name='signup'),
    path('profile/', custom_auth_views.profile_view, name='profile'),
    
    # URLs des fiches
    path('create/', views.fiche_create_view, name='fiche_create'),
    path('create-multiple/', views.fiche_multi_create_view, name='fiche_multi_create'),
    path('edit/<int:fiche_id>/', views.fiche_edit_view, name='fiche_edit'),
    
    
    
    
    path('dupliquer/<int:fiche_id>/', views.fiche_dupliquer_view, name='fiche_dupliquer'),
 
    path('delete/<int:fiche_id>/', views.fiche_delete_view, name='fiche_delete'),
    path('bulk-delete/', views.fiche_bulk_delete, name='fiche_bulk_delete'),
    path('<int:fiche_id>/pdf/', views.fiche_export_pdf, name='fiche_export_pdf'),
    path('<int:fiche_id>/toggle-completion/', views.toggle_completion, name='toggle_completion'),
    path('update-time/<int:fiche_id>/', views.update_session_time, name='update_session_time'),
    path('<int:fiche_id>/', views.fiche_detail_view, name='fiche_detail'),
    path('list/', views.fiche_list_view, name='fiche_list'),
    path('', views.fiche_list_view, name='fiche_home'),  # Page d'accueil
    
    # URLs des annexes
    path('annexe/<int:annexe_id>/', views.annexe_view, name='annexe_view'),
    path('annexe/<int:annexe_id>/delete/', views.annexe_delete_view, name='annexe_delete'),
    
    # API PWA pour mise en cache
    path('api/recent-cache/', views.api_recent_fiches_cache, name='api_recent_fiches_cache'),
    
    # CKEditor upload personnalisé (sans authentification admin)
    path('ckeditor/upload/', upload_views.ckeditor_upload, name='ckeditor_upload'),
    path('ckeditor/upload', upload_views.ckeditor_upload, name='ckeditor_upload_no_slash'),  # Sans slash final
    path('ckeditor/browse/', upload_views.ckeditor_browse, name='ckeditor_browse'),
    
    # APIs de partage
    path('api/my-fiches-to-share/', sharing_views.my_fiches_to_share, name='my_fiches_to_share'),
    path('api/community-fiches/', sharing_views.community_fiches, name='community_fiches'),
    path('api/toggle-share/', sharing_views.toggle_share, name='toggle_share'),
    path('api/import-fiche/', sharing_views.import_fiche, name='import_fiche'),
    path('api/sharing-stats/', sharing_views.sharing_stats, name='sharing_stats'),
]