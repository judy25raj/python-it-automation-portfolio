# Sales Health Suite – Automation & Monitoring  
*(Google IT Automation with Python)*

End-to-end automation & monitoring suite aligned with the **Google IT Automation with Python Professional Certificate**.

This project demonstrates practical, production-style automation patterns:
- Summarizing and categorizing sales data
- Generating PDF reports with **ReportLab**
- Emailing reports to stakeholders
- Monitoring system health (CPU, disk, memory, DNS) and sending alerts

---

## 🔧 Features

### 1) Sales Data Processing (`sales_summary.py`)
- Reads `sales.csv`
- Groups sales by category
- Calculates total quantity & total revenue per category
- Outputs a multi-line summary suitable for console, PDF, or email

### 2) PDF Report Generation (`reports.py`)
- Generates a formatted PDF report using **ReportLab**
- Example title: *Sales Summary Report – YYYY-MM-DD*
- Default output path: `/tmp/sales_report.pdf`

### 3) Automated Email Distribution (`emails.py` + `report_email.py`)
`report_email.py` orchestrates:
1. Summarize sales
2. Generate PDF report
3. Email the PDF to the configured recipient

Default lab-style configuration:
- From: `automation@example.com`
- To: `student@example.com`
- Subject: `Automated Sales Report`

### 4) System Health Monitoring (`health_check.py`)
Checks:
- CPU usage > 80%
- Available disk space < 20%
- Available memory < 100 MB
- `localhost` not resolving to `127.0.0.1`

On any failure, sends an alert email with a clear subject and message.

---

## ▶️ Quick Start

```bash
pip install reportlab psutil

python3 sales_summary.py
python3 report_email.py
python3 health_check.py
```

---

## 📂 Project Structure

```
it-automation-sales-health-suite/
├── sales_summary.py          # Summarize sales by category
├── reports.py                # PDF report generation
├── emails.py                 # Email utilities
├── report_email.py           # Orchestrates summary -> PDF -> email
├── health_check.py           # System health monitoring + email alerts
├── sales.csv                 # Sample sales dataset
├── sales_summary_output.txt  # Example output (optional to generate)
├── banner.png                # GitHub project banner
└── README.md                 # This file
```

---

## 📦 Requirements
- Python 3.8+
- Libraries:
  ```bash
  pip install reportlab psutil
  ```
- SMTP server (localhost in Google lab environments, or your org SMTP relay)

> Note: In some environments, sending email may require configuring SMTP credentials or using an approved relay.

---

## ⏰ Automate Health Checks with cron (Linux)

```bash
crontab -e
# Add (example: run every minute):
* * * * * /usr/bin/python3 /full/path/to/health_check.py
```

This turns the script into a lightweight monitoring agent.

---

## 🧠 Project Story (Portfolio Narrative)

<details>
<summary><strong>Click to expand</strong></summary>

As part of my learning journey with the Google IT Automation with Python program, I wanted to go beyond isolated lab tasks and build a cohesive automation suite that looks and feels like something used by an IT operations team.

I started with a simple requirement: summarize sales data and keep stakeholders informed automatically. From there, I split the work into four parts:

**Data processing** – `sales_summary.py` reads a CSV dataset and aggregates sales by category, computing total quantities and revenues. This reinforced using `csv.DictReader`, dictionaries, and reliable aggregation patterns.

**Report generation** – using ReportLab in `reports.py`, I convert a text summary into a clean PDF report. This mirrors real IT workflows where teams generate daily/weekly PDFs for management.

**Email automation** – `emails.py` and `report_email.py` automate distribution of the report. The pipeline now runs end-to-end: read data → build summary → generate PDF → email it.

**System health monitoring** – inspired by common health-check labs, `health_check.py` continuously monitors CPU, disk, memory, and DNS resolution. When something goes wrong, the script sends a clear, actionable alert email. With cron, this becomes a lightweight monitoring agent.

Together, these scripts demonstrate how Python automation can:
- Reduce repetitive manual tasks
- Create reliable reporting pipelines
- Improve observability and proactive incident response
- Tie data, reporting, email, and monitoring into one dependable workflow

This project reflects how I approach automation in a real IT environment: start small, design modular components, and stitch them into a robust, repeatable solution.

</details>

---

## 🖼 GitHub Banner
A banner image is included as `banner.png`.

To use it on GitHub:
1. Commit `banner.png`
2. Go to **Settings → General → Social preview**
3. Upload `banner.png`

Suggested banner text:
**Sales Health Suite – Python Automation & System Monitoring**
