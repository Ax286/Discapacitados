from fastapi import FastAPI
from fastapi.responses import JSONResponse
from firebase_admin import credentials, initialize_app, db
from fastapi import FastAPI

#http://127.0.0.1:8000
#uvicorn api:app

app=FastAPI()

cred=credentials.Certificate('./json/discapacitados-54473-firebase-adminsdk-92ekf-f52b6a0147.json')
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

