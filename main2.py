from fastapi import FastAPI
from routers import productos, CRUD
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(productos.router)
app.include_router(CRUD.router)
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/")
async def root():
    return{"Hola CJ =) FastAPI, Feliz año jávi"}

@app.get("/url1")
async def url1():
    return{"name":"Javi",
           "apellido": "JARA"}
    
# Inicia el server: uvicorn [name_archivo]:app --reload
# uvicorn main2:app --reload