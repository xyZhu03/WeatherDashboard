import csv
import os

def leer_archivo(ruta_archivo):
    datos = []
    archivo_existe = os.path.isfile(ruta_archivo) and os.path.getsize(ruta_archivo) > 0
    if archivo_existe:
        with open(ruta_archivo, mode='r') as archivo:
            lector_csv = csv.reader(archivo)

            for fila in lector_csv:
                datos.append(fila)
    else: print("Historial vacio")
    return datos

def agregar_al_csv(ruta_archivo, datos_clima):
    columnas = [
        "city", "temperature", "feels_like", "min_temp",
        "max_temp", "description", "humidity", "wind_speed"
    ]

    archivo_existe = os.path.isfile(ruta_archivo) and os.path.getsize(ruta_archivo) > 0

    with open(ruta_archivo, mode='a', newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=columnas)

        if not archivo_existe:
            writer.writeheader()

        writer.writerow(datos_clima)