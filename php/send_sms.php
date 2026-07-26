<?php
// php send_sms.php +14155550123 "Hello"
$key = getenv("SMSROUTE_API_KEY");
if (!$key) {
    fwrite(STDERR, "Set SMSROUTE_API_KEY\n");
    exit(1);
}
$to = $argv[1] ?? "+14155550123";
$body = $argv[2] ?? "Hello from SMSRoute examples";

$ch = curl_init("https://api.smsroute.cc/sms/send");
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        "Authorization: Bearer " . $key,
        "Content-Type: application/json",
    ],
    CURLOPT_POSTFIELDS => json_encode([
        "to" => $to,
        "from" => "INFO",
        "body" => $body,
    ]),
    CURLOPT_RETURNTRANSFER => true,
]);
$resp = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo $code . " " . $resp . PHP_EOL;
