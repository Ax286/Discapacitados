from fastapi import FastAPI
import json


app=FastAPI()

#Leer archivo json
with open('./json/Data.json','r') as myfile:
    datos=myfile.read()

Estados=json.loads(datos)

#http://127.0.0.1:8000
#uvicorn api:app

#Creacion de metodos del API
@app.get("/")
def index():
    return "Main"

@app.get("/Data/")
def obtener_estados():
    return Estados

@app.get("/Data/Discapacitados/General")
def obGeneral():
    return Estados["Discapacitados"]["General"]

@app.get("/Data/Poblacion/")
def obPoblacion():
    return Estados["Poblacion"]

@app.get("/Data/Discapacitados/Tipo/Hombres")
def obTipoHombres():
    return Estados["Discapacitados"]["Tipo"]["Hombres"]

@app.get("/Data/Discapacitados/Tipo/Mujeres")
def obTipoMujeres():
    return Estados["Discapacitados"]["Tipo"]["Mujeres"]

@app.get("/Data/Discapacitados/Edades/Hombres")
def obtEdadHombres():
    return Estados["Discapacitados"]["Edades"]["Hombres"]

@app.get("/Data/Discapacitados/Edades/Mujeres")
def obtEdadMujeres():
    return Estados["Discapacitados"]["Edades"]["Mujeres"]