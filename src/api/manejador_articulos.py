from ..estructuras.lista_circular_doble import ListaEnlazadaCircularDoble
from ..objetos.producto import Articulo
from flask import jsonify
import json

coleccion_de_articulos = ListaEnlazadaCircularDoble()
archivo_datos_productos = "../examples/articulos.json"


#Función que carga la base de datos de clientes del archivo JSON a la lista
def descargar_usuarios():
    #Del archivo_datos_usuarios, cargue todos los usuarios a un objeto de tipo Usuario
    f = open(archivo_datos_productos, 'rw')
    usuarios = json.loads(f.read())
    f.close()
    for id in usuarios:
        datos = usuarios[id].values()
        usuario = Usuario(id, *datos)
        coleccion_de_articulos.insertar_con_orden(usuario)

def cargar_usuarios():
    nuevo_archivo = ""

#Función que crea un nuevo cliente en la base de usuarios
def crear_nuevo_cliente(id,nombres,apellidos,contrasena,
    correo,ciudad,direccion,telefono,zip):
    """
    Función que crea un nuevo cliente

    Parámetros
    ----------
    id: int
        Documento de identidad del usuario
    nombres: string
        Nombres del usuario
    apellidos: string
        Apellidos del usuario
    contrasena: string
        Contraseña del usuario
    correo: string
        Correo del usuario
    ciudad: string
        Ciudad del usuario
    direccion: string
        Dirección de residencia del usuario
    telefono: int
        Teléfono del usuario
    zip: int
        Códido postal del usuario
    Retorna
    ----------
    200 si la inserción fue exitosa y 401 si no lo fue.
    """
    nuevo_cliente = Cliente(id,nombres,apellidos,contrasena,correo,
    ciudad,direccion,telefono,zip)
    #Se inserta al cliente en la colección de usuarios
    coleccion_de_usuarios.insertar_con_orden(nuevo_cliente)
    return jsonify({"message":"OK"},200) 

def crear_nuevo_funcionario(id,nombres,apellidos,contrasena,
    correo,ciudad,direccion,telefono,zip):
    """
    Función que crea un nuevo funcionario

    Parámetros
    ----------
    id: int
        Documento de identidad del usuario
    nombres: string
        Nombres del usuario
    apellidos: string
        Apellidos del usuario
    contrasena: string
        Contraseña del usuario
    correo: string
        Correo del usuario
    ciudad: string
        Ciudad del usuario
    direccion: string
        Dirección de residencia del usuario
    telefono: int
        Teléfono del usuario
    zip: int
        Códido postal del usuario
    Retorna
    ----------
    200 si la inserción fue exitosa y 401 si no lo fue.
    """    
    nuevo_funcionario = Funcionario(id,nombres,apellidos,contrasena,correo,
    ciudad,direccion,telefono,zip)
    #Se inserta al cliente en la colección de usuarios
    coleccion_de_usuarios.insertar_con_orden(nuevo_funcionario)
    return jsonify({"message":"OK"}),200

def ver_datos_usuario(id):
    usuario = coleccion_de_usuarios.buscar_nodo(id).dato
    return jsonify(usuario.obtener_dicc_usuario(),200)

def actualizar_datos_usuario(id,parametro,nuevo_dato):
    usuario = coleccion_de_usuarios.buscar_nodo(id).dato
    if parametro == 1:
        usuario.nombres = nuevo_dato
    elif parametro==2:
        usuario.apellidos = nuevo_dato
    elif parametro==3:
        usuario.contrasena = nuevo_dato
    elif parametro==4:
        usuario.correo = nuevo_dato
    elif parametro==5:
        usuario.ciudad = nuevo_dato
    elif parametro==6:
        usuario.direccion = nuevo_dato
    elif parametro==7:
        usuario.telefono = nuevo_dato
    elif parametro==8:
        usuario.zip = int(nuevo_dato)
    elif parametro==9:
        usuario.zip = int(nuevo_dato)
            
    return jsonify({"message":"OK"}),200


def eliminar_usuario(id):
    coleccion_de_usuarios.eliminar(id)
    return jsonify({"message":"OK"}),200

if __name__=="__main__":
    cargar_usuarios()
    crear_nuevo_cliente(1000182041,"Pepito","Perez","amoamimami","ola@ola.com","Bogotá",
                            "CL 57",3145897656,110141,)
    ver_datos_usuario(1000182041)