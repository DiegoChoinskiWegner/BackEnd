package handlers

import (
	"backend/models"
	"encoding/json"
	"net/http"
)

// Lista mockada de músicas
var playlists = []models.Playlist{
	{
		ID:    1,
		Title: "Classic Rock Favorites",
		Music: []models.Music{
			musics[0], // Bohemian Rhapsody
			musics[2], // Smells Like Teen Spirit
			musics[4], // Hotel California
			musics[6], // Imagine
			musics[8], // Hey Jude
		},
	},
	{
		ID:    2,
		Title: "Pop & Hits",
		Music: []models.Music{
			musics[1], // Billie Jean
			musics[3], // Shape of You
			musics[5], // Rolling in the Deep
			musics[7], // Wonderwall
			musics[9], // Lose Yourself
		},
	},
}

// Handler que retorna a lista de músicas
func GetPlaylist(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(playlists)
}
