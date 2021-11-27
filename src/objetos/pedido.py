import math

class Pedido:

    def __init__(self,id_pedido,id_cliente):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.pedido_padre =  id_pedido
        self.id_conductor = 0
        self.estado = "por entregar"
        self.frecuencia = 0
        self.productos = ""
        self.cantidades = ""
        self.valor_producto_sin_impuestos = 0
        self.impuestos_productos = ""
        self.valor_descuentos = ""
        self.moneda = "COP"
        self.subtotal = 0
        self.impuestos = 0
        self.total = 0

        self.carrito = None
        self.coleccion_de_productos = None

    def cargar_desde_diccionario(self,dicc):
        self.id_pedido = dicc["id_pedido"]
        self.pedido_padre = dicc["pedido_padre"]
        self.id_conductor = dicc["id_conductor"]
        self.estado = dicc["estado"]
        self.frecuencia = int(dicc["frecuencia"])
        self.productos = dicc["productos"]
        self.cantidades = dicc["cantidades"]
        self.valor_producto_sin_impuestos = dicc["valor_producto_sin_impuestos"]
        self.impuestos_productos = dicc["impuestos_productos"]
        self.valor_descuentos = dicc["valor_descuentos"]
        self.moneda = dicc["moneda"]
        self.subtotal = int(dicc["subtotal"])
        self.impuestos = int(dicc["impuestos"])
        self.total = int(dicc["total"])

    def anadir_producto(self,producto,cantidad):
        self.carrito[producto.id] = {producto:producto,cantidad:cantidad}
    
    def actualizar_productos_carrito(self,producto,cantidad):
        self.carrito[producto.id]["cantidad"] = cantidad
    
    def ver_carrito(self):
        return self.carrito        

    def consolidar_carrito(self):
        for articulo in self.carrito.items:
            producto = articulo["producto"]
            cantidad = articulo["cantidad"]

            if cantidad>0:
                self.productos += producto.id
                self.cantidades += str(cantidad)
                self.valor_producto_sin_impuestos += str(producto.precio_antes_impuesto)
                self.impuestos_productos += str(producto.impuesto_porcentaje)
                self.valor_descuentos += str(producto.descuento)
                self.subtotal = self.subtotal+producto.precio_antes_impuesto
                self.impuestos += math.floor(producto*(producto.impuesto_porcentaje)/100)
                self.total += math.floor(producto.precio_antes_impuesto*(1+(self.impuesto_porcentaje/100)))-self.producto_descuentos
        #Al final vaciamos el carrito para ahorrar espacio en memoria
        self.carrito = None
