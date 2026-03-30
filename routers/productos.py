from fastapi import APIRouter

router = APIRouter( prefix="/products",
                    tags= ["products"],
                    responses={404: {"message" : "No encontrado"}}    ,
                                
                   )


list_products = [ "producto 1","producto 2","producto 3","producto 4","producto 5" ]

@router.get("/")
async def products():
    return list_products

@router.get("/{id}")
async def products(id:int):
    return list_products[id]


# Inicia el server: uvicorn [name_archivo]:app --reload
# uvicorn productos:app --reload