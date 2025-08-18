from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Fiche, Phase, Annexe
from pages.models import Page
from main.models import UserDisciplineColorPreference
# CKEditor widgets supprimés - utilisation de CKEditor 5 via CDN
from datetime import datetime, time, timedelta

# === Formulaire d'inscription personnalisé avec email ===
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre adresse email'
        }),
        label="Adresse email"
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nom d\'utilisateur'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmer le mot de passe'
        })
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# === Génération des choix horaires ===
def generate_time_choices(start=time(8, 0), end=time(18, 0), step=10):
    times = []
    current = datetime.combine(datetime.today(), start)
    end_dt = datetime.combine(datetime.today(), end)
    while current <= end_dt:
        val = current.time().strftime('%H:%M')
        times.append((val, val))
        current += timedelta(minutes=step)
    return times

TIME_CHOICES = generate_time_choices()


# === FICHE FORM ===
class FicheForm(forms.ModelForm):
    couleur = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'color',
            'class': 'form-control form-control-color',
            'readonly': 'readonly',
        }),
        label="Couleur de la discipline"
    )

    competences = forms.ModelMultipleChoiceField(
        queryset=Page.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False,
        label="Compétences associées"
    )

    heure_debut = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,
        label="Heure de début"
    )
    heure_fin = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,
        label="Heure de fin"
    )

    class Meta:
        model = Fiche
        fields = [
            'titre', 'discipline', 'competences',
            'date', 'heure_debut', 'heure_fin',
            'sequence', 'duree', 'niveau',
            'bilan', 'couleur', 'competencesSup', 'groupes', 
            'AFC', 'objectifGeneral','materiel'
        ]
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'discipline': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'sequence': forms.TextInput(attrs={'class': 'form-control'}),
            'duree': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau': forms.Select(attrs={'class': 'form-select'}),
            'competencesSup': forms.TextInput(attrs={'class': 'form-control'}),
            'groupes': forms.TextInput(attrs={'class': 'form-control'}), 
            'AFC': forms.TextInput(attrs={'class': 'form-control'}),
            'objectifGeneral': forms.TextInput(attrs={'class': 'form-control'}),
            'materiel': forms.TextInput(attrs={'class': 'form-control'}),
            'bilan': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),  
        }








    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discipline'].queryset = Page.objects.filter(parent=None)

        discipline_id = None
        if self.is_bound:
            discipline_id = self.data.get('discipline')
        elif self.initial.get('discipline'):
            discipline_id = self.initial.get('discipline').id if isinstance(self.initial.get('discipline'), Page) else self.initial.get('discipline')
        elif self.instance and self.instance.discipline:
            discipline_id = self.instance.discipline.id

        if discipline_id:
            try:
                discipline = Page.objects.get(id=discipline_id)
                # Récupérer seulement les compétences simples (feuilles de l'arbre)
                descendants = Page.objects.filter(
                    tree_id=discipline.tree_id,
                    lft__gt=discipline.lft,
                    rght__lt=discipline.rght,
                    published=True
                )
                # Filtrer pour ne garder que les pages sans enfants (compétences simples)
                competences_simples = [comp for comp in descendants if not comp.get_children()]
                self.fields['competences'].queryset = Page.objects.filter(
                    id__in=[comp.id for comp in competences_simples]
                ).order_by('objectifs_generaux', 'competence_generale', 'title')

                if not self.instance.pk or not self.instance.couleur:
                    # Utiliser la couleur personnalisée de l'utilisateur pour cette discipline
                    # Note: Le formulaire ne peut pas accéder directement à request.user ici
                    # Cette logique sera gérée dans la vue
                    if hasattr(discipline, 'couleur') and discipline.couleur:
                        self.initial['couleur'] = discipline.couleur
            except Page.DoesNotExist:
                pass

    def clean_heure_debut(self):
        val = self.cleaned_data.get('heure_debut')
        if val:
            try:
                return datetime.strptime(val, '%H:%M').time()
            except ValueError:
                raise forms.ValidationError('Format d\'heure invalide. Utilisez le format HH:MM')
        return None

    def clean_heure_fin(self):
        val = self.cleaned_data.get('heure_fin')
        if val:
            try:
                return datetime.strptime(val, '%H:%M').time()
            except ValueError:
                raise forms.ValidationError('Format d\'heure invalide. Utilisez le format HH:MM')
        return None


# === PHASE FORMSET (sans CKEditor) ===
PhaseFormSet = inlineformset_factory(
    Fiche, Phase,
    fields=['phase', 'duree', 'ce', 'deroulement', 'posture', 'ordre'],
    widgets={
        'phase': forms.TextInput(attrs={'class': 'form-control'}),
        'duree': forms.TextInput(attrs={'class': 'form-control'}),
        'ce': forms.TextInput(attrs={'class': 'form-control'}),
        'deroulement': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        'posture': forms.TextInput(attrs={'class': 'form-control'}),
        'ordre': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:80px;'}),
    },
    extra=0,
    can_delete=True
)


# === FORMULAIRE COMBINÉ ===
class FicheWithPhasesForm:
    def __init__(self, data=None, instance=None):
        if data:
            self.fiche_form = FicheForm(data, instance=instance)
            self.phase_formset = PhaseFormSet(data, instance=instance)
        else:
            self.fiche_form = FicheForm(instance=instance)
            self.phase_formset = PhaseFormSet(instance=instance)

    def is_valid(self):
        return self.fiche_form.is_valid() and self.phase_formset.is_valid()

    def save(self):
        fiche = self.fiche_form.save()
        self.phase_formset.instance = fiche
        self.phase_formset.save()
        return fiche


# === FORMULAIRE POUR LES ANNEXES ===
class AnnexeForm(forms.ModelForm):
    """
    Formulaire pour l'upload d'annexes (images, PDF).
    """
    class Meta:
        model = Annexe
        fields = ['nom', 'fichier', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de l\'annexe (ex: Fiche d\'exercices, Image du tableau...)'
            }),
            'fichier': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.jpg,.jpeg,.png,.gif,.webp,.pdf',
                'multiple': False
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Description optionnelle de l\'annexe...'
            })
        }
        labels = {
            'nom': 'Nom de l\'annexe',
            'fichier': 'Fichier (Image ou PDF)',
            'description': 'Description (optionnelle)'
        }
    
    def clean_fichier(self):
        fichier = self.cleaned_data.get('fichier')
        if fichier:
            # Vérifier la taille du fichier (max 10MB)
            try:
                if fichier.size > 10 * 1024 * 1024:
                    raise forms.ValidationError('Le fichier ne peut pas dépasser 10 MB.')
            except (FileNotFoundError, OSError):
                # Le fichier n'existe plus physiquement, on ignore la validation de taille
                # mais on log l'incident pour information
                import logging
                logger = logging.getLogger(__name__)
                logger.warning(f"Fichier annexe manquant lors de la validation: {fichier.name}")
                pass
            
            # Vérifier l'extension
            import os
            extension = os.path.splitext(fichier.name)[1].lower()
            extensions_autorisees = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.pdf']
            if extension not in extensions_autorisees:
                raise forms.ValidationError(
                    f'Type de fichier non autorisé. Extensions acceptées: {", ".join(extensions_autorisees)}'
                )
        
        return fichier


# === FORMSET POUR LES ANNEXES ===
AnnexeFormSet = inlineformset_factory(
    Fiche, Annexe,
    form=AnnexeForm,
    extra=1,  # Une annexe vide par défaut
    can_delete=True,
    fields=['nom', 'fichier', 'description']
)
