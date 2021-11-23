from .interfaz_json import InterfazJSON

class Producto(InterfazJSON):
    def __init__(self, id, nombre, descripcion, url_img, stock, valor):
        super().__init__(id)
        self.nombre = nombre
        self.descripcion = descripcion
        self.url_img = url_img
        self.stock = stock
        self.valor = valor
    
    def convertir_JSON(self, id, json):
        """
        Dada la id, de un pedido y su json
        regresa un objeto tipo pedido.
        """
        return Producto(
            id,
            json["nombre"],
            json["descripcion"],
            json["url_img"],
            json["stock"],
            json["valor"]
        )
    def hacer_crear_JSON(self):
        """
        Regresa un diccionario en texto con los datos de
        si mismo SIN EL ID.
        """
        return {
            "nombre":self.nombre,
            "descripcion":self.descripcion,
            "url_img":self.url_img,
            "stock":self.stock,
            "valor":self.valor
        }
