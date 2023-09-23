'''
para poder usar nuestra primera aplicacion de fastAPI, primero 
debemos instalar los frameworks necesarios para esta, primero 
instalamos el fastAPI con este comando:

pip install fastapi

tambien vamos a requerir un  modulo para correr fastapi, en 
este caso va a ser uvicorn:

pip install uvicorn
'''

from fastapi import FastAPI

app =  FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World!"}

'''
si queremos cambiar el puerto que nos asignan por defecto 
podemos hacer lo siguiente:

uvicorn nombre_del_archivo:app --reload --port numero_puerto

y si queremos que se vean en todos los dispositivos podemos
hacer lo sgte: 

uvicorn nombre_del_archivo:app --reload --port numero_puerto --host direccion_host{ip}
'''