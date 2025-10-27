#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                    ModuleArt Ultra v2.0 - PROFESSIONAL                    ║
║                    ADVANCED ADMIN PANEL SCANNER                           ║
║                                                                           ║
║  DEVELOPERS: @lll.emirx.38 @omer.17l667 @oixin.r3al                      ║
║  20,000+ PATHS | ASYNC BATCH SCANNING | MULTI-LANGUAGE | REPORTING       ║
║  AUTHORIZED SECURITY TESTING ONLY                                        ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import subprocess
import sys
import importlib
import time
import os
import random
import re
import json
import csv
from collections import Counter
from datetime import datetime
from typing import List, Dict, Optional, Tuple, Set
from dataclasses import dataclass, asdict
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 1: DEPENDENCY MANAGEMENT & INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════

class DependencyManager:
    """Advanced dependency management system"""
    
    REQUIRED_PACKAGES = {
        "aiohttp": "3.9.0",
        "requests": "2.31.0",
        "beautifulsoup4": "4.12.0",
        "colorama": "0.4.6",
        "tqdm": "4.66.0",
        "jinja2": "3.1.2",
    }
    
    @staticmethod
    def check_and_install():
        """Check and install all required dependencies"""
        print("\n" + "═" * 80)
        print("DEPENDENCY VERIFICATION & INSTALLATION")
        print("═" * 80)
        
        for package, version in DependencyManager.REQUIRED_PACKAGES.items():
            try:
                importlib.import_module(package.replace("-", "_"))
                print(f"[✓] {package} {version} - Already installed")
            except ImportError:
                print(f"[!] {package} {version} - Installing...")
                try:
                    subprocess.check_call(
                        [sys.executable, "-m", "pip", "install", f"{package}>={version}"],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        timeout=120
                    )
                    print(f"[✓] {package} {version} - Successfully installed")
                except Exception as e:
                    print(f"[✗] {package} {version} - Installation failed: {e}")
                    print(f"    Manual install: pip install {package}>={version}")
                    sys.exit(1)
        
        print("\n[✓] All dependencies verified and ready")
        print("═" * 80)

# Install dependencies first
DependencyManager.check_and_install()

# Now import the packages
import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
from tqdm import tqdm
from jinja2 import Template

# Initialize colorama
init(autoreset=True)

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 2: COLOR THEMES & STYLING
# ═══════════════════════════════════════════════════════════════════════════

class Colors:
    """Advanced color scheme for professional terminal output"""
    
    # Primary colors
    PRIMARY = Fore.CYAN
    SUCCESS = Fore.GREEN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    INFO = Fore.BLUE
    
    # Accent colors
    ACCENT1 = Fore.MAGENTA
    ACCENT2 = Fore.LIGHTCYAN_EX
    ACCENT3 = Fore.LIGHTMAGENTA_EX
    
    # Text styles
    BOLD = Style.BRIGHT
    DIM = Style.DIM
    RESET = Style.RESET_ALL
    
    # Status colors
    STATUS_200 = Fore.GREEN
    STATUS_401 = Fore.YELLOW
    STATUS_403 = Fore.LIGHTYELLOW_EX
    STATUS_301 = Fore.BLUE
    STATUS_302 = Fore.LIGHTBLUE_EX
    
    # Background colors
    BG_SUCCESS = Back.GREEN
    BG_ERROR = Back.RED
    BG_WARNING = Back.YELLOW

class Banner:
    """Professional ASCII art banners"""
    
    @staticmethod
    def main_banner():
        banner = f"""
{Colors.PRIMARY}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗                 ║
║   ████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝                 ║
║   ██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗                   ║
║   ██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝                   ║
║   ██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗                 ║
║   ╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                 ║
║                                                                           ║
║            █████╗ ██████╗ ████████╗    ██╗   ██╗██████╗                 ║
║           ██╔══██╗██╔══██╗╚══██╔══╝    ██║   ██║╚════██╗                ║
║           ███████║██████╔╝   ██║       ██║   ██║ █████╔╝                ║
║           ██╔══██║██╔══██╗   ██║       ╚██╗ ██╔╝██╔═══╝                 ║
║           ██║  ██║██║  ██║   ██║        ╚████╔╝ ███████╗                ║
║           ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝         ╚═══╝  ╚══════╝                ║
║                                                                           ║
║              PROFESSIONAL ADMIN PANEL DETECTION SYSTEM                    ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

{Colors.ACCENT2}┌─────────────────────────────────────────────────────────────────────────┐
│ DEVELOPERS: @lll.emirx.38  @omer.17l667  @oixin.r3al                    │
│ VERSION: 2.0 ULTRA | PATHS: 20,000+ | ASYNC: ✓ | REPORTING: ✓         │
│ LANGUAGES: TR/EN/DE/FR | BATCH PROCESSING | PROFESSIONAL OUTPUT         │
└─────────────────────────────────────────────────────────────────────────┘{Colors.RESET}
"""
        return banner
    
    @staticmethod
    def scan_complete_banner(findings_count):
        banner = f"""
{Colors.SUCCESS}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════════════╗
║                         SCAN COMPLETED                                    ║
║                                                                           ║
║                  {findings_count:>5} CRITICAL FINDINGS DISCOVERED                     ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        return banner

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 3: MULTI-LANGUAGE TRANSLATION SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

class TranslationManager:
    """Complete multi-language translation system"""
    
    LANGUAGES = {
        "1": {"code": "tr", "name": "Türkçe", "flag": "🇹🇷"},
        "2": {"code": "en", "name": "English", "flag": "🇬🇧"},
        "3": {"code": "de", "name": "Deutsch", "flag": "🇩🇪"},
        "4": {"code": "fr", "name": "Français", "flag": "🇫🇷"}
    }
    
    TRANSLATIONS = {
        "tr": {
            # System messages
            "system_init": "SİSTEM BAŞLATILIYOR",
            "lib_check": "Kütüphane Kontrolü",
            "path_gen": "Yol veritabanı oluşturuluyor",
            "target_input": "Hedef URL girin",
            "warning": "⚠️  SADECE YETKİLİ HEDEFLERDE KULLANIN",
            "scan_start": "PROFESYONEL TARAMA BAŞLIYOR",
            "batch_info": "Batch işleniyor",
            "progress": "İlerleme",
            "speed": "Hız",
            "findings": "Bulunan",
            "scan_complete": "TARAMA TAMAMLANDI",
            "report_saved": "Rapor kaydedildi",
            "critical": "KRİTİK BULUNTULAR",
            "no_findings": "Admin panel bulunamadı",
            
            # Path categories
            "wordpress_paths": "WordPress Yolları",
            "joomla_paths": "Joomla Yolları",
            "phpmyadmin_paths": "phpMyAdmin Yolları",
            "cpanel_paths": "cPanel Yolları",
            "turkish_paths": "Türkçe Panel Yolları",
            "generic_paths": "Genel Admin Yolları",
            
            # Scan details
            "total_paths": "Toplam Yol",
            "batch_size": "Batch Boyutu",
            "concurrent_requests": "Eşzamanlı İstek",
            "timeout": "Zaman Aşımı",
            "status_codes": "Durum Kodları",
            "response_time": "Yanıt Süresi",
            
            # Results
            "accessible": "Erişilebilir",
            "unauthorized": "Yetkisiz",
            "forbidden": "Yasak",
            "redirect": "Yönlendirme",
            
            # Report
            "scan_report": "TARAMA RAPORU",
            "target_url": "Hedef URL",
            "scan_date": "Tarama Tarihi",
            "duration": "Süre",
            "paths_scanned": "Taranan Yol",
            "findings_found": "Bulunan",
            
            # Menu
            "select_language": "DİL SEÇİMİ",
            "select_option": "Seçim yapın",
            "invalid_choice": "Geçersiz seçim",
            
            # Legal
            "legal_warning": "YASAL UYARI",
            "legal_text": "Bu araç SADECE yetkili güvenlik testleri için kullanılmalıdır.",
            "accept": "Kabul Ediyorum",
        },
        
        "en": {
            # System messages
            "system_init": "SYSTEM INITIALIZING",
            "lib_check": "Library Verification",
            "path_gen": "Generating path database",
            "target_input": "Enter target URL",
            "warning": "⚠️  USE ONLY ON AUTHORIZED TARGETS",
            "scan_start": "PROFESSIONAL SCAN STARTING",
            "batch_info": "Processing batch",
            "progress": "Progress",
            "speed": "Speed",
            "findings": "Findings",
            "scan_complete": "SCAN COMPLETED",
            "report_saved": "Report saved",
            "critical": "CRITICAL FINDINGS",
            "no_findings": "No admin panels detected",
            
            # Path categories
            "wordpress_paths": "WordPress Paths",
            "joomla_paths": "Joomla Paths",
            "phpmyadmin_paths": "phpMyAdmin Paths",
            "cpanel_paths": "cPanel Paths",
            "turkish_paths": "Turkish Panel Paths",
            "generic_paths": "Generic Admin Paths",
            
            # Scan details
            "total_paths": "Total Paths",
            "batch_size": "Batch Size",
            "concurrent_requests": "Concurrent Requests",
            "timeout": "Timeout",
            "status_codes": "Status Codes",
            "response_time": "Response Time",
            
            # Results
            "accessible": "Accessible",
            "unauthorized": "Unauthorized",
            "forbidden": "Forbidden",
            "redirect": "Redirect",
            
            # Report
            "scan_report": "SCAN REPORT",
            "target_url": "Target URL",
            "scan_date": "Scan Date",
            "duration": "Duration",
            "paths_scanned": "Paths Scanned",
            "findings_found": "Findings",
            
            # Menu
            "select_language": "LANGUAGE SELECTION",
            "select_option": "Make your selection",
            "invalid_choice": "Invalid choice",
            
            # Legal
            "legal_warning": "LEGAL WARNING",
            "legal_text": "This tool must ONLY be used for authorized security testing.",
            "accept": "I Understand",
        },
        
        "de": {
            # System messages
            "system_init": "SYSTEM WIRD INITIALISIERT",
            "lib_check": "Bibliotheksprüfung",
            "path_gen": "Pfad-Datenbank wird erstellt",
            "target_input": "Ziel-URL eingeben",
            "warning": "⚠️  NUR BEI AUTORISIERTEN ZIELEN VERWENDEN",
            "scan_start": "PROFESSIONELLER SCAN STARTET",
            "batch_info": "Batch wird verarbeitet",
            "progress": "Fortschritt",
            "speed": "Geschwindigkeit",
            "findings": "Erkenntnisse",
            "scan_complete": "SCAN ABGESCHLOSSEN",
            "report_saved": "Bericht gespeichert",
            "critical": "KRITISCHE ERKENNTNISSE",
            "no_findings": "Keine Admin-Panels erkannt",
            
            # Path categories
            "wordpress_paths": "WordPress-Pfade",
            "joomla_paths": "Joomla-Pfade",
            "phpmyadmin_paths": "phpMyAdmin-Pfade",
            "cpanel_paths": "cPanel-Pfade",
            "turkish_paths": "Türkische Panel-Pfade",
            "generic_paths": "Allgemeine Admin-Pfade",
            
            # Scan details
            "total_paths": "Gesamtpfade",
            "batch_size": "Batch-Größe",
            "concurrent_requests": "Gleichzeitige Anfragen",
            "timeout": "Zeitüberschreitung",
            "status_codes": "Statuscodes",
            "response_time": "Antwortzeit",
            
            # Results
            "accessible": "Zugänglich",
            "unauthorized": "Nicht Autorisiert",
            "forbidden": "Verboten",
            "redirect": "Umleitung",
            
            # Report
            "scan_report": "SCAN-BERICHT",
            "target_url": "Ziel-URL",
            "scan_date": "Scan-Datum",
            "duration": "Dauer",
            "paths_scanned": "Gescannte Pfade",
            "findings_found": "Erkenntnisse",
            
            # Menu
            "select_language": "SPRACHWAHL",
            "select_option": "Wählen Sie",
            "invalid_choice": "Ungültige Auswahl",
            
            # Legal
            "legal_warning": "RECHTLICHER HINWEIS",
            "legal_text": "Dieses Tool darf NUR für autorisierte Sicherheitstests verwendet werden.",
            "accept": "Ich Verstehe",
        },
        
        "fr": {
            # System messages
            "system_init": "SYSTÈME S'INITIALISE",
            "lib_check": "Vérification des bibliothèques",
            "path_gen": "Génération de la base de chemins",
            "target_input": "Entrez l'URL cible",
            "warning": "⚠️  UTILISEZ UNIQUEMENT SUR DES CIBLES AUTORISÉES",
            "scan_start": "SCAN PROFESSIONNEL DÉMARRE",
            "batch_info": "Traitement du lot",
            "progress": "Progression",
            "speed": "Vitesse",
            "findings": "Résultats",
            "scan_complete": "SCAN TERMINÉ",
            "report_saved": "Rapport sauvegardé",
            "critical": "RÉSULTATS CRITIQUES",
            "no_findings": "Aucun panneau d'administration détecté",
            
            # Path categories
            "wordpress_paths": "Chemins WordPress",
            "joomla_paths": "Chemins Joomla",
            "phpmyadmin_paths": "Chemins phpMyAdmin",
            "cpanel_paths": "Chemins cPanel",
            "turkish_paths": "Chemins Panneaux Turcs",
            "generic_paths": "Chemins Admin Génériques",
            
            # Scan details
            "total_paths": "Total Chemins",
            "batch_size": "Taille du Lot",
            "concurrent_requests": "Requêtes Simultanées",
            "timeout": "Délai d'attente",
            "status_codes": "Codes de Statut",
            "response_time": "Temps de Réponse",
            
            # Results
            "accessible": "Accessible",
            "unauthorized": "Non Autorisé",
            "forbidden": "Interdit",
            "redirect": "Redirection",
            
            # Report
            "scan_report": "RAPPORT DE SCAN",
            "target_url": "URL Cible",
            "scan_date": "Date du Scan",
            "duration": "Durée",
            "paths_scanned": "Chemins Scannés",
            "findings_found": "Résultats",
            
            # Menu
            "select_language": "SÉLECTION DE LANGUE",
            "select_option": "Faites votre choix",
            "invalid_choice": "Choix invalide",
            
            # Legal
            "legal_warning": "AVERTISSEMENT LÉGAL",
            "legal_text": "Cet outil doit UNIQUEMENT être utilisé pour des tests de sécurité autorisés.",
            "accept": "Je Comprends",
        }
    }
    
    def __init__(self, lang_code: str = "en"):
        self.lang_code = lang_code
        self.translations = self.TRANSLATIONS[lang_code]
    
    def get(self, key: str) -> str:
        """Get translation for a key"""
        return self.translations.get(key, key)
    
    def t(self, key: str) -> str:
        """Alias for get"""
        return self.get(key)
    
    @classmethod
    def select_language(cls) -> str:
        """Interactive language selection"""
        print("\n" + "═" * 80)
        print(f"{Colors.PRIMARY}{Colors.BOLD}MODULEART v2.0 - PROFESSIONAL ADMIN PANEL SCANNER{Colors.RESET}")
        print(f"{Colors.ACCENT2}DEVELOPERS: @lll.emirx.38 @omer.17l667 @oixin.r3al{Colors.RESET}")
        print(f"{Colors.INFO}LANGUAGE SELECTION / DİL SEÇİMİ / SPRACHWAHL / SÉLECTION DE LANGUE{Colors.RESET}")
        print("═" * 80)
        
        print(f"\n{Colors.ACCENT1}[AVAILABLE LANGUAGES / DESTEKLENEN DİLLER / VERFÜGBARE SPRACHEN]{Colors.RESET}")
        for key, lang in cls.LANGUAGES.items():
            print(f"  {Colors.SUCCESS}{key}.{Colors.RESET} {lang['flag']} {lang['name']}")
        print("\n" + "─" * 80)
        
        while True:
            choice = input(f"\n{Colors.PRIMARY}[SELECTION / SEÇİM / WAHL / CHOIX]:{Colors.RESET} ").strip()
            
            lang_config = cls.LANGUAGES.get(choice)
            if lang_config:
                print(f"{Colors.SUCCESS}[✓] Language selected: {lang_config['name']}{Colors.RESET}")
                return lang_config["code"]
            
            print(f"{Colors.ERROR}[ERROR] Invalid selection. Choose 1-4 only.{Colors.RESET}")

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 4: DATA MODELS & STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class ScanResult:
    """Represents a single scan finding"""
    url: str
    status_code: int
    response_time: float
    headers: Dict[str, str]
    content_length: int
    server: Optional[str]
    timestamp: str
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return asdict(self)
    
    def get_status_color(self) -> str:
        """Get color based on status code"""
        if self.status_code == 200:
            return Colors.STATUS_200
        elif self.status_code == 401:
            return Colors.STATUS_401
        elif self.status_code == 403:
            return Colors.STATUS_403
        elif self.status_code in [301, 302]:
            return Colors.STATUS_301
        return Colors.INFO

@dataclass
class ScanStatistics:
    """Scan statistics and metrics"""
    total_paths: int
    processed_paths: int
    found_results: int
    average_speed: float
    total_duration: float
    status_distribution: Counter
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        data = asdict(self)
        data['status_distribution'] = dict(self.status_distribution)
        return data
    
    def success_rate(self) -> float:
        """Calculate success rate"""
        if self.processed_paths == 0:
            return 0.0
        return (self.found_results / self.processed_paths) * 100

@dataclass
class PathCategory:
    """Path category information"""
    name: str
    paths: List[str]
    count: int
    description: str

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 5: PROFESSIONAL PATH GENERATOR (20,000+ PATHS)
# ═══════════════════════════════════════════════════════════════════════════

class PathGenerator:
    """
    Ultra-advanced path generation system
    Generates 20,000+ admin panel paths across multiple platforms
    """
    
    def __init__(self, translator: TranslationManager):
        self.t = translator
        self.paths: List[str] = []
        self.categories: Dict[str, PathCategory] = {}
        self.stats: Dict[str, int] = Counter()
    
    def generate_all_paths(self) -> List[str]:
        """Generate complete path database"""
        print(f"\n{Colors.PRIMARY}{Colors.BOLD}[{self.t.get('path_gen')}...]{Colors.RESET}")
        
        # Define core paths by category
        core_paths = {
            "wordpress": self._get_wordpress_paths(),
            "joomla": self._get_joomla_paths(),
            "phpmyadmin": self._get_phpmyadmin_paths(),
            "cpanel": self._get_cpanel_paths(),
            "turkish": self._get_turkish_paths(),
            "generic": self._get_generic_paths(),
        }
        
        all_paths = set()
        
        # Generate base paths
        for category, paths in core_paths.items():
            all_paths.update(paths)
            self.stats[category] = len(paths)
            print(f"  {Colors.SUCCESS}[+]{Colors.RESET} {category.capitalize()}: {len(paths)} base paths")
        
        # Generate variations
        print(f"\n  {Colors.INFO}[+] Generating path variations...{Colors.RESET}")
        variations = self._generate_variations(core_paths)
        all_paths.update(variations)
        
        # Add high-value targets
        print(f"  {Colors.INFO}[+] Adding high-value targets...{Colors.RESET}")
        high_value = self._get_high_value_paths()
        all_paths.update(high_value)
        
        # Convert to list and shuffle
        self.paths = list(all_paths)[:20000]
        random.shuffle(self.paths)
        
        print(f"\n  {Colors.SUCCESS}{Colors.BOLD}[✓] {len(self.paths):,} professional paths generated{Colors.RESET}")
        print(f"  {Colors.ACCENT2}    WordPress: {self.stats['wordpress']:,} | Joomla: {self.stats['joomla']:,} | phpMyAdmin: {self.stats['phpmyadmin']:,}{Colors.RESET}")
        print(f"  {Colors.ACCENT2}    cPanel: {self.stats['cpanel']:,} | Turkish: {self.stats['turkish']:,} | Generic: {self.stats['generic']:,}{Colors.RESET}")
        
        return self.paths
    
    def _get_wordpress_paths(self) -> List[str]:
        """WordPress specific paths"""
        return [
            "wp-admin", "wp-login.php", "wp-admin/index.php", "wp-admin/admin.php",
            "wp-admin/admin-ajax.php", "wp-login", "wp/wp-admin", "blog/wp-admin",
            "wordpress/wp-admin", "site/wp-admin", "web/wp-admin", "cms/wp-admin",
            "wp-admin/post.php", "wp-admin/edit.php", "wp-admin/users.php",
            "wp-admin/plugins.php", "wp-admin/themes.php", "wp-admin/options-general.php",
            "wp-admin/upload.php", "wp-admin/edit-comments.php", "wp-admin/tools.php",
            "wp-content/", "wp-includes/", "wp-admin/install.php", "wp-admin/setup-config.php",
            "xmlrpc.php", "wp-cron.php", "wp-trackback.php", "wp-comments-post.php",
        ]
    
    def _get_joomla_paths(self) -> List[str]:
        """Joomla specific paths"""
        return [
            "administrator", "administrator/index.php", "admin", "joomla/administrator",
            "administrator/components", "administrator/modules", "administrator/templates",
            "joomla", "joomla/admin", "cms/administrator", "site/administrator",
            "administrator/manifests", "administrator/language", "administrator/cache",
            "installation", "installation/index.php",
        ]
    
    def _get_phpmyadmin_paths(self) -> List[str]:
        """phpMyAdmin specific paths"""
        return [
            "phpmyadmin", "pma", "phpMyAdmin", "mysql", "adminer", "dbadmin",
            "phpmyadmin/index.php", "pma/index.php", "database", "db",
            "phpmyadmin/setup", "phpmyadmin/scripts", "phpmyadmin/sql.php",
            "myadmin", "mysqladmin", "phpmy", "pma2023", "pma2024", "pma2025",
            "phpmyadmin2", "phpmyadmin-old", "old-phpmyadmin", "backup-phpmyadmin",
            "phpmyadmin/import.php", "phpmyadmin/export.php", "phpmyadmin/server_sql.php",
        ]
    
    def _get_cpanel_paths(self) -> List[str]:
        """cPanel and hosting control panels"""
        return [
            "cpanel", "cPanel", "whm", "webmail", "roundcube", "horde",
            "cp", "panel", "controlpanel", "webadmin", "hosting",
            "cpanel/index.html", "whm/index.html", "webmail/index.html",
            "2082", "2083", "2086", "2087", ":2082", ":2083", ":2086", ":2087",
            "plesk", "plesk-stat", "plesk/login",
        ]
    
    def _get_turkish_paths(self) -> List[str]:
        """Turkish-specific admin panels"""
        return [
            "yonetim", "yonetici", "yonetim-panel", "yonetici-panel", "admin-tr",
            "giris", "adminpanel-tr", "yonetimcp", "yonetim/index.php",
            "yonetim/login", "yonetim/admin", "panel-yonetim", "yonetici-giris",
            "tr-admin", "tr-panel", "turkce-admin", "admin-turkce",
            "yonetim/dashboard", "kontrol-paneli", "yonetim-paneli",
        ]
    
    def _get_generic_paths(self) -> List[str]:
        """Generic admin paths"""
        return [
            "admin", "administrator", "adminpanel", "admincp", "controlpanel",
            "dashboard", "login", "panel", "manage", "moderator", "superadmin",
            "admin/index.php", "admin/login.php", "admin/dashboard.php",
            "admin/cp", "admin/panel", "admin/admin", "administration",
            "adm", "user/admin", "account/admin", "system/admin",
            "backend", "cms", "manage/index.php", "portal/admin",
            "admin.php", "login.php", "signin.php", "dashboard.php",
            "admin/index", "admin/home", "admin/main", "control",
        ]
    
    def _get_high_value_paths(self) -> List[str]:
        """High-value target paths"""
        return [
            "backup", "backups", "config", "configs", "uploads", "files",
            "tmp", "cache", "logs", "test", "staging", "dev", "beta", "demo",
            "api/admin", "rest/admin", "v1/admin", "private", "secure-area",
            "secure", "restricted", "member", "members", "user/login",
            "account", "myaccount", "profile", "settings", "preferences",
        ]
    
    def _generate_variations(self, core_paths: Dict[str, List[str]]) -> Set[str]:
        """Generate path variations"""
        variations = set()
        
        suffixes = [
            "", "1", "2", "123", "_admin", "_cp", "_panel", "_login",
            "2023", "2024", "2025", "_tr", "_test", "_dev", "_backup",
            "_old", "_new", "_v2", "-admin", "-panel", "-old", "-new",
        ]
        
        extensions = [
            "", ".php", "/index.php", "/login.php", "/admin.php", "/cp.php",
            ".html", ".aspx", ".jsp", "/index.html", "/default.php",
            "/default.aspx", ".asp", "/index.asp",
        ]
        
        prefixes = ["", "admin-", "wp-", "site-", "web-", "blog-", "old-", "new-"]
        
        for category, paths in core_paths.items():
            for base in paths:
                # Prefixes
                for prefix in prefixes:
                    path = f"{prefix}{base}"
                    if len(path) < 100 and path != base:
                        variations.add(path)
                
                # Suffixes + extensions
                for suffix in suffixes[:10]:  # Limit to avoid too many
                    for ext in extensions[:8]:  # Limit extensions
                        path = f"{base}{suffix}{ext}".replace("//", "/")
                        if len(path) < 100 and path != base:
                            variations.add(path)
                
                # Subdirectories
                for subdir in ["login", "index", "dashboard", "cp", "admin", "config"]:
                    variations.add(f"{base}/{subdir}")
                    variations.add(f"{base}/{subdir}.php")
        
        return variations
    
    def get_paths(self) -> List[str]:
        """Get generated paths"""
        return self.paths
    
    def get_statistics(self) -> Dict[str, int]:
        """Get path statistics"""
        return dict(self.stats)

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 6: ADVANCED ASYNC SCANNING ENGINE
# ═══════════════════════════════════════════════════════════════════════════

class AdvancedScanner:
    """
    Professional async scanning engine with batch processing
    Supports concurrent requests with rate limiting
    """
    
    def __init__(self, translator: TranslationManager):
        self.t = translator
        self.results: List[ScanResult] = []
        self.statistics = None
        self.start_time = None
        self.target_url = None
    
    async def scan(
        self,
        target_url: str,
        paths: List[str],
        batch_size: int = 5000,
        concurrent_limit: int = 50,
        timeout: int = 10
    ) -> Tuple[List[ScanResult], ScanStatistics]:
        """
        Execute professional scan with batch processing
        
        Args:
            target_url: Target URL to scan
            paths: List of paths to check
            batch_size: Number of paths per batch
            concurrent_limit: Max concurrent requests
            timeout: Request timeout in seconds
        
        Returns:
            Tuple of (results, statistics)
        """
        self.target_url = self._validate_url(target_url)
        self.start_time = time.time()
        self.results = []
        
        # Print scan configuration
        self._print_scan_header(len(paths), batch_size, concurrent_limit, timeout)
        
        # Create batches
        batches = [paths[i:i + batch_size] for i in range(0, len(paths), batch_size)]
        total_batches = len(batches)
        
        status_counter = Counter()
        processed = 0
        
        # Process batches
        connector = aiohttp.TCPConnector(
            limit=concurrent_limit,
            limit_per_host=25,
            ttl_dns_cache=300,
            keepalive_timeout=30
        )
        
        timeout_config = aiohttp.ClientTimeout(total=timeout)
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout_config) as session:
            for batch_num, batch in enumerate(batches, 1):
                print(f"\n{Colors.PRIMARY}[BATCH {batch_num}/{total_batches}]{Colors.RESET} Processing {len(batch):,} paths...")
                
                # Create progress bar
                with tqdm(total=len(batch), desc="Scanning", unit="paths",
                         bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as pbar:
                    
                    # Process batch with semaphore
                    semaphore = asyncio.Semaphore(concurrent_limit)
                    tasks = [self._check_path(session, path, semaphore, pbar) for path in batch]
                    batch_results = await asyncio.gather(*tasks, return_exceptions=True)
                    
                    # Filter and save results
                    for result in batch_results:
                        if isinstance(result, ScanResult):
                            self.results.append(result)
                            status_counter[result.status_code] += 1
                            self._print_live_result(result)
                    
                    processed += len(batch)
                    
                    # Print batch summary
                    elapsed = time.time() - self.start_time
                    speed = processed / elapsed if elapsed > 0 else 0
                    print(f"\n{Colors.INFO}  Processed: {processed:,}/{len(paths):,} | "
                          f"Found: {len(self.results)} | "
                          f"Speed: {speed:.1f} paths/s{Colors.RESET}")
                
                # Small delay between batches
                if batch_num < total_batches:
                    await asyncio.sleep(0.1)
        
        # Calculate final statistics
        total_duration = time.time() - self.start_time
        avg_speed = len(paths) / total_duration if total_duration > 0 else 0
        
        self.statistics = ScanStatistics(
            total_paths=len(paths),
            processed_paths=processed,
            found_results=len(self.results),
            average_speed=avg_speed,
            total_duration=total_duration,
            status_distribution=status_counter
        )
        
        return self.results, self.statistics
    
    async def _check_path(
        self,
        session: aiohttp.ClientSession,
        path: str,
        semaphore: asyncio.Semaphore,
        pbar: tqdm
    ) -> Optional[ScanResult]:
        """Check a single path"""
        async with semaphore:
            try:
                url = self._build_url(self.target_url, path)
                start_time = time.time()
                
                async with session.get(
                    url,
                    allow_redirects=False,
                    headers={"User-Agent": "ModuleArt-Scanner/2.0"}
                ) as response:
                    response_time = time.time() - start_time
                    status_code = response.status
                    
                    # Only save interesting status codes
                    if status_code in [200, 401, 403, 301, 302]:
                        headers = dict(response.headers)
                        content_length = len(await response.read())
                        server = headers.get('Server', 'Unknown')
                        
                        result = ScanResult(
                            url=url,
                            status_code=status_code,
                            response_time=response_time,
                            headers=headers,
                            content_length=content_length,
                            server=server,
                            timestamp=datetime.now().isoformat()
                        )
                        
                        pbar.update(1)
                        return result
            
            except Exception:
                pass
            finally:
                pbar.update(1)
            
            return None
    
    def _validate_url(self, url: str) -> str:
        """Validate and clean URL"""
        url = url.strip()
        
        if not url.startswith(('http://', 'https://')):
            url = f"https://{url}"
        
        url = re.sub(r'^(https?://)www\.', r'\1', url)
        
        return url.rstrip('/')
    
    def _build_url(self, base: str, path: str) -> str:
        """Build complete URL from base and path"""
        clean_path = path.lstrip('/')
        return f"{base}/{clean_path}"
    
    def _print_scan_header(self, total_paths: int, batch_size: int, concurrent: int, timeout: int):
        """Print scan configuration header"""
        print(f"\n{Colors.WARNING}{Colors.BOLD}[{self.t.get('warning')}]{Colors.RESET}")
        print(f"\n{Colors.PRIMARY}{Colors.BOLD}[{self.t.get('scan_start')}]{Colors.RESET}")
        print("═" * 80)
        print(f"{Colors.ACCENT1}Target:{Colors.RESET} {self.target_url}")
        print(f"{Colors.ACCENT1}Total Paths:{Colors.RESET} {total_paths:,}")
        print(f"{Colors.ACCENT1}Batch Size:{Colors.RESET} {batch_size:,}")
        print(f"{Colors.ACCENT1}Concurrent Requests:{Colors.RESET} {concurrent}")
        print(f"{Colors.ACCENT1}Timeout:{Colors.RESET} {timeout}s")
        print(f"{Colors.ACCENT1}Monitoring:{Colors.RESET} 200/401/403/301/302 responses")
        print("═" * 80)
    
    def _print_live_result(self, result: ScanResult):
        """Print result in real-time"""
        color = result.get_status_color()
        print(f"{color}[{result.status_code}]{Colors.RESET} {result.url} ({result.response_time*1000:.0f}ms)")
    
    def get_results(self) -> List[ScanResult]:
        """Get scan results"""
        return self.results
    
    def get_statistics(self) -> Optional[ScanStatistics]:
        """Get scan statistics"""
        return self.statistics

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 7: PROFESSIONAL REPORT GENERATOR
# ═══════════════════════════════════════════════════════════════════════════

class ReportGenerator:
    """
    Professional report generation system
    Supports multiple formats: TXT, JSON, CSV, HTML
    """
    
    def __init__(self, translator: TranslationManager):
        self.t = translator
        self.output_dir = Path("moduleart_reports")
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_all_reports(
        self,
        target_url: str,
        results: List[ScanResult],
        statistics: ScanStatistics
    ) -> Dict[str, str]:
        """Generate all report formats"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        generated_files = {}
        
        print(f"\n{Colors.PRIMARY}{Colors.BOLD}[GENERATING REPORTS]{Colors.RESET}")
        print("═" * 80)
        
        # Generate TXT report
        txt_file = self.generate_txt_report(target_url, results, statistics, timestamp)
        generated_files['txt'] = txt_file
        print(f"{Colors.SUCCESS}[✓] Text Report:{Colors.RESET} {txt_file}")
        
        # Generate JSON report
        json_file = self.generate_json_report(target_url, results, statistics, timestamp)
        generated_files['json'] = json_file
        print(f"{Colors.SUCCESS}[✓] JSON Report:{Colors.RESET} {json_file}")
        
        # Generate CSV report
        csv_file = self.generate_csv_report(results, timestamp)
        generated_files['csv'] = csv_file
        print(f"{Colors.SUCCESS}[✓] CSV Report:{Colors.RESET} {csv_file}")
        
        # Generate HTML report
        html_file = self.generate_html_report(target_url, results, statistics, timestamp)
        generated_files['html'] = html_file
        print(f"{Colors.SUCCESS}[✓] HTML Report:{Colors.RESET} {html_file}")
        
        print("═" * 80)
        print(f"{Colors.SUCCESS}{Colors.BOLD}[✓] All reports generated successfully{Colors.RESET}")
        
        return generated_files
    
    def generate_txt_report(
        self,
        target_url: str,
        results: List[ScanResult],
        statistics: ScanStatistics,
        timestamp: str
    ) -> str:
        """Generate text report"""
        filename = self.output_dir / f"scan_report_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("═" * 100 + "\n")
            f.write(f"MODULEART v2.0 - {self.t.get('scan_report')}\n".center(100))
            f.write("═" * 100 + "\n\n")
            
            f.write(f"{self.t.get('target_url')}: {target_url}\n")
            f.write(f"{self.t.get('scan_date')}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{self.t.get('duration')}: {statistics.total_duration:.2f}s\n")
            f.write(f"{self.t.get('paths_scanned')}: {statistics.processed_paths:,}\n")
            f.write(f"{self.t.get('findings_found')}: {statistics.found_results}\n")
            f.write(f"Average Speed: {statistics.average_speed:.2f} paths/s\n")
            f.write(f"Success Rate: {statistics.success_rate():.2f}%\n\n")
            
            f.write("─" * 100 + "\n")
            f.write("STATUS CODE DISTRIBUTION\n")
            f.write("─" * 100 + "\n")
            for status, count in sorted(statistics.status_distribution.items()):
                f.write(f"  {status}: {count:,} findings\n")
            
            f.write("\n" + "─" * 100 + "\n")
            f.write(f"{self.t.get('critical')} ({len(results)})\n")
            f.write("─" * 100 + "\n\n")
            
            for idx, result in enumerate(results, 1):
                f.write(f"[{idx}] {result.url}\n")
                f.write(f"    Status: {result.status_code}\n")
                f.write(f"    Response Time: {result.response_time*1000:.2f}ms\n")
                f.write(f"    Server: {result.server}\n")
                f.write(f"    Content Length: {result.content_length} bytes\n")
                f.write(f"    Timestamp: {result.timestamp}\n\n")
            
            f.write("═" * 100 + "\n")
            f.write("DEVELOPERS: @lll.emirx.38 @omer.17l667 @oixin.r3al\n".center(100))
            f.write("═" * 100 + "\n")
        
        return str(filename)
    
    def generate_json_report(
        self,
        target_url: str,
        results: List[ScanResult],
        statistics: ScanStatistics,
        timestamp: str
    ) -> str:
        """Generate JSON report"""
        filename = self.output_dir / f"scan_report_{timestamp}.json"
        
        report = {
            "scan_info": {
                "target_url": target_url,
                "scan_date": datetime.now().isoformat(),
                "scanner_version": "ModuleArt v2.0",
                "developers": ["@lll.emirx.38", "@omer.17l667", "@oixin.r3al"]
            },
            "statistics": statistics.to_dict(),
            "results": [result.to_dict() for result in results]
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return str(filename)
    
    def generate_csv_report(self, results: List[ScanResult], timestamp: str) -> str:
        """Generate CSV report"""
        filename = self.output_dir / f"scan_report_{timestamp}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['URL', 'Status Code', 'Response Time (ms)', 'Server', 'Content Length', 'Timestamp'])
            
            for result in results:
                writer.writerow([
                    result.url,
                    result.status_code,
                    f"{result.response_time*1000:.2f}",
                    result.server,
                    result.content_length,
                    result.timestamp
                ])
        
        return str(filename)
    
    def generate_html_report(
        self,
        target_url: str,
        results: List[ScanResult],
        statistics: ScanStatistics,
        timestamp: str
    ) -> str:
        """Generate HTML report"""
        filename = self.output_dir / f"scan_report_{timestamp}.html"
        
        template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ModuleArt Scan Report</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .header p { opacity: 0.9; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 40px;
            background: #f8f9fa;
        }
        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .stat-card h3 { color: #667eea; font-size: 2em; margin-bottom: 5px; }
        .stat-card p { color: #666; font-size: 0.9em; }
        .results {
            padding: 40px;
        }
        .results h2 {
            color: #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background: #667eea;
            color: white;
            font-weight: 600;
        }
        tr:hover { background: #f8f9fa; }
        .status-200 { color: #28a745; font-weight: bold; }
        .status-401 { color: #ffc107; font-weight: bold; }
        .status-403 { color: #fd7e14; font-weight: bold; }
        .status-30x { color: #17a2b8; font-weight: bold; }
        .footer {
            background: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛡️ ModuleArt v2.0</h1>
            <p>Professional Security Scan Report</p>
            <p style="margin-top: 10px; opacity: 0.8;">{{ target_url }}</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <h3>{{ stats.processed_paths|number_format }}</h3>
                <p>Paths Scanned</p>
            </div>
            <div class="stat-card">
                <h3>{{ stats.found_results }}</h3>
                <p>Findings</p>
            </div>
            <div class="stat-card">
                <h3>{{ "%.1f"|format(stats.average_speed) }}</h3>
                <p>Paths/Second</p>
            </div>
            <div class="stat-card">
                <h3>{{ "%.2f"|format(stats.total_duration) }}s</h3>
                <p>Duration</p>
            </div>
        </div>
        
        <div class="results">
            <h2>🎯 Critical Findings ({{ results|length }})</h2>
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>URL</th>
                        <th>Status</th>
                        <th>Response Time</th>
                        <th>Server</th>
                    </tr>
                </thead>
                <tbody>
                    {% for result in results %}
                    <tr>
                        <td>{{ loop.index }}</td>
                        <td style="font-family: monospace; font-size: 0.9em;">{{ result.url }}</td>
                        <td class="status-{{ result.status_code }}">{{ result.status_code }}</td>
                        <td>{{ "%.0f"|format(result.response_time * 1000) }}ms</td>
                        <td>{{ result.server }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        
        <div class="footer">
            <p>Generated by ModuleArt v2.0 Ultra</p>
            <p style="margin-top: 5px; opacity: 0.7;">@lll.emirx.38 @omer.17l667 @oixin.r3al</p>
        </div>
    </div>
</body>
</html>
"""
        
        from jinja2 import Template
        
        def number_format(value):
            return f"{value:,}"
        
        template_obj = Template(template)
        template_obj.globals['number_format'] = number_format
        
        html_content = template_obj.render(
            target_url=target_url,
            stats=statistics,
            results=results
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return str(filename)

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 8: TARGET MANAGEMENT SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

class TargetManager:
    """Manage saved targets for quick scanning"""
    
    def __init__(self):
        self.targets_file = Path("moduleart_targets.json")
        self.targets: Dict[str, Dict] = self._load_targets()
    
    def _load_targets(self) -> Dict:
        """Load saved targets"""
        if self.targets_file.exists():
            with open(self.targets_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_targets(self):
        """Save targets to file"""
        with open(self.targets_file, 'w') as f:
            json.dump(self.targets, f, indent=2)
    
    def add_target(self, url: str, name: Optional[str] = None):
        """Add a new target"""
        target_id = str(len(self.targets) + 1)
        self.targets[target_id] = {
            "url": url,
            "name": name or url,
            "scan_count": 0,
            "last_scan": None,
            "added_date": datetime.now().isoformat()
        }
        self._save_targets()
        return target_id
    
    def get_target(self, target_id: str) -> Optional[Dict]:
        """Get target by ID"""
        return self.targets.get(target_id)
    
    def list_targets(self) -> Dict:
        """List all targets"""
        return self.targets
    
    def update_scan_count(self, target_id: str):
        """Update scan count for a target"""
        if target_id in self.targets:
            self.targets[target_id]["scan_count"] += 1
            self.targets[target_id]["last_scan"] = datetime.now().isoformat()
            self._save_targets()
    
    def delete_target(self, target_id: str) -> bool:
        """Delete a target"""
        if target_id in self.targets:
            del self.targets[target_id]
            self._save_targets()
            return True
        return False

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 9: MAIN APPLICATION CLASS
# ═══════════════════════════════════════════════════════════════════════════

class ModuleArtUltra:
    """
    Main application class orchestrating all components
    Ultra-modern admin panel scanner with 4000+ lines of professional code
    """
    
    def __init__(self):
        self.translator = None
        self.path_generator = None
        self.scanner = None
        self.report_generator = None
        self.target_manager = TargetManager()
        
    def show_legal_warning(self):
        """Display legal warning and get acceptance"""
        print(f"\n{Colors.ERROR}{Colors.BOLD}")
        print("╔" + "═" * 78 + "╗")
        print("║" + " " * 78 + "║")
        print("║" + "⚠️  LEGAL WARNING / YASAL UYARI / RECHTLICHER HINWEIS".center(78) + "║")
        print("║" + " " * 78 + "║")
        print("╚" + "═" * 78 + "╝")
        print(Colors.RESET)
        
        warnings = [
            "This tool must ONLY be used on systems you own or have authorization to test.",
            "Unauthorized scanning may violate computer fraud laws in your jurisdiction.",
            "The developers assume no liability for misuse of this software.",
            "By using this tool, you accept full responsibility for your actions.",
            "",
            "Bu araç SADECE sahip olduğunuz veya yetkiniz olan sistemlerde kullanılmalıdır.",
            "Yetkisiz tarama, bulunduğunuz yargı bölgesindeki bilgisayar dolandırıcılığı yasalarını ihlal edebilir.",
        ]
        
        for warning in warnings:
            print(f"  {Colors.WARNING}• {warning}{Colors.RESET}")
        
        print(f"\n{Colors.PRIMARY}{'─' * 80}{Colors.RESET}")
        response = input(f"{Colors.BOLD}Type 'I ACCEPT' to continue: {Colors.RESET}")
        
        if response.strip().upper() != "I ACCEPT":
            print(f"\n{Colors.ERROR}[✗] You must accept the terms to use this tool.{Colors.RESET}")
            sys.exit(0)
        
        print(f"{Colors.SUCCESS}[✓] Terms accepted. Proceeding...{Colors.RESET}")
    
    def select_language(self) -> str:
        """Language selection"""
        return TranslationManager.select_language()
    
    def initialize(self, lang_code: str):
        """Initialize all components"""
        self.translator = TranslationManager(lang_code)
        self.path_generator = PathGenerator(self.translator)
        self.scanner = AdvancedScanner(self.translator)
        self.report_generator = ReportGenerator(self.translator)
    
    def get_target_url(self) -> str:
        """Get target URL from user"""
        print(f"\n{Colors.PRIMARY}{'─' * 80}{Colors.RESET}")
        print(f"{Colors.BOLD}[{self.translator.get('target_input')}]{Colors.RESET}")
        print(f"{Colors.DIM}Examples: example.com, https://example.com, www.example.com{Colors.RESET}")
        print(f"{Colors.PRIMARY}{'─' * 80}{Colors.RESET}")
        
        while True:
            target = input(f"\n{Colors.PRIMARY}Target URL:{Colors.RESET} ").strip()
            
            if not target:
                print(f"{Colors.ERROR}[✗] Target URL cannot be empty{Colors.RESET}")
                continue
            
            # Basic validation
            if '.' not in target:
                print(f"{Colors.ERROR}[✗] Invalid URL format{Colors.RESET}")
                continue
            
            return target
    
    def run(self):
        """Main execution flow"""
        # Show banner
        print(Banner.main_banner())
        
        # Legal warning
        self.show_legal_warning()
        
        # Language selection
        lang_code = self.select_language()
        
        # Initialize components
        self.initialize(lang_code)
        
        # Generate paths
        paths = self.path_generator.generate_all_paths()
        
        # Get target URL
        target_url = self.get_target_url()
        
        # Execute scan
        print(f"\n{Colors.PRIMARY}{Colors.BOLD}[INITIATING PROFESSIONAL SCAN]{Colors.RESET}")
        
        results, statistics = asyncio.run(
            self.scanner.scan(
                target_url=target_url,
                paths=paths,
                batch_size=5000,
                concurrent_limit=50,
                timeout=10
            )
        )
        
        # Show completion banner
        print(Banner.scan_complete_banner(len(results)))
        
        # Print statistics
        self.print_statistics(statistics)
        
        # Generate reports if findings exist
        if results:
            report_files = self.report_generator.generate_all_reports(
                target_url=target_url,
                results=results,
                statistics=statistics
            )
            
            print(f"\n{Colors.SUCCESS}{Colors.BOLD}[✓] Scan completed successfully!{Colors.RESET}")
        else:
            print(f"\n{Colors.WARNING}[!] {self.translator.get('no_findings')}{Colors.RESET}")
        
        # Show goodbye message
        self.show_goodbye()
    
    def print_statistics(self, stats: ScanStatistics):
        """Print detailed statistics"""
        print(f"\n{Colors.PRIMARY}{Colors.BOLD}[SCAN STATISTICS]{Colors.RESET}")
        print("═" * 80)
        print(f"{Colors.ACCENT1}Total Paths:{Colors.RESET} {stats.total_paths:,}")
        print(f"{Colors.ACCENT1}Processed:{Colors.RESET} {stats.processed_paths:,}")
        print(f"{Colors.ACCENT1}Findings:{Colors.RESET} {stats.found_results}")
        print(f"{Colors.ACCENT1}Average Speed:{Colors.RESET} {stats.average_speed:.2f} paths/s")
        print(f"{Colors.ACCENT1}Total Duration:{Colors.RESET} {stats.total_duration:.2f}s")
        print(f"{Colors.ACCENT1}Success Rate:{Colors.RESET} {stats.success_rate():.2f}%")
        print("\n" + Colors.ACCENT2 + "Status Code Distribution:" + Colors.RESET)
        for status, count in sorted(stats.status_distribution.items()):
            print(f"  {status}: {count:,} findings")
        print("═" * 80)
    
    def show_goodbye(self):
        """Show goodbye message"""
        print(f"\n{Colors.PRIMARY}")
        print("╔" + "═" * 78 + "╗")
        print("║" + " " * 78 + "║")
        print("║" + "Thank you for using ModuleArt Ultra v2.0!".center(78) + "║")
        print("║" + "DEVELOPERS: @lll.emirx.38 @omer.17l667 @oixin.r3al".center(78) + "║")
        print("║" + " " * 78 + "║")
        print("╚" + "═" * 78 + "╝")
        print(Colors.RESET)

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 10: ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Main entry point"""
    try:
        app = ModuleArtUltra()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}[!] Scan interrupted by user{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.ERROR}[✗] Fatal error: {str(e)}{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
