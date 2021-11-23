from lista_circular_doble import ListaEnlazadaCircularDoble

#La cola circular doble implementa la lista enlazada circular doble
class ColaCircularDoble(ListaEnlazadaCircularDoble):
    def __init__(self):
        super().__init__()
    
    def encolar(self,dato):
        super().push_back(dato)
    
    def desencolar(self):
        if not super().empty():
            id_de_la_cabeza = self.cabeza.dato.id
            dato_de_la_cabeza = self.cabeza.dato
            super().erase(id=id_de_la_cabeza)
            return dato_de_la_cabeza
        else:
            raise Exception("Error,cola vacía")

    def peek(self):
        id_de_la_cabeza = self.cabeza.dato.id
        return super().search(id=id_de_la_cabeza)
