# SMSRoute — No-KYC SMS API Examples (Python, Node.js, cURL)

Send SMS and OTP from code with a **no-KYC SMS API** you can pay for in **crypto (BTC, ETH, USDT)**.
No identity documents, no business vetting, no multi-day approval — fund a balance, grab an API key,
and send in minutes. This repo has copy-paste examples in **Python**, **Node.js**, and **cURL**.

> SMSRoute is a no-KYC SMS API with crypto billing. These examples are MIT-licensed and provider-agnostic
> in shape — swap the base URL and key for any HTTP SMS API.

## Why a no-KYC / crypto SMS API?

- **Instant start** — no KYC vetting queue; send the same session.
- **Privacy** — minimal data footprint; no corporate-identity dossier handed to a vendor.
- **Crypto billing** — pay in BTC, ETH, or USDT (stablecoin = no volatility). Great for crypto
  exchanges, Web3 apps, Telegram bots, and teams without a corporate card.
- **International OTP/transactional reach** — clean delivery to 190+ countries.

Honest limit: branded **US A2P** requires 10DLC registration by carrier law — a no-KYC route is for
international, transactional, OTP, and privacy-sensitive sending, not unregistered branded US traffic.

## Quick start (cURL)

```bash
curl -X POST https://api.smsroute.cc/v1/send \
  -H "Authorization: Bearer $SMSROUTE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"to":"+15551234567","from":"MyApp","text":"Your code is 123456"}'
```

## Python

```python
import os, requests

def send_sms(to, text, sender="MyApp"):
    r = requests.post(
        "https://api.smsroute.cc/v1/send",
        headers={"Authorization": f"Bearer {os.environ['SMSROUTE_API_KEY']}"},
        json={"to": to, "from": sender, "text": text},
        timeout=15,
    )
    r.raise_for_status()
    return r.json()

# OTP example
import random
code = f"{random.randint(0, 999999):06d}"
send_sms("+15551234567", f"Your verification code is {code}. Expires in 5 minutes.")
```

Full examples in [`python/`](python/) — OTP verify flow, delivery webhooks, retries.

## Node.js

```js
const send = async (to, text, from = "MyApp") => {
  const res = await fetch("https://api.smsroute.cc/v1/send", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.SMSROUTE_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ to, from, text }),
  });
  if (!res.ok) throw new Error(`SMSRoute ${res.status}`);
  return res.json();
};

// OTP
const code = String(Math.floor(Math.random() * 1e6)).padStart(6, "0");
await send("+15551234567", `Your code is ${code}`);
```

Full examples in [`node/`](node/) — Express OTP endpoint, rate limiting, TypeScript types.

## Common use cases

| Use case | Example |
|---|---|
| Send an OTP / 2FA code | [python/otp_verify.py](python/otp_verify.py) · [node/otp-endpoint.js](node/otp-endpoint.js) |
| Telegram bot sends SMS | [node/telegram-bot-sms.js](node/telegram-bot-sms.js) |
| Crypto exchange verification | [python/exchange_verify.py](python/exchange_verify.py) |
| Delivery receipt webhook | [python/dlr_webhook.py](python/dlr_webhook.py) |

## Keywords

no kyc sms api · anonymous sms api · sms api crypto payment · bitcoin sms api · usdt sms api ·
sms api without registration · send otp without kyc · crypto sms verification · privacy sms api ·
twilio alternative no kyc · sms api python · sms api node.js

## Docs & guides

- [No-KYC SMS API: complete guide](https://smsroute.cc/blog/no-kyc-sms-api-complete-guide-2026)
- [Pay for an SMS API with crypto](https://smsroute.cc/blog/pay-for-sms-api-with-crypto-2026)
- [Send OTP SMS without KYC (5 lines)](https://smsroute.cc/blog/send-otp-sms-without-kyc-2026)
- [Get an API key](https://smsroute.cc/signup)

## License

MIT — see [LICENSE](LICENSE). Examples provided as-is; you own compliance for your destination markets.
