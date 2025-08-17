from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date


class PeriodeScolaire(models.Model):
    """
    Modèle pour représenter une période scolaire (5 maximum par année).
    Permet d'organiser les séquences par périodes dans l'année scolaire.
    """
    
    PERIODE_CHOICES = [
        (1, 'Période 1 - Septembre/Octobre'),
        (2, 'Période 2 - Novembre/Décembre'),
        (3, 'Période 3 - Janvier/Février'),
        (4, 'Période 4 - Mars/Avril'),
        (5, 'Période 5 - Mai/Juin/Juillet'),
    ]
    
    # Informations de base
    nom = models.CharField(
        max_length=100,
        verbose_name="Nom de la période",
        help_text="Ex: Période 1 - Rentrée scolaire"
    )
    
    numero = models.IntegerField(
        choices=PERIODE_CHOICES,
        verbose_name="Numéro de période",
        help_text="Numéro de la période (1 à 5)"
    )
    
    # Dates
    date_debut = models.DateField(
        verbose_name="Date de début",
        help_text="Date de début de la période"
    )
    
    date_fin = models.DateField(
        verbose_name="Date de fin",
        help_text="Date de fin de la période"
    )
    
    # Année scolaire
    annee_scolaire = models.CharField(
        max_length=9,
        verbose_name="Année scolaire",
        help_text="Ex: 2024-2025"
    )
    
    # Relations
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='periodes_scolaires',
        verbose_name="Enseignant"
    )
    
    # Métadonnées
    description = models.TextField(
        blank=True,
        verbose_name="Description",
        help_text="Description optionnelle de la période (thèmes, projets...)"
    )
    
    couleur = models.CharField(
        max_length=7,
        default="#3498db",
        verbose_name="Couleur",
        help_text="Couleur d'affichage de la période (format hex: #RRGGBB)"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Période scolaire"
        verbose_name_plural = "Périodes scolaires"
        ordering = ['annee_scolaire', 'numero']
        unique_together = ['user', 'annee_scolaire', 'numero']  # Une seule période N par année par utilisateur
    
    def clean(self):
        """Validation personnalisée"""
        super().clean()
        
        # Vérifier que la date de fin est après la date de début
        if self.date_debut and self.date_fin:
            if self.date_fin <= self.date_debut:
                raise ValidationError("La date de fin doit être postérieure à la date de début.")
        
        # Vérifier qu'il n'y a pas plus de 5 périodes par année scolaire
        if self.pk is None:  # Nouvelle période
            existing_periods = PeriodeScolaire.objects.filter(
                user=self.user,
                annee_scolaire=self.annee_scolaire
            ).count()
            
            if existing_periods >= 5:
                raise ValidationError(f"Vous ne pouvez pas créer plus de 5 périodes par année scolaire. Vous avez déjà {existing_periods} périodes pour {self.annee_scolaire}.")
    
    def save(self, *args, **kwargs):
        """Override save pour validation"""
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nom} ({self.annee_scolaire})"
    
    @property
    def duree_jours(self):
        """Calcule la durée de la période en jours"""
        if self.date_debut and self.date_fin:
            return (self.date_fin - self.date_debut).days + 1
        return 0
    
    @property
    def est_active(self):
        """Vérifie si la période est actuellement active"""
        today = date.today()
        return self.date_debut <= today <= self.date_fin
    
    @classmethod
    def get_current_period(cls, user):
        """Récupère la période actuelle pour un utilisateur"""
        today = date.today()
        return cls.objects.filter(
            user=user,
            date_debut__lte=today,
            date_fin__gte=today
        ).first()
    
    @classmethod
    def create_default_periods(cls, user, annee_scolaire):
        """Crée les 5 périodes par défaut pour une année scolaire"""
        # Dates approximatives (à ajuster selon les zones)
        periods_data = [
            {
                'numero': 1,
                'nom': 'Période 1 - Rentrée',
                'date_debut': date(int(annee_scolaire.split('-')[0]), 9, 1),
                'date_fin': date(int(annee_scolaire.split('-')[0]), 10, 31),
                'couleur': '#e74c3c'
            },
            {
                'numero': 2,
                'nom': 'Période 2 - Automne',
                'date_debut': date(int(annee_scolaire.split('-')[0]), 11, 1),
                'date_fin': date(int(annee_scolaire.split('-')[0]), 12, 31),
                'couleur': '#f39c12'
            },
            {
                'numero': 3,
                'nom': 'Période 3 - Hiver',
                'date_debut': date(int(annee_scolaire.split('-')[1]), 1, 1),
                'date_fin': date(int(annee_scolaire.split('-')[1]), 2, 28),
                'couleur': '#3498db'
            },
            {
                'numero': 4,
                'nom': 'Période 4 - Printemps',
                'date_debut': date(int(annee_scolaire.split('-')[1]), 3, 1),
                'date_fin': date(int(annee_scolaire.split('-')[1]), 4, 30),
                'couleur': '#2ecc71'
            },
            {
                'numero': 5,
                'nom': 'Période 5 - Fin d\'année',
                'date_debut': date(int(annee_scolaire.split('-')[1]), 5, 1),
                'date_fin': date(int(annee_scolaire.split('-')[1]), 7, 31),
                'couleur': '#9b59b6'
            }
        ]
        
        created_periods = []
        for period_data in periods_data:
            period = cls.objects.create(
                user=user,
                annee_scolaire=annee_scolaire,
                **period_data
            )
            created_periods.append(period)
        
        return created_periods
