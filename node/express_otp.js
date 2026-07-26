// Express OTP endpoints using SMSRoute.
// npm i express
import express from "express";

const app = express();
app.use(express.json());
const key = process.env.SMSROUTE_API_KEY;
const store = new Map(); // phone -> { code, exp }

async function sendSms(to, body) {
  const res = await fetch("https://api.smsroute.cc/sms/send", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${key}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ to, from: "MyApp", body }),
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

app.post("/otp/send", async (req, res) => {
  const phone = req.body?.phone;
  if (!phone) return res.status(400).json({ error: "phone required" });
  const code = String(Math.floor(Math.random() * 1e6)).padStart(6, "0");
  store.set(phone, { code, exp: Date.now() + 5 * 60 * 1000 });
  try {
    await sendSms(phone, `Your code is ${code}. Expires in 5 min.`);
    res.json({ ok: true });
  } catch (e) {
    res.status(502).json({ error: String(e.message || e) });
  }
});

app.post("/otp/verify", (req, res) => {
  const { phone, code } = req.body || {};
  const rec = store.get(phone);
  if (!rec || rec.exp < Date.now()) return res.status(400).json({ ok: false });
  if (rec.code !== code) return res.status(400).json({ ok: false });
  store.delete(phone);
  res.json({ ok: true });
});

app.listen(process.env.PORT || 3000);
