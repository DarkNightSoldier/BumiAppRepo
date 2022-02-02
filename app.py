import src
from flask import Flask, jsonify, request, make_response
from flask.helpers import send_from_directory 
from flask_cors import CORS
from src.estructuras.arbol_bst import ArbolBST
from src.estructuras.arbol_avl import ArbolAVL
from src.estructuras.colas import ColaArrayBased
from src.estructuras.listas_enlazadas import ListaEnlazada, ListaEnlazadaConCola, ListaEnlazadaDoble
from src.objetos.usuario import Cliente, Funcionario
from src.objetos.producto import Articulo
from src.objetos.pedido import Pedido
from src.estructuras.lista_circular_doble import ListaEnlazadaCircularDoble
from src.estructuras.hash import Map

articulos = ArbolBST()
usuarios = ListaEnlazada()
pedidos = ListaEnlazadaDoble()

# Ini app.
app = Flask(__name__)

# Cors.
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('./static', path)

# Main page.
@app.route('/')
def root():
    """
    Return the frontend of the application.
    """
    return send_from_directory("./static", 'index.html')

@app.route("/api/status", methods = ["GET"])
def status():
    """
    App Status
    """
    return jsonify({'status' : 200})

@app.route("/api/usuario/nuevo_cliente", methods = ["POST"])


def nuevo_cliente():
    data = request.values
    id = int(data["id"])
    nombres = data["nombres"]
    apellidos = data["apellidos"]
    contrasena = data["contrasena"]
    correo = data["correo"]
    ciudad = data["ciudad"]
    direccion = data["direccion"]
    telefono = data["telefono"]
    zip = data["zip"]
    cliente = Cliente(id, nombres, apellidos, contrasena, correo, ciudad, direccion, 
                    telefono, zip)
    nodo = usuarios.buscar_nodo(id)
    usuarios.empujar_atras(cliente)
    return jsonify({'status' : 200})

@app.route("/api/usuario/nuevo_funcionario",methods = ["POST"])
def nuevo_funcionario_hash():
    data = request.values
    id = int(data["id"])
    nombres = data["nombres"]
    apellidos = data["apellidos"]
    contrasena = data["contrasena"]
    correo = data["correo"]
    ciudad = data["ciudad"]
    direccion = data["direccion"]
    telefono = data["telefono"]
    zip = data["zip"]
    funcionario = Funcionario(id, nombres, apellidos, contrasena, correo, ciudad, direccion, 
                    telefono, zip)
    # Añadir a tabla Hash
    


@app.route("/api/usuario/nuevo_funcionario", methods = ["POST"])
def nuevo_funcionario():
    """
    Descripción: Insertar un nuevo funcionario en la colección de clientes de Bumi.
    """
    data = request.values
    id = int(data["id"])
    nombres = data["nombres"]
    apellidos = data["apellidos"]
    contrasena = data["contrasena"]
    correo = data["correo"]
    ciudad = data["ciudad"]
    direccion = data["direccion"]
    telefono = data["telefono"]
    zip = data["zip"]
    funcionario = Funcionario(id, nombres, apellidos, contrasena, correo, ciudad, direccion, 
                    telefono, zip)
    nodo = usuarios.buscar_nodo(id)
    if isinstance(nodo, int): 
        jsonify({'mensaje' : "Este funcionario ya existe."}), 401
    usuarios.empujar_atras(funcionario)
    return jsonify({'status' : 200})

@app.route("/api/usuario/actualizar_usuario", methods = ["POST"])
def actualizar_usuario():
    data = request.values
    id = int(data["id"])
    atributo = data["atributo"]
    valor = data["valor"]
    nodo = usuarios.buscar_nodo(id)
    if isinstance(nodo, int): 
        return jsonify({'mensaje' : "El usuario no existe."}), 404
    setattr(nodo.dato, atributo, valor)
    return jsonify({'status' : 200})

@app.route("/api/usuario/consultar_usuario", methods = ["POST"])
def consultar_usuario():
    data = request.values
    id = int(data["id"])
    objeto = usuarios.buscar_nodo(id)
    if isinstance(objeto, int): 
        return jsonify({'mensaje' : "El usuario no existe."}), 404
    data = {}
    data["id"] = objeto.dato.id
    data["nombres"] = objeto.dato.nombres
    data["apellidos"] = objeto.dato.apellidos
    data["rol"] = objeto.dato.rol
    data["contrasena"] = objeto.dato.contrasena
    data["correo"] = objeto.dato.correo
    data["ciudad"] = objeto.dato.ciudad
    data["direccion"] = objeto.dato.direccion
    data["telefono"] = objeto.dato.telefono
    data["zip"] = objeto.dato.zip
    data["pedidos"] = objeto.dato.pedidos.imprimir()
    return jsonify(data), 200

@app.route("/api/usuario/eliminar_usuario", methods = ["POST"])
def eliminar_usuario():
    data = request.values
    id = int(data["id"])
    try:
        usuarios.eliminar(id)
    except: 
        return jsonify({'status' : 401})
    return jsonify({'status' : 200})

@app.route("/api/articulo/crear_nuevo_articulo", methods = ["POST", "GET"])
def crear_nuevo_articulo():
    data = request.get_json()
    if data == None: 
       data = request.values
    id = int(data["id"])
    nodo = articulos.buscar_nodo(id)
    if not isinstance(nodo, int):
        return jsonify({'mensaje' : "El artículo ya existe."}), 401
    nombre = data["nombre"]
    stock = data["stock"]
    url_img = data["url_img"]
    precio_antes_impuesto = data["precio_antes_impuesto"] 
    impuesto_porcentaje = data["impuesto_porcentaje"]
    descuento = data["descuento"]
    articulo = Articulo(id, nombre, stock, url_img, precio_antes_impuesto, impuesto_porcentaje, descuento)
    articulos.insertar(articulo)
    return jsonify({'status' : 200})

@app.route("/api/articulo/actualizar_articulo", methods = ["POST"])
def actualizar_articulo():
    data = request.values
    id = int(data["id"])
    atributo = data["atributo"]
    valor = data["valor"]
    objeto = articulos.buscar_nodo(id)
    if isinstance(objeto, int): 
        return jsonify({'mensaje' : "El artículo no existe."}), 404
    setattr(objeto.dato, atributo, valor)
    return jsonify({'status' : 200})

@app.route("/api/articulo/consultar_articulo", methods = ["POST", "GET"])
def consultar_articulo():
    print("CONSULTAR ARTICULO")
    data = request.get_json()
    if data == None: 
       data = request.values
    id = int(data["id"])
    objeto = articulos.buscar_nodo(id)
    if isinstance(objeto, int): 
        return jsonify({'mensaje' : "El artículo no existe."}), 404
    data = {}
    data["id"] = objeto.dato.id
    data["nombre"] = objeto.dato.nombre
    data["stock"] = objeto.dato.stock
    data["url_img"] = objeto.dato.url_img
    data["precio_antes_impuesto"] = objeto.dato.precio_antes_impuesto
    data["impuesto_porcentaje"] = objeto.dato.impuesto_porcentaje
    data["descuento"] = objeto.dato.descuento
    return jsonify({'datos' : data})

@app.route("/api/articulo/eliminar_articulo", methods = ["POST"])
def eliminar_articulo():
    data = request.values
    id = int(data["id"])
    try:
        articulos.eliminar(id)
    except Exception as e: 
        return jsonify({'error' : str(e)}), 401
    return jsonify({'status' : 200})

@app.route("/api/pedido/crear_pedido", methods = ["POST"])
def crear_pedido():
    data = request.values
    id_pedido = int(data["id"])
    id_cliente = int(data["id_cliente"])
    pedido = Pedido(id_pedido, id_cliente)
    pedido.cargar_desde_diccionario(data)
    pedidos.empujar_atras(pedido)
    return jsonify({'status' : 200})

@app.route("/api/pedido/consultar_pedido", methods = ["POST"])
def consultar_pedido():
    data = request.values
    id = int(data["id"])
    pedido = pedidos.buscar_nodo(id)
    if isinstance(pedido, int):
        return jsonify({'mensaje' : "Id no encontrado."}), 404
    datos = pedido.dato.obtener_informacion()
    return jsonify({'datos' : datos})

@app.route("/api/pedido/eliminar_pedido", methods = ["POST"])
def eliminar_pedido():
    data = request.values
    id = int(data["id"])
    try:
        pedidos.eliminar(id)
    except Exception as e: 
        return jsonify({'error' : str(e)}), 401
    return jsonify({'status' : 200})


@app.route("/api/pedido/actualizar_pedido", methods = ["POST"])
def actualizar_pedido():
    data = request.values
    id = int(data["id"])
    atributo = data["atributo"]
    valor = data["valor"]
    objeto = pedidos.buscar_nodo(id)
    if isinstance(objeto, int): 
        return jsonify({'mensaje' : "El pedido no existe."}), 404
    setattr(objeto.dato, atributo, valor)
    return jsonify({'status' : 200})

@app.route("/api/pedido/mostrar_pedido_en_cola", methods = ["POST"])
def mostrar_pedido_en_cola():
    data = request.values
    id = int(data["id_funcionario"])
    nodo_conductor = usuarios.buscar_nodo(id)
    try:
        pedido = nodo_conductor.dato.pedidos.peek()
        datos = pedido.obtener_informacion()
        return jsonify({'datos' : datos}), 200
    except:
        return jsonify({'status' : 400}), 400

@app.route("/api/pedido/anadir_pedido_a_funcionario", methods = ["POST"])
def anadir_pedido_a_funcionario():
    data = request.values
    id_pedido = int(data["id_pedido"])
    id_funcionario = int(data["id_funcionario"])
    pedido = pedidos.buscar_nodo(id_pedido)
    if isinstance(pedido, int):
        return jsonify({'mensaje' : "El id no existe."})
    funcionario = usuarios.buscar_nodo(int(id_funcionario)).dato
    funcionario.pedidos.encolar(pedido.dato)
    return jsonify({'status' : 200})

#Desencola y marca el pedido como entregado/no entregado
@app.route("/api/pedido/marcar_pedido", methods = ["POST"])
def marcar_pedido():
    data = request.values
    id_funcionario = int(data["id_funcionario"])
    valor = data["valor"]
    nodo_conductor = usuarios.buscar_nodo(id_funcionario)
    try:
        pedido = nodo_conductor.dato.pedidos.peek()
        pedido_en_lista = pedidos.buscar_nodo(pedido.id)
        if isinstance(pedido_en_lista, int): 
            return jsonify({'mensaje' : "El pedido no existe."}), 404
        setattr(pedido_en_lista.dato,"estado", valor)
        dato_pedido = nodo_conductor.dato.pedidos.desencolar()
        return jsonify({'status' : 200})
    except:
        return jsonify({'status' : 400}), 400

@app.route("/api/limpiar_datos", methods = ["GET"])
def limpiar_datos():
    articulos = ListaEnlazadaConCola()
    usuarios = ListaEnlazadaDoble()
    pedidos = ListaEnlazadaDoble()
    return jsonify({'status' : 200})

@app.route("/api/crear_usuario_hash",methods = ["POST"])

def crear_usuario_hash():
    print("Hello")
    dicc: Map = Map() # Implementacion con un Map de Usuario
    dicc.add()
    print("Acabo")


if __name__ == '__main__':
    app.run(port=5000, debug=False)