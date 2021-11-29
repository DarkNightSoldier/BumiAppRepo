from faker import Faker
import random
import numpy as np 
from typing import List 
import json
fake = Faker()

def generar_usuario():
    datos = {}
    datos["nombres"] = fake.name().split(" ")[0]
    datos["apellidos"] = fake.name().split(" ")[1]
    datos["contrasena"] = fake.password()
    datos["correo"] = fake.email()
    datos["ciudad"] = np.random.choice(['Bogota','Miami','Cartagena','Madrid','Fusa','Choconta','Yopal','Funza','Facatativa','Cali','Medellin','Santa Marta'])
    datos["direccion"] = fake.address().replace("\n", " ")
    datos["telefono"] = random.randrange(10000000, 20000000)
    datos["zip"] = random.randrange(1000000, 2000000)
    return datos
     
def generar_articulo():
    import uuid
    u = uuid.uuid4()
    datos = {}
    datos["nombre"] = fake.name()
    datos["stock"] = random.randrange(10, 500)
    datos["url_img"] = "https://" + u.hex + ".png"
    datos["precio_antes_impuesto"] = random.randrange(20000, 50000)
    datos["impuesto_porcentaje"] = 0.19
    datos["descuento"] = random.random()
    return datos

def generar_pedido(id_pedido, id_cliente, id_funcionario):
    datos = {}
    datos["id_cliente"] = id_cliente
    datos["pedido_padre"] = id_pedido
    datos["id_conductor"] = id_funcionario
    datos["estado"] = np.random.choice(['Cancelado','Pendiente'])
    datos["frecuencia"] = int(random.randrange(1, 10))
    datos["productos"] = int(random.randrange(1, 10))
    datos["cantidades"] = int(random.randrange(1, 10))
    valor_productos = int(random.randrange(100000, 300000))
    datos["valor_producto_sin_impuestos"] = valor_productos
    datos["impuestos_productos"] = 0.19
    valor_descuentos = int(random.randrange(10000, 20000))
    datos["valor_descuentos"] = valor_descuentos
    datos["moneda"] = "COP"
    datos["subtotal"] = valor_productos - valor_descuentos
    datos["impuestos"] = datos["subtotal"] * 0.19
    datos["total"] = datos["subtotal"] * (1 + 0.19)
    return datos

def generar_id(ids: List):
    id = random.randrange(1000000000, 20000000000)
    while id in ids: 
        id = random.randrange(1000000000, 20000000000)
    ids.append(id)
    return ids, id

def generar_datos(num_data, func, optional_list = []):
    from copy import deepcopy
    print("FUNC: ", func)
    lista_ids = list()
    if len(optional_list) > 0:
        lista_ids = deepcopy(optional_list)
    datos = {}
    for i in range(num_data):
        dato = func()
        lista_ids, id = generar_id(lista_ids)
        datos[id] = dato
    #print(datos)
    return datos, lista_ids

def guardar_datos(filename, datos, folder = "./"):
    with open(folder + filename, 'w') as fp:
        json.dump(datos, fp)

if __name__ == '__main__':
    num_data = 100000

    clientes = {}
    funcionarios = {}
    articulos = {}
    pedidos = {}
    
    # Generar datos.
    clientes, ids_clientes = generar_datos(num_data, generar_usuario)
    guardar_datos("clientes.json", clientes, folder = "./datos2/")
    clientes = {}

    funcionarios, ids_funcionarios = generar_datos(1, generar_usuario, optional_list = ids_clientes)
    guardar_datos("funcionarios.json", funcionarios, folder = "./datos2/")
    funcionarios = {}

    ids_funcionarios = list(set(ids_funcionarios) - set(ids_clientes))
    articulos, ids_articulos = generar_datos(num_data, generar_articulo)
    guardar_datos("articulos.json", articulos, folder = "./datos2/")
    articulos = {}

    for i in range(num_data):
        id_random_cliente = int(np.random.choice(ids_clientes))
        id_random_funcionario = int(np.random.choice(ids_funcionarios))
        id_pedido = random.randrange(100000000, 2000000000)
        pedido = generar_pedido(id_pedido, id_random_cliente, id_random_funcionario)
        pedidos[id_pedido] = pedido
    guardar_datos("pedidos.json", pedidos, folder = "./datos2/")
    pedidos = {}