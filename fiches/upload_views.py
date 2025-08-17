import os
import json
from django.http import JsonResponse

# Import conditionnel de python-magic avec fallback gracieux
try:
    import magic
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.decorators.csrf import ensure_csrf_cookie
import uuid


@login_required
@require_POST
@ensure_csrf_cookie
def ckeditor_upload(request):
    """
    Vue personnalisée pour l'upload d'images CKEditor sans authentification admin
    """
    try:
        # Vérifier qu'un fichier a été uploadé
        if 'upload' not in request.FILES:
            return JsonResponse({
                'error': {
                    'message': 'Aucun fichier uploadé'
                }
            }, status=400)
        
        uploaded_file = request.FILES['upload']
        
        # Validation stricte de sécurité
        # 1. Vérification de l'extension
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()
        
        if file_extension not in allowed_extensions:
            return JsonResponse({
                'error': {
                    'message': 'Le fichier doit être une image (jpg, jpeg, png, gif, webp)'
                }
            }, status=400)
        
        # 2. Vérification de la taille (max 5MB)
        max_size = 5 * 1024 * 1024  # 5MB
        if uploaded_file.size > max_size:
            return JsonResponse({
                'error': {
                    'message': 'Le fichier est trop volumineux (max 5MB)'
                }
            }, status=400)
        
        # 3. Vérification du type MIME réel (si python-magic est disponible)
        if MAGIC_AVAILABLE:
            try:
                file_content = uploaded_file.read()
                uploaded_file.seek(0)  # Reset pour la sauvegarde
                
                # Utilisation de python-magic pour détecter le vrai type MIME
                mime_type = magic.from_buffer(file_content, mime=True)
                allowed_mimes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
                
                if mime_type not in allowed_mimes:
                    return JsonResponse({
                        'error': {
                            'message': f'Type de fichier non autorisé: {mime_type}'
                        }
                    }, status=400)
            except Exception:
                # Fallback si la détection MIME échoue
                pass
        # Si python-magic n'est pas disponible, on se fie à l'extension (moins sûr mais fonctionnel)
        
        # Générer un nom de fichier unique
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        
        # Créer le dossier uploads s'il n'existe pas
        upload_dir = os.path.join(settings.MEDIA_ROOT, settings.UPLOAD_PATH)
        os.makedirs(upload_dir, exist_ok=True)
        
        # Chemin de sauvegarde
        upload_path = os.path.join(settings.UPLOAD_PATH, unique_filename)
        
        # Sauvegarder le fichier
        file_path = default_storage.save(upload_path, ContentFile(uploaded_file.read()))
        
        # URL complète du fichier
        file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)
        
        # Réponse au format attendu par CKEditor (format strict)
        response_data = {
            'uploaded': 1,
            'fileName': unique_filename,
            'url': file_url
        }
        
        # Si c'est une requête avec responseType=json, on retourne directement
        if 'responseType' in request.GET and request.GET['responseType'] == 'json':
            return JsonResponse(response_data)
        
        # Sinon format standard CKEditor
        return JsonResponse(response_data)
        
    except Exception as e:
        # Log l'erreur pour debug
        import traceback
        print(f"Erreur upload CKEditor: {str(e)}")
        print(traceback.format_exc())
        
        return JsonResponse({
            'error': {
                'message': f'Erreur lors de l\'upload: {str(e)}'
            }
        }, status=500)


@login_required
def ckeditor_browse(request):
    """
    Vue pour parcourir les images uploadées (optionnelle)
    """
    try:
        upload_dir = os.path.join(settings.MEDIA_ROOT, settings.UPLOAD_PATH)
        
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        files = []
        for filename in os.listdir(upload_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_url = settings.MEDIA_URL + settings.UPLOAD_PATH + filename
                files.append({
                    'name': filename,
                    'url': file_url,
                    'thumb': file_url  # Pour les miniatures
                })
        
        return JsonResponse({
            'files': files
        })
        
    except Exception as e:
        return JsonResponse({
            'error': {
                'message': f'Erreur lors du parcours: {str(e)}'
            }
        }, status=500)
