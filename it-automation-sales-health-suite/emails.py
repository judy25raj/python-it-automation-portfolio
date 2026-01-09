
#!/usr/bin/env python3
"""emails.py

Helper functions to create and send emails, with or without attachments.
"""

import os
import mimetypes
import smtplib
from email.message import EmailMessage


def generate_email(sender: str,
                   recipient: str,
                   subject: str,
                   body: str,
                   attachment_path: str = None) -> EmailMessage:
    """Create an EmailMessage object.

    If attachment_path is provided, attach that file to the email.
    """
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path:
        mime_type, _ = mimetypes.guess_type(attachment_path)
        if mime_type is None:
            mime_type = "application/octet-stream"
        maintype, subtype = mime_type.split("/", 1)

        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)

        message.add_attachment(file_data,
                               maintype=maintype,
                               subtype=subtype,
                               filename=file_name)
    return message


def send_email(message: EmailMessage, smtp_server: str = "localhost") -> None:
    """Send the email via the given SMTP server.

    In a lab environment, 'localhost' is often configured with an SMTP service.
    Adjust smtp_server as needed for your setup.
    """
    with smtplib.SMTP(smtp_server) as server:
        server.send_message(message)
