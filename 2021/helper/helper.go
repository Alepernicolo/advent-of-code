package aocHelper

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func GetPuzzleInput(day int) string {
	client := http.DefaultClient
	url := fmt.Sprintf("https://adventofcode.com/2022/day/%d/input", day)
	req, err := http.NewRequest("GET", url, nil)

	if err != nil {
		fmt.Printf("Failed to create new GET request %s", err)
		os.Exit(1)
	}

	sessionField := fmt.Sprintf("session=%s", os.Getenv("AOC_Session"))

	req.Header.Add("Cookie", sessionField)
	resp, err := client.Do(req)

	if err != nil {
		fmt.Printf("Failed to send GET request %s", err)
		os.Exit(1)
	}

	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)

	if err != nil {
		fmt.Printf("Body weird")
		os.Exit(1)
	}
	return string(body[:])

}
