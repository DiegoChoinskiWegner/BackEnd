package handlers

import (
	"backend/models"
	"encoding/json"
	"net/http"
	"time"
)

// Lista mockada de músicas
var musics = []models.Music{
	{
		ID:     1,
		Title:  "Bohemian Rhapsody",
		Artist: "Queen",
		ReleaseDate: func() *time.Time {
			t, _ := time.Parse("2006-01-02", "1975-10-31")
			return &t
		}(),
		Genre:    "Rock",
		Duration: 354,
		URL:      ptr("https://open.spotify.com/track/1AhDOtG9vPSOmsWgNW0BEY"),
		Musicians: &[]string{
			"Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon",
		},
	},
	{
		ID:     2,
		Title:  "Billie Jean",
		Artist: "Michael Jackson",
		ReleaseDate: func() *time.Time {
			t, _ := time.Parse("2006-01-02", "1983-01-02")
			return &t
		}(),
		Genre:    "Pop",
		Duration: 294,
		URL:      ptr("https://open.spotify.com/track/5ChkMS8OtdzJeqyybCc9R5"),
		Musicians: &[]string{
			"Michael Jackson",
		},
	},
	{
		ID:     3,
		Title:  "Smells Like Teen Spirit",
		Artist: "Nirvana",
		ReleaseDate: func() *time.Time {
			t, _ := time.Parse("2006-01-02", "1991-09-10")
			return &t
		}(),
		Genre:    "Grunge",
		Duration: 301,
		URL:      ptr("https://open.spotify.com/track/5ghIJDpPoe3CfHMGu71E6T"),
		Musicians: &[]string{
			"Kurt Cobain", "Krist Novoselic", "Dave Grohl",
		},
	},
	{
		ID:     4,
		Title:  "Shape of You",
		Artist: "Ed Sheeran",
		ReleaseDate: func() *time.Time {
			t, _ := time.Parse("2006-01-02", "2017-01-06")
			return &t
		}(),
		Genre:    "Pop",
		Duration: 233,
		URL:      ptr("https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3"),
		Musicians: &[]string{
			"Ed Sheeran", "Steve Mac", "Johnny McDaid",
		},
	},
	{
		ID:     5,
		Title:  "Hotel California",
		Artist: "Eagles",
		ReleaseDate: func() *time.Time {
			t, _ := time.Parse("2006-01-02", "1976-12-08")
			return &t
		}(),
		Genre:    "Rock",
		Duration: 391,
		URL:      ptr("https://open.spotify.com/track/40riOy7x9W7GXjyGp4pjAv"),
		Musicians: &[]string{
			"Don Henley", "Glenn Frey", "Joe Walsh", "Don Felder", "Randy Meisner",
		},
	},
	{
		ID:     6,
		Title:  "Rolling in the Deep",
		Artist: "Adele",
		ReleaseDate: func() *time.Time {
			t, _ := time.Parse("2006-01-02", "2010-11-29")
			return &t
		}(),
		Genre:    "Soul",
		Duration: 228,
		URL:      ptr("https://open.spotify.com/track/7h2gU6aJmObE5gJtz2B2UP"),
		Musicians: &[]string{
			"Adele", "Paul Epworth",
		},
	},
	{
		ID:     7,
		Title:  "Imagine",
		Artist: "John Lennon",
		ReleaseDate: func() *time.Time {
			t, _ := time.Parse("2006-01-02", "1971-10-11")
			return &t
		}(),
		Genre:    "Soft Rock",
		Duration: 183,
		URL:      ptr("https://open.spotify.com/track/7pKfPomDEeI4TPT6EOYjn9"),
		Musicians: &[]string{
			"John Lennon",
		},
	},
	{
		ID:     8,
		Title:  "Wonderwall",
		Artist: "Oasis",
		ReleaseDate: func() *time.Time {
			t, _ := time.Parse("2006-01-02", "1995-10-02")
			return &t
		}(),
		Genre:    "Britpop",
		Duration: 259,
		URL:      ptr("https://open.spotify.com/track/2L0b4z0L7Evk1bt1N8Zf2b"),
		Musicians: &[]string{
			"Noel Gallagher", "Liam Gallagher",
		},
	},
	{
		ID:     9,
		Title:  "Hey Jude",
		Artist: "The Beatles",
		ReleaseDate: func() *time.Time {
			t, _ := time.Parse("2006-01-02", "1968-08-26")
			return &t
		}(),
		Genre:    "Rock",
		Duration: 431,
		URL:      ptr("https://open.spotify.com/track/7DD7eSuYSC5xk2ArU62esN"),
		Musicians: &[]string{
			"Paul McCartney", "John Lennon", "George Harrison", "Ringo Starr",
		},
	},
	{
		ID:     10,
		Title:  "Lose Yourself",
		Artist: "Eminem",
		ReleaseDate: func() *time.Time {
			t, _ := time.Parse("2006-01-02", "2002-10-28")
			return &t
		}(),
		Genre:    "Hip Hop",
		Duration: 326,
		URL:      ptr("https://open.spotify.com/track/4xkOaSrkexMciUUogZKVTS"),
		Musicians: &[]string{
			"Eminem", "Jeff Bass", "Luis Resto",
		},
	},
}

// Função auxiliar para criar ponteiros de string rapidamente
func ptr(s string) *string {
	return &s
}

// Handler que retorna a lista de músicas
func GetMusics(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(musics)
}
