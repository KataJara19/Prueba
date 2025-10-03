# Prueba

🛡️ API de Autenticación y Prueba de Fuerza Bruta
Este proyecto incluye un servidor de autenticación en FastAPI (main.py) y un script de ataque (ataqueapi.py) para probar la seguridad del login.

1. Ejecución del Servidor (API)
Requisitos
Asegúrate de tener Python y las siguientes librerías instaladas:

fastapi[standard]
sqlmodel
request

Pasos
Iniciar la API: Abre una terminal y ejecuta: fastapi dev 

Servidor Listo: La API estará corriendo en: http://127.0.0.1:8000

Credenciales de Prueba (BDD)
La API tiene estos usuarios precargados en main.py:

**Endpoint de Login:** `/login` (método POST)
* **Credenciales de Prueba (Base de Datos en Memoria):**
    | Usuario | Contraseña |
    | :--- | :--- |
    | `admin` | `123` |
    | `kata` | `345` |
    | `criss` | `AbC` |



🕵️ 2. Ejecución de la Prueba de Ataque
El script ataque.py intenta adivinar las contraseñas enviando combinaciones al endpoint /login.

Requisitos
Asegúrate de tener la librería requests instalada:

pip install requests

Pasos
Verificar el Objetivo: Abre el archivo ataque.py y ajusta la variable usuario_ataque (ej: "admin").

Lanzar el Ataque: Abre una segunda terminal y ejecuta: python ataque.py
