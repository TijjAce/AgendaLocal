import requests
from datetime import datetime, date
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

class SchoolHolidaysService:
    """Service pour récupérer les vacances scolaires depuis l'API du gouvernement français"""
    
    BASE_URL = "https://data.education.gouv.fr/api/explore/v2.0/catalog/datasets/fr-en-calendrier-scolaire"
    
    # Zones scolaires disponibles
    ZONES = {
        'A': 'Zone A',
        'B': 'Zone B', 
        'C': 'Zone C',
        'Corse': 'Corse'
    }
    
    # Données de secours pour les vacances scolaires (années 2023-2025)
    FALLBACK_HOLIDAYS = {
        '2023-2024': {
            'Zone A': [
                {'description': 'Vacances de la Toussaint', 'start_date': '2023-10-21', 'end_date': '2023-11-06'},
                {'description': 'Vacances de Noël', 'start_date': '2023-12-23', 'end_date': '2024-01-08'},
                {'description': 'Vacances d\'Hiver', 'start_date': '2024-02-10', 'end_date': '2024-02-26'},
                {'description': 'Vacances de Printemps', 'start_date': '2024-04-13', 'end_date': '2024-04-29'},
                {'description': 'Vacances d\'Eté', 'start_date': '2024-07-06', 'end_date': '2024-09-02'},
            ],
            'Zone B': [
                {'description': 'Vacances de la Toussaint', 'start_date': '2023-10-21', 'end_date': '2023-11-06'},
                {'description': 'Vacances de Noël', 'start_date': '2023-12-23', 'end_date': '2024-01-08'},
                {'description': 'Vacances d\'Hiver', 'start_date': '2024-02-24', 'end_date': '2024-03-11'},
                {'description': 'Vacances de Printemps', 'start_date': '2024-04-20', 'end_date': '2024-05-06'},
                {'description': 'Vacances d\'Eté', 'start_date': '2024-07-06', 'end_date': '2024-09-02'},
            ],
            'Zone C': [
                {'description': 'Vacances de la Toussaint', 'start_date': '2023-10-21', 'end_date': '2023-11-06'},
                {'description': 'Vacances de Noël', 'start_date': '2023-12-23', 'end_date': '2024-01-08'},
                {'description': 'Vacances d\'Hiver', 'start_date': '2024-02-17', 'end_date': '2024-03-04'},
                {'description': 'Vacances de Printemps', 'start_date': '2024-04-06', 'end_date': '2024-04-22'},
                {'description': 'Vacances d\'Eté', 'start_date': '2024-07-06', 'end_date': '2024-09-02'},
            ]
        },
        '2024-2025': {
            'Zone A': [
                {'description': 'Vacances de la Toussaint', 'start_date': '2024-10-19', 'end_date': '2024-11-04'},
                {'description': 'Vacances de Noël', 'start_date': '2024-12-21', 'end_date': '2025-01-06'},
                {'description': 'Vacances d\'Hiver', 'start_date': '2025-02-22', 'end_date': '2025-03-10'},
                {'description': 'Vacances de Printemps', 'start_date': '2025-04-19', 'end_date': '2025-05-05'},
                {'description': 'Vacances d\'Eté', 'start_date': '2025-07-05', 'end_date': '2025-09-01'},
            ],
            'Zone B': [
                {'description': 'Vacances de la Toussaint', 'start_date': '2024-10-19', 'end_date': '2024-11-04'},
                {'description': 'Vacances de Noël', 'start_date': '2024-12-21', 'end_date': '2025-01-06'},
                {'description': 'Vacances d\'Hiver', 'start_date': '2025-03-01', 'end_date': '2025-03-17'},
                {'description': 'Vacances de Printemps', 'start_date': '2025-04-12', 'end_date': '2025-04-28'},
                {'description': 'Vacances d\'Eté', 'start_date': '2025-07-05', 'end_date': '2025-09-01'},
            ],
            'Zone C': [
                {'description': 'Vacances de la Toussaint', 'start_date': '2024-10-19', 'end_date': '2024-11-04'},
                {'description': 'Vacances de Noël', 'start_date': '2024-12-21', 'end_date': '2025-01-06'},
                {'description': 'Vacances d\'Hiver', 'start_date': '2025-02-15', 'end_date': '2025-03-03'},
                {'description': 'Vacances de Printemps', 'start_date': '2025-04-05', 'end_date': '2025-04-22'},
                {'description': 'Vacances d\'Eté', 'start_date': '2025-07-05', 'end_date': '2025-09-01'},
            ]
        }
    }
    
    @classmethod
    def get_school_holidays(cls, year: int, zone: str = None) -> List[Dict]:
        """
        Récupère les vacances scolaires pour une année civile donnée
        
        Args:
            year: Année civile (ex: 2024 pour récupérer les vacances de 2024)
            zone: Zone scolaire ('A', 'B', 'C', 'Corse') - optionnel
            
        Returns:
            Liste des périodes de vacances
        """
        try:
            # Pour une année civile donnée, on doit récupérer deux années scolaires :
            # - L'année scolaire qui se termine cette année (ex: 2023-2024 pour l'année 2024)
            # - L'année scolaire qui commence cette année (ex: 2024-2025 pour l'année 2024)
            school_years = [
                f"{year-1}-{year}",  # Année scolaire précédente
                f"{year}-{year+1}"   # Année scolaire actuelle
            ]
            
            all_holidays = []
            
            for school_year in school_years:
                # Construction de la requête
                # Paramètres de la requête (utilisation de refine au lieu de where)
                params = {
                    'refine': f'annee_scolaire:{school_year}',
                    'limit': 100  # Limite maximale de l'API
                }
                
                # Appel à l'API avec en-têtes simplifiés
                headers = {
                    'User-Agent': 'Python/requests',
                    'Accept': 'application/json'
                }
                
                response = requests.get(f"{cls.BASE_URL}/records", params=params, headers=headers, timeout=15)
                response.raise_for_status()
                
                data = response.json()
                holidays = []
            
                for record in data.get('records', []):
                    fields = record.get('record', {}).get('fields', {})
                    
                    # Extraction des données
                    holiday = {
                        'id': record.get('record', {}).get('id'),
                        'description': fields.get('description', ''),
                        'start_date': cls._parse_date(fields.get('start_date')),
                        'end_date': cls._parse_date(fields.get('end_date')),
                        'zone': fields.get('zones', ''),
                        'location': fields.get('location', ''),
                        'population': fields.get('population', ''),
                        'school_year': fields.get('annee_scolaire', '')
                    }
                    
                    if holiday['start_date'] and holiday['end_date']:
                        # Filtrer par zone si spécifié (filtrage côté client)
                        if zone and zone in cls.ZONES:
                            if holiday['zone'] != cls.ZONES[zone]:
                                continue
                        
                        # Filtrer seulement les vacances qui touchent l'année civile demandée
                        if (holiday['start_date'].year == year or holiday['end_date'].year == year):
                            holidays.append(holiday)
                
                all_holidays.extend(holidays)
            
            # Supprimer les doublons basés sur l'ID
            unique_holidays = {}
            for holiday in all_holidays:
                unique_holidays[holiday['id']] = holiday
            
            final_holidays = list(unique_holidays.values())
            # Trier par date de début
            final_holidays.sort(key=lambda x: x['start_date'])
            
            logger.info(f"Récupéré {len(final_holidays)} périodes de vacances uniques pour l'année civile {year}")
            return final_holidays
            
        except requests.RequestException as e:
            logger.warning(f"API indisponible, utilisation des données de secours: {e}")
            return cls._get_fallback_holidays(year, zone)
        except Exception as e:
            logger.error(f"Erreur inattendue, utilisation des données de secours: {e}")
            return cls._get_fallback_holidays(year, zone)
    
    @classmethod
    def _parse_date(cls, date_str: str) -> Optional[date]:
        """Parse une date ISO string en objet date avec gestion des timezones"""
        if not date_str:
            return None
        try:
            # Parse ISO format avec timezone
            if date_str.endswith('Z'):
                dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            elif '+' in date_str or date_str.count('-') > 2:
                dt = datetime.fromisoformat(date_str)
            else:
                # Format sans timezone
                dt = datetime.fromisoformat(date_str)
            
            # Convertir en heure locale française (UTC+1/UTC+2)
            # Les vacances scolaires françaises sont définies en heure locale
            return dt.date()
        except (ValueError, AttributeError) as e:
            logger.warning(f"Erreur de parsing de date '{date_str}': {e}")
            return None
    
    @classmethod
    def get_holidays_for_date_range(cls, start_date: date, end_date: date, zone: str = None) -> List[Dict]:
        """
        Récupère les vacances scolaires pour une période donnée
        
        Args:
            start_date: Date de début
            end_date: Date de fin
            zone: Zone scolaire optionnelle
            
        Returns:
            Liste des vacances dans la période
        """
        # Récupérer les vacances pour toutes les années concernées par la période
        years_to_check = set()
        years_to_check.add(start_date.year)
        years_to_check.add(end_date.year)
        
        all_holidays = []
        for year in years_to_check:
            holidays = cls.get_school_holidays(year, zone)
            all_holidays.extend(holidays)
        
        # Supprimer les doublons
        unique_holidays = {}
        for holiday in all_holidays:
            unique_holidays[holiday['id']] = holiday
        
        # Filtre les vacances qui chevauchent avec la période demandée
        filtered_holidays = []
        for holiday in unique_holidays.values():
            if (holiday['start_date'] <= end_date and holiday['end_date'] >= start_date):
                filtered_holidays.append(holiday)
        
        return filtered_holidays
    
    @classmethod
    def is_school_holiday(cls, check_date: date, zone: str = None) -> Optional[Dict]:
        """
        Vérifie si une date donnée est pendant les vacances scolaires
        
        Args:
            check_date: Date à vérifier
            zone: Zone scolaire optionnelle
            
        Returns:
            Dictionnaire des vacances si la date est en vacances, None sinon
        """
        holidays = cls.get_school_holidays(check_date.year, zone)
        
        for holiday in holidays:
            if holiday['start_date'] <= check_date <= holiday['end_date']:
                return holiday
        
        return None
    
    @classmethod
    def _get_fallback_holidays(cls, year: int, zone: str = None) -> List[Dict]:
        """
        Récupère les vacances scolaires depuis les données de secours
        
        Args:
            year: Année civile
            zone: Zone scolaire optionnelle
            
        Returns:
            Liste des périodes de vacances
        """
        holidays = []
        
        # Déterminer les années scolaires concernées
        school_years = [
            f"{year-1}-{year}",
            f"{year}-{year+1}"
        ]
        
        for school_year in school_years:
            if school_year in cls.FALLBACK_HOLIDAYS:
                year_data = cls.FALLBACK_HOLIDAYS[school_year]
                
                # Filtrer par zone si spécifié
                zones_to_process = [cls.ZONES[zone]] if zone and zone in cls.ZONES else year_data.keys()
                
                for zone_name in zones_to_process:
                    if zone_name in year_data:
                        for holiday_data in year_data[zone_name]:
                            try:
                                start_date = datetime.strptime(holiday_data['start_date'], '%Y-%m-%d').date()
                                end_date = datetime.strptime(holiday_data['end_date'], '%Y-%m-%d').date()
                                
                                # Filtrer par année civile
                                if start_date.year == year or end_date.year == year:
                                    holiday = {
                                        'id': f"fallback_{school_year}_{zone_name}_{holiday_data['description'].replace(' ', '_')}",
                                        'description': holiday_data['description'],
                                        'start_date': start_date,
                                        'end_date': end_date,
                                        'zone': zone_name,
                                        'location': 'France',
                                        'population': '-',
                                        'school_year': school_year
                                    }
                                    holidays.append(holiday)
                            except (ValueError, KeyError) as e:
                                logger.warning(f"Erreur parsing données de secours: {e}")
                                continue
        
        # Supprimer les doublons et trier
        unique_holidays = {}
        for holiday in holidays:
            unique_holidays[holiday['id']] = holiday
        
        final_holidays = list(unique_holidays.values())
        final_holidays.sort(key=lambda x: x['start_date'])
        
        logger.info(f"Données de secours: {len(final_holidays)} périodes pour l'année {year}")
        return final_holidays
    
    @classmethod
    def get_available_zones(cls) -> Dict[str, str]:
        """Retourne les zones scolaires disponibles"""
        return cls.ZONES.copy()
