'''
FastApi tiene una documentacion automatizada con swagger, la 
cual va a describir cada uno de los endpoints que tiene 
nuestra aplicacion basandose en los estandares de openai 

para acceder a nuestra url con la documentacion hacemos lo 
sgte:

localhost/host_donde_encuentra/docs
'''

from fastapi import FastAPI

app =  FastAPI()
app.title = "Primera APP"
app.version = "0.0.1"
app.description = "FastAPI desde cero"


@app.get('/', tags= ["home"])
def read_root():
    return {"Hello": "World!"}

'''
tambien hay otra forma de hacer estos cambios de manera mas
simplificar el nombre y etc:
app =  FastAPI(title = "Primera APP", 
version = "0.0.1")
'''