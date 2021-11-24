from ..estructuras.lista_circular_doble import ListaEnlazadaCircularDoble
from ..objetos.producto import Articulo

coleccion_de_articulos = None
estructura_de_datos = 1
file_data_products = "../examples/articulos.json"

#Funciones de la API que proveen funcionalidades CRUD sobre el manejo de usuarios

def seleccionar_estructura():
    if estructura_de_datos == 1:
        coleccion_de_articulos = ListaEnlazadaCircularDoble()

#Función que carga la base de datos de productos del archivo JSON a la lista
def descargar_productos():
    #Del file_data_products, cargue todos los articulos a un objeto de tipo Articulo
    pass

def crear_nuevo_producto(id):
    pass

def eliminar_producto(id):
    pass

def actualizar_productos(id):
    pass

def ver_producto(id):
    #Generar JSON del artículo
    pass