# RootPhantom# 👻 RootPhantom - The Silent Operator

> *Moves in silence, hits like a ghost.*  
> A stealthy, root-level Linux-based hacking toolkit for ethical hackers and pentesters.

![RootPhantom Banner](https://img.shields.io/badge/status-active-success?style=for-the-badge&logo=linux&logoColor=white)
![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/flask-2.3-lightgrey?style=flat-square&logo=flask)

---

## 🧠 Overview

**RootPhantom** is a modular, web-powered hacking toolkit made for educational penetration testing on Linux systems. With a Flask backend and a sleek HTML frontend, it simulates real-world hacking tools like port scanners, reverse shells, and DDoS modules — all in one dashboard.

---

## 🧰 Features

- 🔍 **Port Scanner** – Scan open ports on any IP address.
- 📡 **IP Tracker** – Locate and fetch metadata about any IP.
- 📲 **Phone Hijack (Simulated)** – Mockup tool for phishing or social engineering scenarios.
- 📶 **WiFi Cracker (Placeholder)** – Setup for future aircrack-ng integration.
- ⚠️ **Exploit Launcher (Simulated)** – Simulated shell exploit to test payload deployment.
- 💻 **Web Dashboard** – A clean, hacker-styled UI built with Flask + HTML/CSS.
-  **Modular Design** – Easily plug in your own tools.

---

##  Installation

```bash
git clone https://github.com/yourusername/RootPhantom.git
cd RootPhantom
pip install -r requirements.txt
python3 app.py
Then, open your browser at:
http://127.0.0.1:5000

 Directory Structure
php
Copy
Edit
RootPhantom/
├── app.py                  # Flask main server
├── templates/
│   └── index.html          # Dashboard UI
├── static/
│   └── style.css           # Styling for the UI
├── modules/
│   ├── port_scanner.py     # Port scanner logic
│   ├── net_info.py         # IP and network info tool
│   └── exploit_demo.py     # Demo payload simulator
└── assets/
    └── banner.txt          # Terminal ASCII banner
 Screenshots
Add these after running the app locally:

 Main dashboard

 Port scanner results

 IP tracking module

 Reverse shell demo (coming soon!)

 Disclaimer
 For educational and ethical hacking only!

This toolkit is intended only for use in controlled environments or with explicit permission. Misuse of RootPhantom may result in legal consequences. You are fully responsible for your actions.

 Future Plans
Reverse shell payload generator (bash, python, nc)

Auth system for dashboard login

Integration with nmap, hydra, aircrack-ng

Dark-mode terminal emulator in browser





 License
MIT License — use it, modify it, learn from it. Just don’t be evil. 

yaml
Copy
Edit

---
