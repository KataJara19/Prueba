from fastapi import FastAPI, status
from sqlmodel import SQLModel


class UsuarioBD(SQLModel):
    
    id: int 
    nombre_usuario: str
    email: str 
    activo: bool
    contrasena: str 
 

class UsuarioNuevo(SQLModel):
    nombre_usuario: str
    email: str
    contrasena: str

 
 
class Credenciales (SQLModel):
    nombre_usuario: str
    contrasena: str   
    
        
    
BDD = [
    
    UsuarioBD(id=1, nombre_usuario="admin", email="admin@uide.com", activo=True, contrasena="123"), 
    
    UsuarioBD(id=2, nombre_usuario="kata", email="kata@uide.com", activo=True, contrasena="345") ,
    
    UsuarioBD(id=3, nombre_usuario="katty", email="katty@uide.com", activo=True, contrasena="123") ,
    
    UsuarioBD(id=4, nombre_usuario="criss", email="criss@uide.com", activo=True, contrasena="AbC") ,
]



app = FastAPI()

#Crud

# Crear 

@app.post("/usuarios/")

def crear_usuario(datos: UsuarioNuevo):
    
    for usr in BDD:
        if usr.nombre_usuario == datos.nombre_usuario:
            return {"mensaje": "Ha ocurrido un error, el usuario ya existe"}

    
    nuevo_id = len(BDD) + 1 
        
    nuevo_usr = UsuarioBD(
        id=nuevo_id,
        nombre_usuario=datos.nombre_usuario,
        email=datos.email,
        activo=True,
        contrasena=datos.contrasena
    )
    
    BDD.append(nuevo_usr)
    
    
    return nuevo_usr


# Leer

@app.get("/usuarios/")

def leer_usuarios():
    return BDD


@app.get("/usuarios/{id_usr}")

def obtener_usuario(id_usr: int):
    
    for usr in BDD:
        if usr.id == id_usr:
            return usr
    
    return {"mensaje": f" el usuario con ID {id_usr} no se ha encontrado"}


# Actualizar


@app.put("/usuarios/{id_usr}")

def actualizar_usuario(id_usr: int, datos: UsuarioNuevo):
    
    for usr in BDD:
        if usr.id == id_usr:
                      
            usr.nombre_usuario = datos.nombre_usuario
            usr.email = datos.email
          
            return usr
    
    return {"mensaje": f"El usuario con ID {id_usr} no se ha encontrado"}




# Borrar

@app.delete("/usuarios/{id_usr}")

def eliminar_usuario(id_usr: int):
    
    for usr in BDD:
        if usr.id == id_usr:
            BDD.remove(usr)
            return {"mensaje": f"El usuario con ID {id_usr} ha sido eliminado"}
    
    return {"mensaje": f"El usuario con ID {id_usr} no se ha encontrado"}


# Login

@app.post("/login")

def verificarLogin(datos: Credenciales):
    
    for usuario in BDD:
        
        if usuario.nombre_usuario == datos.nombre_usuario and usuario.contrasena == datos.contrasena:
            return status.HTTP_200_OK       
    return status.HTTP_401_UNAUTHORIZED
    