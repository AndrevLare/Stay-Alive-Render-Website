import urllib.request
import json

# URL a la que quieres hacer la solicitud GET
url = "https://andrevlare.onrender.com"

try:
    # Hacer la solicitud GET
    with urllib.request.urlopen(url) as response:
        # Leer la respuesta y convertirla a formato JSON
        data = json.load(response)
        
        # Si llegamos aquí, la solicitud fue exitosa
        print("Solicitud exitosa! \n")
        # Aquí puedes hacer algo con los datos obtenidos, si lo deseas
        print(data)  # Esto imprime el contenido de la respuesta en formato JSON
        
except Exception as e:
    # Manejo de errores si la solicitud falla
    print(f"Ocurrió un error: {e} \n")
