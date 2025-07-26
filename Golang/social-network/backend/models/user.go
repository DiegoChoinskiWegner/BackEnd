package models

import (
	"time"
)

type User struct {
	ID                 int       `json:"id"`
	Username           string    `json:"username"`             // obrigatório
	Password           string    `json:"password"`             // obrigatório
	Email              string    `json:"email"`                // obrigatório
	Name               string    `json:"name"`                 // obrigatório
	BirthDate          time.Time `json:"birth_date"`           // obrigatório
	YouTubeProfile     *string   `json:"youtube_profile"`      // opcional
	SpotifyProfile     *string   `json:"spotify_profile"`      // opcional
	AmazonMusicProfile *string   `json:"amazon_music_profile"` // opcional
}
