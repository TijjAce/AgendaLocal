"""
Générateur d'avatars SVG personnalisés
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string


class AvatarGenerator:
    """Générateur d'avatars SVG personnalisés"""
    
    @staticmethod
    def generate_svg_avatar(profile):
        """
        Génère un avatar SVG basé sur les préférences du profil utilisateur
        """
        # Configuration par défaut si le profil n'a pas de préférences
        config = {
            'skin_color': profile.avatar_skin_color if profile.avatar_skin_color else '#FDBCB4',
            'hair_style': profile.avatar_hair_style if profile.avatar_hair_style else 'short',
            'hair_color': profile.avatar_hair_color if profile.avatar_hair_color else '#8B4513',
            'eye_color': profile.avatar_eye_color if profile.avatar_eye_color else '#4A90E2',
            'clothing_color': profile.avatar_clothing_color if profile.avatar_clothing_color else '#2E86AB',
            'accessories': profile.avatar_accessories if profile.avatar_accessories else 'none',
        }
        
        # Template SVG de base
        svg_template = f'''
        <svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <!-- Arrière-plan circulaire -->
            <circle cx="100" cy="100" r="95" fill="#f8f9fa" stroke="#dee2e6" stroke-width="2"/>
            
            <!-- Corps/Vêtements -->
            <ellipse cx="100" cy="160" rx="45" ry="35" fill="{config['clothing_color']}"/>
            
            <!-- Cou -->
            <rect x="85" y="130" width="30" height="25" fill="{config['skin_color']}" rx="15"/>
            
            <!-- Visage -->
            <ellipse cx="100" cy="100" rx="40" ry="45" fill="{config['skin_color']}"/>
            
            <!-- Cheveux -->
            {AvatarGenerator._generate_hair_svg(config['hair_style'], config['hair_color'])}
            
            <!-- Yeux -->
            <ellipse cx="88" cy="95" rx="6" ry="8" fill="white"/>
            <ellipse cx="112" cy="95" rx="6" ry="8" fill="white"/>
            <ellipse cx="88" cy="95" rx="4" ry="6" fill="{config['eye_color']}"/>
            <ellipse cx="112" cy="95" rx="4" ry="6" fill="{config['eye_color']}"/>
            <ellipse cx="89" cy="93" rx="1.5" ry="2" fill="black"/>
            <ellipse cx="113" cy="93" rx="1.5" ry="2" fill="black"/>
            
            <!-- Sourcils -->
            <ellipse cx="88" cy="85" rx="8" ry="2" fill="{config['hair_color']}" opacity="0.7"/>
            <ellipse cx="112" cy="85" rx="8" ry="2" fill="{config['hair_color']}" opacity="0.7"/>
            
            <!-- Nez -->
            <ellipse cx="100" cy="105" rx="2" ry="4" fill="{config['skin_color']}" opacity="0.8"/>
            
            <!-- Bouche -->
            <path d="M 92 115 Q 100 122 108 115" stroke="#d63384" stroke-width="2" fill="none" stroke-linecap="round"/>
            
            <!-- Accessoires -->
            {AvatarGenerator._generate_accessories_svg(config['accessories'])}
        </svg>
        '''
        
        return svg_template.strip()
    
    @staticmethod
    def _generate_hair_svg(hair_style, hair_color):
        """Génère le SVG pour les cheveux selon le style"""
        if hair_style == 'bald':
            return ''
        elif hair_style == 'short':
            return f'''
            <path d="M 65 75 Q 100 55 135 75 Q 135 85 130 90 Q 100 70 70 90 Q 65 85 65 75" fill="{hair_color}"/>
            '''
        elif hair_style == 'medium':
            return f'''
            <path d="M 60 70 Q 100 50 140 70 Q 140 90 135 100 Q 100 65 65 100 Q 60 90 60 70" fill="{hair_color}"/>
            '''
        elif hair_style == 'long':
            return f'''
            <path d="M 55 65 Q 100 45 145 65 Q 145 95 140 110 Q 100 60 60 110 Q 55 95 55 65" fill="{hair_color}"/>
            <path d="M 65 110 Q 70 130 75 140" stroke="{hair_color}" stroke-width="8" fill="none" stroke-linecap="round"/>
            <path d="M 135 110 Q 130 130 125 140" stroke="{hair_color}" stroke-width="8" fill="none" stroke-linecap="round"/>
            '''
        elif hair_style == 'curly':
            return f'''
            <path d="M 65 75 Q 100 55 135 75 Q 135 85 130 90 Q 100 70 70 90 Q 65 85 65 75" fill="{hair_color}"/>
            <circle cx="75" cy="70" r="5" fill="{hair_color}"/>
            <circle cx="90" cy="65" r="4" fill="{hair_color}"/>
            <circle cx="110" cy="65" r="4" fill="{hair_color}"/>
            <circle cx="125" cy="70" r="5" fill="{hair_color}"/>
            '''
        else:
            return f'''
            <path d="M 65 75 Q 100 55 135 75 Q 135 85 130 90 Q 100 70 70 90 Q 65 85 65 75" fill="{hair_color}"/>
            '''
    
    @staticmethod
    def _generate_accessories_svg(accessories):
        """Génère le SVG pour les accessoires"""
        if accessories == 'glasses':
            return '''
            <rect x="78" y="90" width="16" height="12" fill="none" stroke="#333" stroke-width="2" rx="2"/>
            <rect x="106" y="90" width="16" height="12" fill="none" stroke="#333" stroke-width="2" rx="2"/>
            <line x1="94" y1="96" x2="106" y2="96" stroke="#333" stroke-width="2"/>
            '''
        elif accessories == 'hat':
            return '''
            <ellipse cx="100" cy="65" rx="50" ry="8" fill="#8B4513"/>
            <ellipse cx="100" cy="55" rx="35" ry="15" fill="#8B4513"/>
            '''
        elif accessories == 'earrings':
            return '''
            <circle cx="65" cy="105" r="3" fill="#FFD700"/>
            <circle cx="135" cy="105" r="3" fill="#FFD700"/>
            '''
        else:
            return ''
    
    @staticmethod
    def get_random_config():
        """Génère une configuration aléatoire pour un avatar"""
        skin_colors = ['#FDBCB4', '#F1C27D', '#E0AC69', '#C68642', '#8D5524', '#A0522D']
        hair_styles = ['short', 'medium', 'long', 'curly', 'bald']
        hair_colors = ['#8B4513', '#D2691E', '#000000', '#654321', '#FFD700', '#FF6347']
        eye_colors = ['#4A90E2', '#228B22', '#8B4513', '#9932CC', '#FF1493']
        clothing_colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6A994E']
        accessories = ['none', 'glasses', 'hat', 'earrings']
        
        return {
            'avatar_skin_color': random.choice(skin_colors),
            'avatar_hair_style': random.choice(hair_styles),
            'avatar_hair_color': random.choice(hair_colors),
            'avatar_eye_color': random.choice(eye_colors),
            'avatar_clothing_color': random.choice(clothing_colors),
            'avatar_accessories': random.choice(accessories),
        }
