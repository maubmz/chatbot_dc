import mysql.connector
from fastapi import FastAPI

from metodos.Metodo_Openai import get_datos
from metodos.texto_A_lista import texto_lista

app = FastAPI()
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='M1x_2021',
    database='cliente'
)

cursor = connection.cursor()

@app.get("/prueba")
def get_mensaje():
    return "Buenas"

@app.post("/datos-texto")
def obtener_datos(texto: str):
    cadena = get_datos(texto)
    lista = texto_lista(cadena)
    return lista
