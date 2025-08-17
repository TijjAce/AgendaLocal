from django.urls import path
from . import views

app_name = 'friends'

urlpatterns = [
    path('', views.friends_dashboard, name='dashboard'),
    path('add/', views.add_friend, name='add_friend'),
    path('respond/<int:friendship_id>/', views.respond_friend_request, name='respond_friend_request'),
    path('map/', views.france_map, name='france_map'),
    path('profile/', views.update_profile, name='update_profile'),
    path('share/sequence/<int:sequence_id>/', views.share_sequence, name='share_sequence'),
    path('share/fiche/<int:fiche_id>/', views.share_fiche, name='share_fiche'),
    path('shared-content/', views.shared_content, name='shared_content'),
    path('update-location-ajax/', views.update_location_ajax, name='update_location_ajax'),
    path('simple-map/', views.simple_map, name='simple_map'),
    path('shared-fiche/<int:fiche_id>/', views.shared_fiche_detail, name='shared_fiche_detail'),
    path('shared-sequence/<int:sequence_id>/', views.shared_sequence_detail, name='shared_sequence_detail'),
    # Générateur d'avatar
    path('avatar/generate/', views.generate_avatar_svg, name='generate_avatar_svg'),
    path('avatar/update/', views.update_avatar_config, name='update_avatar_config'),
    path('avatar/randomize/', views.randomize_avatar, name='randomize_avatar'),
]
