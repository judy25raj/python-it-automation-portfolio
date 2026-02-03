<h1 align="center">Processing Text Files and Uploading to a Web Service</h1>

<p align="center">
  Python • Requests • File Processing • REST Automation
</p>

<hr/>

This project is based on the Google IT Automation with Python lab
"Processing Text Files with Python Dictionaries and Uploading to a Running Web Service".

## 🧩 Scenario
You work for a company that sells second-hand cars. The company collects customer feedback as plain text files, one review per .txt file. Each file contains:

- Title
- Customer name
- Date
- Feedback text (can span multiple lines)

Management wants these reviews to appear on the company website, which is powered by a Django web service and exposes a /feedback REST endpoint.

Your job is to automate the upload of all feedback files using Python.

## ✅ What This Project Demonstrates
- Iterating files with os.listdir
- Parsing text into Python dictionaries
- Sending HTTP POST requests with requests
- Handling responses from a REST service

## 📂 Project Structure
```
google-it-automation-feedback-uploader/
├─ run.py          # Main script: process text files & upload as feedback
├─ feedback/
│   ├─ 001.txt
│   ├─ 005.txt
│   └─ 007.txt
└─ README.md
```

## ▶️ How It Works
**Input format (each .txt file):**
```
<title>
<name>
<date>
<feedback text>
```

**run.py logic:**
- Reads all files in feedback/
- Extracts fields
- Builds a dictionary
- Sends POST request to endpoint
- Prints status

## ⚙️ Configuration
Defaults:
- FEEDBACK_DIR = "feedback"
- FEEDBACK_ENDPOINT = "http://localhost/feedback/"

Override with:
```
export FEEDBACK_DIR="feedback"
export FEEDBACK_ENDPOINT="http://<corpweb-external-IP>/feedback/"
```

## ▶️ How to Run
Install requests:
```
pip install requests
```

Run:
```
python3 run.py
```

## 🧠 Project Story
Automated conversion of raw customer feedback text into structured dictionaries and uploaded them to a Django REST endpoint, replacing manual data entry with a repeatable Python workflow.
