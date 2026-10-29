# Send an SMS from code — curl, Python, Node and PHP examples

A no-KYC SMS API issues you a key after an email-only signup, with no identity document and no company
registration, and bills in cryptocurrency instead of a card. This repository contains working examples
for sending one message, reading a delivery receipt, and handling the errors you will actually hit.

Last verified: 2026-10-29.

## What you need

- An API key (email signup, no documents)
- A funded balance — top-ups start at $5, paid in BTC, ETH, USDT or XMR
- The destination number in E.164 format, e.g. `+4915112345678`

## Quick start (curl)

```bash
export SMS_API_KEY="your_key_here"

curl -X POST https://api.sendsmsnokyc.com/sms/send   -H "Authorization: Bearer $SMS_API_KEY"   -H "Content-Type: application/json"   -d '{"to":"+4915112345678","from":"MyBrand","body":"Hello from the API"}'
```

A successful call returns a message id. Delivery is asynchronous — poll or receive a webhook.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| POST | `/sms/send` | Send one message |
| GET | `/sms/{id}` | Fetch delivery status |
| GET | `/balance` | Remaining credit |

## Examples by language

| Language | File |
|---|---|
| cURL | `curl/send.sh` |
| Python | `python/send_sms.py` |
| Node.js | `node/send_sms.js` |
| PHP | `php/send_sms.php` |
| Go | `go/main.go` |

## Error codes

| Code | Meaning | What to do |
|---|---|---|
| 400 | Malformed number or body | Check E.164 formatting |
| 401 | Missing or invalid key | Re-issue the key |
| 402 | Insufficient balance | Top up |
| 429 | Rate limited | Back off and retry |
| 5xx | Provider-side failure | Retry with backoff; failed sends are not billed |

## Pricing

| Destination | Price per one-part SMS |
|---|---|
| United States | from $0.0079 |
| United Kingdom | from $0.0380 |
| Germany | from $0.0410 |
| India | from $0.0040 |

Full per-country table: https://sendsmsnokyc.com/prices

## FAQ

### Do I need to register a company?
No. Signup requires an email address. Destination-country rules (10DLC in the US, DLT in India,
sender-ID pre-registration in parts of the EU) still apply to the traffic itself.

### Can I send without a phone number?
Yes. You send from a sender ID or shared route. Receiving replies requires a number, which is a
different product.

### How do delivery receipts work?
Either poll `GET /sms/{id}` or configure a webhook. A receipt means the handset acknowledged the
message, not that a human read it.

## Licence

MIT — see LICENSE.
