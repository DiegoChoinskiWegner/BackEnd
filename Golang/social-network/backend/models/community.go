package models

type Community struct {
	ID    int      `json:"id"`
	Title string   `json:"title"`
	Users []string `json:"users"`
}
