from django.db import models
from pages.models import Page
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import os

class Fiche(models.Model):
    # Relation avec l'utilisateur
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='fiches',
        verbose_name="Utilisateur",
        null=True,  # Temporaire pour la migration
        blank=True
    )
    titre = models.CharField(max_length=255)
    groupes = models.CharField(max_length=50, blank=True, verbose_name="groupes")
    discipline = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='fiches',
        verbose_name="Discipline"
    )
    objectifGeneral= models.CharField(max_length=400, blank=True, verbose_name="objectifGeneral")
    date = models.DateField(default=timezone.now)

    heure_debut = models.TimeField(null=True, blank=True, verbose_name="Heure de début")
    heure_fin = models.TimeField(null=True, blank=True, verbose_name="Heure de fin")
    duree = models.CharField(max_length=50, blank=True, verbose_name="Durée (calculée ou manuelle)")
    materiel =models.CharField(max_length=250, blank=True, verbose_name="materiel")
    
    # Durée persistante en minutes pour optimiser les performances et analyses
    duration_minutes = models.IntegerField(
        null=True, 
        blank=True, 
        verbose_name="Durée en minutes",
        help_text="Durée calculée automatiquement à partir des heures de début et fin"
    )

    sequence = models.CharField(max_length=255, blank=True, verbose_name="Séquence")
    
    # Nouvelle relation vers le modèle Sequence
    sequence_obj = models.ForeignKey(
        'sequences.Sequence',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='seances',
        verbose_name="Séquence (objet)",
        help_text="Séquence pédagogique à laquelle appartient cette séance"
    )
    
    NIVEAU_CHOICES = [
        ('PS', 'PS - Petite Section'),
        ('MS', 'MS - Moyenne Section'),
        ('GS', 'GS - Grande Section'),
        ('CP', 'CP - Cours Préparatoire'),
        ('CE1', 'CE1 - Cours Élémentaire 1'),
        ('CE2', 'CE2 - Cours Élémentaire 2'),
        ('CM1', 'CM1 - Cours Moyen 1'),
        ('6eme', '6ème - Sixième'),
    ]
    
    niveau = models.CharField(
        max_length=10,
        choices=NIVEAU_CHOICES,
        blank=True,
        verbose_name="Niveau de classe"
    )

    competences = models.ManyToManyField(
        Page,
        blank=True,
        related_name='fiches_competences',
        verbose_name="Compétences associées"
    )
    competencesSup = models.CharField(max_length=255, blank= True)  
    AFC =  models.CharField(max_length=255, blank=True) 
    bilan = models.TextField(blank=True, verbose_name="Bilan de la séance")
    
    # Champ pour marquer la séance comme réalisée
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Séance réalisée",
        help_text="Indique si cette séance a été effectuée"
    )
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Date de réalisation",
        help_text="Date et heure à laquelle la séance a été marquée comme réalisée"
    )

    couleur = models.CharField(
        max_length=7,
        blank=True,
        help_text="Code hexadécimal (ex: #ff0000)",
        verbose_name="Couleur de la discipline"
    )

    # Champs de partage
    is_shared = models.BooleanField(
        default=False,
        verbose_name="Partagé avec la communauté",
        help_text="Permet aux autres utilisateurs de voir et importer cette fiche"
    )
    shared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Date de partage"
    )
    import_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Nombre d'importations",
        help_text="Nombre de fois que cette fiche a été importée par d'autres utilisateurs"
    )
    original_author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='authored_fiches',
        verbose_name="Auteur original",
        help_text="Utilisateur qui a créé la fiche originale (pour les fiches importées)"
    )
    
    # Champs de suivi de réalisation
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Séance réalisée",
        help_text="Indique si la séance a été réalisée"
    )
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Validée le",
        help_text="Date et heure de validation de la réalisation"
    )
    
    # Ajout de champs utiles pour structuration future
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', 'titre']
        verbose_name = "Fiche de préparation"
        verbose_name_plural = "Fiches de préparation"

    def __str__(self):
        return f"{self.titre} ({self.date.strftime('%d/%m/%Y')})"

    def clean(self):
        if self.heure_debut and self.heure_fin and self.heure_debut >= self.heure_fin:
            raise ValidationError("L'heure de début doit être inférieure à l'heure de fin.")

    def calculer_duree(self):
        """Calcule la durée en hh:mm à partir des heures si elles existent."""
        if self.heure_debut and self.heure_fin:
            delta = (self.heure_fin.hour * 60 + self.heure_fin.minute) - (self.heure_debut.hour * 60 + self.heure_debut.minute)
            if delta > 0:
                heures = delta // 60
                minutes = delta % 60
                return f"{heures}h{minutes:02d}"
        return None
    
    def calculer_duree_minutes(self):
        """Calcule la durée en minutes à partir des heures si elles existent."""
        if self.heure_debut and self.heure_fin:
            delta = (self.heure_fin.hour * 60 + self.heure_fin.minute) - (self.heure_debut.hour * 60 + self.heure_debut.minute)
            return delta if delta > 0 else 0
        return 0
    
    def update_duration_minutes(self):
        """Met à jour le champ duration_minutes avec la durée calculée."""
        self.duration_minutes = self.calculer_duree_minutes()
        return self.duration_minutes

    def save(self, *args, **kwargs):
        # Calculer automatiquement la durée textuelle si vide
        if not self.duree:
            self.duree = self.calculer_duree() or ""
        
        # Toujours mettre à jour la durée en minutes pour la persistance
        self.update_duration_minutes()
        
        super().save(*args, **kwargs)
        
        # Mettre à jour la durée totale de la séquence si elle existe
        if self.sequence_obj:
            self.sequence_obj.update_total_duration()


class Phase(models.Model):
    fiche = models.ForeignKey(
        Fiche,
        related_name='phases',
        on_delete=models.CASCADE,
        verbose_name="Fiche de préparation"
    )
    phase = models.CharField(max_length=255, verbose_name="Nom de la phase")
    duree = models.CharField(max_length=50, blank=True, verbose_name="Durée")
    ce = models.CharField(max_length=255, blank=True, verbose_name="Compétence évaluée")
    deroulement = models.TextField(blank=True, verbose_name="Déroulement de la phase")
    posture = models.CharField(max_length=255, blank=True, verbose_name="Posture de l'enseignant")
    ordre = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['ordre']
        verbose_name = "Phase"
        verbose_name_plural = "Phases"

    def __str__(self):
        return f"{self.phase} (Fiche: {self.fiche.titre})"

    def save(self, *args, **kwargs):
        if self.ordre == 0:  # Si ordre non défini, on le place à la fin
            last_order = Phase.objects.filter(fiche=self.fiche).aggregate(models.Max('ordre'))['ordre__max'] or 0
            self.ordre = last_order + 1
        super().save(*args, **kwargs)


def annexe_upload_path(instance, filename):
    """
    Génère le chemin d'upload pour les annexes.
    Format: annexes/user_id/fiche_id/filename
    """
    return f'annexes/{instance.fiche.user.id}/{instance.fiche.id}/{filename}'


class Annexe(models.Model):
    """
    Modèle pour les annexes (images, PDF) associées aux fiches.
    """
    TYPES_FICHIER = [
        ('image', 'Image'),
        ('pdf', 'PDF'),
        ('document', 'Document'),
    ]
    
    fiche = models.ForeignKey(
        Fiche,
        on_delete=models.CASCADE,
        related_name='annexes',
        verbose_name="Fiche de préparation"
    )
    
    nom = models.CharField(
        max_length=255,
        verbose_name="Nom de l'annexe",
        help_text="Nom descriptif de l'annexe"
    )
    
    fichier = models.FileField(
        upload_to=annexe_upload_path,
        verbose_name="Fichier",
        help_text="Image (JPG, PNG, GIF) ou document PDF"
    )
    
    type_fichier = models.CharField(
        max_length=20,
        choices=TYPES_FICHIER,
        verbose_name="Type de fichier"
    )
    
    taille_fichier = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Taille du fichier (bytes)"
    )
    
    date_ajout = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date d'ajout"
    )
    
    description = models.TextField(
        blank=True,
        verbose_name="Description",
        help_text="Description optionnelle de l'annexe"
    )
    
    ordre = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )
    
    class Meta:
        ordering = ['ordre', 'date_ajout']
        verbose_name = "Annexe"
        verbose_name_plural = "Annexes"
    
    def __str__(self):
        return f"{self.nom} ({self.fiche.titre})"
    
    def save(self, *args, **kwargs):
        # Déterminer automatiquement le type de fichier
        if self.fichier:
            extension = os.path.splitext(self.fichier.name)[1].lower()
            if extension in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                self.type_fichier = 'image'
            elif extension == '.pdf':
                self.type_fichier = 'pdf'
            else:
                self.type_fichier = 'document'
            
            # Stocker la taille du fichier
            if hasattr(self.fichier, 'size'):
                self.taille_fichier = self.fichier.size
        
        # Définir l'ordre si non spécifié
        if self.ordre == 0:
            last_order = Annexe.objects.filter(fiche=self.fiche).aggregate(models.Max('ordre'))['ordre__max'] or 0
            self.ordre = last_order + 1
        
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # Supprimer le fichier physique lors de la suppression de l'annexe
        if self.fichier:
            if os.path.isfile(self.fichier.path):
                os.remove(self.fichier.path)
        super().delete(*args, **kwargs)
    
    @property
    def taille_lisible(self):
        """Retourne la taille du fichier dans un format lisible."""
        if not self.taille_fichier:
            return "Inconnue"
        
        for unit in ['B', 'KB', 'MB', 'GB']:
            if self.taille_fichier < 1024.0:
                return f"{self.taille_fichier:.1f} {unit}"
            self.taille_fichier /= 1024.0
        return f"{self.taille_fichier:.1f} TB"
    
    @property
    def est_image(self):
        """Vérifie si l'annexe est une image."""
        return self.type_fichier == 'image'
    
    @property
    def est_pdf(self):
        """Vérifie si l'annexe est un PDF."""
        return self.type_fichier == 'pdf'
