// Telegram bot that sends an SMS via SMSRoute (no-KYC, crypto-billed).
// npm i node-telegram-bot-api
const TelegramBot = require("node-telegram-bot-api");

const bot = new TelegramBot(process.env.TG_TOKEN, { polling: true });
const key = process.env.SMSROUTE_API_KEY;

async function sendSMS(to, text) {
  const res = await fetch("https://api.smsroute.cc/sms/send", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${key}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ to, from: "MyBot", body: text }),
  });
  if (!res.ok) throw new Error(`SMSRoute ${res.status}: ${await res.text()}`);
  return res.json();
}

bot.onText(/\/verify (.+)/, async (msg, m) => {
  const phone = m[1];
  const code = String(Math.floor(Math.random() * 1e6)).padStart(6, "0");
  try {
    await sendSMS(phone, `Your MyBot code is ${code}`);
    bot.sendMessage(msg.chat.id, `Sent a code to ${phone}.`);
  } catch (e) {
    bot.sendMessage(msg.chat.id, `Send failed: ${e.message}`);
  }
});
