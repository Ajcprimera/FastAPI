from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query #El metodo path nos va a ayudar con las validaciones de parametros de ruta y el Query es para parametros query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from starlette.requests import Request #El jsonresponse es otro tipo de respuesta
import read_file
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any, Coroutine, Optional
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer #el httpbearer nos permitar autenticar el login del user

app =  FastAPI()
app.title = "Primera APP"
app.version = "0.0.1"
app.description = "FastAPI desde cero"

'''creamos la clase que nos va a ayudar a crear los esquema 
para las peliculas'''

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request): #creamos una funcion asincrona que accedera la peticion del login
        auth =  await super().__call__(request) #desde la clase superior llamamos al metodo call y le pasamos la peticion
        data = validate_token(auth.credentials) #validamos las credenciales del usuario para generar el token
        if data ['email'] != 'admin@gmail.com':
            raise HTTPException(status_code=403, detail='credenciales son invalidas')


#clase para que el usuario pueda loguearse
class User(BaseModel):
    email: str
    password: str

class Movie(BaseModel):
    id: Optional[int] = None
    title : str = Field(min_length=5, max_length = 15)
    '''title : str = Field(default = "mi pelicula", min_length=5, max_length = 15) 
    aqui estamos mostrando una breve descrpcion en la 
    interfaz para hacer saber al usuario que colocar'''
    overview : str = Field(min_length=10, max_length = 50)
    year : int = Field(ge = 2000, lt= 2030) 
    rating : int = Field(ge = 0, le = 10)
    category : str = Field(min_length=5, max_length = 15)
    
    #forma mas optima de crear un ejemplo de schema
    model_config ={
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi Pelicula",
                    "overview": "Descripcion de la pelicula",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción"
                }
            ]
        }}

    #https://fastapi.tiangolo.com/es/tutorial/path-params-numeric-validations/#recap
@app.get('/', tags= ["home"])
def read_root():
    #creamos un metodo get que nos retorna en formato html
    return HTMLResponse('<h1>Hola mundo usando HTML</h1>')

@app.get('/movies', tags= ["movies"], status_code= 200, dependencies= [Depends(JWTBearer())])#El status code no ayuda a retorna un codigo de respuesta exitoso en la api
#estamos creando la dependencia para generar la validacion del token y una vez autorizado se permite la extraccion de la data
def get_movies():
    #obtenemos el archivo json
    return JSONResponse(content=read_file.data)#muestra el contenido de la data
'''nota: No sería del todo necesario usar JSONResponse si
es que no es para un caso especifico.'''

#metodo para obtenerlos mediante su ruta
@app.get('/movies/{id}')#colocamos el parametro 
def get_movie(id : int = Path(ge=1, le=2000)):#la funcion recive el parametro para buscar el id
    movies = read_file.data
    movie = list(filter(lambda x: x['id'] == id,movies))#Aqui hacemos un filtrado de la lista para obtener la pelicula que deeseamos
    return movie if len(movie) > 0 else JSONResponse(status_code= 404, content= "movie no found")
    #return movie if len(movie) > 0 else "error: movie not found" #condicion en caso de no encontrar la pelicula

'''Un query parameter es un conjunto de parámetros opcionales 
los cuales son añadidos al finalizar la ruta, con el objetivo 
de definir contenido o acciones en la url, estos elementos se 
añaden después de un ?, para agregar más query parameters 
utilizamos &.'''
@app.get('/movies/', tags= ["movies"]) 
def get_movie(category : str = Query(min_length=4, max_length= 20)):
    movies = read_file.data
    movie = list(filter(lambda x: x['category'] == category,movies))
    return movie[0] if len(movie) > 0 else "error: movie not found"

@app.post('/movies', tags=["movies"])
def post_movie(movie: Movie):
    movies = read_file.data
    movies.append(movie)
    return movies

@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)

'''def post_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: int = Body(), category: str = Body()):
    movies = read_file.data
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category  
    })
    return movies'''

@app.delete('/movies/{id}', tags=["movies"])
def remove_movie(id: int):
    movies = read_file.data
    for i in movies:
        if i["id"]==id:
            movies.remove(i)
            return movies
'''esta es una forma mas ordenada y practicar de simplificar el 
codigo gracias a la creacion de esquemas con la libreria de 
pydantic
'''
@app.put('/movies/{id}', tags=["movies"])

def update_movie(id: int, movie: Movie):
    movies = read_file.data
    for i in movies:
        if i["id"]==id:
            i["id"] = movie.id
            i["title"] = movie.title
            i["overview"]= movie.overview
            i["year"] = movie.year
            i["rating"] = movie.rating
            i["category"]= movie.category  
            return movies


'''def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: int = Body(), category: str = Body()):
    movies = read_file.data
    for i in movies:
        if i["id"]==id:
            i["id"] = id
            i["title"] = title
            i["overview"]= overview
            i["year"] = year
            i["rating"] = rating
            i["category"]= category  
            return movies'''