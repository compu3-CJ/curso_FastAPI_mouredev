from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter( prefix="/users",
                    tags= ["users"],
                    responses={404: {"message" : "No encontrado"}}    ,
                                )

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

#########################################################################################################

@router.get("/")
async def users_class():
    return users_list

## PATH -  http://127.0.0.1:8000/user/1
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)


## QUERY -  http://127.0.0.1:8000/user/?id=1
"""
@router.get("/user_query/")
async def user_query(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"Usuario no valido"}
"""
@router.get("/user/")
async def user(id: int):
    return search_user(id)    

#########################################################################################################
# {"id": 4, "name" : "Mateo", "surname" : "Carry" , "url" : "https://falso.mate" , "age" : 17}
## POST
@router.post("/user/",status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404,detail="El usuario ya existe, pendejo")
        #return {"error": "El usuario ya existe"}
    else:
        users_list.routerend(user)
        return user


## PUT
@router.put("/user/")
async def user(user: User):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error":"Usuario no actualizdo"}
    else:
        return user

## DELETE
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index] 
            found = True
            
    if not found:
        return {"error":"Usuario no EXISTE"}
    else:
        return {"aviso":"Usuario BORRADO CON EXITO"}
    
#########################################################################################################    

# FUNCION DE BUSQUEDA POR ID
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"Usuario no valido"}


# Inicia el server: uvicorn [name_archivo]:router --reload
# uvicorn CRUD:router --reload