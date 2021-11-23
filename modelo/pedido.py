from .interfaz_json import InterfazJSON

class Pedido(InterfazJSON):
    def __init__(self, id, id_cliente, estado, frecuencia, moneda, lista_subpedidos):
        super().__init__(id)
        """
        subpedidos es una lista con las id de los subpedidos
        """
        self.id_cliente = id_cliente
        self.estado = estado
        self.frecuencia = frecuencia
        self.moneda = moneda
        self.subpedido = self.buscar_subpedidos(lista_subpedidos)
    
    def buscar_subpedidos(self, lista_subpedidos):
        lista = []
        for subpedido in lista_subpedidos:
            if subpedido.pedido_padre == self.id:
                lista.append(subpedido)
        return lista
    
    def convertir_JSON(self, id, json, lista_subpedidos):
        """
        Dada la id, de un pedido y su json
        regresa un objeto tipo pedido.
        """
        return Pedido(
            id,
            json["id_cliente"],
            json["estado"],
            json["frecuencia"],
            json["moneda"],
            lista_subpedidos
        )
    def hacer_crear_JSON(self):
        """
        Regresa un diccionario en texto con los datos de
        si mismo SIN EL ID.
        """
        return {
            "id_cliente":self.id_cliente,
            "estado":self.estado,
            "frecuencia":self.frecuencia,
            "moneda":self.moneda
        }
