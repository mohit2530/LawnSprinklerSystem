package main

import (
	"log"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/mohit2530/LawnSprinklerSystem/internal/handler"
)

func main() {
	router := mux.NewRouter()

	router.HandleFunc("/api/v1/health", handler.GetSystemHealth).Methods(http.MethodPost)

	port := ":4165"
	log.Printf("Using port: %+v", port)
	http.ListenAndServe(port, router)
}
