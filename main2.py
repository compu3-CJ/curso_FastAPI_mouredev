from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"Hola CJ =) FastAPI, Feliz año jávi"}

@app.get("/url1")
async def url1():
    return{"name":"Javi",
           "apellido": "JARA"}