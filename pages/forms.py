from django import forms
from django.forms import inlineformset_factory
from .models import Page, PageAnnexe


class PageAnnexeForm(forms.ModelForm):
    """
    Formulaire pour l'upload d'annexes (images/PDF) sur les compétences (Pages).
    """
    
    class Meta:
        model = PageAnnexe
        fields = ['nom', 'description', 'fichier', 'ordre']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de l\'annexe'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Description (optionnelle)'
            }),
            'fichier': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.jpg,.jpeg,.png,.gif,.webp,.pdf'
            }),
            'ordre': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'value': 0
            })
        }
    
    def clean_fichier(self):
        """Validation personnalisée du fichier."""
        fichier = self.cleaned_data.get('fichier')
        
        if fichier:
            # Vérifier la taille (max 10MB)
            max_size = 10 * 1024 * 1024  # 10MB
            if fichier.size > max_size:
                raise forms.ValidationError('Le fichier est trop volumineux. Taille maximum: 10MB')
            
            # Vérifier l'extension
            import os
            file_extension = os.path.splitext(fichier.name)[1].lower()
            allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.pdf']
            
            if file_extension not in allowed_extensions:
                raise forms.ValidationError(
                    f'Type de fichier non autorisé. Extensions autorisées: {", ".join(allowed_extensions)}'
                )
        
        return fichier


# Formset pour gérer plusieurs annexes
PageAnnexeFormSet = inlineformset_factory(
    Page,
    PageAnnexe,
    form=PageAnnexeForm,
    extra=1,
    can_delete=True,
    min_num=0,
    validate_min=True
)
