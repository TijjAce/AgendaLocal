/**
 * Configuration CKEditor 5 avec support CSRF et upload d'images
 * Ce script configure automatiquement CKEditor 5 pour envoyer le token CSRF
 * et gérer l'upload d'images de manière sécurisée
 */

// Configuration globale pour CKEditor 5
class CKEditor5Config {
    constructor() {
        this.csrfToken = this.getCSRFToken();
        this.uploadUrl = '/fiches/ckeditor/upload/';
    }

    // Récupération du token CSRF
    getCSRFToken() {
        const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
        if (csrfInput) {
            return csrfInput.value;
        }
        
        // Alternative : récupération via les cookies
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            if (name === 'csrftoken') {
                return value;
            }
        }
        
        console.warn('Token CSRF non trouvé');
        return '';
    }

    // Configuration de base pour CKEditor 5
    getConfig() {
        return {
            toolbar: {
                items: [
                    'heading',
                    '|',
                    'bold',
                    'italic',
                    'underline',
                    '|',
                    'link',
                    'bulletedList',
                    'numberedList',
                    '|',
                    'outdent',
                    'indent',
                    '|',
                    'imageUpload',
                    'blockQuote',
                    'insertTable',
                    '|',
                    'undo',
                    'redo'
                ]
            },
            language: 'fr',
            image: {
                toolbar: [
                    'imageTextAlternative',
                    'imageStyle:inline',
                    'imageStyle:block',
                    'imageStyle:side'
                ]
            },
            table: {
                contentToolbar: [
                    'tableColumn',
                    'tableRow',
                    'mergeTableCells'
                ]
            },
            simpleUpload: {
                uploadUrl: this.uploadUrl,
                withCredentials: true,
                headers: {
                    'X-CSRFToken': this.csrfToken,
                    'X-Requested-With': 'XMLHttpRequest'
                }
            },
            heading: {
                options: [
                    { model: 'paragraph', title: 'Paragraphe', class: 'ck-heading_paragraph' },
                    { model: 'heading1', view: 'h1', title: 'Titre 1', class: 'ck-heading_heading1' },
                    { model: 'heading2', view: 'h2', title: 'Titre 2', class: 'ck-heading_heading2' },
                    { model: 'heading3', view: 'h3', title: 'Titre 3', class: 'ck-heading_heading3' }
                ]
            }
        };
    }

    // Initialiser CKEditor 5 sur un élément donné
    async initEditor(element) {
        try {
            if (!window.ClassicEditor) {
                throw new Error('CKEditor 5 ClassicEditor n\'est pas chargé');
            }

            // Détruire l'instance existante si elle existe
            if (element.ckeditorInstance) {
                await element.ckeditorInstance.destroy();
                element.ckeditorInstance = null;
            }

            console.log('Initialisation CKEditor 5 pour élément:', element.id || element.name);

            const editor = await ClassicEditor.create(element, this.getConfig());
            
            // Stocker la référence de l'éditeur
            element.ckeditorInstance = editor;

            // Synchroniser avec le formulaire
            editor.model.document.on('change:data', () => {
                element.value = editor.getData();
            });

            console.log('CKEditor 5 initialisé avec succès pour:', element.id || element.name);
            return editor;

        } catch (error) {
            console.error('Erreur lors de l\'initialisation de CKEditor 5:', error);
            throw error;
        }
    }

    // Initialiser tous les éditeurs sur la page
    async initAllEditors(selector = 'textarea[name*="deroulement"]') {
        const textareas = document.querySelectorAll(selector);
        const promises = [];

        textareas.forEach(textarea => {
            promises.push(this.initEditor(textarea));
        });

        try {
            await Promise.all(promises);
            console.log(`${textareas.length} éditeur(s) CKEditor 5 initialisé(s)`);
        } catch (error) {
            console.error('Erreur lors de l\'initialisation des éditeurs:', error);
        }
    }

    // Détruire un éditeur
    async destroyEditor(element) {
        if (element.ckeditorInstance) {
            try {
                await element.ckeditorInstance.destroy();
                element.ckeditorInstance = null;
                console.log('Éditeur CKEditor 5 détruit pour:', element.id || element.name);
            } catch (error) {
                console.error('Erreur lors de la destruction de l\'éditeur:', error);
            }
        }
    }
}

// Instance globale
window.ckeditor5Config = new CKEditor5Config();

// Initialisation automatique au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    // Attendre que CKEditor 5 soit chargé
    const checkCKEditor = setInterval(function() {
        if (typeof ClassicEditor !== 'undefined') {
            clearInterval(checkCKEditor);
            
            // Initialiser tous les éditeurs existants
            window.ckeditor5Config.initAllEditors();
        }
    }, 100);

    // Timeout de sécurité
    setTimeout(() => {
        clearInterval(checkCKEditor);
        if (typeof ClassicEditor === 'undefined') {
            console.error('CKEditor 5 n\'a pas pu être chargé dans les temps');
        }
    }, 10000);
});

// Fonction utilitaire pour initialiser un nouvel éditeur (pour l'ajout dynamique)
window.initNewCKEditor5 = function(element) {
    if (window.ckeditor5Config) {
        return window.ckeditor5Config.initEditor(element);
    } else {
        console.error('CKEditor5Config n\'est pas disponible');
    }
};

// Fonction utilitaire pour détruire un éditeur
window.destroyCKEditor5 = function(element) {
    if (window.ckeditor5Config) {
        return window.ckeditor5Config.destroyEditor(element);
    }
};
