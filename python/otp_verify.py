"""No-KYC SMS OTP verify flow with SMSRoute. pip install requests"""
import os, random, time, requests

BASE = "https://api.smsroute.cc/v1"
KEY = os.environ["SMSROUTE_API_KEY"]
_store = {}  # phone -> (code, expires) — use Redis in production

def send_otp(phone: str) -> None:
    code = f"{random.randint(0, 999999):06d}"
    _store[phone] = (code, time.time() + 300)  # 5-min expiry
    requests.post(f"{BASE}/send",
        headers={"Authorization": f"Bearer {KEY}"},
        json={"to": phone, "from": "MyApp", "text": f"Your code is {code}. Expires in 5 min."},
        timeout=15).raise_for_status()

def verify_otp(phone: str, code: str, max_attempts=5) -> bool:
    rec = _store.get(phone)
    if not rec: return False
    stored, exp = rec
    if time.time() > exp:
        del _store[phone]; return False           # expired
    if code == stored:
        del _store[phone]; return True             # one-time use
    return False

if __name__ == "__main__":
    send_otp("+15551234567")
    print(verify_otp("+15551234567", input("code: ")))
