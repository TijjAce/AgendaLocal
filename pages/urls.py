from django.urls import path, re_path
from . import views

# Note: Les URLs spécifiques doivent être définies AVANT l'URL générale catch-all
# pour éviter les conflits de routage
urlpatterns = [
    path('', views.page_view, name='home'),  # racine du site (ex: /)
    re_path(r'^(?P<path>.*)/$', views.page_view, name='page'),  # toutes les autres pages
]
