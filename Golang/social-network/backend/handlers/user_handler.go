package handlers

import (
	"backend/models"
	"encoding/json"
	"log"
	"net/http"
)

var mockUsers = []models.User{
	{ID: 1, Username: "john123", Email: "john@email.com", Name: "John Doe"},
	{ID: 2, Username: "sara_music", Email: "sara@email.com", Name: "Sara Smith"},
	{ID: 3, Username: "rockfan", Email: "rock@email.com", Name: "Mike Rock"},
	{ID: 4, Username: "poplover", Email: "pop@email.com", Name: "Anna Pop"},
}

func CreateUser(w http.ResponseWriter, r *http.Request) {
	log.Println("Criando usuário...")
	w.WriteHeader(http.StatusCreated)
	w.Write([]byte("Usuário criado!"))
}

func GetUsers(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(mockUsers)
}
