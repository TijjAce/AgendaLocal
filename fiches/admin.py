
from django.contrib import admin
from .models import Fiche, Phase


#testffe


class PhaseInline(admin.TabularInline):
    model = Phase
    extra = 1  # Nombre de formulaires vides affichés par défaut
    fields = ['phase', 'duree', 'ce', 'deroulement', 'posture', 'ordre']
    ordering = ['ordre']

@admin.register(Fiche)
class FicheAdmin(admin.ModelAdmin):
    list_display = ['titre', 'date', 'discipline', 'niveau']
    list_filter = ['date', 'discipline', 'niveau']
    search_fields = ['titre', 'sequence', 'niveau']
    inlines = [PhaseInline]