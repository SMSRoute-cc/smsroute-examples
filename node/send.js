// Minimal Node send. Node 18+ (fetch).
const key = process.env.SMSROUTE_API_KEY;
if (!key) {
  console.error("Set SMSROUTE_API_KEY");
  process.exit(1);
}

const to = process.argv[2] || "+14155550123";
const body = process.argv[3] || "Hello from SMSRoute examples";

const res = await fetch("https://api.smsroute.cc/sms/send", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${key}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ to, from: "INFO", body }),
});
console.log(res.status, await res.text());
