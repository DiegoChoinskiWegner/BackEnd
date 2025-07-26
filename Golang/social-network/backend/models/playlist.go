package models

type Playlist struct {
	ID    int     `json:"id"`
	Title string  `json:"title"`
	Music []Music `json:"music"`
}
