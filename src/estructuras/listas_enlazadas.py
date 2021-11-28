class Nodo:
    def __init__(self, dato = None):
        self.dato = dato
        self.siguiente = None

    def imprimir(self):
        return self.dato

class NodoBidirecional(Nodo):
    def __init__(self, dato = None):
        super().__init__(dato)
        self.previo = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    # Push Front.
    def empujar_adelante(self, dato): 
        nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        return self.cabeza
    
    # Push Back.
    def empujar_atras(self, dato):
        temp = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = temp
            return temp
        actual = self.cabeza
        while actual.siguiente != None:
            actual = actual.siguiente
        actual.siguiente = temp
        return temp

    # Pop Back.
    def eliminar_atras(self):
        if self.cabeza == None:
            raise None
        if self.cabeza.siguiente == None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = None

    # AddAfter
    def anadir_despues(self, id, dato):
        nodo = Nodo(dato)
        if self.cabeza == None:
            return None
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                if actual.dato.id == id:
                    siguiente = actual.siguiente
                    actual.siguiente = nodo
                    nodo.siguiente = siguiente
                    return nodo
                actual = actual.siguiente
            return "Id not found."
    
    # AddBefore
    def anadir_antes(self, id, dato):
        nodo = Nodo(dato)
        if self.cabeza == None:
            return None
        if self.cabeza.dato.id == id:
            self.empujar_adelante(dato)
        else:
            previo = self.cabeza
            actual = self.cabeza
            while actual.siguiente != None:
                if actual.dato.id == id:
                    previo.siguiente = nodo
                    nodo.siguiente = actual
                    return nodo
                previo = actual
                actual = actual.siguiente
            return "Id not found."

    # Delete using id.
    def eliminar(self, id):
        if self.cabeza == None:
            return None
        if self.cabeza.dato.id == id:
            self.cabeza = self.cabeza.siguiente
        else:
            previo = self.cabeza
            actual = self.cabeza
            while actual.siguiente != None:
                if actual.dato.id == id:
                    previo.siguiente = actual.siguiente
                    return 1
                previo = actual
                actual = actual.siguiente
    
    # Search.
    def buscar_nodo(self, id):
        if self.cabeza == None:
            raise None
        else:
            actual = self.cabeza
            while actual != None:
                if actual.dato.id == id:
                    return actual
                actual = actual.siguiente
        return -1
    
    # Print list.
    def imprimir_lista(self):
        actual = self.cabeza
        if actual == None:
            print(None)
        else:
            print(actual.dato, end = " => ")
            while actual.siguiente != None:
                actual = actual.siguiente
                print(actual.dato, end = " => ")
            print(None)

class ListaEnlazadaConCola(ListaEnlazada):
    def __init__(self):
        super().__init__()
        self.cola = None
    
    # Push Back.
    def empujar_atras(self, dato):
        temp = Nodo(dato)
        if self.cola != None:
            self.cola.siguiente = temp
            self.cola = self.cola.siguiente
        else:
            self.cabeza = temp
            self.cola = temp

    # Push Front.
    def empujar_adelante(self, dato): 
        nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nodo
            self.cola = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        return self.cabeza

    # Pop front.
    def eliminar_adelante(self):
        if self.cabeza == None:
            raise Exception("Lista vacía.")
        else: 
            if self.cabeza.siguiente != None:
                self.cabeza = self.cabeza.siguiente
            else:
                self.cabeza = None
                self.cola = None

    # Pop Back.
    def eliminar_atras(self):
        if self.cabeza == None:
            raise Exception("Lista vacía.")
        if self.cabeza.siguiente == None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = None
            self.cola = actual

    # AddAfter
    def anadir_despues(self, id, dato):
        nodo = Nodo(dato)
        if self.cabeza == None:
            return Exception("Lista vacía.")
        elif self.cola.dato.id == id:
            self.empujar_atras(dato)
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                if actual.dato.id == id:
                    siguiente = actual.siguiente
                    actual.siguiente = nodo
                    nodo.siguiente = siguiente
                    return nodo
                actual = actual.siguiente
            return "Id not found."
    
    # AddBefore
    def anadir_antes(self, id, dato):

        nodo = Nodo(dato)
        if self.cabeza == None:
            return Exception("Lista vacía.")
        if self.cabeza.dato.id == id:
            self.empujar_adelante(dato)
        else:
            previo = self.cabeza
            actual = self.cabeza
            while actual.siguiente != None:
                if actual.dato.id == id:
                    previo.siguiente = nodo
                    nodo.siguiente = actual
                    return nodo
                previo = actual
                actual = actual.siguiente
            if actual.dato.id == id:
                previo.siguiente = nodo
                nodo.siguiente = actual
                return nodo
            return "Id not found."

    # Delete using id.
    def eliminar(self, id):
        if self.cabeza == None:
            return Exception("Lista vacía.")
        if self.cabeza.dato.id == id:
            self.eliminar_adelante()
        else:
            previo = self.cabeza
            actual = self.cabeza
            while actual.siguiente != None:
                if actual.dato.id == id:
                    previo.siguiente = actual.siguiente
                    if self.cola == actual:
                        if actual.siguiente != None:
                            self.cola = actual.siguiente
                        else: 
                            self.cola = previo
                    return 1
                previo = actual
                actual = actual.siguiente
            if actual.dato.id == id:
                previo.siguiente = actual.siguiente
                if self.cola == actual:
                    if actual.siguiente != None:
                        self.cola = actual.siguiente
                    else: 
                        self.cola = previo
                return 1
    
class ListaEnlazadaDoble(ListaEnlazadaConCola):
    
    def __init__(self, cabeza = None):
        super().__init__()
    
    # Push Front.
    def empujar_adelante(self, dato): 
        nodo = NodoBidirecional(dato)
        if self.cabeza == None:
            self.cabeza = nodo
            self.cola = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        return self.cabeza

    # Push Back.
    def empujar_atras(self, dato):
        temp = NodoBidirecional(dato)
        print("empujar atras")
        if self.cola != None:
            print("not null")
            temp.previo = self.cola
            self.cola.siguiente = temp
            self.cola = self.cola.siguiente
        else:
            print("?????????????previo")
            self.cabeza = temp
            self.cola = temp
        return temp

    # AddAfter
    def anadir_despues(self, id, dato):
        nodo = NodoBidirecional(dato)
        if self.cabeza == None:
            return Exception("Lista vacía.")
        elif self.cola.dato.id == id:
            self.empujar_atras(dato)
            return self.cola
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                if actual.dato.id == id:
                    siguiente = actual.siguiente
                    actual.siguiente = nodo
                    nodo.siguiente = siguiente
                    nodo.previo = actual
                    return nodo
                actual = actual.siguiente
            return "Id not found."
    
    # AddBefore
    def anadir_antes(self, id, dato):
        nodo = Nodo(dato)
        if self.cabeza == None:
            return Exception("Lista vacía.")
        if self.cabeza.dato.id == id:
            self.empujar_adelante(dato)
            return self.cabeza
        else:
            previo = self.cabeza
            actual = self.cabeza
            while actual.siguiente != None:
                if actual.dato.id == id:
                    previo.siguiente = nodo
                    nodo.siguiente = actual
                    nodo.previo = previo
                    return nodo
                previo = actual
                actual = actual.siguiente
            if actual.dato.id == id:
                previo.siguiente = nodo
                nodo.siguiente = actual
                nodo.previo = previo
                return nodo
            return "Id not found."
    
class Dato:
    def __init__(self, id, dato): 
        self.id = id
        self.dato = dato

    def __repr__(self) -> str:
        return self.dato