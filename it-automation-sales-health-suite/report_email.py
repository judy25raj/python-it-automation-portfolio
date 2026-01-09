
#!/usr/bin/env python3
"""report_email.py

Summarizes sales data, generates a PDF report, and emails it.
"""

from datetime import datetime

from sales_summary import process_sales_data
from reports import generate_report
import emails


def main():
    # 1) Summarize sales data
    csv_path = "sales.csv"
    summary_text = process_sales_data(csv_path)

    # 2) Generate PDF
    today = datetime.today().strftime("%Y-%m-%d")
    title = f"Sales Summary Report - {today}"
    pdf_path = "/tmp/sales_report.pdf"
    generate_report(pdf_path, title, summary_text)

    # 3) Email the PDF
    sender = "automation@example.com"
    recipient = "student@example.com"  # change for your environment
    subject = "Automated Sales Report"
    body = (
        "Please find attached the latest sales summary report.\n\n"
        "This report was generated automatically."
    )

    message = emails.generate_email(
        sender=sender,
        recipient=recipient,
        subject=subject,
        body=body,
        attachment_path=pdf_path,
    )
    emails.send_email(message)
    print("Sales report emailed successfully.")


if __name__ == "__main__":
    main()
