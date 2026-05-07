#!/usr/bin/env python3
"""
Ebook Delivery Script for AI Automation Playbook
Sends all 8 chapters + README as email attachments to a buyer.

Usage:
    python deliver.py <email_address> <order_id>
    python deliver.py buyer@example.com ORDER-12345
"""

import smtplib
import os
import sys
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pathlib import Path

# ─── CONFIGURATION ───────────────────────────────────────────────────────────
# Ebook files directory
EBOOK_DIR = Path(__file__).parent / "AI_AUTOMATION_PLAYBOOK"

# Email settings (configure with your SMTP details)
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "your_email@gmail.com")
SMTP_PASS = os.environ.get("SMTP_PASS", "your_app_password")
FROM_NAME = "AI Automation Playbook"
FROM_EMAIL = SMTP_USER

# Email content
EMAIL_SUBJECT = "Your AI Automation Playbook is Here!"
EMAIL_BODY = """Hi there,

Thank you for purchasing the AI Automation Playbook!

Your order is confirmed. Attached to this email you'll find all 8 chapters of the playbook:

1. Chapter 1: The AI Revolution Is Already Here — Are You In?
2. Chapter 2: Building Your First AI Workforce
3. Chapter 3: Automating Content Creation at Scale
4. Chapter 4: Lead Generation on Autopilot
5. Chapter 5: Conversational Sales That Close While You Sleep
6. Chapter 6: Customer Support Without Hiring
7. Chapter 7: Analytics and Optimization
8. Chapter 8: Scaling Beyond Solo

Plus the README with setup instructions and resource links.

If you have any questions, just reply to this email.

To your automated success,
The AI Automation Playbook Team
"""

THANK_YOU_EMAIL_SUBJECT = "Thanks for Your Order — AI Automation Playbook"
THANK_YOU_EMAIL_BODY = """Hi there,

Thank you for purchasing the AI Automation Playbook!

Your order is confirmed and your download is on its way in a separate email.

If you don't receive the attachment email within a few minutes, please check your spam folder.

To your automated success,
The AI Automation Playbook Team
"""

# ─── CHAPTER FILES ────────────────────────────────────────────────────────────
CHAPTER_FILES = [
    "Chapter_01.md",
    "Chapter_02.md",
    "Chapter_03.md",
    "Chapter_04.md",
    "Chapter_05.md",
    "Chapter_06.md",
    "Chapter_07.md",
    "Chapter_08.md",
]

EXTRA_FILES = [
    "README.md",
]


def find_ebook_files():
    """Find all ebook files to attach."""
    files = []
    for fname in CHAPTER_FILES:
        fpath = EBOOK_DIR / fname
        if fpath.exists():
            files.append(fpath)
        else:
            print(f"WARNING: {fpath} not found, skipping")

    for fname in EXTRA_FILES:
        fpath = EBOOK_DIR / fname
        if fpath.exists():
            files.append(fpath)
        else:
            print(f"NOTE: {fpath} not found, skipping (optional)")

    return files


def build_email(to_email, order_id):
    """Build the delivery email with all attachments."""
    msg = MIMEMultipart()
    msg['From'] = f"{FROM_NAME} <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = f"{EMAIL_SUBJECT} [Order: {order_id}]"

    # Add body
    body_with_order = f"{EMAIL_BODY}\n\nOrder ID: {order_id}"
    msg.attach(MIMEText(body_with_order, 'plain'))

    # Attach files
    files = find_ebook_files()
    print(f"Found {len(files)} files to attach:")
    for f in files:
        print(f"  - {f.name}")

    for fpath in files:
        with open(fpath, 'rb') as f:
            part = MIMEApplication(f.read(), Name=fpath.name)
        part['Content-Disposition'] = f'attachment; filename="{fpath.name}"'
        msg.attach(part)

    return msg


def send_email(msg, to_email):
    """Send email via SMTP."""
    print(f"Connecting to {SMTP_HOST}:{SMTP_PORT}...")
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(FROM_EMAIL, [to_email], msg.as_string())
    print(f"Email sent to {to_email}")


def log_delivery(email, order_id, status):
    """Append delivery to a local log file."""
    log_path = Path(__file__).parent / "delivery_log.txt"
    import datetime
    timestamp = datetime.datetime.now().isoformat()
    with open(log_path, "a") as f:
        f.write(f"{timestamp} | {order_id} | {email} | {status}\n")
    print(f"Logged to {log_path}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python deliver.py <email_address> <order_id>")
        print("Example: python deliver.py buyer@example.com ORDER-12345")
        sys.exit(1)

    email = sys.argv[1]
    order_id = sys.argv[2]

    print(f"\n=== Ebook Delivery ===")
    print(f"Email: {email}")
    print(f"Order ID: {order_id}")
    print()

    try:
        msg = build_email(email, order_id)
        send_email(msg, email)
        log_delivery(email, order_id, "SUCCESS")
        print("\nDelivery complete!")
    except Exception as e:
        log_delivery(email, order_id, f"FAILED: {e}")
        print(f"\nERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
