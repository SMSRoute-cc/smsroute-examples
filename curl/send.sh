#!/usr/bin/env bash
# Send one SMS via SMSRoute. Requires: SMSROUTE_API_KEY
set -euo pipefail
: "${SMSROUTE_API_KEY:?set SMSROUTE_API_KEY}"
TO="${1:-+14155550123}"
FROM="${2:-INFO}"
BODY="${3:-Your code is 482913}"

curl -sS -X POST "https://api.smsroute.cc/sms/send" \
  -H "Authorization: Bearer ${SMSROUTE_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: demo-$(date +%s)" \
  -d "$(printf '{"to":"%s","from":"%s","body":"%s"}' "$TO" "$FROM" "$BODY")"
echo
