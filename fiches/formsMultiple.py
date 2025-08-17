from django import forms
from .models import Page
# CKEditor widget supprimé - utilisation de CKEditor 5 via CDN
from django.core.exceptions import ValidationError
from datetime import datetime

# Génération dynamique des créneaux horaires : toutes les 30 min de 07h00 à 20h00
TIME_CHOICES = [(f"{h:02d}:{m:02d}", f"{h:02d}:{m:02d}") for h in range(7, 21) for m in (0, 30)]

class MultiFicheForm(forms.Form):
    titre = forms.CharField(
        label="Titre commun",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre des fiches'})
    )

    discipline = forms.ModelChoiceField(
        queryset=Page.objects.filter(parent=None),
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    sequence = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la séquence'}),
        label="Séquence"
    )

    niveau = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exemple : CP, CE1'}),
        label="Niveau"
    )

    dates = forms.CharField(
        label="Dates de séances",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'dates-picker',
            'placeholder': 'Cliquez pour choisir plusieurs dates'
        }),
        required=True,
        help_text="Sélectionnez une ou plusieurs dates"
    )

    heure_debut = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Heure de début"
    )

    heure_fin = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Heure de fin"
    )

    bilan = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        label="Bilan"
    )

    def clean(self):
        cleaned_data = super().clean()

        heure_debut_str = cleaned_data.get('heure_debut')
        heure_fin_str = cleaned_data.get('heure_fin')
        dates_str = cleaned_data.get('dates')

        # Validation heures (fin > début)
        if heure_debut_str and heure_fin_str:
            heure_debut = datetime.strptime(heure_debut_str, "%H:%M").time()
            heure_fin = datetime.strptime(heure_fin_str, "%H:%M").time()
            if heure_fin <= heure_debut:
                raise ValidationError("L'heure de fin doit être après l'heure de début.")

        # Validation des dates
        if dates_str:
            dates_list = [d.strip() for d in dates_str.split(',') if d.strip()]
            if not dates_list:
                raise ValidationError("Veuillez sélectionner au moins une date.")
            for d in dates_list:
                try:
                    datetime.strptime(d, "%Y-%m-%d")
                except ValueError:
                    raise ValidationError(f"La date '{d}' n'est pas au format valide (YYYY-MM-DD).")
        else:
            raise ValidationError("Veuillez renseigner les dates.")

        return cleaned_data
