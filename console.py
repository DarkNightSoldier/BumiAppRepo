import os
import json
import requests 
import pyfiglet
import time
#from src.api.usuarios import ver_datos_usuario
#from src.objetos.usuario import Usuario
#from src.objetos.pedido import Pedido
#from src.objetos.producto import Articulo
#welcome = pyfiglet.figlet_format("Welcome to Bumi!")
#print(welcome)

class Consola:
    
    def __init__(self, endpoint = "http://localhost:5000"):
        self.endpoint = endpoint
        self.opciones = {
            1: self.nuevo_cliente,
            2: self.nuevo_funcionario, 
            3: self.actualizar_usuario,
            4: self.consultar_usuario,
            5: self.eliminar_usuario,
            6: self.crear_articulo,
            7: self.actualizar_articulo,
            8: self.consultar_articulo,
            9: self.eliminar_articulo,
            10: self.crear_pedido,
            11: self.consultar_pedido,
            12: self.eliminar_pedido,
            13: self.actualizar_pedido,
            14: self.mostrar_pedido_cola,
            15: self.anadir_pedido_funcionario,
            16: self.marcar_pedido_entregado,
            17: self.nuevo_cliente_hash,
            18: self.consultar_cliente_hash,
            19: self.clear,
        }
        bienvenida = pyfiglet.figlet_format("Te damos la bienvenida a Bumi!")
        print(bienvenida)

    def menu(self):
        print("1. Crear cliente.")
        print("2. Crear nuevo funcionario")
        print("3. Actualizar usuario")
        print("4. Consultar usuario")
        print("5. Eliminar usuario")
        print("6. Crear artículo")
        print("7. Actualizar artículo")
        print("8. Consultar artículo")
        print("9. Eliminar artículo")
        print("10. Crear pedido")
        print("11. Consultar pedido")
        print("12. Eliminar pedido")
        print("13. Actualizar pedido")
        print("14. Mostrar pedido en cola")
        print("15. Añadir pedido a funcionario")
        print("16. Marca pedido como entregado")
        print("17. Agregar cliente con tabla hash")
        print("18. Consultar cliente con tabla hash")
        print("19. Limpiar Consola")
        print("20. Salir de la consola")
        print("")
        seleccion = int(input("Digite una opción: "))
        print("")
        if seleccion != 20:
            self.opciones[seleccion]()
            self.menu()
        else: 
            print("Hasta pronto!")

    def clear(self):
        # Limpia la consola
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def ingresar_info_usuario(self):
        kwargs = {}
        kwargs["id"] = input("Digite el id del cliente: ")
        kwargs["nombres"] = input("Digite el nombre del cliente: ")
        kwargs["apellidos"] = input("Digite el apellidos del cliente: ")
        kwargs["contrasena"] = input("Digite el contrasena del cliente: ")
        kwargs["correo"] = input("Digite el correo del cliente: ")
        kwargs["ciudad"] = input("Digite el ciudad del cliente: ")
        kwargs["direccion"] = input("Digite el direccion del cliente: ")
        kwargs["telefono"] = input("Digite el telefono del cliente: ")
        kwargs["zip"] = input("Digite el zip del cliente: ")
        return kwargs

    def ingresar_info_articulo(self):
        kwargs = {}
        kwargs["id"] = input("Digite el Id del artículo: ")
        kwargs["nombre"] = input("Digite el nombre del artículo: ")
        kwargs["stock"] = input("Digite el stock del artículo: ")
        kwargs["url_img"] = input("Digite url de la imagen del artículo: ")
        kwargs["precio_antes_impuesto"] = input("Digite el precio antes de impuestos: ")
        kwargs["impuesto_porcentaje"] = input("Digite el porcentaje a pagar en impuestos: ")
        kwargs["descuento"] = input("Digite el descuento del artículo: ")
        return kwargs

    def ingresar_info_pedido(self):
        kwargs = {}
        kwargs["id"] = input("Digite el Id del pedido: ")
        kwargs["id_cliente"] = input("Digite el Id del cliente: ")
        kwargs["pedido_padre"] = kwargs["id"]
        kwargs["id_conductor"] = input("Digite el id del conductor: ")
        kwargs["estado"] = input("Digite el estado del pedido: ")
        kwargs["frecuencia"] = input("Digite la frecuencia del pedido: ")
        kwargs["productos"] = input("Digite los productos: ")
        kwargs["cantidades"] = input("Digite las cantidades: ")
        kwargs["valor_producto_sin_impuestos"] = input("Digite el valor de los productos sin impuesto: ")
        kwargs["impuestos_productos"] = input("Digite los impuestos de los productos: ")
        kwargs["valor_descuentos"] = input("Digite el valor de los descuentos: ")
        kwargs["moneda"] = input("Digite la moneda del pedido: ")
        kwargs["subtotal"] = input("Digite el subtotal del pedido: ")
        kwargs["impuestos"] = input("Digite los impuestos del pedido: ")
        kwargs["total"] = input("Digite el total del pedido: ")
        return kwargs

    def procesar_respuesta(self, res):
        if res.status_code != 200: 
            res = res.json()
            error = res["mensaje"]
            print(error)
            return 500
        else: 
            print("Solicitud ejecutada exitosamente.")
            return 200

    # Nuevo cliente
    def nuevo_cliente_hash(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs = self.ingresar_info_usuario()
        res = requests.post(self.endpoint + "/api/usuario/nuevo_cliente_hash", kwargs)
        self.procesar_respuesta(res)

    # Nuevo cliente
    def nuevo_cliente(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs = self.ingresar_info_usuario()
        res = requests.post(self.endpoint + "/api/usuario/nuevo_cliente", kwargs)
        self.procesar_respuesta(res)

    # Nuevo funcionario
    def nuevo_funcionario(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs = self.ingresar_info_usuario()
        res = requests.post(self.endpoint + "/api/usuario/nuevo_funcionario", kwargs)
        self.procesar_respuesta(res)

    # Actualizar usuario.
    def actualizar_usuario(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs = {}
            kwargs["id"] = input("Digite el id del usuario: ")
            kwargs["atributo"] = input("Digite el nombre del atributo a modificar: ")
            kwargs["valor"] = input("Digite el nuevo valor del atributo: ")
        res = requests.post(self.endpoint + "/api/usuario/actualizar_usuario", kwargs)
        self.procesar_respuesta(res)

    # Consultar usuario.
    def consultar_usuario(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del usuario: ")
        res = requests.post(self.endpoint + "/api/usuario/consultar_usuario", kwargs)
        status = self.procesar_respuesta(res)
        if status == 200:
            res = res.json()
            for key, value in res.items():
                print(key, ': ', value)

    # Consultar usuario.
    def consultar_cliente_hash(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del usuario: ")
        res = requests.post(self.endpoint + "/api/usuario/consultar_cliente_hash", kwargs)
        status = self.procesar_respuesta(res)
        if status == 200:
            res = res.json()
            for key, value in res.items():
                print(key, ': ', value)

    # Eliminar usuario.
    def eliminar_usuario(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del usuario: ")
        res = requests.post(self.endpoint + "/api/usuario/eliminar_usuario", kwargs)
        self.procesar_respuesta(res)

    # Crear artículo.
    def crear_articulo(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs = self.ingresar_info_articulo()
        res = requests.post(self.endpoint + "/api/articulo/crear_nuevo_articulo", kwargs)
        self.procesar_respuesta(res)

    # Actualizar artículo.
    def actualizar_articulo(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs = {}
            kwargs["id"] = input("Digite el id del articulo:")
            kwargs["atributo"] = input("Digite el nombre del atributo a modificar: ")
            kwargs["valor"] = input("Digite el nuevo valor del atributo: ")
        res = requests.post(self.endpoint + "/api/articulo/actualizar_articulo", kwargs)
        self.procesar_respuesta(res)

    # Consultar artículo.
    def consultar_articulo(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del artículo: ")
        res = requests.post(self.endpoint + "/api/articulo/consultar_articulo", kwargs)
        status = self.procesar_respuesta(res)
        if status == 200:
            res = res.json()
            for key, value in res.items():
                print(key, ': ', value)

    # Eliminar artículo.
    def eliminar_articulo(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del artículo: ")
        res = requests.post(self.endpoint + "/api/articulo/eliminar_articulo", kwargs)
        self.procesar_respuesta(res)

    # Crear pe17dido.
    def crear_pedido(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs = self.ingresar_info_pedido()
        res = requests.post(self.endpoint + "/api/pedido/crear_pedido", kwargs)
        self.procesar_respuesta(res)

    # Consultar pedido.
    def consultar_pedido(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del pedido: ")
        res = requests.post(self.endpoint + "/api/pedido/consultar_pedido", kwargs)
        status = self.procesar_respuesta(res)
        if status == 200:
            res = res.json()
            for key, value in res.items():
                print(key, ': ', value)

    # Eliminar pedido.
    def eliminar_pedido(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del pedido: ")
        res = requests.post(self.endpoint + "/api/pedido/eliminar_pedido", kwargs)
        self.procesar_respuesta(res)

    # Actualizar pedido.
    def actualizar_pedido(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs = {}
            kwargs["id"] = input("Digite el id del pedido: ")
            kwargs["atributo"] = input("Digite el nombre del atributo a modificar: ")
            kwargs["valor"] = input("Digite el nuevo valor del atributo: ")
        res = requests.post(self.endpoint + "/api/pedido/actualizar_pedido", kwargs)
        self.procesar_respuesta(res)

    # Mostrar pedido en la cola.
    def mostrar_pedido_cola(self, **kwargs):
        res = requests.get(self.endpoint + "/api/pedido/mostrar_pedido_en_cola")
        status = self.procesar_respuesta(res)
        if status == 200:
            res = res.json()
            for key, value in res.items():
                print(key, ': ', value)

    # Añadir pedido a funcionario.
    def anadir_pedido_funcionario(self, **kwargs):
        pass

    # Marcar pedido como entregado.
    def marcar_pedido_entregado(self, **kwargs):
        pass

    def limpiar_datos(self):
        res = requests.get(self.endpoint + "/api/limpiar_datos")
        self.procesar_respuesta(res)


endpoint = "http://localhost:5000"
gui = Consola(endpoint = endpoint)
gui.menu()


#guy.iniciar_sesion()
#guy.guardar_usuario()
#guy.eliminar_usuario(100000)
#guy.editar_usuario(100000)

#guy.buscar_usuario(100000).mostrar()

#guy.cerrar_sesion()