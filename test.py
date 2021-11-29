from console import Consola
import json 
import time
consola = Consola()
filename = "./examples"
usuarios = json.load(filename + "/usuarios.json")
articulos = json.load(filename + "/articulos.json")
pedidos = json.load(filename + "/pedidos.json")
maximoDatos = 1000

def medir_tiempo(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return (end_time - start_time)

# Cargar datos:

def cargar_usuarios():
    # iterar sobre los ids.
    # extraer el mapa => **kwargs
    contador = 0
    for id in usuarios:
        kwargs = usuarios[id]
        kwargs["id"] = id
        consola.nuevo_cliente(**kwargs)

        # Limite de datos
        contador += 1
        if contador < maximoDatos:
            break

def cargar_articulos():
    contador = 0
    for id in articulos:
        kwargs = usuarios[id]
        kwargs["id"] = id
        consola.crear_articulo(**kwargs)

        # Limite de datos
        contador += 1
        if contador < maximoDatos:
            break

def cargar_pedidos():
    contador = 0
    for id in pedidos:
        kwargs = usuarios[id]
        kwargs["id"] = id
        consola.crear_pedido(**kwargs)

        contador += 1
        if contador < maximoDatos:
            break

# Buscar datos:

def buscar_usuario(id):
    kwargs = {"id": id}
    consola.consultar_usuario(**kwargs)

def buscar_pedido(id):
    kwargs = {"id": id}
    consola.consultar_pedido(**kwargs)    

def buscar_articulo(id):
    kwargs = {"id": id}
    consola.consultar_articulo(**kwargs)    

# Eliminar datos:

def eliminar_usuario(id):
    kwargs = {"id": id}
    consola.eliminar_usuario(**kwargs)

def eliminar_pedido(id):
    kwargs = {"id": id}
    consola.eliminar_pedido(**kwargs)

def eliminar_articulo(id):
    kwargs = {"id": id}
    consola.eliminar_articulo(**kwargs)

if __name__ == '__main__':
    print("Hello world.")
    
    tiempo = medir_tiempo(cargar_usuarios)
    
    print(tiempo)
    