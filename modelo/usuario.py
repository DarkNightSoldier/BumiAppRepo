from .interfaz_json import InterfazJSON

class Usuario(InterfazJSON):
    def __init__(self, id, nombre, apellido, rol, contrasena,
        correo, ciudad, direccion, telefono, zip):
        """
        Inicializa la clase usuario
        """
        super().__init__(id)
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.contrasena = contrasena
        self.correo = correo
        self.ciudad = ciudad
        self.direccion = direccion
        self.telefono = telefono
        self.zip = zip
    def convertir_JSON(self, id, json):
        """
        Dada la id, de un usuario y su json
        regresa un objeto tipo usuario.
        """
        return Usuario(
            id,
            json["nombre"],
            json["apellido"],
            json["rol"],
            json["contrasena"],
            json["correo"],
            json["ciudad"],
            json["direccion"],
            json["telefono"],
            json["zip"]
        )
    def hacer_crear_JSON(self):
        """
        Regresa un diccionario en texto con los datos de
        si mismo SIN EL ID.
        """
        return {
            "nombre":self.nombre,
            "apellido":self.apellido,
            "rol":self.rol,
            "contrasena":self.contrasena,
            "correo":self.correo,
            "ciudad":self.ciudad,
            "direccion":self.direccion,
            "telefono":self.telefono,
            "zip":self.zip
        }