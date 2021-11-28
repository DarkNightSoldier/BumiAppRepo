import src
from flask import Flask, jsonify, request, make_response
from flask.helpers import send_from_directory 
from flask_cors import CORS
from src.estructuras.colas import ColaArrayBased
from src.estructuras.listas_enlazadas import ListaEnlazada, ListaEnlazadaConCola, ListaEnlazadaDoble
from src.objetos.usuario import Cliente, Funcionario
from src.objetos.producto import Articulo
from src.objetos.pedido import Pedido

articulos = ListaEnlazadaConCola()
usuarios = ListaEnlazadaDoble()
pedidos = ColaArrayBased()

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
    if isinstance(nodo, int): 
        jsonify({'mensaje' : "Este cliente ya existe."}), 401
    usuarios.empujar_atras(cliente)
    return jsonify({'status' : 200})

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
    setattr(nodo, atributo, valor)
    return jsonify({'status' : 200})

@app.route("/api/usuario/consultar_usuario", methods = ["POST"])
def consultar_usuario():
    data = request.values
    id = int(data["id"])
    objeto = usuarios.buscar_nodo(id)
    if isinstance(objeto, int): 
        return jsonify({'mensaje' : "El usuario no existe."}), 404
    data = {}
    data["id"] = objeto.id
    data["nombres"] = objeto.nombres
    data["apellidos"] = objeto.apellidos
    data["rol"] = objeto.rol
    data["contrasena"] = objeto.contrasena
    data["correo"] = objeto.correo
    data["ciudad"] = objeto.ciudad
    data["direccion"] = objeto.direccion
    data["telefono"] = objeto.telefono
    data["zip"] = objeto.zip
    data["pedidos"] = objeto.pedidos
    return jsonify({'status' : 200})

@app.route("/api/usuario/eliminar_usuario", methods = ["POST"])
def eliminar_usuario():
    data = request.values
    id = int(data["id"])
    try:
        usuarios.eliminar(id)
    except Exception as e: 
        return jsonify({'error' : str(e)}), 401
    return jsonify({'status' : 200})

@app.route("/api/articulo/crear_nuevo_articulo", methods = ["POST"])
def crear_nuevo_articulo():
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
    articulos.empujar_atras(articulo)
    return jsonify({'status' : 200})

@app.route("/api/articulo/actualizar_articulo", methods = ["POST"])
def actualizar_articulo():
    data = request.values
    id = data["id"]
    atributo = data["atributo"]
    valor = data["valor"]
    objeto = articulos.buscar_nodo(id)
    if isinstance(objeto, int): 
        return jsonify({'mensaje' : "El artículo no existe."}), 404
    setattr(objeto, atributo, valor)
    return jsonify({'status' : 200})

@app.route("/api/articulo/consultar_articulo", methods = ["POST"])
def consultar_articulo():
    data = request.values
    id = data["id"]
    objeto = articulos.buscar_nodo(id)
    if isinstance(objeto, int): 
        return jsonify({'mensaje' : "El usuario no existe."}), 404
    data = {}
    data["id"] = objeto.id
    data["nombre"] = objeto.nombre
    data["stock"] = objeto.stock
    data["url_img"] = objeto.url_img
    data["precio_antes_impuesto"] = objeto.precio_antes_impuesto
    data["impuesto_porcentaje"] = objeto.impuesto_porcentaje
    data["descuento"] = objeto.descuento
    return jsonify({'datos' : data})

@app.route("/api/articulo/eliminar_articulo", methods = ["POST"])
def eliminar_articulo():
    data = request.values
    id = data["id"]
    try:
        articulos.eliminar(id)
    except Exception as e: 
        return jsonify({'error' : str(e)}), 401
    return jsonify({'status' : 200})

@app.route("/api/pedido/crear_pedido", methods = ["POST"])
def crear_pedido():
    data = request.values
    id_pedido = data["id"]
    id_cliente = data["id_cliente"]
    pedido = Pedido(id_pedido, id_cliente)
    pedido.cargar_desde_diccionario(data)
    pedidos.encolar(pedido)
    return jsonify({'status' : 200})

@app.route("/api/pedido/consultar_pedido", methods = ["POST"])
def consultar_pedido():
    data = request.values
    id = data["id"]
    pedido = pedidos.buscar(id)
    if isinstance(pedido, int):
        return jsonify({'mensaje' : "Id no encontrado."}), 404
    datos = pedido.obtener_informacion()
    return jsonify({'datos' : datos})

@app.route("/api/pedido/eliminar_pedido", methods = ["POST"])
def eliminar_pedido():
    data = request.values
    id = data["id"]
    try:
        pedidos.eliminar(id)
        return jsonify({'status' : 200})
    except Exception as e: 
        return jsonify({'status' : str(e)})

@app.route("/api/pedido/actualizar_pedido", methods = ["POST"])
def actualizar_pedido():
    data = request.values
    id = data["id"]
    atributo = data["atributo"]
    valor = data["valor"]
    try:
        pedidos.actualizar_elemento(id, atributo, valor)
    except Exception as e: 
        return jsonify({"mensaje": str(e)})

@app.route("/api/pedido/mostrar_pedido_en_cola", methods = ["POST"])
def mostrar_pedido_en_cola():
    data = request.values
    try:
        pedido = pedidos.peek()
        datos = pedido.obtener_informacion()
        return jsonify({'datos' : datos})
    except:
        return jsonify({'status' : 200})

@app.route("/api/pedido/anadir_pedido_a_funcionario", methods = ["POST"])
def anadir_pedido_a_funcionario():
    data = request.values
    id = data["id"]
    return jsonify({'status' : 200})

@app.route("/api/pedido/marcar_pedido", methods = ["POST"])
def marcar_pedido():
    data = request.values
    id = data["id"]
    return jsonify({'status' : 200})

if __name__ == '__main__':
    app.run(debug=False)