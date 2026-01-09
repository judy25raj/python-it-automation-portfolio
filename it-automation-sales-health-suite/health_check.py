
#!/usr/bin/env python3
"""health_check.py

Checks system health and sends alert emails on failure:
- CPU usage over 80%
- Available disk space less than 20%
- Available memory less than 100MB
- 'localhost' hostname not resolving to 127.0.0.1
"""

import shutil
import psutil
import socket

import emails


def check_cpu(threshold: float = 80.0) -> bool:
    usage = psutil.cpu_percent(interval=1)
    return usage < threshold


def check_disk(threshold: float = 20.0, path: str = "/") -> bool:
    du = shutil.disk_usage(path)
    free_percent = du.free / du.total * 100
    return free_percent > threshold


def check_memory(min_available_mb: int = 100) -> bool:
    mem = psutil.virtual_memory()
    available_mb = mem.available / (1024 * 1024)
    return available_mb > min_available_mb


def check_localhost() -> bool:
    try:
        ip = socket.gethostbyname("localhost")
        return ip == "127.0.0.1"
    except socket.error:
        return False


def send_error(subject: str):
    sender = "automation@example.com"
    recipient = "student@example.com"
    body = "Please check your system and resolve the issue as soon as possible."

    message = emails.generate_email(
        sender=sender,
        recipient=recipient,
        subject=subject,
        body=body,
        attachment_path=None,
    )
    emails.send_email(message)


def main():
    if not check_cpu():
        send_error("Error - CPU usage is over 80%")
    if not check_disk():
        send_error("Error - Available disk space is less than 20%")
    if not check_memory():
        send_error("Error - Available memory is less than 100MB")
    if not check_localhost():
        send_error("Error - localhost cannot be resolved to 127.0.0.1")


if __name__ == "__main__":
    main()
