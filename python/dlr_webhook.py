"""Minimal Flask DLR webhook for SMSRoute status_callback.

Verify X-SmsRoute-Signature: t={unix},v1={hmac}
HMAC-SHA256 over f"{t}.{raw_body}" with your webhook secret.

pip install flask
"""
from __future__ import annotations

import hashlib
import hmac
import os
import time

from flask import Flask, abort, request

app = Flask(__name__)
SECRET = os.environ.get("SMSROUTE_WEBHOOK_SECRET", "")


def valid_signature(raw: bytes, header: str | None) -> bool:
    if not SECRET or not header:
        return False
    # t=...,v1=...
    parts = dict(
        p.split("=", 1) for p in header.split(",") if "=" in p
    )
    t = parts.get("t")
    v1 = parts.get("v1")
    if not t or not v1:
        return False
    try:
        ts = int(t)
    except ValueError:
        return False
    if abs(time.time() - ts) > 300:
        return False
    digest = hmac.new(
        SECRET.encode(), f"{t}.".encode() + raw, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(digest, v1)


@app.post("/webhooks/smsroute")
def dlr():
    raw = request.get_data()
    if SECRET and not valid_signature(raw, request.headers.get("X-SmsRoute-Signature")):
        abort(401)
    payload = request.get_json(force=True, silent=True) or {}
    # statuses: accepted -> sent -> delivered | undelivered | failed
    print("dlr", payload.get("message_id"), payload.get("status"), payload.get("to"))
    return {"ok": True}


if __name__ == "__main__":
    app.run(port=8080)
