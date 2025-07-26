package handlers

import (
	"backend/models"
	"encoding/json"
	"net/http"
)

// Lista mockada de músicas
var communities = []models.Community{
	{
		ID:    1,
		Title: "Rock Legends Fans",
		Users: []string{
			mockUsers[0].Name, // John
			mockUsers[2].Name, // Mike
		},
	},
	{
		ID:    2,
		Title: "Pop Music Lovers",
		Users: []string{
			mockUsers[1].Name, // Sara
			mockUsers[3].Name, // Anna
		},
	},
}

// Handler que retorna a lista de músicas
func GetCommunities(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(communities)
}
