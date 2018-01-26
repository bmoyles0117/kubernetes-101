package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"

	"github.com/urfave/negroni"
)

func greetingHandler(w http.ResponseWriter, r *http.Request) {
	hostname, _ := os.Hostname()
	greetingFormat := os.Getenv("GREETING_FORMAT")
	if greetingFormat == "" {
		greetingFormat = "Hello %s."
	}

	json.NewEncoder(w).Encode(map[string]string{
		"server":   hostname,
		"greeting": fmt.Sprintf(greetingFormat, r.FormValue("name")),
	})
}

func healthzHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "OK")
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/greeting", greetingHandler)
	mux.HandleFunc("/healthz", healthzHandler)

	n := negroni.Classic()
	n.UseHandler(mux)

	if err := http.ListenAndServe(":5000", n); err != nil {
		fmt.Printf("Server has died: %s", err)
	}
}
