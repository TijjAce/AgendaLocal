# === CONFIGURATIONS DE SÉCURITÉ POUR LES MIDDLEWARES ===
import os

# Mode maintenance (à activer/désactiver selon les besoins)
MAINTENANCE_MODE = False

# Déterminer si on est en mode debug
DEBUG_MODE = os.environ.get('DJANGO_DEBUG', 'True').lower() == 'true'

# Configuration des sessions pour la sécurité
SESSION_COOKIE_AGE = 3600 * 24 * 7  # 7 jours
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = not DEBUG_MODE  # HTTPS uniquement en production

# Restriction d'accès par IP (optionnel - décommentez pour activer)
# ALLOWED_IPS = [
#     '127.0.0.1',
#     '192.168.1.0/24',  # Réseau local
#     # Ajoutez vos IPs autorisées ici
# ]

# Configuration de sécurité renforcée
if not DEBUG_MODE:
    # Protection CSRF renforcée
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    CSRF_USE_SESSIONS = True
    
    # Protection contre les attaques de timing
    USE_TZ = True
    
    # Sécurité des cookies
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    
    # Headers de sécurité supplémentaires
    SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
    
# Limitation du taux de requêtes (peut être étendu avec django-ratelimit)
# RATELIMIT_ENABLE = True
# RATELIMIT_USE_CACHE = 'default'

# Logging de sécurité robuste (compatible production Railway)
import os

# Créer le dossier logs s'il n'existe pas
LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
if not os.path.exists(LOGS_DIR):
    try:
        os.makedirs(LOGS_DIR, exist_ok=True)
    except (OSError, PermissionError):
        # En cas d'échec, utiliser uniquement la console
        LOGS_DIR = None

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'secure': {
            'format': '{levelname} {asctime} [{name}] {message}',
            'style': '{',
        },
        'detailed': {
            'format': '{levelname} {asctime} [{name}] {pathname}:{lineno} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'secure',
        },
        'console_errors': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'main.middleware': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'main.middleware.secure_error_middleware': {
            'handlers': ['console_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
    },
}

# Ajouter les handlers de fichiers seulement si le dossier logs est accessible
if LOGS_DIR and os.access(LOGS_DIR, os.W_OK):
    LOGGING['handlers'].update({
        'security_file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, 'security.log'),
            'formatter': 'secure',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, 'errors.log'),
            'formatter': 'detailed',
        },
    })
    
    # Ajouter les handlers de fichiers aux loggers
    LOGGING['loggers']['main.middleware']['handlers'].append('security_file')
    LOGGING['loggers']['main.middleware.secure_error_middleware']['handlers'].append('error_file')
    LOGGING['loggers']['django.security']['handlers'].append('security_file')
