
#!/usr/bin/env python3
"""reports.py

Generates a simple PDF report using ReportLab.
"""

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter


def generate_report(output_path: str, title: str, body: str) -> None:
    """Generate a PDF report.

    Args:
        output_path: Where to save the PDF (e.g., '/tmp/sales_report.pdf').
        title: Title of the report.
        body: Main text (can be multi-line).
    """
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(output_path, pagesize=letter)

    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(body.replace("\n", "<br/>"), styles["BodyText"])

    elements = [report_title, Spacer(1, 20), report_body]
    report.build(elements)
