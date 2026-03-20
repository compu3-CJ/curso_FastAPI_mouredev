from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user
class User(BaseModel):
      name : str
      surname : str
      url : str
      age : int

users_list = [User(name = "Crist", surname = "Jara" , url = "https://cris.jara" , age = 29 ),
              User(name = "Alex", surname = "Jaramillo" , url = "https://alex.jara" , age = 25 ),
              User(name = "Brais", surname = "Moure" , url = "https://moure.dev" , age = 35 )]

@app.get("/users_class")
async def users_class():
    return users_list


@app.get("/users_list_json")
async def users_list_json():
    return [{"name" : "Brais", "surname": "Moure", "url" : "https://moure.dev", "age":35},
            {"name" : "Alex", "surname": "Jara", "url" : "https://alito.jara", "age":25},
            {"name" : "Javi", "surname": "Omar", "url" : "https://javi.oma",  "age":29}
            ]

# Inicia el server: uvicorn [name_archivo]:app --reload
# uvicorn Curso_FastAPI.users2:app --reload