#!/usr/bin/env python3
"""emails.py

Helper functions to create and send emails with an attachment.
API compatible with the Google lab:
    generate(sender, recipient, subject, body, attachment_path)
    send(message)
"""

import email.message
import mimetypes
import os.path
import smtplib


def generate(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachment."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    if mime_type is None:
        mime_type = "application/octet-stream"
    maintype, mime_subtype = mime_type.split("/", 1)

    with open(attachment_path, "rb") as ap:
        message.add_attachment(
            ap.read(),
            maintype=maintype,
            subtype=mime_subtype,
            filename=attachment_filename,
        )

    return message


def send(message):
    """Sends the message to the configured SMTP server (localhost)."""
    mail_server = smtplib.SMTP("localhost")
    mail_server.send_message(message)
    mail_server.quit()
