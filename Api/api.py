from fastapi import FastAPI
from fastapi.responses import JSONResponse
from firebase_admin import credentials, initialize_app, db
from fastapi import FastAPI

app=FastAPI()

cred=credentials.Certificate('.\json\discapacitados-54473-firebase-adminsdk-92ekf-f52b6a0147.json')
firebase_app=initialize_app(cred,{'databaseURL':'https://discapacitados-54473-default-rtdb.firebaseio.com/'})

app = FastAPI()

# Rutas de ejemplo
@app.get("/Data")
def main():
    # Lectura de datos desde Firebase
    ref = db.reference('/')
    data = ref.get()
    return JSONResponse(content=data)

@app.get("/Discapacitados")
def discapacitados():
    ref=db.reference('/Discapacitados')
    data=ref.get()
    return JSONResponse(content=data)

@app.get("/Poblacion")
def poblacion():
    ref=db.reference('/Poblacion')
    data=ref.get()
    return JSONResponse(content=data)

#Leer archivo json
#with open('./json/Data.json','r') as myfile:
#    datos=myfile.read()

#Estados=json.loads(datos)

#http://127.0.0.1:8000
#uvicorn api:app

"""
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
"""