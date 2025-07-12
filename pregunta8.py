import requests
import zipfile
import os

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
nombre_imagen = "imagen_descargada.jpg"

try:
    response = requests.get(url)
    response.raise_for_status()
    with open(nombre_imagen, "wb") as file:
        file.write(response.content)
    print("Imagen descargada correctamente.")
except requests.RequestException as e:
    print("Error al descargar la imagen:", e)

nombre_zip = "imagen_comprimida.zip"

with zipfile.ZipFile(nombre_zip, "w") as zipf:
    zipf.write(nombre_imagen)
    print("Imagen comprimida en archivo zip.")

directorio_destino = "imagen_extraida"

if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)
with zipfile.ZipFile(nombre_zip, "r") as zipf:
    zipf.extractall(directorio_destino)
    print(f"Imagen extraída en la carpeta '{directorio_destino}'.")
