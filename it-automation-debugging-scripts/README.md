<h1 align="center">Debugging a Cloud Web Server (ws01)</h1>

<p align="center">
  Linux Troubleshooting • systemd • Apache • Incident Debugging
</p>

<hr/>

This project is based on the Google IT Automation with Python lab
"Debugging a problem with a Cloud Deployment and Fix it".

## 🧩 Scenario
This role an IT administrator for a small startup. A cloud VM (ws01) serves the company website. One day, the site returns:

**HTTP 500 – Internal Server Error**

The task is to troubleshoot and restore service on ws01.

During the investigation the process will:
- Interpret HTTP status codes (4xx vs 5xx)
- Check web server status using `systemctl`
- Inspect port usage with `netstat`
- Identify rogue processes with `ps`
- Stop/disable a misconfigured `systemd` service
- Restart Apache (`apache2`) and verify recovery

This folder is a portfolio version of that troubleshooting exercise.

## 🔍 High-Level Findings
- `apache2` was failed and could not bind to port **80**
- `netstat` showed port **80** already in use by a `python3` process
- `ps` revealed `/usr/local/bin/jimmytest.py` was listening on port 80
- A `systemd` unit (`jimmytest.service`) was configured to keep restarting the test script

Because of this:
- Apache could not start (**Address already in use**)
- The website returned HTTP 500 errors

## 🧪 What This Project Demonstrates
Practical Linux service debugging using:
- `systemctl status`
- `journalctl`
- `netstat -nlp`
- `ps -ax | grep ...`

Key skills:
- Understanding port conflicts (multiple processes trying to use port 80)
- Working with `systemd` services (stop/disable misconfigured services)
- Restoring a production web service (Apache) with minimal downtime

## 📂 Project Files
- **README.md** — Overview, scenario, and key learning points (this file)
- **ws01_debug_playbook.sh** — Commented Bash playbook with diagnostic + remediation commands
- **ws01_debug_report.md** — Short incident-style report (symptoms, timeline, root cause, fix, prevention)

These files are meant to show how the system think and work when debugging live systems.

## ▶️ Portfolio Narrative
Portfolio Summary:

> Investigated and resolved an HTTP 500 issue on a cloud-hosted Apache web server by tracing a port conflict on 0.0.0.0:80 to a developer test script (jimmytest.py) managed by systemd. Used systemctl, netstat, and ps to identify the rogue service, disabled it, and successfully restarted Apache, restoring the production website.
