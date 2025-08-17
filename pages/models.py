from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import os

class Page(MPTTModel):
    CYCLE_CHOICES = [
        ('cycle_1', 'Cycle 1'),
        ('cycle_2', 'Cycle 2'),
        ('cycle_3', 'Cycle 3'),
    ]

    title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=320, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        db_index=True
    )
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False)

    # Champs pédagogiques pour les enfants
    cycle_enseignement = models.CharField(
        max_length=10,
        choices=CYCLE_CHOICES,
        blank=True,
        null=True,
        verbose_name="Cycle d'enseignement"
    )
    objectifs_generaux = models.TextField(
        blank=True,
        null=True,
        verbose_name="Objectifs généraux"
    )
    competence_generale = models.TextField(
        blank=True,
        null=True,
        verbose_name="Compétence générale"
    )

    # Couleur pour la discipline (racine)
    couleur = models.CharField(
        max_length=7,
        blank=True,
        null=True,
        help_text="Couleur hexadécimale (ex: #0d6efd). S'applique aux enfants.",
        verbose_name="Couleur de la discipline"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        ordering = ['tree_id', 'lft']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.parent:
            return f'{self.parent.get_absolute_url()}/{self.slug}'
        return f'/{self.slug}'

    def is_discipline_root(self):
        """Retourne True si la page est une racine (donc une discipline)."""
        return self.parent is None

    def get_heritable_field(self, field_name):
        """Retourne la valeur du champ, sinon remonte à travers les parents."""
        value = getattr(self, field_name)
        if value:
            return value
        elif self.parent:
            return self.parent.get_heritable_field(field_name)
        return None

    def get_discipline_color(self):
        """Retourne la couleur définie dans la racine (discipline)."""
        if self.is_discipline_root():
            return self.couleur
        elif self.parent:
            return self.parent.get_discipline_color()
        return None


class PageAnnexe(models.Model):
    """
    Modèle pour gérer les annexes (images et PDF) des compétences (Pages).
    Similaire au modèle Annexe des fiches mais pour les Pages.
    """
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name='annexes',
        verbose_name="Compétence"
    )
    nom = models.CharField(
        max_length=255,
        verbose_name="Nom de l'annexe"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description"
    )
    fichier = models.FileField(
        upload_to='pages/annexes/',
        verbose_name="Fichier"
    )
    type_fichier = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Type de fichier"
    )
    taille_fichier = models.PositiveIntegerField(
        default=0,
        verbose_name="Taille en octets"
    )
    date_ajout = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date d'ajout"
    )
    ordre = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )
    
    class Meta:
        ordering = ['ordre', 'date_ajout']
        verbose_name = "Annexe de compétence"
        verbose_name_plural = "Annexes de compétences"
    
    def __str__(self):
        return f"{self.nom} - {self.page.title}"
    
    def save(self, *args, **kwargs):
        """Détecter automatiquement le type et la taille du fichier."""
        if self.fichier:
            # Détecter le type de fichier
            file_extension = os.path.splitext(self.fichier.name)[1].lower()
            
            type_mapping = {
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.gif': 'image/gif',
                '.webp': 'image/webp',
                '.pdf': 'application/pdf',
            }
            
            self.type_fichier = type_mapping.get(file_extension, 'application/octet-stream')
            
            # Calculer la taille du fichier
            if hasattr(self.fichier, 'size'):
                self.taille_fichier = self.fichier.size
        
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        """Supprimer le fichier physique lors de la suppression de l'annexe."""
        if self.fichier:
            try:
                if os.path.isfile(self.fichier.path):
                    os.remove(self.fichier.path)
            except (ValueError, OSError):
                pass  # Le fichier n'existe pas ou erreur d'accès
        super().delete(*args, **kwargs)
    
    @property
    def taille_lisible(self):
        """Retourne la taille du fichier dans un format lisible."""
        if self.taille_fichier == 0:
            return "0 B"
        
        taille = self.taille_fichier
        unites = ['B', 'KB', 'MB', 'GB']
        
        for unite in unites:
            if taille < 1024:
                return f"{taille:.1f} {unite}"
            taille /= 1024
        
        return f"{taille:.1f} TB"
    
    @property
    def est_image(self):
        """Vérifie si le fichier est une image."""
        return self.type_fichier.startswith('image/')
    
    @property
    def est_pdf(self):
        """Vérifie si le fichier est un PDF."""
        return self.type_fichier == 'application/pdf'
    
    def clean(self):
        """Validation personnalisée du fichier."""
        from django.core.exceptions import ValidationError
        
        if self.fichier:
            # Vérifier la taille (max 10MB)
            max_size = 10 * 1024 * 1024  # 10MB
            if self.fichier.size > max_size:
                raise ValidationError(f'Le fichier est trop volumineux. Taille maximum: 10MB')
            
            # Vérifier l'extension
            file_extension = os.path.splitext(self.fichier.name)[1].lower()
            allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.pdf']
            
            if file_extension not in allowed_extensions:
                raise ValidationError(
                    f'Type de fichier non autorisé. Extensions autorisées: {", ".join(allowed_extensions)}'
                )
