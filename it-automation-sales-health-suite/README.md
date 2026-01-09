
# google-it-automation-sales-health-suite

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![ReportLab](https://img.shields.io/badge/PDF-ReportLab-lightgrey)
![Automation](https://img.shields.io/badge/Focus-Automation-success)

End-to-end automation & monitoring project based on the **Google IT Automation with Python Professional Certificate**.

This suite demonstrates real-world IT automation skills:
- Summarizing and categorizing sales data
- Generating PDF reports using Python (ReportLab)
- Automatically emailing reports to stakeholders
- Monitoring system health and sending alerts (CPU, disk, memory, DNS)

It pairs nicely with the classic Google lab *“Automating updation of catalog information”* and can be presented as **Project 2 – Automation & Monitoring** in your Google portfolio.

---

## 📂 Project Structure

```text
google-it-automation-sales-health-suite/
├─ sales_summary.py          # Summarize sales by category
├─ reports.py                # PDF report generation
├─ emails.py                 # Email generation & sending utilities
├─ report_email.py           # Orchestrates summary -> PDF -> email
├─ health_check.py           # System health monitoring + email alerts
├─ sales.csv                 # Sample sales dataset
├─ sales_summary_output.txt  # Example output (optional to generate)
├─ banner.png                # GitHub project banner
└─ README.md                 # This file
```

---

## 🔧 Features

### 1. Sales Data Processing (`sales_summary.py`)
- Reads `sales.csv`
- Groups sales by **category**
- Calculates total quantity & total revenue per category
- Outputs a multi-line summary suitable for console, PDF, or email

### 2. PDF Report Generation (`reports.py`)
- Uses **ReportLab** to generate a formatted PDF report
- Title example: `Sales Summary Report - 2025-11-18`
- Default output path: `/tmp/sales_report.pdf`

### 3. Automated Emailing (`emails.py` + `report_email.py`)
- `report_email.py`:
  1. Summarizes sales
  2. Generates a PDF report
  3. Emails the PDF to the configured recipient

Default email configuration (lab-style):
- From: `automation@example.com`
- To: `student@example.com`
- Subject: `Automated Sales Report`

### 4. System Health Monitoring (`health_check.py`)
- Checks:
  - CPU usage > 80%
  - Available disk space < 20%
  - Available memory < 100MB
  - `localhost` not resolving to `127.0.0.1`
- On any failure, sends an alert email with a clear subject and message.

---

## ▶️ How to Run

1. **Summarize sales**

   ```bash
   python3 sales_summary.py
   ```

2. **Generate PDF & email it**

   ```bash
   python3 report_email.py
   ```

3. **Run system health check**

   ```bash
   python3 health_check.py
   ```

4. **Automate health checks with cron (Linux)**

   ```bash
   crontab -e
   # Add:
   * * * * * /usr/bin/python3 /full/path/to/health_check.py
   ```

---

## 📦 Requirements

- Python 3.8+
- Libraries:
  ```bash
  pip install reportlab psutil
  ```
- SMTP server (for example, `localhost` in a Google lab environment)

---

## 🧠 Project Story (Portfolio Narrative)

As part of my learning journey with the **Google IT Automation with Python** program, I wanted to go beyond isolated lab tasks and build a small, cohesive automation suite that looks and feels like something used by an IT team in production.

I started with a simple requirement: **summarize sales data and keep stakeholders informed automatically**. From there, I broke the work into four parts:

1. **Data processing** – I wrote `sales_summary.py` to read a CSV file and aggregate sales by category, computing total quantities and revenues. This reinforced working with `csv.DictReader`, dictionaries, and basic data analysis patterns in Python.

2. **Report generation** – Using `ReportLab`, I built `reports.py` to convert the text summary into a clean PDF report. This mirrors real IT workflows where teams generate daily/weekly PDFs for management.

3. **Email automation** – With `emails.py` and `report_email.py`, I automated distribution of the report. The script now runs end-to-end: read data → build summary → generate PDF → email it. This is conceptually similar to the Google fruit-store lab where uploaded data is confirmed via a report back to the supplier.

4. **System health monitoring** – Inspired by the `health_check.py` lab, I extended the suite with continuous monitoring for CPU, disk, memory, and DNS resolution. When something goes wrong, the script sends a clear, actionable alert email. Combined with cron, this becomes a lightweight monitoring agent.

Together, these scripts demonstrate how Python automation can:
- Reduce repetitive manual tasks
- Create reliable reporting pipelines
- Improve observability and proactive incident response
- Tie multiple responsibilities (data, reporting, email, monitoring) into one cohesive solution

This project represents how I would approach automation in a real IT environment: start small, break the problem into clear components, then stitch them together into a dependable workflow.

---

## 🖼 GitHub Banner

A simple banner image is included as `banner.png`. To use it on GitHub:

1. Commit `banner.png` to the root of the repository.
2. In your GitHub repo, go to **Settings → General → Social preview**.
3. Upload `banner.png` as the social preview image.

You can also redesign this banner in tools like Canva or Figma using the same text:
**google-it-automation-sales-health-suite – Python Automation & System Health**
