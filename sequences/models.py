from django.db import models
from django.contrib.auth.models import User
from pages.models import Page
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date


class Sequence(models.Model):
    """
    Modèle pour représenter une séquence pédagogique.
    Une séquence regroupe plusieurs séances (fiches) autour d'un thème ou objectif commun.
    """
    
    # Informations de base
    name = models.CharField(
        max_length=255,
        verbose_name="Nom de la séquence",
        help_text="Titre de la séquence pédagogique"
    )
    
    description = models.TextField(
        blank=True,
        verbose_name="Description",
        help_text="Description détaillée de la séquence et de ses objectifs"
    )
    
    # Relations
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sequences',
        verbose_name="Enseignant",
        help_text="Enseignant qui a créé cette séquence"
    )
    
    discipline = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name='sequences',
        verbose_name="Discipline",
        help_text="Discipline à laquelle appartient cette séquence (optionnel)",
        limit_choices_to={'parent__isnull': True},  # Seulement les disciplines (pages parentes)
        null=True,
        blank=True
    )
    
    # Période scolaire (optionnelle)
    periode_scolaire = models.ForeignKey(
        'PeriodeScolaire',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sequences',
        verbose_name="Période scolaire",
        help_text="Période scolaire dans laquelle s'inscrit cette séquence"
    )
    
    # Métadonnées pédagogiques
    NIVEAU_CHOICES = [
        ('PS', 'PS - Petite Section'),
        ('MS', 'MS - Moyenne Section'),
        ('GS', 'GS - Grande Section'),
        ('CP', 'CP - Cours Préparatoire'),
        ('CE1', 'CE1 - Cours Élémentaire 1'),
        ('CE2', 'CE2 - Cours Élémentaire 2'),
        ('CM1', 'CM1 - Cours Moyen 1'),
        ('CM2', 'CM2 - Cours Moyen 2'),
        ('6eme', '6ème - Sixième'),
        ('5eme', '5ème - Cinquième'),
        ('4eme', '4ème - Quatrième'),
        ('3eme', '3ème - Troisième'),
    ]
    
    niveau = models.CharField(
        max_length=10,
        choices=NIVEAU_CHOICES,
        blank=True,
        verbose_name="Niveau de classe",
        help_text="Niveau scolaire visé par cette séquence"
    )
    
    duree_estimee = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Durée estimée (séances)",
        help_text="Nombre de séances prévues pour cette séquence"
    )
    
    # Durée totale persistante en minutes pour optimiser les performances et analyses
    total_duration_minutes = models.IntegerField(
        default=0,
        verbose_name="Durée totale en minutes",
        help_text="Durée totale calculée automatiquement à partir de toutes les séances de la séquence"
    )
    
    # Métadonnées temporelles
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Dernière modification"
    )
    
    # Ordre d'affichage
    ordre = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage",
        help_text="Ordre d'affichage dans la liste des séquences"
    )
    
    class Meta:
        ordering = ['discipline', 'ordre', 'name']
        verbose_name = "Séquence pédagogique"
        verbose_name_plural = "Séquences pédagogiques"
        unique_together = ['user', 'name', 'discipline']  # Éviter les doublons
    
    def __str__(self):
        return f"{self.name} ({self.discipline.title})"
    
    def get_seances(self):
        """
        Récupère toutes les séances (fiches) associées à cette séquence.
        Utilise la nouvelle relation ForeignKey sequence_obj.
        """
        return self.seances.all().order_by('date', 'heure_debut')
    
    def get_seances_count(self):
        """Retourne le nombre de séances dans cette séquence."""
        return self.get_seances().count()
    
    def get_progression_percentage(self):
        """
        Calcule le pourcentage de progression de la séquence.
        Basé sur le nombre de séances réalisées (complétées) vs total de séances.
        """
        seances = self.get_seances()
        total_seances = seances.count()
        
        if total_seances == 0:
            return 0
        
        completed_seances = seances.filter(is_completed=True).count()
        return round((completed_seances / total_seances) * 100, 1)
    
    def get_next_seance_number(self):
        """Retourne le numéro de la prochaine séance à créer."""
        return self.get_seances_count() + 1
    
    def get_competences(self):
        """
        Récupère toutes les compétences travaillées dans cette séquence.
        """
        from fiches.models import Fiche
        competences_ids = Fiche.objects.filter(
            user=self.user,
            discipline=self.discipline,
            sequence=self.name
        ).values_list('competences', flat=True).distinct()
        
        return Page.objects.filter(id__in=competences_ids)
    
    def calculate_total_duration_minutes(self):
        """Calcule la durée totale en minutes de toutes les séances de cette séquence."""
        total_minutes = 0
        for seance in self.get_seances():
            if seance.duration_minutes:
                total_minutes += seance.duration_minutes
        return total_minutes
    
    def update_total_duration(self):
        """Met à jour le champ total_duration_minutes avec la durée calculée."""
        self.total_duration_minutes = self.calculate_total_duration_minutes()
        # Utiliser update() pour éviter les boucles infinies avec save()
        Sequence.objects.filter(id=self.id).update(total_duration_minutes=self.total_duration_minutes)
        return self.total_duration_minutes
    
    def get_total_duration_str(self):
        """Retourne la durée totale formatée en chaîne (ex: '2h15', '1h', '45min')."""
        if not self.total_duration_minutes:
            return "0h"
        
        hours = self.total_duration_minutes // 60
        minutes = self.total_duration_minutes % 60
        
        if hours > 0 and minutes > 0:
            return f"{hours}h{minutes:02d}"
        elif hours > 0:
            return f"{hours}h"
        else:
            return f"{minutes}min"
    
    def save(self, *args, **kwargs):
        """
        Surcharge de la méthode save pour gérer l'ordre automatique.
        """
        if not self.ordre:
            # Définir l'ordre comme le maximum + 1 pour cette discipline/utilisateur
            max_ordre = Sequence.objects.filter(
                user=self.user,
                discipline=self.discipline
            ).aggregate(models.Max('ordre'))['ordre__max']
            
            self.ordre = (max_ordre or 0) + 1
        
        super().save(*args, **kwargs)


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
        # Périodes selon le calendrier scolaire français
        periods_data = [
            {
                'numero': 1,
                'nom': 'Période 1',
                'description': 'Début septembre → mi-octobre',
                'date_debut': date(int(annee_scolaire.split('-')[0]), 9, 1),
                'date_fin': date(int(annee_scolaire.split('-')[0]), 10, 31),
                'couleur': '#e74c3c'
            },
            {
                'numero': 2,
                'nom': 'Période 2',
                'description': 'Début novembre → mi-décembre',
                'date_debut': date(int(annee_scolaire.split('-')[0]), 11, 1),
                'date_fin': date(int(annee_scolaire.split('-')[0]), 12, 31),
                'couleur': '#f39c12'
            },
            {
                'numero': 3,
                'nom': 'Période 3',
                'description': 'Début janvier → mi-février',
                'date_debut': date(int(annee_scolaire.split('-')[1]), 1, 1),
                'date_fin': date(int(annee_scolaire.split('-')[1]), 2, 28),
                'couleur': '#3498db'
            },
            {
                'numero': 4,
                'nom': 'Période 4',
                'description': 'Fin février → mi-avril',
                'date_debut': date(int(annee_scolaire.split('-')[1]), 3, 1),
                'date_fin': date(int(annee_scolaire.split('-')[1]), 4, 30),
                'couleur': '#2ecc71'
            },
            {
                'numero': 5,
                'nom': 'Période 5',
                'description': 'Fin avril → début juillet',
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
