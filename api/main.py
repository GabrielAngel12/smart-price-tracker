from fastapi import FastAPI, HTTPException
from typing import List
import uvicorn

# Creamos una "base de datos" temporal en memoria para empezar
# Más adelante la reemplazaremos con PostgreSQL
db_products = []

#Aquí le damos a nuestro robot su identidad.
app = FastAPI(
    title="Smart Price Tracker API",
    description="Una API para monitorear precios de productos y recibir alertas.",
    version="0.1.0"
)

# Modelo simple para un producto (usaremos Pydantic más adelante)
class Product:
    def __init__(self, id: int, url: str, name: str):
        self.id = id
        self.url = url


        
        self.name = name

@app.get("/")
def read_root():
    return {"status": "API en funcionamiento"}

@app.post("/products", status_code=201)
def add_product_to_track(url: str, name: str):
    """
    Añade un nuevo producto para monitorear.
    En el body de la petición se envía un JSON con 'url' y 'name'.
    """
    new_id = len(db_products) + 1
    new_product = Product(id=new_id, url=url, name=name)
    db_products.append(new_product)
    return {"message": "Producto añadido", "product_id": new_id}

@app.get("/products")
def get_tracked_products():
    """
    Devuelve la lista de todos los productos que se están monitoreando.
    """
    return [p.__dict__ for p in db_products]

# Para ejecutar la API, guarda este archivo y en tu terminal (en la raíz del proyecto) ejecuta:
# uvicorn api.main:app --reload