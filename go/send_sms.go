package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

func main() {
	key := os.Getenv("SMSROUTE_API_KEY")
	if key == "" {
		fmt.Fprintln(os.Stderr, "Set SMSROUTE_API_KEY")
		os.Exit(1)
	}
	to := "+14155550123"
	if len(os.Args) > 1 {
		to = os.Args[1]
	}
	payload, _ := json.Marshal(map[string]string{
		"to":   to,
		"from": "INFO",
		"body": "Hello from SMSRoute examples",
	})
	req, err := http.NewRequest("POST", "https://api.smsroute.cc/sms/send", bytes.NewReader(payload))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer "+key)
	req.Header.Set("Content-Type", "application/json")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	buf := new(bytes.Buffer)
	buf.ReadFrom(resp.Body)
	fmt.Println(resp.StatusCode, buf.String())
}
