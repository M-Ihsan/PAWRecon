<div align="center">

```
                                           ____   _    __        __  ____  _____ ____ ___  _   _ 
                                          |  _ \ / \   \ \      / / |  _ \| ____/ ___/ _ \| \ | |
                                          | |_) / _ \   \ \ /\ / /  | |_) |  _|| |  | | | |  \| |
                                          |  __/ ___ \   \ V  V /   |  _ <| |__| |__| |_| | |\  |
                                          |_| /_/   \_\   \_/\_/    |_| \_\_____\____\___/|_| \_|

____   _    __        __  ____  _____ ____ ___  _   _ 
|  _ \ / \   \ \      / / |  _ \| ____/ ___/ _ \| \ | |
| |_) / _ \   \ \ /\ / /  | |_) |  _|| |  | | | |  \| |
|  __/ ___ \   \ V  V /   |  _ <| |__| |__| |_| | |\  |
|_| /_/   \_\   \_/\_/    |_| \_\_____\____\___/|_| \_|
```


### 🐾 Penetration And Recon Workshop — Reconnaissance Toolkit 🐾

**Network Port Scanner + Subdomain Enumerator, built with pure Python — no third-party dependencies.**


[![Python](https://img.shields.io/badge/python-3.x-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![Made with](https://img.shields.io/badge/made%20with-%F0%9F%90%BE%20%2B%20%E2%98%95-orange.svg)]()

</div>

---

## 🐱 What is PAW RECON?

**PAW RECON** is a lightweight, menu-driven CLI recon tool for the early reconnaissance phase of a penetration test. It's built to be simple enough to read top-to-bottom, while still being genuinely useful for a first-pass look at a target's attack surface.

It does two things, and does them cleanly:

| 🐾 | Module | What it does |
|---|---|---|
| 1️⃣ | **Network Port Scanner** | Checks a target IP against 30+ commonly used ports (SSH, HTTP/S, FTP, SMB, databases, RDP, VNC, etc.) |
| 2️⃣ | **Subdomain Enumerator** | Resolves 50+ common subdomain prefixes (`admin`, `api`, `dev`, `staging`, `vpn`...) against a target domain via DNS |

> ⚠️ **Use responsibly.** PAW RECON is for authorized security testing and educational purposes only. Only scan systems and domains you own or have explicit permission to test.

---

## 🐾 Features

- 🎨 Interactive, color-coded terminal menu (ANSI escape codes — zero extra libraries)
- 🔍 TCP port scanner covering 30+ common ports with live OPEN/CLOSED output
- ✅ Input validation on target IPs before scanning starts
- 🌐 Subdomain enumerator with a curated 50+ entry wordlist
- 📊 Auto-generated summary at the end of every scan
- 💾 Optional save-to-file — results are written as timestamped reports in `Reports/`
- ⌨️ Graceful `Ctrl+C` handling mid-scan — no ugly crashes
- 🐍 100% Python standard library — nothing to `pip install`

---

## 🐈 Demo

```
  PAW> 1

==============================================
         NETWORK PORT SCANNER
==============================================
  Enter target IP: 192.168.1.10

  Scanning: 192.168.1.10
  Started: 2026-07-21 14:32:00

  [OPEN]   Port 22     SSH
  [CLOSED] Port 23     Telnet
  [OPEN]   Port 80     HTTP
  [OPEN]   Port 443    HTTPS
  ...

==============================================
  SCAN COMPLETE
  Open ports found: 3
==============================================
```

*(Add your own screenshots here — see [Screenshots](#-screenshots) below 🐾)*

---

## 🐾 Getting Started

### Requirements

- Python 3.x
- That's it. No pip installs, no virtual environments needed.

### Installation

```bash
git clone https://github.com/<your-username>/pawrecon.git
cd pawrecon
```

### Run it

```bash
python3 pawrecon.py
```

You'll land on the main menu:

```
==============================================
  Select an option:
  [1] Network Port Scanner
  [2] Subdomain Enumerator
  [3] About PAW RECON
  [4] Exit
==============================================
```

---

## 🐱 Usage

| Option | Action |
|---|---|
| `1` | Enter a target IPv4 address → scans 30+ common ports → shows OPEN/CLOSED results → optional save to `Reports/` |
| `2` | Enter a target domain (e.g. `example.com`) → checks 50+ subdomain prefixes → shows FOUND/MISS results → optional save to `Reports/` |
| `3` | Shows tool info: version, author, purpose |
| `4` | Exits the program |

Saved reports land in a local `Reports/` folder, named like:

```
Reports/pawrecon_scan_192.168.1.10_20260721_143200.txt
Reports/pawrecon_subs_example.com_20260721_144510.txt
```

---

## 🐾 Project Structure

```
pawrecon/
├── pawrecon.py       # main script — everything lives here
├── Reports/          # auto-created, holds saved scan/enum results
└── README.md
```

---

## 🐈‍⬛ How It Works

- **Port Scanner** — opens a TCP socket per port with a 1-second timeout and calls `connect_ex()`; a return of `0` means the port is open.
- **Subdomain Enumerator** — prefixes each wordlist entry onto the target domain and calls `socket.gethostbyname()`; a successful resolution means the subdomain is live.

---

## 🐾 Screenshots

> _Add your own terminal screenshots here before publishing:_

| Banner & Menu | Port Scan | Subdomain Enum |
|---|---|---|
| `![banner](docs/screenshot-menu.png)` | `![portscan](docs/screenshot-ports.png)` | `![subdomains](docs/screenshot-subs.png)` |

---

## 🐱 Roadmap

- [ ] Multithreaded scanning for speed
- [ ] Banner grabbing on open ports
- [ ] Certificate-transparency log lookups for deeper subdomain discovery
- [ ] JSON / CSV export options
- [ ] Custom port range / wordlist input

---

## 🐾 Disclaimer

PAW RECON is built for **educational purposes and authorized security testing only**. Scanning systems or domains without explicit permission may be illegal in your jurisdiction. The author is not responsible for misuse of this tool.

---

## 🐈 Author

**Muhammad Ihsan**
Built as part of a Penetration And Recon Workshop project.

---


<div align="center">

🐾 *made with curiosity, coffee, and a curious cat* 🐾

</div>
