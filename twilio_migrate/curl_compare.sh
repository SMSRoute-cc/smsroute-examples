#!/usr/bin/env bash
# Side-by-side mental model — Twilio vs SMSRoute (do not run Twilio side without creds).
set -euo pipefail

echo "== Twilio shape (reference only) =="
cat <<'EOF'
curl -X POST https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages.json \
  -u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN \
  --data-urlencode "To=+14155550123" \
  --data-urlencode "From=+15017122661" \
  --data-urlencode "Body=Your code is 482913"
EOF

echo
echo "== SMSRoute equivalent =="
cat <<'EOF'
curl -X POST https://api.smsroute.cc/sms/send \
  -H "Authorization: Bearer $SMSROUTE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"to":"+14155550123","from":"INFO","body":"Your code is 482913"}'
EOF
