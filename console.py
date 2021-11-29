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

def clear():
    # Limpia la consola
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

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
        print("17. Salir de la consola")
        print("")
        seleccion = int(input("Digite una opción: "))
        print("")
        if seleccion != 17:
            self.opciones[seleccion]()
            self.menu()
        else: 
            print("Hasta pronto!")

    def ingresar_info_usuario(self):
        kwargs = {}
        kwargs["id"] = input("Digite el id del cliente")
        kwargs["nombres"] = input("Digite el nombre del cliente")
        kwargs["apellidos"] = input("Digite el nombre del cliente")
        kwargs["contrasena"] = input("Digite el nombre del cliente")
        kwargs["correo"] = input("Digite el nombre del cliente")
        kwargs["ciudad"] = input("Digite el nombre del cliente")
        kwargs["direccion"] = input("Digite el nombre del cliente")
        kwargs["telefono"] = input("Digite el nombre del cliente")
        kwargs["zip"] = input("Digite el nombre del cliente")
        return kwargs

    def ingresar_info_articulo(self):
        kwargs = {}
        kwargs["id"] = input("Digite el Id del artículo")
        kwargs["nombre"] = input("Digite el nombre del artículo")
        kwargs["stock"] = input("Digite el stock del artículo")
        kwargs["url_img"] = input("Digite url de la imagen del artículo")
        kwargs["precio_antes_impuesto"] = input("Digite el precio antes de impuestos")
        kwargs["impuesto_porcentaje"] = input("Digite el porcentaje a pagar en impuestos")
        kwargs["descuento"] = input("Digite el descuento del artículo")

    def ingresar_info_pedido(self):
        kwargs = {}
        kwargs["id"] = input("Digite el Id del pedido")
        kwargs["id_cliente"] = input("Digite el Id del cliente")
        kwargs["pedido_padre"] = kwargs["id"]
        kwargs["id_conductor"] = input("Digite el id del conductor")
        kwargs["estado"] = input("Digite el estado del pedido")
        kwargs["frecuencia"] = input("Digite la frecuencia del pedido")
        kwargs["productos"] = input("Digite los productos")
        kwargs["cantidades"] = input("Digite las cantidades")
        kwargs["valor_producto_sin_impuestos"] = input("Digite el valor de los productos sin impuesto")
        kwargs["impuestos_productos"] = input("Digite los impuestos de los productos")
        kwargs["valor_descuentos"] = input("Digite el valor de los descuentos")
        kwargs["moneda"] = input("Digite la moneda del pedido")
        kwargs["subtotal"] = input("Digite el subtotal del pedido")
        kwargs["impuestos"] = input("Digite los impuestos del pedido")
        kwargs["total"] = input("Digite el total del pedido")

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
            kwargs["id"] = input("Digite el id del usuario")
            kwargs["atributo"] = input("Digite el nombre del atributo a modificar")
            kwargs["valor"] = input("Digite el nuevo valor del atributo")
        res = requests.post(self.endpoint + "/api/usuario/actualizar_usuario", kwargs)
        self.procesar_respuesta(res)

    # Consultar usuario.
    def consultar_usuario(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del usuario.")
        res = requests.post(self.endpoint + "/api/usuario/consultar_usuario", kwargs)
        status = self.procesar_respuesta(res)
        if status == 200:
            res = res.json()
            for key, value in res.items():
                print(key, ': ', value)

    # Eliminar usuario.
    def eliminar_usuario(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del usuario.")
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
            kwargs["id"] = input("Digite el id del usuario")
            kwargs["atributo"] = input("Digite el nombre del atributo a modificar")
            kwargs["valor"] = input("Digite el nuevo valor del atributo")
        res = requests.post(self.endpoint + "/api/articulo/actualizar_articulo", kwargs)
        self.procesar_respuesta(res)

    # Consultar artículo.
    def consultar_articulo(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del artículo.")
        res = requests.post(self.endpoint + "/api/articulo/consultar_articulo", kwargs)
        status = self.procesar_respuesta(res)
        if status == 200:
            res = res.json()
            for key, value in res.items():
                print(key, ': ', value)

    # Eliminar artículo.
    def eliminar_articulo(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del artíuclo.")
        res = requests.post(self.endpoint + "/api/articulo/eliminar_articulo", kwargs)
        self.procesar_respuesta(res)

    # Crear pedido.
    def crear_pedido(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs = self.ingresar_info_pedido()
        res = requests.post(self.endpoint + "/api/pedido/crear_pedido", kwargs)
        self.procesar_respuesta(res)

    # Consultar pedido.
    def consultar_pedido(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del pedido.")
        res = requests.post(self.endpoint + "/api/pedido/consultar_pedido", kwargs)
        status = self.procesar_respuesta(res)
        if status == 200:
            res = res.json()
            for key, value in res.items():
                print(key, ': ', value)

    # Eliminar pedido.
    def eliminar_pedido(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs["id"] = input("Digite el id del pedido.")
        res = requests.post(self.endpoint + "/api/pedido/eliminar_pedido", kwargs)
        self.procesar_respuesta(res)

    # Actualizar pedido.
    def actualizar_pedido(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs = {}
            kwargs["id"] = input("Digite el id del pedido")
            kwargs["atributo"] = input("Digite el nombre del atributo a modificar")
            kwargs["valor"] = input("Digite el nuevo valor del atributo")
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

class Consola2:
    def __init__(self, usuario = None):
        self.usuario = usuario
        
    """
    Funciones de gestion de sesion:
    """

    def iniciar_sesion(self):
        clear()
        print("Ingresa tus datos prro:")
        id = input("ID: ")
        contrasena = input("Contrasena: ")
        self.verificar_sesion(id, contrasena)
        return 0

    def verificar_sesion(self, id, contrasena):
        """
        Recibe id, contrasena guarda el usuario si existe.
        De lo contrario; regresa un mensaje de error
        """

        f = open('examples/usuarios.json', 'r')
        posibles_usuarios = json.loads(f.read())
        f.close()
        """
        Aqui se debería hacer una request al server para traer
        los datos de un usuario en la base de datos...

        Pero como no se hacer eso, utilicé los dos usuarios ubicados en
        examples/usuarios.json
        """
        
        if id in posibles_usuarios:
            verdadera_contrasena = posibles_usuarios[id]["contrasena"]
            if verdadera_contrasena == contrasena:
                dicc_usuario = posibles_usuarios[id]
                dicc_usuario["id"] = id
                self.usuario = Usuario.crear_usuario_dicc(Usuario, dicc_usuario)
            else:
                print("Contrasena incorrecta, intenta de nuevo\n")
        else:
            print("Usuario no encontrado\n")
        

        """
        De nuevo, aquí debería mandar un mensaje al server con el 200 pa indicar
        que todo fue bien... Pero no se hacer eso :v
        """
        return 0
    
    def cerrar_sesion(self):
        if self.usuario is not None:
            print(f"\nCerrando sesion... Hasta la proxima {self.usuario.nombres}")
            self.usuario = None
        return 0
    

    """
    Funciones de guardado
    """
    def guardar_usuario(self, texto = None):
        """
        Crea un cliente... No se porque necesito especificar mas
        """
        if self.usuario is not None:
            if self.usuario.rol == "funcionario":
                print("¡Ingresa los datos del cliente a ingresar!\n")
                if texto is None:
                    texto = '{\n'
                
                    for atributo in self.usuario.__dict__:
                        if atributo == 'id':
                            texto = f'"{input(f"ID: ")}":'+ texto
                            continue
                        texto += f'"{atributo}": "' + input(f"{atributo}: ") + '",\n'
                    
                    texto = texto[:-2]

                    texto += '\n}\n'
                f = open('examples/usuarios.json', 'r')
                archivo_antes = f.readlines()
                archivo_antes[len(archivo_antes) - 2] += ','
                archivo_antes[len(archivo_antes) - 1] = texto
                archivo_antes.append('}')
                f.close()

                f = open('examples/usuarios.json', 'w')
                f.writelines(archivo_antes)
                f.close()

                print("\nNuevo usuario ingresado correctamente")
            else:
                print("Permisos no suficientes para esta operacion")
        
        return 0
    
    """
    Funciones de buscado
    """
    def buscar_usuario(self, id):
        id = str(id)
        f = open('examples/usuarios.json', 'r')
        posibles_usuarios = json.loads(f.read())
        f.close()
        if id in posibles_usuarios:
            posibles_usuarios[id]["id"] = id
            usuario = Usuario.crear_usuario_dicc(posibles_usuarios[id])
            return usuario
        else:
            print("El usuario no existe en la base de datos.")
            return 0
    
    """
    Funciones de editado
    """

    def editar_usuario(self, id):
        dic_usuario = self.buscar_usuario(id)
        if dic_usuario:
            dic_usuario = dic_usuario.obtener_dicc_usuario()
            atributo_modificar = input("Ingrese el atributo del usuario a modificar: ")
            nuevo_valor = input(f"El valor actual de ese atributo es {dic_usuario[atributo_modificar]}\nIngrese el nuevo valor: ")
            dic_usuario[atributo_modificar] = nuevo_valor

            texto = f'"{id}": ' + '{'
            for atributo in dic_usuario:
                texto += f'"{atributo}": "{dic_usuario[atributo]}",\n'
        
            texto = texto[:-3] # Borra la ultima coma y salto de linea
            texto += '\n}'
            self.eliminar_usuario(id)
            self.guardar_usuario(texto)

            print("¡Cambios hechos con exito!")


    """
    Funciones de eliminado
    """

    def eliminar_usuario(self, id):
        id = str(id)
        f = open('examples/usuarios.json', 'r')
        posibles_usuarios = json.loads(f.read())
        f.close()

        if id in posibles_usuarios:
            posibles_usuarios.pop(id)

            f = open('examples/usuarios.json', 'w')
            f.write(json.dumps(posibles_usuarios))
            f.close()
        else:
            print("\nUsuario no encontrado :c")
        return 0

endpoint = "http://localhost:5000"
gui = Consola(endpoint = endpoint)
gui.menu()


#guy.iniciar_sesion()
#guy.guardar_usuario()
#guy.eliminar_usuario(100000)
#guy.editar_usuario(100000)

#guy.buscar_usuario(100000).mostrar()

#guy.cerrar_sesion()