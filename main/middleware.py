from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.deprecation import MiddlewareMixin
from django.utils.html import escape
from django.conf import settings
import logging
import os

logger = logging.getLogger(__name__)

def is_ip_authorized(client_ip, authorized_ips):
    """
    Vérifie si une IP client est autorisée.
    Supporte les IP exactes et les préfixes IPv6 (ex: 2a01:cb19:948c:f500::/64)
    """
    import ipaddress
    
    logger.error(f"=== DEBUG VALIDATION IP ===")
    logger.error(f"IP client à valider: {client_ip}")
    logger.error(f"IPs autorisées: {authorized_ips}")
    
    for allowed in authorized_ips:
        logger.error(f"Test avec: {allowed}")
        if '/' in allowed:  # C'est un préfixe réseau
            try:
                network = ipaddress.ip_network(allowed, strict=False)
                client_addr = ipaddress.ip_address(client_ip)
                logger.error(f"Réseau: {network}, IP client: {client_addr}")
                if client_addr in network:
                    logger.error(f"SUCCÈS: IP {client_ip} autorisée via préfixe {allowed}")
                    return True
                else:
                    logger.error(f"ÉCHEC: IP {client_ip} PAS dans le préfixe {allowed}")
            except (ipaddress.AddressValueError, ValueError) as e:
                logger.error(f"ERREUR parsing IP/préfixe: {e}")
                continue
        else:  # IP exacte
            if client_ip == allowed:
                logger.error(f"SUCCÈS: IP {client_ip} autorisée (correspondance exacte)")
                return True
            else:
                logger.error(f"ÉCHEC: IP {client_ip} != {allowed}")
    
    logger.error(f"AUCUNE CORRESPONDANCE TROUVÉE pour {client_ip}")
    logger.error(f"=== FIN DEBUG VALIDATION ===")
    return False

def get_client_ip(request):
    """
    Récupération IP ultra-sécurisée avec validation stricte.
    Supporte les préfixes IPv6 pour éviter les blocages dus aux changements d'IPv6.
    Impossible à compromettre par falsification de headers.
    """
    # IP de la connexion directe (non falsifiable)
    remote_addr = request.META.get('REMOTE_ADDR', 'unknown')
    
    # Récupérer les IPs autorisées depuis la variable d'environnement
    allowed_ips_env = os.getenv('RAILWAY_ALLOWED_IPS', '')
    if not allowed_ips_env:
        logger.error("Variable RAILWAY_ALLOWED_IPS non définie")
        return remote_addr
    
    # Parser les IPs autorisées
    authorized_ips = [ip.strip() for ip in allowed_ips_env.split(',') if ip.strip()]
    
    # Si REMOTE_ADDR est directement une IP autorisée, parfait !
    if is_ip_authorized(remote_addr, authorized_ips):
        logger.debug(f"IP autorisée détectée directement via REMOTE_ADDR: {remote_addr}")
        return remote_addr
    
    # Si c'est Railway (100.64.x.x), vérifier les headers Cloudflare + Railway DE MANIÈRE SÉCURISÉE
    if remote_addr.startswith('100.64.'):
        # Headers à vérifier dans l'ordre de priorité (Cloudflare + Railway)
        headers_to_check = [
            'HTTP_CF_CONNECTING_IP',    # Cloudflare : IP réelle du client
            'HTTP_X_FORWARDED_FOR',     # Standard : peut contenir votre IPv4
            'HTTP_X_REAL_IP',           # Nginx/Railway : IP réelle
        ]
        
        for header_name in headers_to_check:
            header_value = request.META.get(header_name, '')
            if header_value:
                logger.debug(f"Vérification header {header_name}: {header_value}")
                
                # Pour X-Forwarded-For, analyser toutes les IPs de la chaîne
                if header_name == 'HTTP_X_FORWARDED_FOR':
                    ips_chain = [ip.strip() for ip in header_value.split(',')]
                    logger.debug(f"Chaîne IPs X-Forwarded-For: {ips_chain}")
                    
                    # Chercher votre IP (IPv4 ou IPv6) dans toute la chaîne
                    for ip in ips_chain:
                        if is_ip_authorized(ip, authorized_ips):
                            logger.debug(f"IP autorisée trouvée dans la chaîne X-Forwarded-For: {ip}")
                            return ip
                else:
                    # Pour les autres headers, vérification directe
                    ip = header_value.strip()
                    if is_ip_authorized(ip, authorized_ips):
                        logger.debug(f"IP autorisée détectée via {header_name}: {ip}")
                        return ip
        
        # Log de debug pour comprendre ce qui arrive
        logger.warning(f"Aucune IP autorisée trouvée dans les headers Cloudflare/Railway")
        
        # DEBUG COMPLET : Logger TOUS les headers HTTP pour trouver l'IPv4
        logger.error("=== DEBUG HEADERS COMPLET ===")
        for key, value in request.META.items():
            if key.startswith('HTTP_') or key in ['REMOTE_ADDR', 'SERVER_NAME']:
                logger.error(f"{key}: {value}")
        logger.error("=== FIN DEBUG HEADERS ===")
        
        # Headers spécifiques à vérifier
        logger.debug(f"CF_CONNECTING_IP: {request.META.get('HTTP_CF_CONNECTING_IP', 'absent')}")
        logger.debug(f"X_FORWARDED_FOR: {request.META.get('HTTP_X_FORWARDED_FOR', 'absent')}")
        logger.debug(f"X_REAL_IP: {request.META.get('HTTP_X_REAL_IP', 'absent')}")
    
    # Si aucune validation ne passe, retourner l'IP détectée pour logging
    logger.warning(f"Aucune IP autorisée trouvée. REMOTE_ADDR: {remote_addr}")
    return remote_addr

class AuthenticationMiddleware(MiddlewareMixin):
    """
    Middleware pour protéger tout le site.
    Redirige les utilisateurs non authentifiés vers la page de connexion.
    """
    
    # URLs publiques accessibles sans authentification
    PUBLIC_URLS = [
        '/',  # Page d'accueil
        '/fiches/login/',  # Page de connexion
        '/fiches/register/',  # Page d'inscription (si elle existe)
        '/fiches/signup/',  # Page d'inscription (URL réelle)
        '/fiches/signup-success/',  # Page de succès d'inscription
        '/fiches/validate-email/',  # Page de validation d'email
        '/fiches/resend-validation/',  # Page de renvoi de validation
        '/admin/login/',  # Admin login
        '/static/',  # Fichiers statiques
        '/media/',  # Fichiers média
        '/favicon.ico',  # Favicon
    ]
    
    # URLs qui commencent par ces patterns sont publiques
    PUBLIC_URL_PATTERNS = [
        '/static/',
        '/media/',
        '/admin/jsi18n/',  # JavaScript i18n pour l'admin
        # '/ckeditor/',  # CKEditor 4 assets (supprimé)
        '/fiches/validate-email/',  # URLs de validation d'email avec token
    ]
    
    def process_request(self, request):
        """
        Vérifie l'authentification pour chaque requête.
        """
        # Récupérer le chemin de la requête
        path = request.path_info
        
        # Vérifier si l'URL est publique
        if self.is_public_url(path):
            return None
        
        # Vérifier si l'utilisateur est authentifié
        if not request.user.is_authenticated:
            # Stocker l'URL demandée pour redirection après connexion
            request.session['next_url'] = request.get_full_path()
            
            # Ajouter un message d'information
            messages.info(request, "Vous devez vous connecter pour accéder à cette page.")
            
            # Rediriger vers la page de connexion
            return redirect('login')
        
        return None
    
    def is_public_url(self, path):
        """
        Détermine si une URL est publique (accessible sans authentification).
        """
        # Vérifier les URLs exactes
        if path in self.PUBLIC_URLS:
            return True
        
        # Vérification spéciale pour les URLs de validation d'email avec UUID
        if path.startswith('/fiches/validate-email/') and len(path) > len('/fiches/validate-email/'):
            return True
        
        # Vérifier les patterns d'URLs
        for pattern in self.PUBLIC_URL_PATTERNS:
            if path.startswith(pattern):
                return True
        
        return False


class SessionSecurityMiddleware(MiddlewareMixin):
    """
    Middleware de sécurité pour les sessions.
    Gère l'expiration des sessions et la sécurité.
    """
    
    def process_request(self, request):
        """
        Vérifie la validité de la session.
        """
        # Si l'utilisateur est authentifié
        if request.user.is_authenticated:
            # Vérifier si la session a expiré (optionnel)
            # Vous pouvez ajouter ici une logique d'expiration personnalisée
            
            # Régénérer l'ID de session périodiquement pour la sécurité
            if not request.session.get('session_regenerated'):
                request.session.cycle_key()
                request.session['session_regenerated'] = True
        
        return None


class IPWhitelistMiddleware(MiddlewareMixin):
    """
    Middleware pour restreindre l'accès à certaines adresses IP.
    Utilise la variable d'environnement RAILWAY_ALLOWED_IPS pour définir les IP autorisées (IPv4 uniquement).
    """
    
    def process_request(self, request):
        """
        Vérifie si l'adresse IP du client est autorisée.
        """
        # Récupérer les IPs autorisées depuis la variable d'environnement Railway
        allowed_ips_env = os.getenv('RAILWAY_ALLOWED_IPS', '')
        
        # En mode DEBUG (développement), permettre l'accès même sans RAILWAY_ALLOWED_IPS
        if not allowed_ips_env:
            if settings.DEBUG:
                # En développement, permettre l'accès local
                logger.info("Mode DEBUG: RAILWAY_ALLOWED_IPS non définie, autorisation localhost")
                ALLOWED_IPS = ["127.0.0.1", "localhost", "::1"]
            else:
                # En production, refuser l'accès si pas de configuration
                logger.error("Variable d'environnement RAILWAY_ALLOWED_IPS non définie - accès refusé")
                from django.http import HttpResponseForbidden
                return HttpResponseForbidden(
                    "<h1>Accès refusé</h1>"
                    "<p>Configuration de sécurité manquante. Contactez l'administrateur.</p>"
                )
        else:
            # Parser les IPs depuis la variable d'environnement (séparées par des virgules)
            ALLOWED_IPS = [ip.strip() for ip in allowed_ips_env.split(',') if ip.strip()]
        
        # Ajouter localhost en mode DEBUG (si pas déjà inclus)
        if settings.DEBUG and allowed_ips_env:
            # Ajouter localhost seulement si on a des IPs définies via env
            localhost_ips = ["127.0.0.1", "localhost", "::1"]
            for ip in localhost_ips:
                if ip not in ALLOWED_IPS:
                    ALLOWED_IPS.append(ip)
        
        # Récupérer l'IP du client
        client_ip = get_client_ip(request)
        
        # Vérifier si l'IP est autorisée (supporte les préfixes IPv6)
        if not is_ip_authorized(client_ip, ALLOWED_IPS):
            logger.warning(f"Accès refusé pour l'IP: {client_ip} (IPs autorisées: {', '.join(ALLOWED_IPS)})")
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden(
                f"<h1>Accès refusé</h1>"
                f"<p>Votre adresse IP ({escape(client_ip)}) n'est pas autorisée à accéder à cette application.</p>"
                f"<p>IPs autorisées: {escape(', '.join(ALLOWED_IPS))}</p>"
            )
        
        return None


class MaintenanceMiddleware(MiddlewareMixin):
    """
    Middleware pour activer un mode maintenance.
    """
    
    def process_request(self, request):
        """
        Vérifie si le site est en maintenance.
        """
        from django.conf import settings
        from django.http import HttpResponse
        
        # Vérifier si le mode maintenance est activé
        if getattr(settings, 'MAINTENANCE_MODE', False):
            # Permettre l'accès aux superutilisateurs
            if request.user.is_authenticated and request.user.is_superuser:
                return None
            
            # Afficher la page de maintenance
            maintenance_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Maintenance - Planif Facile</title>
                <meta charset="utf-8">
                <style>
                    body { 
                        font-family: Arial, sans-serif; 
                        text-align: center; 
                        padding: 50px;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white;
                    }
                    .container {
                        max-width: 600px;
                        margin: 0 auto;
                        background: rgba(255,255,255,0.1);
                        padding: 40px;
                        border-radius: 10px;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🔧 Maintenance en cours</h1>
                    <p>Planif Facile est temporairement indisponible pour maintenance.</p>
                    <p>Nous serons de retour très bientôt !</p>
                </div>
            </body>
            </html>
            """
            return HttpResponse(maintenance_html, status=503)
        
        return None


class AccessLoggingMiddleware:
    """
    Middleware pour enregistrer tous les accès à l'application
    Utile pour détecter les bots et les tentatives d'intrusion
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        
        # Chemins à ignorer pour éviter le spam de logs
        self.ignored_paths = [
            '/static/',
            '/media/',
            '/favicon.ico',
            '/robots.txt',
            '/sitemap.xml'
        ]
    
    def __call__(self, request):
        # Enregistrer l'accès avant de traiter la requête
        self.log_access(request)
        
        response = self.get_response(request)
        return response
    
    def log_access(self, request):
        """Enregistre l'accès dans la base de données"""
        try:
            # Ignorer certains chemins pour éviter le spam
            if any(request.path.startswith(ignored) for ignored in self.ignored_paths):
                return
            
            from .models import AccessLog
            
            ip_address = get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            path = request.path
            method = request.method
            user = request.user if request.user.is_authenticated else None
            
            # Créer le log d'accès
            AccessLog.objects.create(
                ip_address=ip_address,
                user_agent=user_agent,
                path=path,
                method=method,
                user=user
            )
            
        except Exception as e:
            # Ne pas faire planter l'application si le logging échoue
            logger.error(f"Erreur lors de l'enregistrement de l'accès: {e}")


class SecureErrorHandlingMiddleware(MiddlewareMixin):
    """
    Middleware pour gérer les erreurs de manière sécurisée
    Empêche la divulgation d'informations sensibles en production
    """
    
    def process_exception(self, request, exception):
        """
        Traite les exceptions de manière sécurisée
        """
        # Log l'erreur complète pour le débogage (côté serveur uniquement)
        logger.error(
            f"Exception in {request.path}: {type(exception).__name__}: {str(exception)}",
            exc_info=True,
            extra={
                'request': request,
                'user': getattr(request, 'user', None),
                'ip': get_client_ip(request),
            }
        )
        
        # En mode DEBUG, laisser Django gérer normalement
        if settings.DEBUG:
            return None
        
        # En production, retourner des erreurs génériques
        return self.handle_secure_error(request, exception)
    
    def handle_secure_error(self, request, exception):
        """
        Retourne une réponse d'erreur sécurisée sans informations sensibles
        """
        from django.http import JsonResponse
        from django.template.response import TemplateResponse
        
        # Déterminer le type de réponse attendu
        if request.content_type == 'application/json' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
            return self.json_error_response(request, exception)
        else:
            return self.html_error_response(request, exception)
    
    def json_error_response(self, request, exception):
        """
        Retourne une réponse JSON d'erreur sécurisée
        """
        from django.http import JsonResponse
        
        error_data = {
            'error': True,
            'message': 'Une erreur interne s\'est produite. Veuillez réessayer plus tard.',
            'code': 'INTERNAL_ERROR'
        }
        
        # Codes d'erreur spécifiques sans divulgation
        if hasattr(exception, 'status_code'):
            status_code = exception.status_code
        else:
            status_code = 500
            
        return JsonResponse(error_data, status=status_code)
    
    def html_error_response(self, request, exception):
        """
        Retourne une réponse HTML d'erreur sécurisée
        """
        from django.http import HttpResponse
        from django.template.response import TemplateResponse
        
        # Template d'erreur générique
        context = {
            'error_title': 'Erreur interne',
            'error_message': 'Une erreur s\'est produite. Nos équipes ont été notifiées.',
            'support_email': 'support@planiffacile.com',
        }
        
        try:
            return TemplateResponse(
                request,
                'errors/500.html',
                context,
                status=500
            )
        except:
            # Fallback si le template n'existe pas
            return HttpResponse(
                """
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Erreur - Planif facile</title>
                    <meta charset="utf-8">
                    <style>
                        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
                        .error-container { max-width: 500px; margin: 0 auto; }
                        h1 { color: #dc3545; }
                        p { color: #6c757d; margin: 20px 0; }
                        .btn { 
                            display: inline-block; 
                            padding: 10px 20px; 
                            background: #007bff; 
                            color: white; 
                            text-decoration: none; 
                            border-radius: 5px; 
                        }
                    </style>
                </head>
                <body>
                    <div class="error-container">
                        <h1>Erreur interne</h1>
                        <p>Une erreur s'est produite. Nos équipes ont été notifiées.</p>
                        <p>Veuillez réessayer dans quelques instants.</p>
                        <a href="/" class="btn">Retour à l'accueil</a>
                    </div>
                </body>
                </html>
                """,
                status=500,
                content_type='text/html'
            )
