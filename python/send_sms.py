"""Minimal SMS send via SMSRoute. pip install requests"""
from __future__ import annotations

import os
import sys

import requests

BASE = "https://api.smsroute.cc"
KEY = os.environ.get("SMSROUTE_API_KEY")
if not KEY:
    sys.exit("Set SMSROUTE_API_KEY")


def send_sms(to: str, body: str, sender: str = "INFO", **extra) -> dict:
    payload = {"to": to, "from": sender, "body": body, **extra}
    r = requests.post(
        f"{BASE}/sms/send",
        headers={"Authorization": f"Bearer {KEY}"},
        json=payload,
        timeout=20,
    )
    r.raise_for_status()
    return r.json() if r.content else {"status_code": r.status_code}


if __name__ == "__main__":
    to = sys.argv[1] if len(sys.argv) > 1 else "+14155550123"
    print(send_sms(to, "Hello from SMSRoute examples"))
