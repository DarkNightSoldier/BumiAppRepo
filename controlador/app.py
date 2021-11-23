"""
Si quieren cambiar la lista que estan utilizando,
solo deben cambiar el import y la asignacion a TipoLista
"""

# Utilidades
import os.path
import json
from typing import final
from utilidades.singleton import Singleton
from utilidades.listas import ListaEnlazada

TipoLista = ListaEnlazada

# Clases del modelo
from modelo.usuario import Usuario
from modelo.producto import Producto
from modelo.pedido import Pedido
from modelo.subpedido import Subpedido

# Clases de la vista
from vista.consola import Consola

# Datos
clases = ['usuario',
    'pedido',
    'producto']
subclases = ['subpedido']
base_DIR = os.path.dirname(os.path.abspath(__file__))

opcionesClases = {'usuario': Usuario,
    'pedido': Pedido,
    'producto': Producto,
    'subpedido': Subpedido}

# App debe ser una singleton
class App(metaclass=Singleton):

    def __init__(self):
        self.usuario = TipoLista()
        self.pedido = TipoLista()
        self.producto = TipoLista()
        self.consola = Consola()
        self.traer_datos()
    
    # Operaciones de modelo:

    def traer_datos(self):
        """
        Se traen los datos de la base de datos...
        En este caso, de los JSON
        """
        Subclases = {}
        for subclase in subclases:
            Subclases[subclase] = []
            final_path = os.path.join(os.path.dirname(base_DIR), f"Data/{subclase}.json")
            archivo = open(final_path, 'r', encoding = "utf-8")
            lista_de_datos = json.loads(archivo.read())
            archivo.close()
            for id in lista_de_datos:
                nuevo_dato = opcionesClases[subclase].convertir_JSON(opcionesClases[subclase], id, lista_de_datos[id])
                Subclases[subclase].append(nuevo_dato)

        for clase in clases:
            final_path = os.path.join(os.path.dirname(base_DIR), f"Data/{clase}.json")
            archivo = open(final_path, 'r', encoding = "utf-8")
            lista_de_datos = json.loads(archivo.read())
            archivo.close()
            for id in lista_de_datos:
                argumentos_JSON = [opcionesClases[clase], id, lista_de_datos[id]]
                if 'sub' + clase in Subclases:
                    argumentos_JSON.append(Subclases['sub' + clase])
                nuevo_dato = opcionesClases[clase].convertir_JSON(*argumentos_JSON)
                self.__dict__[clase].insertar_con_orden(nuevo_dato)
    
    # Operaciones de vista:
    def bienvenida(self):
        self.consola.mensaje_bienvenida(self)

    def verificar_sesion(self, id, contrasena):
        return self.consola.verificar_sesion(id, contrasena, self.usuario)
    
    def cerrar_sesion(self):
        return self.consola.cerrar_sesion()