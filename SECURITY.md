# Security Policy

<<<<<<< HEAD
## Reporting a Vulnerability
If you find a security issue in this repository or in the SMSRoute API/service,
please email **valentinazealk@onet.pl** with details. We aim to acknowledge
reports within 48 hours.

Please do not open a public GitHub issue for security-sensitive reports.
=======
## Reporting
Email security issues to the operator contact on https://smsroute.cc — do not open public issues for key leaks.

## Guidelines for examples
- Never commit `SMSROUTE_API_KEY` or webhook secrets.
- Prefer server-side sends; do not embed keys in mobile/browser clients.
- Validate `X-SmsRoute-Signature` on DLR webhooks when a secret is configured.
- Treat SMS content as sensitive (OTP codes); minimize logs.
>>>>>>> 3ee0744 (feat: hard-fill examples + canonical API fields (body/from) + openapi)
