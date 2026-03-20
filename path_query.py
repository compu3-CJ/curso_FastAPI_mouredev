from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user
class User(BaseModel):
      id : int
      name : str
      surname : str
      url : str
      age : int

users_list = [User(id= 1, name = "Crist", surname = "Jara" , url = "https://cris.jara" , age = 29 ),
              User(id= 2, name = "Alex", surname = "Jaramillo" , url = "https://alex.jara" , age = 25 ),
              User(id= 3, name = "Brais", surname = "Moure" , url = "https://moure.dev" , age = 35 )]

@app.get("/users")
async def users_class():
    return users_list

## PATH -  http://127.0.0.1:8000/user/1
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


## QUERY -  http://127.0.0.1:8000/user/?id=1
"""
@app.get("/user_query/")
async def user_query(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"Usuario no valido"}
"""
@app.get("/user/")
async def user(id: int):
    return search_user(id)    


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"Usuario no valido"}







# Inicia el server: uvicorn [name_archivo]:app --reload
# uvicorn path_query:app --reload