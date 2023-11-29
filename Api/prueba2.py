import requests
from fastapi.responses import JSONResponse
from firebase_admin import credentials, initialize_app, db
from fastapi import FastAPI

"""
from keras.models import Sequential
from keras.layers import Dense

x=[]
y=[]

# Crear un modelo secuencial
modelo = Sequential()

# Añadir capas al modelo
modelo.add(Dense(units=64, activation='relu', input_shape=(100,)))
modelo.add(Dense(units=10, activation='softmax'))

# Compilar el modelo
modelo.compile(loss='categorical_crossentropy', optimizer='sgd', 
               metrics=['accuracy'])

modelo.fit(x,y,epochs=100)
"""

cred=credentials.Certificate('.\json\discapacitados-54473-firebase-adminsdk-92ekf-f52b6a0147.json')
firebase_app=initialize_app(cred,{'databaseURL':'https://discapacitados-54473-default-rtdb.firebaseio.com/'})

app = FastAPI()

# Rutas de ejemplo
@app.get("/")
def read_root():
    # Ejemplo de lectura de datos desde Firebase
    ref = db.reference('/')
    data = ref.get()
    return JSONResponse(content=data)

#peticion=requests.get('https://discapacitados-54473-default-rtdb.firebaseio.com/.json')

#Datos discapacitados (general)
#if(peticion.status_code==200):
#    data=peticion.json()
#    print(data)