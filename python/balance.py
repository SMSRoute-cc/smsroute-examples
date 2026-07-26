"""Check prepaid balance. pip install requests"""
import os
import sys

import requests

KEY = os.environ.get("SMSROUTE_API_KEY")
if not KEY:
    sys.exit("Set SMSROUTE_API_KEY")

r = requests.get(
    "https://api.smsroute.cc/account/balance",
    headers={"Authorization": f"Bearer {KEY}"},
    timeout=20,
)
print(r.status_code, r.text)
