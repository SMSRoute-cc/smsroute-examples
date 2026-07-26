# SMSRoute — No-KYC SMS API Code Examples

Copy-paste code to send SMS via a **no-KYC SMS API** with **crypto billing** (BTC / ETH / USDT).  
Twilio-style REST without card KYC or 10DLC onboarding theater. **149 countries · from $0.004/SMS · $5 free credits.**

**Target queries:** `no kyc sms api` · `sms api crypto` · `twilio alternative` · `otp verification api` · `send sms programmatically`

Get an API key: [smsroute.cc/register](https://smsroute.cc/register) · Docs: [smsroute.cc/developers](https://smsroute.cc/developers) · Pricing: [smsroute.cc/prices](https://smsroute.cc/prices)

## Quick Start (cURL)

```bash
export SMSROUTE_API_KEY=your_key_here

curl -X POST https://api.smsroute.cc/sms/send \
  -H "Authorization: Bearer $SMSROUTE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: demo-$(date +%s)" \
  -d '{
    "to": "+14155550123",
    "from": "INFO",
    "body": "Your code is 482913"
  }'
```

## Python

```python
import os, requests

r = requests.post(
    "https://api.smsroute.cc/sms/send",
    headers={"Authorization": f"Bearer {os.environ['SMSROUTE_API_KEY']}"},
    json={
        "to": "+14155550123",
        "from": "INFO",
        "body": "Your code is 482913",
    },
    timeout=15,
)
print(r.status_code, r.json())
```

See `python/` for OTP flow, balance check, and DLR webhook handler.

## Node.js

```javascript
const res = await fetch("https://api.smsroute.cc/sms/send", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.SMSROUTE_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    to: "+14155550123",
    from: "INFO",
    body: "Your code is 482913",
  }),
});
console.log(await res.json());
```

See `node/` for Telegram bot SMS notifier and Express OTP endpoint.

## PHP

```php
<?php
$ch = curl_init("https://api.smsroute.cc/sms/send");
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        "Authorization: Bearer " . getenv("SMSROUTE_API_KEY"),
        "Content-Type: application/json",
    ],
    CURLOPT_POSTFIELDS => json_encode([
        "to" => "+14155550123",
        "from" => "INFO",
        "body" => "Your code is 482913",
    ]),
    CURLOPT_RETURNTRANSFER => true,
]);
echo curl_exec($ch);
```

Full file: `php/send_sms.php`.

## Go

```go
// see go/send_sms.go
```

## Migrate from Twilio (5-line mental model)

| Twilio | SMSRoute |
|--------|----------|
| Account SID + Auth Token | `Authorization: Bearer API_KEY` |
| `Body` | `body` |
| `From` / Messaging Service | `from` (3–11 alphanumeric where allowed) |
| Card + KYC + 10DLC | Email signup + crypto top-up |
| `StatusCallback` | `status_callback` |

Side-by-side: `twilio_migrate/curl_compare.sh`

## Why SMSRoute (honest table)

| Feature | SMSRoute | Typical CPaaS (Twilio-class) |
|---------|----------|------------------------------|
| Signup KYC | Email-only | ID + business docs common |
| Billing | BTC / ETH / USDT (+ site rails) | Card / invoice |
| Floor price | From **$0.004**/SMS (route-dependent) | Higher + fees |
| Coverage | **149** countries | Broad, enterprise packaging |
| Free start | **$5** credits | Trial varies |
| Best for | OTP / transactional / crypto-native ops | Full omnichannel suites |

US domestic can be *less* competitive than Twilio at scale — international + crypto rails are the wedge. Always test your routes.

## Repo map

| Path | Intent keyword |
|------|----------------|
| `curl/send.sh` | send sms api |
| `python/send_sms.py` | python sms api |
| `python/otp_verify.py` | otp verification |
| `python/balance.py` | account balance |
| `python/dlr_webhook.py` | delivery receipt webhook |
| `node/send.js` | node sms api |
| `node/telegram-bot-sms.js` | telegram bot sms |
| `node/express_otp.js` | otp endpoint |
| `php/send_sms.php` | php sms api |
| `go/send_sms.go` | go sms api |
| `twilio_migrate/` | twilio alternative |
| `openapi.json` | machine-readable API |

## API surface (canonical)

Base: `https://api.smsroute.cc`

- `POST /sms/send` — `{to, from, body, status_callback?, reference?, validity_period?}`
- `POST /sms/send/bulk` — batch ≤1000
- `GET /sms/single/{messageId}/status`
- `GET /account/balance`
- `GET /prices` · `GET /prices?country=US` · `GET /prices/lookup?to=+1...`

## Crypto top-up

Fund in the dashboard with **BTC / ETH / USDT**, then spend prepaid balance. No card required for the core loop.

## Security

See `SECURITY.md`. Do not commit API keys. Prefer env vars + short-lived server-side sends.

## License

MIT — official examples for [smsroute.cc](https://smsroute.cc). Issues welcome.
