/**
 * Utilitaires de sécurité pour prévenir les attaques XSS
 * Utilisés pour échapper les données avant injection dans le DOM
 */

/**
 * Échappe les caractères HTML dangereux pour prévenir les attaques XSS
 * @param {string} text - Le texte à échapper
 * @returns {string} - Le texte échappé
 */
function escapeHtml(text) {
    if (typeof text !== 'string') {
        return text;
    }
    
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Crée un élément DOM de manière sécurisée
 * @param {string} tagName - Le nom de la balise
 * @param {Object} attributes - Les attributs à définir
 * @param {string} textContent - Le contenu textuel (échappé automatiquement)
 * @returns {HTMLElement} - L'élément créé
 */
function createSecureElement(tagName, attributes = {}, textContent = '') {
    const element = document.createElement(tagName);
    
    // Définir les attributs de manière sécurisée
    for (const [key, value] of Object.entries(attributes)) {
        if (typeof value === 'string') {
            element.setAttribute(key, value);
        }
    }
    
    // Définir le contenu textuel (automatiquement échappé)
    if (textContent) {
        element.textContent = textContent;
    }
    
    return element;
}

/**
 * Remplace innerHTML de manière sécurisée
 * @param {HTMLElement} element - L'élément cible
 * @param {string} content - Le contenu à insérer (sera échappé)
 */
function setSecureContent(element, content) {
    element.textContent = content;
}

/**
 * Valide et nettoie une URL pour prévenir les attaques XSS via javascript:
 * @param {string} url - L'URL à valider
 * @returns {string} - L'URL nettoyée ou une URL sûre par défaut
 */
function sanitizeUrl(url) {
    if (!url || typeof url !== 'string') {
        return '#';
    }
    
    // Supprimer les espaces
    url = url.trim();
    
    // Bloquer les protocoles dangereux
    const dangerousProtocols = ['javascript:', 'data:', 'vbscript:', 'file:'];
    const lowerUrl = url.toLowerCase();
    
    for (const protocol of dangerousProtocols) {
        if (lowerUrl.startsWith(protocol)) {
            return '#';
        }
    }
    
    return url;
}

/**
 * Crée une carte de fiche de manière sécurisée
 * @param {Object} fiche - Les données de la fiche
 * @returns {HTMLElement} - L'élément de carte créé
 */
function createSecureFicheCard(fiche) {
    const card = createSecureElement('div', { class: 'card mb-2' });
    const cardBody = createSecureElement('div', { class: 'card-body p-2' });
    const flexContainer = createSecureElement('div', { 
        class: 'd-flex justify-content-between align-items-center' 
    });
    
    // Conteneur des informations
    const infoDiv = createSecureElement('div');
    const title = createSecureElement('h6', { class: 'mb-1' }, fiche.titre);
    const subtitle = createSecureElement('small', { class: 'text-muted' }, 
        `${fiche.discipline_nom} - ${fiche.date}`);
    
    infoDiv.appendChild(title);
    infoDiv.appendChild(subtitle);
    
    // Conteneur du switch
    const switchDiv = createSecureElement('div', { class: 'form-check form-switch' });
    const checkbox = createSecureElement('input', {
        class: 'form-check-input',
        type: 'checkbox',
        id: `share_${fiche.id}`
    });
    
    if (fiche.is_shared) {
        checkbox.checked = true;
    }
    
    checkbox.addEventListener('change', function() {
        toggleShare(fiche.id, this.checked);
    });
    
    const label = createSecureElement('label', {
        class: 'form-check-label',
        for: `share_${fiche.id}`
    }, fiche.is_shared ? 'Partagé' : 'Privé');
    
    switchDiv.appendChild(checkbox);
    switchDiv.appendChild(label);
    
    flexContainer.appendChild(infoDiv);
    flexContainer.appendChild(switchDiv);
    cardBody.appendChild(flexContainer);
    card.appendChild(cardBody);
    
    return card;
}

/**
 * Affiche un message d'erreur de manière sécurisée
 * @param {HTMLElement} container - Le conteneur cible
 * @param {string} message - Le message d'erreur
 * @param {string} type - Le type de message (warning, danger, muted)
 */
function showSecureMessage(container, message, type = 'muted') {
    const messageDiv = createSecureElement('div', {
        class: `text-center text-${type} py-3`
    }, message);
    
    container.innerHTML = '';
    container.appendChild(messageDiv);
}
