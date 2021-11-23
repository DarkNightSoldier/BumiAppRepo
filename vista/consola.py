from utilidades.singleton import Singleton

class Consola(metaclass= Singleton):
    def __init__(self):
        self.usuario = None

    def mensaje_bienvenida(self, app):
        print("\t----- Bienvenido a BUMI (version en consola)-----")
        print("Ingrese sesión para continuar:\n")
        self.iniciar_sesion(app)
        return 0
    
    def iniciar_sesion(self, app):
        intentos = 0
        while intentos < 5:
            intentos += 1
            id = input("Id de usuario: ")
            contrasena = input("Contrasena: ")
            self.usuario = app.verificar_sesion(id, contrasena)
            if self.usuario:
                break
        
        if self.usuario is None:
            print("Demasiados intentos... Quizá intenta otro día :c")
        
    def verificar_sesion(self, id, contrasena, lista_de_usuarios):
        try:
            usuario = lista_de_usuarios.buscar_nodo(id)
            if not usuario:
                print("Ese usuario no existe... Intenta otro :p\n")
                return None
            usuario = usuario.dato
            if usuario.contrasena != contrasena:
                print("Contrasena incorrecta, intenta de nuevo\n")
                return None
            else:
                print(f"¡Bienvenido {usuario.nombre} :D!")
                return usuario
        except:
            raise Exception("El usuario no se encuentra en la red :c")
    
    def cerrar_sesion(self):
        try:
            if self.usuario:
                print(f"Fue un gusto que te nos unieras hoy {self.usuario.nombre}")
                print(f"¡Hasta la proxima!")
                self.usuario = None
        except:
            raise Exception("No hay ningun usuario que haya iniciado sesion")