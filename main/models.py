from django.db import models
from django.contrib.auth.models import User
from pages.models import Page
import uuid
from django.utils import timezone
from datetime import timedelta

class UserDisciplineColorPreference(models.Model):
    """
    Modèle pour stocker les préférences de couleur de discipline par utilisateur.
    Permet à chaque utilisateur d'avoir sa propre couleur pour chaque discipline.
    """
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name="Utilisateur"
    )
    discipline = models.ForeignKey(
        Page, 
        on_delete=models.CASCADE,
        limit_choices_to={'parent__isnull': True},  # Seulement les disciplines racines
        verbose_name="Discipline"
    )
    couleur = models.CharField(
        max_length=7,
        help_text="Couleur hexadécimale (ex: #0d6efd)",
        verbose_name="Couleur personnalisée"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'discipline')
        verbose_name = "Préférence de couleur de discipline"
        verbose_name_plural = "Préférences de couleur de disciplines"
        
    def __str__(self):
        return f"{self.user.username} - {self.discipline.title} ({self.couleur})"
    
    @staticmethod
    def get_user_discipline_color(user, discipline):
        """
        Récupère la couleur personnalisée d'une discipline pour un utilisateur.
        Si l'utilisateur n'a pas de préférence, retourne la couleur par défaut de la discipline.
        """
        try:
            preference = UserDisciplineColorPreference.objects.get(
                user=user, 
                discipline=discipline
            )
            return preference.couleur
        except UserDisciplineColorPreference.DoesNotExist:
            # Retourner la couleur par défaut de la discipline ou une couleur par défaut
            return discipline.couleur or '#0d6efd'
    
    @staticmethod
    def set_user_discipline_color(user, discipline, couleur):
        """
        Définit ou met à jour la couleur personnalisée d'une discipline pour un utilisateur.
        """
        preference, created = UserDisciplineColorPreference.objects.get_or_create(
            user=user,
            discipline=discipline,
            defaults={'couleur': couleur}
        )
        if not created:
            preference.couleur = couleur
            preference.save()
        return preference

# Modèle EmailValidationToken supprimé - authentification simplifiée

class AccessLog(models.Model):
    """
    Modèle pour enregistrer les accès à l'application (IPs, User-Agents, etc.)
    Utile pour détecter les bots et les tentatives d'intrusion
    """
    ip_address = models.GenericIPAddressField(
        verbose_name="Adresse IP"
    )
    user_agent = models.TextField(
        blank=True,
        null=True,
        verbose_name="User Agent"
    )
    path = models.CharField(
        max_length=500,
        verbose_name="Chemin d'accès"
    )
    method = models.CharField(
        max_length=10,
        default='GET',
        verbose_name="Méthode HTTP"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Utilisateur (si connecté)"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Horodatage"
    )
    is_bot = models.BooleanField(
        default=False,
        verbose_name="Bot détecté"
    )
    is_suspicious = models.BooleanField(
        default=False,
        verbose_name="Activité suspecte"
    )
    
    class Meta:
        verbose_name = "Log d'accès"
        verbose_name_plural = "Logs d'accès"
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['ip_address', '-timestamp']),
            models.Index(fields=['is_bot', '-timestamp']),
            models.Index(fields=['is_suspicious', '-timestamp']),
        ]
    
    def __str__(self):
        return f"{self.ip_address} - {self.path} ({self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"
    
    @property
    def is_known_bot(self):
        """Détecte si le User-Agent correspond à un bot connu"""
        if not self.user_agent:
            return False
        
        bot_patterns = [
            'googlebot', 'bingbot', 'slurp', 'duckduckbot', 'baiduspider',
            'yandexbot', 'facebookexternalhit', 'twitterbot', 'linkedinbot',
            'whatsapp', 'telegrambot', 'curl', 'wget', 'python-requests',
            'sqlmap', 'nmap', 'nikto', 'dirb', 'gobuster', 'wpscan'
        ]
        
        user_agent_lower = self.user_agent.lower()
        return any(pattern in user_agent_lower for pattern in bot_patterns)
    
    @property
    def is_security_tool(self):
        """Détecte si le User-Agent correspond à un outil de sécurité/scan"""
        if not self.user_agent:
            return False
        
        security_patterns = [
            'sqlmap', 'nmap', 'nikto', 'dirb', 'gobuster', 'wpscan',
            'burp', 'owasp', 'zap', 'acunetix', 'nessus', 'openvas'
        ]
        
        user_agent_lower = self.user_agent.lower()
        return any(pattern in user_agent_lower for pattern in security_patterns)
    
    def save(self, *args, **kwargs):
        """Override save pour détecter automatiquement les bots et activités suspectes"""
        self.is_bot = self.is_known_bot
        self.is_suspicious = self.is_security_tool
        super().save(*args, **kwargs)

# Create your models here.
