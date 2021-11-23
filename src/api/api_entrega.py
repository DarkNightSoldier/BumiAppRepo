from cola_circular import ColaCircularDoble
from pedido import Pedido

cola_de_pedidos = None
estructura_de_datos = 1
file_data_clients = "../examples/pedidos.json"

#Funciones de la API que proveen funcionalidades CRUD sobre los usuarios

def seleccionar_estructura():
    if estructura_de_datos == 1:
        cola_de_pedidos = ColaCircularDoble

def descargar_pedidos_conductor(id_conductor):
    #Cargar a la cola los pedidos
    pass

def ver_pedido_proximo():
    #nodo = peek()
    #verpedido(nodo)
    pass

def entregar_pedido():
    #nodo = ColaCircularDoble.desencolar()
    #verpedido(nodo)
    pass