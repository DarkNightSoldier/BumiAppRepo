# Quedan pendientes las clases de 
# ListaEnlazadaCircular
# ListaEnlazadaDobleCircular

class Nodo:
    def __init__(self, dato = None):
        self.dato = dato
        self.siguiente = None

class DobleNodo(Nodo):
    def __init__(self, dato = None):
        super().__init__(dato)
        self.previo = None

# La siguiente clase NO es una Lista.
class PlantillaListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def buscar_nodo(self, id):
        """
        Retorna el nodo en la lista que guarda el dato
        con la id suministrada
        """
        if self.cabeza.dato is None:
            raise Exception("No encontrado")
        else:
            nodo = self.cabeza
            while nodo is not None:
                if nodo.dato.id == id:
                    break
                nodo = nodo.siguiente
        return nodo
    
    def mostrar(self, id = None):
        if id is None:
            nodo = self.cabeza
            while nodo is not None:
                print(f"{nodo.dato.mostrar()}\n")
                nodo = nodo.siguiente
        else:
            nodo = self.buscar_nodo(id)
            print(nodo.dato)

    def insertar_con_orden(self, dato, tipoNodo):
        """
        Inserta el dato de forma ordenada (menor a mayor);
        el orden viene dado por la id de los datos.

        tipoNodo puede ser Nodo o DobleNodo, dependiendo de la lista
        """
        nodoPrevio = None
        
        if self.cabeza.dato is None:
            self.cabeza.dato = dato
        elif self.cabeza.dato.id > dato.id:
            nodoPrevio = self.empujar_adelante(dato)
        else:
            nodoPrevio = self.cabeza
            temporal = tipoNodo(dato)
            while nodoPrevio is not None:
                if nodoPrevio.dato.id > dato.id:
                    temporal.siguiente = nodoPrevio.siguiente
                    nodoPrevio.siguiente = temporal
                elif nodoPrevio.siguiente is None:
                    nodoPrevio.siguiente = temporal
                    break
                else:
                    nodoPrevio = nodoPrevio.siguiente
        
        return nodoPrevio
    
    # Metodos abstractos:
    def empujar_adelante(self, dato):
        pass

# Desde este punto nos encontramos con las verdaderas listas:
class ListaEnlazada(PlantillaListaEnlazada):
    def __init__(self):
        self.cabeza = Nodo()
    
    def empujar_adelante(self, dato):
        if self.cabeza.dato is None:
            dato = self.dato
        else:
            nuevo = Nodo(dato)
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        return self.cabeza
    
    def eliminar(self, id):
        dato_a_borrar = None
        nodoPrevio = self.head
        if self.cabeza.dato is None:
            raise Exception("Intento de eliminacion en lista vacia")
        elif self.cabeza.dato.id == id:
            dato_a_borrar = self.cabeza.dato
            if self.cabeza.siguiente is not None:
                self.cabeza = self.cabeza.siguiente
            else:
                self.cabeza.dato = None
            nodoPrevio.dato = None
        else:
            while nodoPrevio.siguiente is not None:
                if nodoPrevio.siguiente.dato.id == id:
                    dato_a_borrar = nodoPrevio.siguiente.dato
                    nodoPrevio.siguiente = nodoPrevio.siguiente.siguiente
                    break
                nodoPrevio = nodoPrevio.siguiente
        return dato_a_borrar

    def insertar_con_orden(self, dato):
        return super().insertar_con_orden(dato, Nodo)
    
class ListaEnlazadaCola(ListaEnlazada):
    def __init__(self):
        super().__init__()
        self.cola = self.cabeza
    
    def empujar_atras(self, dato):
        if self.cola.dato is None:
            self.cola.dato = dato
        else:
            nuevo = Nodo(dato)
            self.cola.siguiente = nuevo
            self.cola = nuevo
        return self.cola
    
    def eliminar_cola(self):
        dato_a_borrar = self.cola.dato
        nodo = self.cabeza
        if self.cabeza == self.cola:
            dato_a_borrar = self.cabeza.dato
        else:
            while nodo.siguiente.siguiente is not None:
                nodo = nodo.siguiente
            nodo.siguiente = None
            self.cola = nodo
        return dato_a_borrar

    def eliminar(self, id):
        if self.cola.dato.id == id:
            dato_a_borrar = self.eliminar_cola()
        else:
            dato_a_borrar = super().eliminar(id)
        return dato_a_borrar
    

class ListaEnlazadaDoble(PlantillaListaEnlazada):
    def __init__(self):
        self.cabeza = DobleNodo()
    
    def empujar_adelante(self, dato):
        if self.cabeza.dato is None:
            dato = self.dato
        else:
            nuevo = DobleNodo(dato)
            nuevo.siguiente = self.cabeza
            self.cabeza.previo = nuevo
            self.cabeza = nuevo
        return self.cabeza
    
    def insertar_con_orden(self, dato):
        
        nodo = super().insertar_con_orden(dato, DobleNodo)
        if nodo != self.cabeza:
            siguiente = nodo.siguiente
            siguiente.previo = nodo
            if siguiente.siguiente is not None:
                nsiguiente = siguiente.siguiente
                nsiguiente.previo = siguiente
        return nodo
    
    def eliminar(self, id):
        dato_a_borrar = None
        nodoPrevio = self.head
        if self.cabeza.dato is None:
            raise Exception("Intento de eliminacion en lista vacia")
        elif self.cabeza.dato.id == id:
            dato_a_borrar = self.cabeza.dato
            if self.cabeza.siguiente is not None:
                self.cabeza = self.cabeza.siguiente
            else:
                self.cabeza.dato = None
            nodoPrevio.dato = None
        else:
            while nodoPrevio.siguiente is not None:
                if nodoPrevio.siguiente.dato.id == id:
                    dato_a_borrar = nodoPrevio.siguiente.dato
                    sig = nodoPrevio.siguiente.siguiente
                    nodoPrevio.siguiente = sig
                    if sig is not None:
                        sig.previo = nodoPrevio
                    break
                nodoPrevio = nodoPrevio.siguiente
        return dato_a_borrar

class ListaEnlazadaDobleCola(ListaEnlazadaDoble):
    def __init__(self):
        super().__init__()
        self.cola = self.cabeza
    
    def empujar_atras(self, dato):
        if self.cola.dato is None:
            self.cola.dato = dato
        else:
            nuevo = DobleNodo(dato)
            self.cola.siguiente = nuevo
            nuevo.previo = self.cola
            self.cola = nuevo
        return self.cola
    
    def eliminar_cola(self):
        dato_a_borrar = self.cola.dato
        self.cola = self.cola.previo
        self.cola.siguiente = None
        return dato_a_borrar

    def eliminar(self, id):
        if self.cola.dato.id == id:
            dato_a_borrar = self.eliminar_cola()
        else:
            dato_a_borrar = super().eliminar(id)
        return dato_a_borrar