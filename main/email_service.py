"""
Service d'envoi d'emails simplifié pour développement local
"""

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging

logger = logging.getLogger(__name__)

class EmailService:
    """Service pour l'envoi d'emails via Django backend"""
    
    def __init__(self):
        """Initialise le service"""
        pass
    
    def send_welcome_email(self, user_email, username):
        """
        Envoie un email de bienvenue (mode développement - console)
        """
        try:
            subject = f"Bienvenue {username} !"
            message = f"Bonjour {username},\n\nBienvenue sur Planif Facile !\n\nCordialement,\nL'équipe Planif Facile"
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
                fail_silently=False,
            )
            
            logger.info(f"Email de bienvenue envoyé à {user_email}")
            return True
            
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi de l'email à {user_email}: {str(e)}")
            return False
    
    def send_confirmation_email(self, user_email, username, confirmation_token=None):
        """
        Envoie un email de confirmation (mode développement - console)
        """
        try:
            subject = "Confirmez votre inscription"
            message = f"Bonjour {username},\n\nMerci de votre inscription !\n\nToken: {confirmation_token}\n\nCordialement,\nL'équipe Planif Facile"
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
                fail_silently=False,
            )
            
            logger.info(f"Email de confirmation envoyé à {user_email}")
            return True
                
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi de l'email: {str(e)}")
            return False

# Instance globale du service
email_service = EmailService()
