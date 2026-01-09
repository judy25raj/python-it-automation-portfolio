#!/usr/bin/env python3
"""run.py

Google Project 4 – Processing Text Files with Python Dictionaries
and Uploading to a Running Web Service.

Scenario:
- You work for a company that sells second-hand cars.
- Customer feedback is stored as .txt files in a directory.
- Each text file has 4 lines: title, name, date, feedback.
- You need to:
    * Read all .txt feedback files from a directory
    * Convert each file into a Python dictionary
    * Upload each dictionary to a Django-based web service via HTTP POST
"""

import os
import requests


def load_feedback_from_dir(directory: str):
    """Read all .txt files in a directory and yield feedback dictionaries.

    Each file is expected to have the following format:
        line 1: title
        line 2: name
        line 3: date
        line 4+: feedback text (can be multiple lines)

    Returns:
        Generator of dicts with keys: title, name, date, feedback
    """"
    for filename in os.listdir(directory):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]

        if len(lines) < 4:
            # Skip files that don't meet the expected format
            print(f"[WARN] Skipping {filename}: not enough lines")
            continue

        title = lines[0]
        name = lines[1]
        date = lines[2]
        feedback = " ".join(lines[3:])  # join remaining lines as one feedback string

        feedback_dict = {
            "title": title,
            "name": name,
            "date": date,
            "feedback": feedback,
        }
        yield feedback_dict


def main():
    # In the Google lab, the feedback files live in /data/feedback.
    # For this standalone project, we use a local 'feedback' directory by default.
    feedback_dir = os.environ.get("FEEDBACK_DIR", "feedback")

    # In the lab, this is http://<corpweb-external-IP>/feedback
    # For portability, use an environment variable, with a placeholder default.
    url = os.environ.get("FEEDBACK_ENDPOINT", "http://localhost/feedback/")

    if not os.path.isdir(feedback_dir):
        print(f"[ERROR] Feedback directory not found: {feedback_dir}")
        return

    for feedback in load_feedback_from_dir(feedback_dir):
        try:
            response = requests.post(url, data=feedback)
            if response.status_code == 201:
                print(f"[OK] Uploaded feedback: {feedback['title']}")
            else:
                print(
                    f"[WARN] Failed to upload '{feedback['title']}'. "
                    f"Status code: {response.status_code}, Response: {response.text}"
                )
        except Exception as e:
            print(f"[ERROR] Exception while uploading '{feedback['title']}': {e}")


if __name__ == "__main__":
    main()
