"""No-KYC SMS OTP verify flow with SMSRoute. pip install requests"""
from __future__ import annotations

import os
import random
import sys
import time

import requests

BASE = "https://api.smsroute.cc"
KEY = os.environ.get("SMSROUTE_API_KEY")
if not KEY:
    sys.exit("Set SMSROUTE_API_KEY")

# phone -> (code, expires_at). Use Redis in production.
_store: dict[str, tuple[str, float]] = {}


def send_otp(phone: str, sender: str = "MyApp", ttl_sec: int = 300) -> None:
    code = f"{random.randint(0, 999999):06d}"
    _store[phone] = (code, time.time() + ttl_sec)
    r = requests.post(
        f"{BASE}/sms/send",
        headers={"Authorization": f"Bearer {KEY}"},
        json={
            "to": phone,
            "from": sender,
            "body": f"Your code is {code}. Expires in {ttl_sec // 60} min.",
        },
        timeout=20,
    )
    r.raise_for_status()


def verify_otp(phone: str, code: str) -> bool:
    rec = _store.get(phone)
    if not rec:
        return False
    stored, exp = rec
    if time.time() > exp:
        del _store[phone]
        return False
    if code == stored:
        del _store[phone]
        return True
    return False


if __name__ == "__main__":
    phone = sys.argv[1] if len(sys.argv) > 1 else "+15551234567"
    send_otp(phone)
    entered = input("code: ").strip()
    print("ok" if verify_otp(phone, entered) else "fail")
