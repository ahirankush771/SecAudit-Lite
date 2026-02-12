#!/usr/bin/env python3

import os
import subprocess
import psutil
from rich.console import Console
from rich.table import Table

console = Console()

def run_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        return result.decode().strip()
    except:
        return None

def check_ssh_config():
    ssh_file = "/etc/ssh/sshd_config"
    findings = []

    if not os.path.exists(ssh_file):
        return ["SSH not installed"]

    with open(ssh_file, "r") as f:
        data = f.read()

    if "PermitRootLogin yes" in data:
        findings.append("Root login is ENABLED")
    else:
        findings.append("Root login is disabled")

    if "PasswordAuthentication yes" in data:
        findings.append("Password authentication enabled")
    else:
        findings.append("Password authentication disabled")

    return findings

def check_firewall():
    ufw_status = run_command("ufw status")
    if ufw_status:
        if "inactive" in ufw_status.lower():
            return "Firewall inactive"
        else:
            return "Firewall active"
    return "UFW not installed"

def main():
    console.print("SecAudit-Lite - Linux Hardening Scanner")

    table = Table(title="Security Audit Report")
    table.add_column("Check")
    table.add_column("Result")

    ssh_results = check_ssh_config()
    for item in ssh_results:
        table.add_row("SSH Config", item)

    table.add_row("Firewall", check_firewall())

    console.print(table)

if __name__ == "__main__":
    main()
