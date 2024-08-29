from fastapi import FastAPI 

app = FastAPI()
app.title = "Mi aplicacion con FastAPI movies"
app.version = "0.0.1"
@app.get('/', tags=["Home"]) 
def message ():
    return "Bootcamp Programacion Python pruebas 2024 132"

from fastapi import FastAPI

app = FastAPI()

@app.get("E:\GitHubDesk\bootcamp-de-python\My-Movie-API")
def message():
    return {"message": "Hello World"}

from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 
app = FastAPI()
app.title = "Mi aplicacion con FastAPI movies"
app.version = "0.0.1"
movies_list = [
    {
        "id": 1,
        "title": "Matrix",
        "overview": "pelicula de ficcion ",
        "year": "2001",
        "rating": 9.5
    },
        {
            "id": 2,
            "title": "Juegos de Honor",
            "overview": "Un recuento inspirador sobre el entrenador de básquetbol Ken Carte",
            "year": "2005",
            "rating": 9.8
        }
    
]
@app.get('/', tags=["Home"]) 
def message ():
    #return {"Hello":"World"}
    return HTMLResponse('<h1>Hello World</h1>')
@app.get('/movies', tags = ["Movies"])
def movies():
    return movies_list


@app.get('/movies/{id}', tags = ["Movies"])
def get_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item
    return []