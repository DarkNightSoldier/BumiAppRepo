class Articulo:
    def __init__(self,id,nombre,stock,url_img,precio_antes_impuesto,impuesto_porcentaje,descuento):
        self.id = id
        self.nombre = nombre
        self.stock = stock
        self.url_img = url_img
        self.precio_antes_impuesto = precio_antes_impuesto
        self.impuesto_porcentaje = impuesto_porcentaje
        self.descuento = descuento