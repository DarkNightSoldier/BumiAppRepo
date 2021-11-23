from modelo.pedido import Pedido
from .interfaz_json import InterfazJSON

class Subpedido(InterfazJSON):
    def __init__(self, id, pedido_padre, id_producto, cantidad, impuesto, descuento):
        super().__init__(id)
        self.pedido_padre = pedido_padre
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.impuesto = impuesto
        self.descuento = descuento
    
    def convertir_JSON(self, id, json):
        """
        Dada la id, de un pedido y su json
        regresa un objeto tipo pedido.
        """
        return Subpedido(
            id,
            json["pedido_padre"],
            json["id_producto"],
            json["cantidad"],
            json["impuesto"],
            json["descuento"]
        )
    def hacer_crear_JSON(self):
        """
        Regresa un diccionario en texto con los datos de
        si mismo SIN EL ID.
        """
        return {
            "pedido_padre":self.pedido_padre,
            "id_producto":self.id_producto,
            "cantidad":self.cantidad,
            "impuesto":self.impuesto,
            "descuento":self.descuento
        }