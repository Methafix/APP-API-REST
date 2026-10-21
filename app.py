# Nombre: Felipe Verdugo Ávila
# Aplicación API-REST

import requests

# API de productos de DummyJSON
BASE_URL = "https://dummyjson.com/products"

def mostrar_respuesta(respuesta):
    # Mostrar el código HTTP y los datos recibidos
    print("Código HTTP", respuesta.status_code)

    if respuesta.text:
        print("Respuesta JSON:")
        print(respuesta.json())
    else:
        print("La respuesta no tiene datos")

try:
    # ===========================
    # GET: CONSULTAR UN PRODUCTO
    # ===========================

    respuesta = requests.get(
        f"{BASE_URL}/3001",
        timeout = 10
    )

    respuesta.raise_for_status()
    producto = respuesta.json()

    print("Producto:", producto["title"])
    print("Precio:", producto["price"])
    print("Categoría:", producto["category"])

    # ===========================
    # METODO POST
    # ===========================

except requests.exceptions.Timeout:
    print("Error: Se agotó el tiempo de espera")