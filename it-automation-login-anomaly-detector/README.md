<h1 align="center">Login Anomaly Detector</h1>

<p align="center">
  Python Security Automation • Anomaly Detection • CLI Tool
</p>

<p align="center">
  <a href="https://github.com/judy25raj/python-it-automation-portfolio">← Back to IT Automation Portfolio</a>
</p>

<hr/>

A Python security automation project completed as part of the Google IT Automation with Python Professional Certificate.

This tool analyzes user login activity and flags potentially suspicious behavior when the current day's login count is significantly higher than the historical average. The project started from an incomplete script and was enhanced using Generative AI and the TCREI prompting framework to become a fully working automation solution.

## Purpose of the Activity
This exercise demonstrates how Generative AI can help IT professionals by:

- Debugging Python scripts – Identifying missing logic, edge cases, and incomplete behavior.
- Identifying risks and anomalies – Using ratio-based detection to highlight suspicious login spikes.
- Optimizing logic – Refactoring code for clarity, scalability, and robustness.
- Reducing manual investigation time – Automating login monitoring instead of manually reviewing logs.
- Applying the TCREI framework to improve AI-assisted development.

## Features
- Calculates ratio: current_day_logins / average_day_logins
- Configurable anomaly threshold (default: 3.0x)
- Alerts when activity is considered potentially suspicious
- Supports:
  - Single-user analysis via CLI
  - Batch analysis from a CSV file
- Input validation and warnings for invalid data
- Pure Python, no external dependencies

## Project Structure
```
login-anomaly-detector/
├─ analyze_logins.py       # main script (function + CLI)
├─ sample_logins.csv       # example data
└─ results.txt             # example run output
```

## How to Run
### 1. Analyze a single user
```
python analyze_logins.py --username ejones --current 45 --average 10 --threshold 3.0
```

### 2. Analyze multiple users from CSV
```
python analyze_logins.py --csv sample_logins.csv --threshold 3.0
```

## Example CSV (sample_logins.csv)
```
username,current_day_logins,average_day_logins
ejones,45,10
asmith,12,11
bgarcia,5,6
tlee,30,8
mnguyen,3,3
```

## Example Output
See results.txt for a captured example run.
