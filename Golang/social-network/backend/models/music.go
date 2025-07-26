package models

import (
	"time"
)

type Music struct {
	ID          int        `json:"id"`
	Title       string     `json:"title"`
	Artist      string     `json:"artist"`
	ReleaseDate *time.Time `json:"release_date"`
	Genre       string     `json:"genre"`
	Duration    int        `json:"duration"`
	URL         *string    `json:"url"`
	Musicians   *[]string  `json:"musicians"`
}
