from .listas_enlazadas import ListaEnlazadaConCola,ListaEnlazadaDoble
from .lista_circular_doble import ListaEnlazadaCircularDoble


#La colaSLL implementa la lista enlazada con cola
class ColaSLL(ListaEnlazadaConCola):
    def __init__(self):
        super().__init__()
    
    def encolar(self,dato):
        super().empujar_atras(dato)
    
    def desencolar(self):
        if self.cabeza!=None:
            dato_a_borrar = self.cabeza.dato
            self.eliminar_adelante()
            return dato_a_borrar
        else:
            raise Exception("Error,cola vacía")

    def peek(self):
        return self.cabeza.dato

    def imprimir(self):
        a_imprimir = ""
        if self.cabeza!=None:
            nodo_actual = self.cabeza
            a_imprimir += nodo_actual.dato.id
            while nodo_actual.siguiente!=None:
                nodo_actual = nodo_actual.siguiente
                a_imprimir += nodo_actual.dato.id
        return a_imprimir
        

#La colaDLL implementa la lista doblemente enlazada con cola
class ColaDLL(ListaEnlazadaDoble):
    def __init__(self):
        super().__init__()
    
    def encolar(self,dato):
        super().empujar_atras(dato)
    
    def desencolar(self):
        if self.cabeza!=None:
            dato_a_borrar = self.cabeza.dato
            self.eliminar_adelante()
            return dato_a_borrar
        else:
            raise Exception("Error,cola vacía")

    def peek(self):
        return self.cabeza.dato
    
    def imprimir(self):
        a_imprimir = ""
        if self.cabeza!=None:
            nodo_actual = self.cabeza
            a_imprimir += nodo_actual.dato.id
            while nodo_actual.siguiente!=None:
                nodo_actual = nodo_actual.siguiente
                a_imprimir += nodo_actual.dato.id
        return a_imprimir

#La cola circular doble implementa la lista enlazada circular doble
class ColaCircularDoble(ListaEnlazadaCircularDoble):
    def __init__(self):
        super().__init__()
    
    def encolar(self,dato):
        super().empujar_atras(dato)
    
    def desencolar(self):
        if not super().esta_vacio():
            dato_a_borrar = self.cabeza.dato
            self.eliminar_adelante()
            return dato_a_borrar
        else:
            raise Exception("Error,cola vacía")

    def peek(self):
        return self.cabeza.dato

    def imprimir(self):
        a_imprimir = ""
        if self.cabeza!=None:
            nodo_actual = self.cabeza
            a_imprimir += nodo_actual.dato.id
            while nodo_actual.siguiente!=None:
                nodo_actual = nodo_actual.siguiente
                a_imprimir += nodo_actual.dato.id
        return a_imprimir

class ColaArrayBased():
    def __init__(self):
        self.lista = list()
    
    def encolar(self,dato):
        self.lista.append(dato)
    
    def desencolar(self):
        if len(self.lista) > 0:
            return self.lista.pop(0)
        else:
            raise Exception("Error, cola vacía")

    def peek(self):
        if len(self.lista) > 0:
            return self.lista[0]
        else: 
            raise Exception("Error, cola vacía.")

    def obtener_indice(self, id):
        for i in range(self.lista):
            elemento = self.lista[i]
            if elemento.id == id:
                return i
        return -1

    def buscar(self, id):
        for i in range(self.lista):
            elemento = self.lista[i]
            if elemento.id == id:
                return elemento
        return -1

    def eliminar(self, id):
        existe = not isinstance(self.buscar(id), int)
        if not existe: 
            raise Exception("El Id no existe.")
        else: 
            copia = list()
            for i in range(self.lista):
                elemento = self.lista[i]
                if elemento.id != id:
                    copia.append(elemento)
            self.lista = copia
            return self.lista

    def actualizar_elemento(self, id, atributo, valor):
        j = self.obtener_indice(id)
        if j != -1:
            setattr(self.lista[j], atributo, valor)
            return 1
        else: 
            raise Exception("El Id no existe.")

    def imprimir(self):

        a_imprimir = ""
        for i in range(0,len(self.lista)):
            a_imprimir += self.lista[i].id
        return a_imprimir
