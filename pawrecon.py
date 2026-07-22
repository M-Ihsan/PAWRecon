#!/usr/bin/env python3
# ================================
#   Penetration And Recon Workshop - PAW RECON - Reconnaissance Toolkit
#   By: Muhammad Ihsan
#   Version: 1.0
#   Description: Network Scanner +
#   Subdomain Enumerator
# ================================

import os
import socket
import subprocess
import sys
from datetime import datetime

# Colors for terminal output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
MAGENTA = "\033[35m"
GOLD = "\033[33m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"


def ensure_reports_dir():
    reports_dir = "Reports"
    os.makedirs(reports_dir, exist_ok=True)
    return reports_dir


# Common ports dictionary
COMMON_PORTS = {
    # Core Infrastructure & Mail
    20: "FTP-Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    587: "SMTP-Submission",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    # Databases
    1433: "MSSQL",
    1521: "Oracle",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    27017: "MongoDB",
    # Web & Remote Access
    3389: "RDP",
    5900: "VNC",
    8000: "HTTP-Alt",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    8888: "HTTP-Alt",
}

# Subdomain wordlist

SUBDOMAINS = [
    # Top Traffic & Essential
    "www",
    "m",
    "mobile",
    "mail",
    "webmail",
    "smtp",
    "pop",
    "imap",
    "ns1",
    "ns2",
    # Development & Testing
    "dev",
    "developer",
    "test",
    "staging",
    "stage",
    "beta",
    "demo",
    "sandbox",
    "qa",
    "old",
    # APIs & Gateways
    "api",
    "v1",
    "v2",
    "gateway",
    "ws",
    "graphql",
    # Auth & Admin
    "admin",
    "portal",
    "login",
    "auth",
    "sso",
    "secure",
    "dashboard",
    "cpanel",
    "vpn",
    "remote",
    # Content & Media
    "cdn",
    "static",
    "assets",
    "img",
    "images",
    "media",
    "files",
    "download",
    "uploads",
    # Business & Services
    "app",
    "blog",
    "shop",
    "store",
    "forum",
    "support",
    "help",
    "docs",
    "status",
    "pay",
    # Auto-Config
    "autodiscover",
    "autoconfig",
]


def banner():
    print(rf"""
{CYAN}
 ____   _    __        __  ____  _____ ____ ___  _   _ 
|  _ \ / \   \ \      / / |  _ \| ____/ ___/ _ \| \ | |
| |_) / _ \   \ \ /\ / /  | |_) |  _|| |  | | | |  \| |
|  __/ ___ \   \ V  V /   |  _ <| |__| |__| |_| | |\  |
|_| /_/   \_\   \_/\_/    |_| \_\_____\____\___/|_| \_|
{RESET}
{YELLOW}             Reconnaissance Toolkit v1.0{RESET}
{WHITE}        Network Scanner + Subdomain Enumerator{RESET}

{CYAN}
    =^.,.^=       {YELLOW}~ sniff sniff... targets detected ~{CYAN}
{RESET}
    """)


# Information about the tool


def scan_info():
    print(f"\n{CYAN}{'='*67}")
    print(f"Penetration And Recon Workshop - PAW RECON - Reconnaissance Toolkit")
    print(f"{'='*67}{RESET}")
    print(f"{WHITE}  Tool:     PAW RECON v1.0{RESET}")
    print(f"{WHITE}  Author:   Muhammad Ihsan{RESET}")
    print(f"{WHITE}  Purpose:  Reconnaissance Toolkit{RESET}")
    print(f"{WHITE}  Features: Port Scanner + Subdomain Enum{RESET}")
    print(
        f"{WHITE}  Warning:  Use only on authorized targets and ethical purposes{RESET}"
    )
    print(f"{CYAN}{'='*63}{RESET}\n")


# Main menu function


def main_menu():
    print(f"\n{CYAN}{'='*45}{RESET}")
    print(f"{YELLOW}  Select an option:{RESET}")
    print(f"{GREEN}  [1] Network Port Scanner{RESET}")
    print(f"{GREEN}  [2] Subdomain Enumerator{RESET}")
    print(f"{BLUE}  [3] About PAW RECON{RESET}")
    print(f"{RED}  [4] Exit{RESET}")
    print(f"{CYAN}{'='*45}{RESET}")
    choice = input(f"{YELLOW}  PAW> {RESET}")
    return choice


# Network Port Scanner function


def port_scanner():
    print(f"\n{CYAN}{'='*45}")
    print(f"         NETWORK PORT SCANNER")
    print(f"{'='*45}{RESET}")

    target = input(f"{YELLOW}  Enter target IP: {RESET}").strip()

    # Validate input
    try:
        socket.inet_aton(target)
    except socket.error:
        print(f"{RED}  Invalid IP address{RESET}")
        return

    print(f"\n{CYAN}  Scanning: {target}")
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}\n")

    open_ports = []

    for port, service in COMMON_PORTS.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"{GREEN}  [OPEN]   Port {port:<6} {service}{RESET}")
                open_ports.append((port, service))
            else:
                print(f"{RED}  [CLOSED] Port {port:<6} {service}{RESET}")
            sock.close()

        except KeyboardInterrupt:
            print(f"\n{YELLOW}  Scan interrupted by user{RESET}")
            break
        except Exception as e:
            print(f"{RED}  Error on port {port}: {e}{RESET}")

    # Network Port Scanner Summary
    print(f"\n{CYAN}{'='*45}")
    print(f"  SCAN COMPLETE")
    print(f"  Open ports found: {len(open_ports)}")
    print(f"{'='*45}{RESET}")
    print(f"{YELLOW}  Results:{RESET}")
    for port, service in open_ports:
        print(f"  Port {port:<6} {service}")

    # Network Port Scanner - Save results
    save = input(f"\n{YELLOW}  Save results? (y/n): {RESET}")
    if save.lower() == "y":
        reports_dir = ensure_reports_dir()
        safe_target = target.replace("/", "_").replace(":", "_")
        filename = os.path.join(
            reports_dir,
            f"pawrecon_scan_{safe_target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"PAW RECON - Network Scan Results\n")
            f.write(f"Target: {target}\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write(f"{'='*40}\n")
            for port, service in open_ports:
                f.write(f"OPEN: Port {port} - {service}\n")
        print(f"{GREEN}  Saved to: {filename}{RESET}")


# Subdomain Enumerator function


def subdomain_enum():
    print(f"\n{CYAN}{'='*45}")
    print(f"         SUBDOMAIN ENUMERATOR")
    print(f"{'='*45}{RESET}")

    domain = input(f"{YELLOW}  Enter target domain (e.g. google.com): {RESET}").strip()

    print(f"\n{CYAN}  Target: {domain}")
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Testing {len(SUBDOMAINS)} subdomains...{RESET}\n")

    found = []

    for sub in SUBDOMAINS:
        url = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(url)
            print(f"{GREEN}  [FOUND]  {url:<40} {ip}{RESET}")
            found.append((url, ip))
        except socket.gaierror:
            print(f"{RED}  [MISS]   {url}{RESET}")
        except KeyboardInterrupt:
            print(f"\n{YELLOW}  Scan interrupted{RESET}")
            break

    # Subdomain Enumerator Summary
    print(f"\n{CYAN}{'='*45}")
    print(f"  ENUMERATION COMPLETE")
    print(f"  Subdomains found: {len(found)}")
    print(f"{'='*45}{RESET}")
    print(f"{YELLOW}  Results:{RESET}")
    for url, ip in found:
        print(f"  {url:<40} {ip}")

    # Subdomain Enumerator - Save results
    if found:
        save = input(f"\n{YELLOW}  Save results? (y/n): {RESET}")
        if save.lower() == "y":
            reports_dir = ensure_reports_dir()
            safe_domain = domain.replace("/", "_").replace(":", "_")
            filename = os.path.join(
                reports_dir,
                f"pawrecon_subs_{safe_domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            )
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"PAW RECON - Subdomain Enumeration\n")
                f.write(f"Target: {domain}\n")
                f.write(f"Date: {datetime.now()}\n")
                f.write(f"{'='*40}\n")
                for url, ip in found:
                    f.write(f"FOUND: {url} -> {ip}\n")
            print(f"{GREEN}  Saved to: {filename}{RESET}")


# Main execution block

# Update main loop

if __name__ == "__main__":
    banner()
    while True:
        choice = main_menu()
        if choice == "1":
            port_scanner()
        elif choice == "2":
            subdomain_enum()
        elif choice == "3":
            scan_info()
        elif choice == "4":
            print(f"{CYAN}Goodbye! Stay safe out there :3{RESET}")
            sys.exit()
        else:
            print(f"{RED}  Invalid option. Try again.{RESET}")
