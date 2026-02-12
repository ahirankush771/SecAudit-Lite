# SecAudit-Lite 🔐

Tool created by **Ankush Kumar**  
Diploma CSE Student | Cybersecurity Learner  

SecAudit-Lite is a lightweight Linux security hardening checker built for learning and basic system auditing purposes.  
It is designed mainly for Kali Linux and Debian-based systems, but it can also run in Termux (with limited checks).

---

## 📌 What This Tool Does

SecAudit-Lite performs basic system security audits such as:

- SSH configuration analysis
- Root login status check
- Password authentication check
- Firewall (UFW) status check
- Clean formatted terminal output using the Rich library

This tool helps identify simple security misconfigurations in Linux environments.

---

## ⚙️ System Requirements

- Python 3.x
- Internet connection (for installing dependencies)
- Root (sudo) access for full audit (recommended for Kali/Linux)

Supported Environments:
- Kali Linux ✅ (Recommended)
- Ubuntu / Debian ✅
- Termux ⚠ (Limited functionality)

---

# 🚀 Installation Guide (Kali Linux / Ubuntu)

## Step 1: Update System (Recommended)
sudo apt update
## Step 2: Install Git and Python (If Not Installed)
sudo apt install git python3 python3-pip -y
## Step 3: Clone the Repository
git clone https://github.com/ahiraankush771/SecAudit-Lite.git�
## Step 4: Move into Project Directory
cd SecAudit-Lite
## Step 5: Install Required Dependencies
pip install -r requirements.txt
## Step 6: Run the Tool (Recommended with sudo)
sudo python3 secaudit.py

---

# 📱 Installation Guide (Termux)

Note: Termux has limited Linux system access, so some checks may show as "not installed".

## Step 1: Update Termux
pkg update
## Step 2: Install Required Packages
pkg install git python -y
## Step 3: Clone the Repository
git clone https://github.com/ahiraankush771/SecAudit-Lite.git�
## Step 4: Move into Directory
cd SecAudit-Lite
## Step 5: Install Dependencies
pip install -r requirements.txt
## Step 6: Run the Tool
python3 secaudit.py
---

# 🧠 About the Developer

Hi, I’m **Ankush Kumar**, a Diploma CSE student passionate about:

- Cybersecurity
- Ethical Hacking
- Linux System Security
- Building practical security tools

I am currently focused on developing hands-on cybersecurity projects to strengthen my real-world technical skills.

This tool is part of my practical learning journey in defensive security and system hardening.

---

# ⚠ Disclaimer

This tool is created strictly for educational and defensive security purposes only.  
Do not use it on systems without proper authorization.

---

# 📌 Future Improvements

- Open ports detection
- Sudo user audit
- World-writable file detection
- Risk scoring system
- JSON report export
- Advanced Linux hardening checks

---

⭐ If you find this project useful, consider giving it a star.
