# SMSRoute — No-KYC SMS API Code Examples

Copy-paste code to send SMS programmatically without a phone number, using a **no-KYC SMS API** with **crypto billing**. No identity docs, no business verification, no 10DLC registration. Fund with BTC/ETH/USDT/XMR/LTC/SOL and send in minutes.

**Target queries:** send SMS programmatically without phone number, Twilio alternative code, SMS API no KYC

## Quick Start (cURL)

```bash
curl -X POST https://api.smsroute.cc/sms/send \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"to": "+14155550123", "from": "INFO", "message": "Your code is 482913"}'
```

Get your API key at [smsroute.cc](https://smsroute.cc/) — email-only signup, no documents.

## Python

```python
import requests

resp = requests.post(
    "https://api.smsroute.cc/sms/send",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json={"to": "+14155550123", "from": "INFO", "message": "Your code is 482913"},
)
print(resp.json())  # message ID + status
```

Full Python examples (OTP verify flow, delivery webhooks, retries) are in the [examples repository](https://github.com/SMSRoute-cc/smsroute-examples).

## Node.js

```javascript
const res = await fetch('https://api.smsroute.cc/sms/send', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ to: '+14155550123', from: 'INFO', message: 'Your code is 482913' })
});
console.log(await res.json()); // message ID + status
```

Full Node.js examples (Express OTP endpoint, rate limiting, TypeScript types) are in the [examples repository](https://github.com/SMSRoute-cc/smsroute-examples).

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
        "message" => "Your code is 482913",
    ]),
    CURLOPT_RETURNTRANSFER => true,
]);
$response = curl_exec($ch);
curl_close($ch);
?>
```

Full PHP examples (Laravel integration, webhook handler) are in the [examples repository](https://github.com/SMSRoute-cc/smsroute-examples).

## Go

```go
package main

import (
    "bytes"
    "encoding/json"
    "net/http"
    "os"
)

func sendSMS(to, text, sender string) error {
    body, _ := json.Marshal(map[string]string{
        "to":      to,
        "from":    sender,
        "message": text,
    })
    req, _ := http.NewRequest("POST", "https://api.smsroute.cc/sms/send", bytes.NewBuffer(body))
    req.Header.Set("Authorization", "Bearer "+os.Getenv("SMSROUTE_API_KEY"))
    req.Header.Set("Content-Type", "application/json")
    _, err := http.DefaultClient.Do(req)
    return err
}
```

Full Go examples (concurrent sending, DLR polling) are in the [examples repository](https://github.com/SMSRoute-cc/smsroute-examples).

## Migrate from Twilio in 5 Lines

Replace Twilio with SMSRoute — no KYC, no business verification, no 10DLC:

```python
# Before (Twilio)
from twilio.rest import Client
client = Client(account_sid, auth_token)
client.messages.create(to="+15551234567", from_="+15559876543", body="Hello")

# After (SMSRoute)
import requests
requests.post("https://api.smsroute.cc/sms/send",
    headers={"Authorization": f"Bearer {os.environ['SMSROUTE_API_KEY']}"},
    json={"to": "+15551234567", "from": "INFO", "message": "Hello"})
```

No account SID, no phone number purchase, no identity verification. See the full [Twilio alternative guide](https://smsroute-cc.github.io/twilio-alternative-no-business-verification.html).

## Why SMSRoute?

| Feature | SMSRoute | Twilio/Vonage/Plivo |
|---|---|---|
| KYC required | **No** — email-only signup | Yes — identity + business docs |
| Billing | Crypto (BTC/ETH/USDT/XMR/LTC/SOL) + auto top-up | Credit card only |
| 10DLC/DLT registration | Not required | Required for US traffic |
| Data retention | Minimal | Retains message content |
| Pricing | From $0.004/message | Varies, often higher |
| Coverage | 149 countries | Similar, but with restrictions |
| Failed messages | Auto-credited | Manual dispute |
| Support | 24/7 Telegram + email | Ticket-based |

## Pricing & Coverage

- **From $0.004/message** (premium corridors up to $0.035)
- **149 countries** — see full [pricing page](https://smsroute.cc/prices/)
- **99.9%+ uptime** TTM with real-time DLR webhooks
- **Free test credits** on signup

## Crypto Payments

Pay with **BTC, ETH, USDT (TRC-20/ERC-20), XMR, LTC, SOL** — automatic top-up confirmation, no volatility risk with stablecoins. See [crypto payments guide](https://smsroute-cc.github.io/sms-api-accepts-bitcoin-crypto.html) and [Monero guide](https://smsroute-cc.github.io/sms-api-monero-xmr.html).

## Common Use Cases

| Use case | Example |
|---|---|
| Send OTP / 2FA without KYC | python/otp_verify.py · node/otp-endpoint.js |
| Crypto exchange verification | python/exchange_verify.py |
| Telegram bot sends SMS | node/telegram-bot-sms.js |
| Anonymous SMS for privacy apps | python/anonymous_send.py |
| Delivery receipt webhook | python/dlr_webhook.py |

All examples are available in the [examples repository](https://github.com/SMSRoute-cc/smsroute-examples).

## Resources

- [No-KYC SMS API guide](https://smsroute-cc.github.io/best-no-kyc-sms-api.html)
- [Anonymous SMS API for developers](https://smsroute-cc.github.io/anonymous-sms-api-for-developers.html)
- [Cheapest international bulk SMS API](https://smsroute-cc.github.io/cheapest-international-bulk-sms-api.html)
- [Full API reference](https://smsroute.cc/api/)