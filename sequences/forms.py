from django import forms
from .models import Sequence
from pages.models import Page


class SequenceForm(forms.ModelForm):
    """
    Formulaire pour créer et modifier des séquences pédagogiques
    """
    
    class Meta:
        model = Sequence
        fields = ['name', 'discipline', 'niveau', 'description', 'duree_estimee']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de la séquence'
            }),
            'discipline': forms.Select(attrs={
                'class': 'form-select'
            }),
            'niveau': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 6ème, CM2, etc.'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Description de la séquence...'
            }),
            'duree_estimee': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'placeholder': 'Durée en heures'
            })
        }
        labels = {
            'name': 'Nom de la séquence',
            'discipline': 'Discipline',
            'niveau': 'Niveau',
            'description': 'Description',
            'duree_estimee': 'Durée estimée (heures)'
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Filtrer les disciplines pour l'utilisateur connecté
        if user:
            # Récupérer toutes les disciplines (pages parentes)
            self.fields['discipline'].queryset = Page.objects.filter(
                parent__isnull=True
            ).order_by('title')
        
        # Rendre certains champs optionnels
        self.fields['description'].required = False
        self.fields['duree_estimee'].required = False
    
    def clean_name(self):
        """Validation du nom de la séquence"""
        name = self.cleaned_data.get('name')
        if name:
            name = name.strip()
            if len(name) < 3:
                raise forms.ValidationError("Le nom de la séquence doit contenir au moins 3 caractères.")
        return name
    
    def clean_duree_estimee(self):
        """Validation de la durée estimée"""
        duree = self.cleaned_data.get('duree_estimee')
        if duree is not None and duree <= 0:
            raise forms.ValidationError("La durée doit être supérieure à 0.")
        return duree
