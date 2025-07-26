package main

import (
	"backend/handlers"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {

	router := mux.NewRouter()

	// User routes
	router.HandleFunc("/users", handlers.GetUsers).Methods("GET")

	// Music routes
	router.HandleFunc("/musics", handlers.GetMusics).Methods("GET")

	// Playlist routes
	router.HandleFunc("/playlists", handlers.GetPlaylist).Methods("GET")

	// Community routes
	router.HandleFunc("/communities", handlers.GetCommunities).Methods("GET")

	log.Println("🚀 Servidor rodando na porta 8080...")
	log.Fatal(http.ListenAndServe(":8080", router))
}
