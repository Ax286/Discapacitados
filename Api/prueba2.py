import requests
from fastapi.responses import JSONResponse
from firebase_admin import credentials, initialize_app, db
from fastapi import FastAPI

peticion=requests.get('http://127.0.0.1:8000/Data')

if(peticion.status_code==200):
    data=peticion.json()
    print(data)