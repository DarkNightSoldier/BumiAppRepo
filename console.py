import os
import json

#import pyfiglet
#from src.api.usuarios import ver_datos_usuario
from src.objetos.usuario import Usuario
from src.objetos.pedido import Pedido
from src.objetos.producto import Articulo
#welcome = pyfiglet.figlet_format("Welcome to Bumi!")
#print(welcome)

def clear():
    # Limpia la consola
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Consola:
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
            usuario = Usuario.crear_usuario_dicc(Usuario, posibles_usuarios[id])
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

guy = Consola()
guy.iniciar_sesion()
guy.guardar_usuario()
guy.eliminar_usuario(100000)
guy.editar_usuario(100000)

#guy.buscar_usuario(100000).mostrar()

guy.cerrar_sesion()