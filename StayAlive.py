import requests
import time
import random

# URL a la que quieres hacer la solicitud GET
url = "https://andrevlare.onrender.com"

# Bucle infinito para hacer la solicitud cada 2 a 3 minutos
while True:
    try:
        # Hacer la solicitud GET
        response = requests.get(url)

        # Comprobar el código de estado de la respuesta (200 significa éxito)
        if response.status_code == 200:
            print("Solicitud exitosa! \n")
        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code} \n")

    except Exception as e:
        print(f"Ocurrió un error: {e} \n")

    # Generar un intervalo aleatorio entre 120 y 180 segundos
    intervalo = random.uniform(120, 180)
    
    # Pausar el programa mostrando el tiempo restante
    for i in range(int(intervalo), 0, -1):
        print(f"Próxima solicitud en {i} segundos...", end="\r")
        time.sleep(1)