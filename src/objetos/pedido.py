class Pedido:
    def __init__(self,id_cliente,coleccion_de_productos):
        self.id_cliente = id_cliente
        self.coleccion_de_productos = coleccion_de_productos

        self.pedido_padre = 0
        self.id_conductor = 0
        self.estado = "por entregar"
        self.frecuencia = 0
        self.productos = ""
        self.cantidades = ""
        self.valor_producto_sin_impuestos = 0
        self.impuestos_productos = ""
        self.valor_descuentos = ""
        self.moneda = "COP"
        self.subtotal = ""
        self.impuestos = 0
        self.total = 0

    def añadir_producto(producto):
        pass
    
    def actualizar_carrito(coleccion_de_productos):
        pass

