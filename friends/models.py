from django.db import models
from django.contrib.auth.models import User
from sequences.models import Sequence
from fiches.models import Fiche
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class UserProfile(models.Model):
    """Profil utilisateur étendu pour les informations de localisation et avatar"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bitmoji_url = models.URLField(
        max_length=500, 
        blank=True, 
        null=True,
        help_text="URL du Bitmoji de l'utilisateur (obsolète)"
    )
    
    # Nouveaux champs pour le générateur d'avatar
    avatar_type = models.CharField(
        max_length=20,
        choices=[
            ('bitmoji', 'Bitmoji (import)'),
            ('generated', 'Avatar généré'),
        ],
        default='generated',
        help_text="Type d'avatar utilisé"
    )
    
    # Configuration de l'avatar généré
    avatar_skin_color = models.CharField(
        max_length=7,
        default='#FDBCB4',
        help_text="Couleur de peau (hex)"
    )
    avatar_hair_style = models.CharField(
        max_length=20,
        choices=[
            ('short', 'Cheveux courts'),
            ('medium', 'Cheveux mi-longs'),
            ('long', 'Cheveux longs'),
            ('curly', 'Cheveux bouclés'),
            ('bald', 'Chauve'),
        ],
        default='short',
        help_text="Style de cheveux"
    )
    avatar_hair_color = models.CharField(
        max_length=7,
        default='#8B4513',
        help_text="Couleur des cheveux (hex)"
    )
    avatar_eye_color = models.CharField(
        max_length=7,
        default='#4A90E2',
        help_text="Couleur des yeux (hex)"
    )
    avatar_clothing_color = models.CharField(
        max_length=7,
        default='#2E86AB',
        help_text="Couleur des vêtements (hex)"
    )
    avatar_accessories = models.CharField(
        max_length=50,
        choices=[
            ('none', 'Aucun'),
            ('glasses', 'Lunettes'),
            ('hat', 'Chapeau'),
            ('earrings', 'Boucles d\'oreilles'),
        ],
        default='none',
        help_text="Accessoires"
    )
    latitude = models.FloatField(
        blank=True, 
        null=True,
        validators=[MinValueValidator(41.0), MaxValueValidator(51.5)],
        help_text="Latitude de la position sur la carte de France (41.0 à 51.5)"
    )
    longitude = models.FloatField(
        blank=True, 
        null=True,
        validators=[MinValueValidator(-5.5), MaxValueValidator(10.0)],
        help_text="Longitude de la position sur la carte de France (-5.5 à 10.0)"
    )
    ville = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Ville de l'utilisateur"
    )
    departement = models.CharField(
        max_length=3, 
        blank=True, 
        null=True,
        help_text="Code département (ex: 75, 69, 13)"
    )
    bio = models.TextField(
        max_length=500, 
        blank=True, 
        null=True,
        help_text="Biographie courte de l'utilisateur"
    )
    is_public = models.BooleanField(
        default=True,
        help_text="Profil visible sur la carte publique"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Profil utilisateur"
        verbose_name_plural = "Profils utilisateurs"
        
    def __str__(self):
        return f"Profil de {self.user.username}"
    
    @property
    def has_location(self):
        return self.latitude is not None and self.longitude is not None

class Friendship(models.Model):
    """Modèle pour gérer les relations d'amitié entre utilisateurs"""
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('accepted', 'Acceptée'),
        ('declined', 'Refusée'),
        ('blocked', 'Bloquée'),
    ]
    
    requester = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='sent_friend_requests',
        verbose_name="Demandeur"
    )
    addressee = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='received_friend_requests',
        verbose_name="Destinataire"
    )
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='pending',
        verbose_name="Statut"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('requester', 'addressee')
        verbose_name = "Amitié"
        verbose_name_plural = "Amitiés"
        
    def __str__(self):
        return f"{self.requester.username} -> {self.addressee.username} ({self.status})"
    
    @classmethod
    def are_friends(cls, user1, user2):
        """Vérifie si deux utilisateurs sont amis"""
        return cls.objects.filter(
            models.Q(requester=user1, addressee=user2, status='accepted') |
            models.Q(requester=user2, addressee=user1, status='accepted')
        ).exists()
    
    @classmethod
    def get_friends(cls, user):
        """Récupère tous les amis d'un utilisateur"""
        friendships = cls.objects.filter(
            models.Q(requester=user, status='accepted') |
            models.Q(addressee=user, status='accepted')
        )
        
        friends = []
        for friendship in friendships:
            if friendship.requester == user:
                friends.append(friendship.addressee)
            else:
                friends.append(friendship.requester)
        return friends

class SharedSequence(models.Model):
    """Modèle pour le partage de séquences entre amis"""
    sequence = models.ForeignKey(
        Sequence, 
        on_delete=models.CASCADE,
        verbose_name="Séquence"
    )
    shared_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='shared_sequences',
        verbose_name="Partagé par"
    )
    shared_with = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='received_sequences',
        verbose_name="Partagé avec"
    )
    message = models.TextField(
        max_length=500, 
        blank=True, 
        null=True,
        help_text="Message d'accompagnement"
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name="Lu"
    )
    can_edit = models.BooleanField(
        default=False,
        help_text="L'ami peut-il modifier cette séquence ?"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('sequence', 'shared_by', 'shared_with')
        verbose_name = "Séquence partagée"
        verbose_name_plural = "Séquences partagées"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.sequence.titre} partagée par {self.shared_by.username} avec {self.shared_with.username}"

class SharedFiche(models.Model):
    """Modèle pour le partage de fiches entre amis"""
    fiche = models.ForeignKey(
        Fiche, 
        on_delete=models.CASCADE,
        verbose_name="Fiche"
    )
    shared_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='shared_fiches',
        verbose_name="Partagé par"
    )
    shared_with = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='received_fiches',
        verbose_name="Partagé avec"
    )
    message = models.TextField(
        max_length=500, 
        blank=True, 
        null=True,
        help_text="Message d'accompagnement"
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name="Lu"
    )
    can_edit = models.BooleanField(
        default=False,
        help_text="L'ami peut-il modifier cette fiche ?"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('fiche', 'shared_by', 'shared_with')
        verbose_name = "Fiche partagée"
        verbose_name_plural = "Fiches partagées"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.fiche.titre} partagée par {self.shared_by.username} avec {self.shared_with.username}"
