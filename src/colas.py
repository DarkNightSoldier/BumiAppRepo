from listas_enlazadas import ListaEnlazadaConCola,ListaEnlazadaDoble
from lista_circular_doble import ListaEnlazadaCircularDoble


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

class ColaArrayBased():
    def __init__(self):
        self.lista = list()
    
    def encolar(self,dato):
        self.lista.append(dato)
    
    def desencolar(self):
        if len(self.lista)>0:
            self.lista.pop(0)
        else:
            raise Exception("Error,cola vacía")

    def peek(self):
        return self.lista[0]

    