from fastapi import FastAPI 

app = FastAPI()
app.title = "Mi aplicacion con FastAPI movies"
app.version = "0.0.1"
@app.get('/', tags=["Home"]) 
def message ():
    return "Bootcamp Programacion Python pruebas 2024 132"