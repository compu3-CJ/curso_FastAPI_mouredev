from fastapi import FastAPI , Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Entidad user
class User(BaseModel):
      username : str
      full_name : str
      email : str
      disabled : bool
      
class UserDB(User):
    password : str
    

users_db = {
    "cj_admin" :{
        "username" : "cj",
        "full_name" : "Javier",
        "email" : "javi@gmail.com",
        "disabled" : False,
        "password" : "123456"
    },
    "alex1" :{
        "username" : "alexmijin",
        "full_name" : "Alex",
        "email" : "alex@gmail.com",
        "disabled" : False,
        "password" : "654321"
    },
    "carlos1" :{
        "username" : "carlos",
        "full_name" : "Carlos",
        "email" : "carlos@gmail.com",
        "disabled" : False,
        "password" : "321654"
    },
}


def serch_user(username:str):
    if username in users_db:
        return UserDB(users_db[username])

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    
    




# Inicia el server: uvicorn [name_archivo]:app --reload
# uvicorn autenticacion_basica:app --reload