import requests
from fastapi.responses import JSONResponse
from firebase_admin import credentials, initialize_app, db
from fastapi import FastAPI

cred=credentials.Certificate('Api/json/discapacitados-54473-firebase-adminsdk-92ekf-f52b6a0147.json')
firebase_app=initialize_app(cred,{'databaseURL':'https://discapacitados-54473-default-rtdb.firebaseio.com/'})

ref=db.reference('/')

data=ref.get()

print(JSONResponse(content=data))