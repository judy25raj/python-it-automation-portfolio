# Google Project 6 – Debugging a Cloud Web Server (ws01)

This project is based on the **Google IT Automation with Python** lab  
**"Debugging a problem with a Cloud Deployment and Fix it"**.

## 🧩 Scenario

You're an IT administrator for a small startup. A cloud VM `ws01` serves the
company website. One day, the site returns:

> **HTTP 500 – Internal Server Error**

Your task is to **troubleshoot and restore service** on `ws01`.

During the investigation you will:

- Interpret HTTP status codes (4xx vs 5xx)
- Check web server status using `systemctl`
- Inspect port usage with `netstat`
- Identify rogue processes with `ps`
- Stop/disable a misconfigured systemd service
- Restart Apache (`apache2`) and verify recovery

This folder is a **portfolio version** of that troubleshooting exercise.

---

## 🔍 High-Level Findings

- `apache2` was **failed** and could not bind to port **80**.
- `netstat` showed port 80 already in use by a `python3` process.
- `ps` revealed that `/usr/local/bin/jimmytest.py` was listening on port 80.
- A `systemd` unit **`jimmytest.service`** was configured to keep restarting this test script.
- Because of this:
  - Apache could not start (`Address already in use`)
  - The website returned HTTP 500 errors.

---

## 🧪 What This Project Demonstrates

- Practical Linux **service debugging** using:
  - `systemctl status`
  - `journalctl`
  - `netstat -nlp`
  - `ps -ax | grep ...`
- Understanding of **port conflicts** (multiple processes trying to use port 80)
- Working with **systemd services**:
  - Stopping and disabling a problematic service
- Restoring a production web service (Apache) with minimal downtime.

---

## 📂 Project Files

- `README.md`  
  Overview, scenario, and key learning points (this file).

- `ws01_debug_playbook.sh`  
  A **commented Bash playbook** that documents the main diagnostic and
  remediation commands you would run on the VM.

- `ws01_debug_report.md`  
  A short **incident-style report**:
  - Symptoms
  - Timeline
  - Root cause
  - Fix
  - Prevention

These files are meant to show **how you think and work** when debugging live systems.

---

## ▶️ How to Use This in Your Portfolio

You can describe this project as:

> *"Investigated and resolved an HTTP 500 issue on a cloud-hosted Apache web
> server by tracing a port conflict on 0.0.0.0:80 to a developer test script
> (`jimmytest.py`) managed by systemd. Used `systemctl`, `netstat`, and `ps`
> to identify the rogue service, disabled it, and successfully restarted
> Apache, restoring the production website."*

On GitHub, you can:

- Put these files in a repo called for example:  
  `google-it-automation-ws01-debug`
- Add this project to a "Google IT Automation – Cloud & Troubleshooting"
  section in your README or portfolio site.
