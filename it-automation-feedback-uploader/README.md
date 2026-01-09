# Google Project 4 – Processing Text Files and Uploading to a Web Service

This project is based on the **Google IT Automation with Python** lab  
**"Processing Text Files with Python Dictionaries and Uploading to a Running Web Service"**.

## 🧩 Scenario

You work for a company that sells second-hand cars. The company collects customer
feedback as plain text files, one review per `.txt` file. Each file contains:

1. Title  
2. Customer name  
3. Date  
4. Feedback text (can span multiple lines)

Management wants these reviews to appear on the company website, which is powered by
a Django web service and exposes a `/feedback` REST endpoint.

Your job is to **automate** the upload of all feedback files using Python.

---

## ✅ What This Project Demonstrates

- Using the **`os` module** to iterate over files in a directory (`os.listdir`)
- Parsing text files into **Python dictionaries**
- Using the **`requests`** library to send HTTP **POST** requests to a REST endpoint
- Handling success and error responses from a running web service

This is a direct, portfolio-ready implementation of Google’s “Project 4” lab.

---

## 📂 Project Structure

```text
google-it-automation-feedback-uploader/
├─ run.py          # Main script: process text files & upload as feedback
├─ feedback/
│   ├─ 001.txt     # Sample feedback 1
│   ├─ 005.txt     # Sample feedback 2
│   └─ 007.txt     # Sample feedback 3
└─ README.md       # This file
```

---

## ▶️ How It Works

### Input Format (each .txt file)

```text
<title>
<name>
<date>
<feedback text (may span multiple lines)>
```

Example:

```text
Good deal for a 2015 RAV4
Anonymous
2018-04-17
Called them to look for a second-hand RAV4 and they were very patient helping me compare options...
```

### `run.py` Logic

1. Reads all `.txt` files in the `feedback/` directory.
2. For each file:
   - Extracts:
     - `title`  → line 1  
     - `name`   → line 2  
     - `date`   → line 3  
     - `feedback` → all remaining lines joined into a single string
   - Builds a dictionary:
     ```python
     {
       "title": "...",
       "name": "...",
       "date": "...",
       "feedback": "..."
     }
     ```
3. Sends each dictionary as form data in an HTTP `POST` request to the configured endpoint:
   ```python
   requests.post(url, data=feedback_dict)
   ```
4. Prints the HTTP status code and basic success/error messages.

---

## ⚙️ Configuration

By default, the script uses:

- Feedback directory: `feedback/`
- Endpoint URL: `http://localhost/feedback/`

You can override these using environment variables:

```bash
export FEEDBACK_DIR="feedback"
export FEEDBACK_ENDPOINT="http://<corpweb-external-IP>/feedback/"
```

In the original Google lab, the endpoint looked like:

```text
http://<corpweb-external-IP>/feedback
```

---

## ▶️ How to Run

1. Install `requests` if needed:
   ```bash
   pip install requests
   ```

2. Run the script:
   ```bash
   python3 run.py
   ```

3. Check your Django/REST endpoint:
   - In the lab: refresh the corpweb external IP page to see the feedback
   - Locally: inspect logs or responses from your own test endpoint

---

## 🧠 Project Story (Portfolio Narrative)

This project demonstrates how to bridge **raw text data** and a **live web service**:

- I started from a collection of unstructured `.txt` files storing customer reviews.
- Using `os.listdir` and simple file I/O, I transformed each file into a structured
  Python dictionary with `title`, `name`, `date`, and `feedback`.
- I then used the `requests` library to POST each dictionary to a Django REST
  endpoint, automating what would otherwise be a tedious, manual data entry task.
- The script includes basic error handling and status-code checks so failures can be
  detected quickly.

In a real environment, this pattern can be extended to:
- Pull data from other sources (log files, CSV exports, etc.),
- Push data into ticketing systems, CRMs, or internal APIs,
- And schedule the script via `cron` to keep websites or dashboards automatically updated.

You can describe this project in your portfolio as:

> "Automated a pipeline that converts raw customer feedback text files into structured
> JSON-like dictionaries and uploads them to a Django-based web service using HTTP
> POST requests, replacing manual data entry with a repeatable Python workflow."
