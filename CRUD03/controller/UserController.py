from fastapi import FastAPI
import UserRepository as UserRepository
import model.User as User

app = FastAPI()

@app.get("/user")
def hello_root():
    return {"message": "Hello World"}


class UserController:
    UserRepository.Users.__add__(User.User)

    UserRepository.Users.   