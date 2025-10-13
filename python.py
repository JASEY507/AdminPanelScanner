#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ModuleArt v1.0 - PROFESSIONAL ADMIN PANEL SCANNER
DEVELOPERS: @lll.emirx.38 @omer.17l667 @oixin.r3al
20K PATHS | LIVE BATCH SCANNING | MULTILINGUAL SUPPORT
AUTHORIZED SECURITY TESTING ONLY
"""

import subprocess
import sys
import importlib
import time
import os
import random
import re
from collections import Counter
import asyncio
import aiohttp
from datetime import datetime

# Language configurations (Kürtçe REMOVED)
LANGUAGES = {
    "1": {"code": "tr", "name": "Türkçe"},
    "2": {"code": "en", "name": "English"},
    "3": {"code": "de", "name": "Deutsch"},
    "4": {"code": "fr", "name": "Français"}
}

class Colors:
    HEADER = '\033[95m'; OKBLUE = '\033[94m'; OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'; WARNING = '\033[93m'; FAIL = '\033[91m'
    ENDC = '\033[0m'; BOLD = '\033[1m'

def print_status(text, color=Colors.ENDC, end='\n'):
    sys.stdout.write(f"{color}{text}{Colors.ENDC}")
    sys.stdout.write(end)
    sys.stdout.flush()

def show_language_menu():
    """Display multilingual language selection"""
    print_status("\n" + "="*80, Colors.HEADER)
    print_status("MODULEART v6.2 - PROFESSIONAL ADMIN PANEL SCANNER", Colors.OKGREEN)
    print_status("DEVELOPERS: @lll.emirx.38 @omer.17l667 @oixin.r3al", Colors.OKCYAN)
    print_status("LANGUAGE SELECTION / DİL SEÇİMİ / SPRACHWAHL / SÉLECTION DE LANGUE", Colors.WARNING)
    print_status("="*80, Colors.HEADER)
    
    print_status("\n[AVAILABLE LANGUAGES / DESTEKLELEN DİLLER / VERFÜGBARE SPRACHEN]", Colors.OKBLUE)
    for key, lang in LANGUAGES.items():
        print_status(f"  {key}. {lang['name']}", Colors.OKGREEN)
    print_status("\n" + "-"*80, Colors.WARNING)
    
    while True:
        choice = input("\n[SELECTION / SEÇİM / WAHL / CHOIX]: ").strip()
        
        lang_config = LANGUAGES.get(choice)
        if lang_config:
            print_status(f"[+] Language selected: {lang_config['name']}", Colors.OKGREEN)
            return lang_config["code"]
        
        print_status("[ERROR] Invalid selection. Choose 1-4 only.", Colors.FAIL)

def get_translations(lang):
    """Get language-specific translations"""
    translations = {
        "tr": {
            "system_init": "SİSTEM BAŞLATILIYOR",
            "lib_check": "Kütüphane Kontrolü",
            "path_gen": "Yol veritabanı oluşturuluyor",
            "target_input": "Hedef URL girin",
            "warning": "SADECE YETKİLİ HEDEFLERDE KULLANIN",
            "scan_start": "PROFESYONEL TARAMA BAŞLIYOR",
            "batch_info": "Batch işleniyor",
            "progress": "İlerleme",
            "speed": "Hız",
            "findings": "Bulunan",
            "scan_complete": "TARAMA TAMAMLANDI",
            "report_saved": "Rapor kaydedildi",
            "critical": "KRİTİK BULUNTULAR",
            "no_findings": "Admin panel bulunamadı"
        },
        "en": {
            "system_init": "SYSTEM INITIALIZING",
            "lib_check": "Library verification", 
            "path_gen": "Generating path database",
            "target_input": "Enter target URL",
            "warning": "USE ONLY ON AUTHORIZED TARGETS",
            "scan_start": "PROFESSIONAL SCAN STARTING",
            "batch_info": "Processing batch",
            "progress": "Progress",
            "speed": "Speed",
            "findings": "Findings",
            "scan_complete": "SCAN COMPLETED",
            "report_saved": "Report saved",
            "critical": "CRITICAL FINDINGS",
            "no_findings": "No admin panels detected"
        },
        "de": {
            "system_init": "SYSTEM WIRD INITIALISIERT",
            "lib_check": "Bibliotheksprüfung",
            "path_gen": "Pfad-Datenbank wird erstellt",
            "target_input": "Ziel-URL eingeben",
            "warning": "NUR BEI AUTORISIERTEN ZIELEN VERWENDEN",
            "scan_start": "PROFESSIONELLER SCAN STARTET",
            "batch_info": "Batch wird verarbeitet",
            "progress": "Fortschritt",
            "speed": "Geschwindigkeit",
            "findings": "Erkenntnisse",
            "scan_complete": "SCAN ABGESCHLOSSEN",
            "report_saved": "Bericht gespeichert",
            "critical": "KRITISCHE ERKENNTNISSE",
            "no_findings": "Keine Admin-Panels erkannt"
        },
        "fr": {
            "system_init": "SYSTÈME S'INITIALISE",
            "lib_check": "Vérification des bibliothèques",
            "path_gen": "Génération de la base de chemins",
            "target_input": "Entrez l'URL cible",
            "warning": "UTILISEZ UNIQUEMENT SUR DES CIBLES AUTORISÉES",
            "scan_start": "SCAN PROFESSIONNEL DÉMARRE",
            "batch_info": "Traitement du lot",
            "progress": "Progression",
            "speed": "Vitesse",
            "findings": "Résultats",
            "scan_complete": "SCAN TERMINÉ",
            "report_saved": "Rapport sauvegardé",
            "critical": "RÉSULTATS CRITIQUES",
            "no_findings": "Aucun panneau d'administration détecté"
        }
    }
    return translations.get(lang, translations["en"])

def initialize_system(lang_trans):
    """Multilingual system initialization"""
    print_status(f"\n[{lang_trans['system_init']}]", Colors.HEADER)
    print_status("DEVELOPERS: @lll.emirx.38 @omer.17l667 @oixin.r3al", Colors.OKCYAN)
    print_status("Library verification and dependency check", Colors.WARNING)
    
    packages = ["aiohttp", "requests"]
    for pkg in packages:
        try:
            importlib.import_module(pkg)
            print_status(f"[+] {pkg} loaded successfully", Colors.OKGREEN)
        except ImportError:
            print_status(f"[-] {pkg} not found, installing...", Colors.WARNING)
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", pkg], timeout=60)
                print_status(f"[+] {pkg} installed", Colors.OKGREEN)
            except:
                print_status(f"[!] Manual install: pip3 install --user {pkg}", Colors.FAIL)
                sys.exit(1)
    
    global aiohttp, requests
    import aiohttp
    import requests
    print_status("[+] All systems operational", Colors.OKGREEN)
    print_status("="*80, Colors.HEADER)

def generate_professional_paths(lang_trans):
    """Generate 20K admin paths - FIXED unhashable type error"""
    print_status(f"\n[{lang_trans['path_gen']}]...", Colors.OKBLUE)
    
    # Core admin paths - HIGH SUCCESS RATE
    core_paths = [
        # WordPress
        "wp-admin", "wp-login.php", "wp-admin/index.php", "wp-admin/admin.php",
        "wp-admin/admin-ajax.php", "wp-login", "wp/wp-admin", "blog/wp-admin",
        
        # phpMyAdmin
        "phpmyadmin", "pma", "phpMyAdmin", "mysql", "adminer", "dbadmin",
        "phpmyadmin/index.php", "pma/index.php", "database", "db",
        "phpmyadmin/setup", "phpmyadmin/scripts",
        
        # Joomla
        "administrator", "administrator/index.php", "admin", "joomla/administrator",
        
        # cPanel/Hosting
        "cpanel", "cPanel", "whm", "webmail", "roundcube", "horde",
        "cp", "panel", "controlpanel", "webadmin",
        
        # Generic admin
        "admin", "administrator", "adminpanel", "admincp", "controlpanel",
        "dashboard", "login", "panel", "manage", "moderator", "superadmin",
        
        # Turkish panels
        "yonetim", "yonetici", "yonetim-panel", "yonetici-panel", "admin-tr",
        "giris", "adminpanel-tr", "yonetimcp", "yonetim/index.php"
    ]
    
    # Path modifiers
    suffixes = ["", "1", "2", "123", "_admin", "_cp", "_panel", "_login", 
                "2023", "2024", "2025", "_tr", "_test", "_dev", "_backup"]
    extensions = ["", ".php", "/index.php", "/login.php", "/admin.php", "/cp.php"]
    
    all_paths = set()  # FIXED: Using set() not dict
    
    # Add base paths first
    print_status("  [+] Building base administrative paths...", Colors.OKCYAN)
    for base in core_paths:
        all_paths.add(base)
        # Common subpaths
        for sub in ["login", "index", "dashboard", "cp", "admin", "config"]:
            all_paths.add(f"{base}/{sub}")
            all_paths.add(f"{base}/{sub}.php")
    
    # Generate combinations systematically
    print_status("  [+] Generating path variations...", Colors.WARNING)
    processed_bases = 0
    target_paths = 20000
    
    for base in core_paths:
        if len(all_paths) >= target_paths:
            break
            
        for suffix in suffixes:
            if len(all_paths) >= target_paths:
                break
            for ext in extensions:
                path = f"{base}{suffix}{ext}".strip('/')
                if path and len(path) < 100:
                    all_paths.add(path)
        
        processed_bases += 1
        if processed_bases % 10 == 0:
            print_status(f"    Progress: {len(all_paths):,} paths generated", Colors.OKCYAN)
    
    # Additional high-value targets
    high_value = [
        "backup", "backups", "config", "configs", "uploads", "files",
        "tmp", "cache", "logs", "test", "staging", "dev", "beta", "demo",
        "api/admin", "rest/admin", "user/admin", "private", "secure-area"
    ]
    all_paths.update(high_value)
    
    path_list = list(all_paths)[:20000]
    random.shuffle(path_list)
    
    print_status(f"  [+] {len(path_list):,} professional paths prepared", Colors.OKGREEN)
    return path_list

def validate_target(lang_trans):
    """Multilingual target validation"""
    while True:
        target_input = input(f"\n[{lang_trans['target_input']}]: ").strip()
        if target_input.startswith(('http://', 'https://')):
            return target_input
        if '.' in target_input:
            clean = target_input.lstrip('www.')
            return f"https://{clean}"
        print_status("[ERROR] Invalid URL format", Colors.FAIL)
        print_status("  Example: example.com or https://example.com", Colors.WARNING)

async def professional_scan(target, paths, lang_trans):
    """Professional batch scanning with live results"""
    total_paths = len(paths)
    stats = Counter()
    all_found = []
    batch_size = 5000
    
    print_status(f"\n[{lang_trans['warning']}]", Colors.FAIL)
    print_status(f"[{lang_trans['scan_start']}]", Colors.HEADER)
    print_status(f"Target: {target}", Colors.OKCYAN)
    print_status(f"Total paths: {total_paths:,}", Colors.OKCYAN)
    print_status(f"Batch size: {batch_size:,}", Colors.OKCYAN)
    print_status("Monitoring: 200/401/403/301/302 responses", Colors.WARNING)
    print_status("-" * 80, Colors.HEADER)
    
    connector = aiohttp.TCPConnector(
        limit=100, 
        limit_per_host=25,
        ttl_dns_cache=300,
        keepalive_timeout=30
    )
    timeout = aiohttp.ClientTimeout(total=10)
    
    start_time = time.time()
    batches = [paths[i:i+batch_size] for i in range(0, total_paths, batch_size)]
    
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        for batch_num, batch in enumerate(batches, 1):
            print_status(f"\n[BATCH {batch_num}/{len(batches)}] Processing {len(batch):,} paths", Colors.OKBLUE)
            
            semaphore = asyncio.Semaphore(50)
            
            async def check_path(path):
                async with semaphore:
                    try:
                        url = f"{target.rstrip('/')}/{path.lstrip('/')}"
                        async with session.get(url, allow_redirects=False) as resp:
                            status = resp.status
                            if status in [200, 401, 403, 301, 302]:
                                return (url, status)
                    except:
                        pass
                    return None
            
            tasks = [check_path(path) for path in batch]
            batch_results = await asyncio.gather(*tasks, return_exceptions=True)
            
            batch_found = [r for r in batch_results if isinstance(r, tuple)]
            all_found.extend(batch_found)
            
            for url, status in batch_found:
                stats[status] += 1
            
            # Live progress update
            elapsed = time.time() - start_time
            processed = min(batch_num * batch_size, total_paths)
            progress = (processed / total_paths) * 100
            speed = processed / elapsed if elapsed > 0 else 0
            
            print_status(f"  [{lang_trans['progress']}]: {progress:6.2f}% | {processed:,}/{total_paths:,}", Colors.OKCYAN)
            print_status(f"  [{lang_trans['speed']}]: {speed:6.1f} p/s | Elapsed: {elapsed:6.1f}s", Colors.OKBLUE)
            print_status(f"  [{lang_trans['findings']}]: {len(all_found)} | Stats: {dict(stats)}", Colors.WARNING)
            
            # Display recent findings
            recent_findings = batch_found[-5:] if batch_found else []
            for url, status in recent_findings:
                path = url.split('/')[-1][:50]
                color = Colors.OKGREEN if status == 200 else Colors.WARNING
                print_status(f"    [{status}] {path}", color)
    
    return all_found, stats

def generate_report(found, target, stats, duration, lang):
    """Generate professional scan report"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    lang_name = LANGUAGES[[k for k, v in LANGUAGES.items() if v["code"] == lang][0]]["name"]
    filename = f"moduleart_scan_{lang_name.lower()}_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("MODULEART v6.2 PROFESSIONAL SCAN REPORT\n")
        f.write("DEVELOPERS: @lll.emirx.38 @omer.17l667 @oixin.r3al\n")
        f.write("=" * 80 + "\n")
        f.write(f"Language: {lang_name}\n")
        f.write(f"Target: {target}\n")
        f.write(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Paths: {len(found)}\n")
        f.write(f"Duration: {duration:.2f} seconds\n")
        f.write(f"Scan Rate: {len(found)/duration:.1f} paths/second\n")
        f.write(f"Statistics: {dict(stats)}\n")
        f.write("=" * 80 + "\n\n")
        
        if found:
            f.write("DETECTED ENDPOINTS:\n")
            f.write("-" * 80 + "\n")
            for i, (url, status) in enumerate(found, 1):
                f.write(f"{i:4d}. [{status}] {url}\n")
        else:
            f.write("No administrative endpoints detected.\n")
    
    return filename

def main():
    """Main professional scanner"""
    try:
        # Language selection
        lang = show_language_menu()
        lang_trans = get_translations(lang)
        
        # System initialization
        initialize_system(lang_trans)
        
        # Target validation
        target = validate_target(lang_trans)
        print_status(f"[+] Target confirmed: {target}", Colors.OKGREEN)
        
        # Path generation
        paths = generate_professional_paths(lang_trans)
        
        # Confirmation
        print_status(f"\n[{lang_trans['warning']}]", Colors.FAIL)
        confirm = input("[CONFIRM / ONAYLA / BESTÄTIGEN / CONFIRMER] (y/N): ").lower().strip()
        if confirm != 'y':
            print_status("[ABORT] Scan cancelled by user", Colors.WARNING)
            return
        
        # Execute scan
        start_time = time.time()
        found, stats = asyncio.run(professional_scan(target, paths, lang_trans))
        duration = time.time() - start_time
        
        # Final results
        print_status(f"\n[{lang_trans['scan_complete']}]", Colors.OKGREEN)
        print_status("="*80, Colors.HEADER)
        print_status(f"Total paths tested: {len(paths):,}", Colors.OKCYAN)
        print_status(f"Endpoints discovered: {len(found)}", Colors.OKGREEN)
        print_status(f"Scan duration: {duration:.2f} seconds", Colors.WARNING)
        print_status(f"Average rate: {len(paths)/duration:.1f} paths/second", Colors.OKCYAN)
        print_status(f"Response statistics: {dict(stats)}", Colors.WARNING)
        
        # Generate report
        report_file = generate_report(found, target, stats, duration, lang)
        print_status(f"\n[REPORT] Results saved to: {report_file}", Colors.OKGREEN)
        
        # Display critical findings
        if found:
            print_status(f"\n[{lang_trans['critical']}]", Colors.FAIL)
            critical = [(u,s) for u,s in found if s == 200]
            restricted = [(u,s) for u,s in found if s in [401, 403]]
            
            if critical:
                print_status("  200 OK (Accessible):", Colors.OKGREEN)
                for url, _ in critical[:5]:
                    print_status(f"    {url.split('/')[-1]}", Colors.OKGREEN)
            
            if restricted:
                print_status("  401/403 (Protected):", Colors.WARNING)
                for url, status in restricted[:5]:
                    print_status(f"    [{status}] {url.split('/')[-1]}", Colors.WARNING)
        else:
            print_status(f"\n[{lang_trans['no_findings']}]", Colors.WARNING)
            print_status("  - Verify target accessibility", Colors.OKCYAN)
            print_status("  - Check firewall and rate limiting", Colors.OKCYAN)
        
        print_status("\nDEVELOPERS: @lll.emirx.38 @omer.17l667 @oixin.r3al", Colors.OKCYAN)
        print_status("="*80, Colors.HEADER)
        
    except KeyboardInterrupt:
        print_status("\n[INTERRUPT] Scan terminated by user", Colors.FAIL)
    except Exception as e:
        print_status(f"\n[ERROR] {str(e)}", Colors.FAIL)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
