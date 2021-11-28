from console import Consola
import json 
import time
consola = Consola()
filename = "./examples"
usuarios = json.load(filename + "/usuarios.json")
articulos = json.load(filename + "/articulos.json")
pedidos = json.load(filename + "/pedidos.json")

def medir_tiempo(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return (end_time - start_time)

def cargar_usuarios():
    # iterar sobre los ids.
    # extraer el mapa => **kwargs
    consola.nuevo_cliente(**kwargs)

def cargar_articulos():
    pass

def cargar_pedidos():
    pass

kwargs = {}
consola.nuevo_cliente()

if __name__ == '__main__':
    print("Hello world.")
    tiempo = medir_tiempo(cargar_usuarios)
    print(tiempo)
    