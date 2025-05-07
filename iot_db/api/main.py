from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from pymongo import MongoClient

app = FastAPI()

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.iot_db
collection = db.ciudades

# Modelo para validación automática con Pydantic
class Ciudad(BaseModel):
    nombre: str
    pais: str
    poblacion: int
    continente: str

@app.get("/ciudades", response_model=List[Ciudad])
def obtener_ciudades():
    ciudades = list(collection.find({}, {"_id": 0}))
    return ciudades

@app.get("/ciudades/{nombre}", response_model=Ciudad)
def obtener_ciudad(nombre: str):
    ciudad = collection.find_one({"nombre": nombre}, {"_id": 0})
    if ciudad:
        return ciudad
    raise HTTPException(status_code=404, detail="Ciudad no encontrada")

@app.post("/ciudades", status_code=201)
def agregar_ciudad(ciudad: Ciudad):
    if collection.find_one({"nombre": ciudad.nombre}):
        raise HTTPException(status_code=400, detail="La ciudad ya existe")
    collection.insert_one(ciudad.dict())
    return {"mensaje": "Ciudad agregada"}

@app.put("/ciudades/{nombre}")
def actualizar_ciudad(nombre: str, ciudad: Ciudad):
    result = collection.update_one({"nombre": nombre}, {"$set": ciudad.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    return {"mensaje": "Ciudad actualizada"}

@app.delete("/ciudades/{nombre}")
def eliminar_ciudad(nombre: str):
    result = collection.delete_one({"nombre": nombre})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    return {"mensaje": "Ciudad eliminada"}
