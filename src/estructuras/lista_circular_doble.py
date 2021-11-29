from .listas_enlazadas import NodoBidirecional as Nodo

#Esta lista enlazada circular doble posee orden decreciente respecto al id
class ListaEnlazadaCircularDoble():
    def __init__(self):
        self.cabeza = None
        self.length = 0
    
    def empujar_adelante(self,dato):
        """
        Añade el nuevo nodo antes de la cabeza/cursor y 
        cambia el cursor/cabeza al nuevo nodo.
        """
        nuevo_nodo = Nodo(dato)
        if self.length==0:
            self.cabeza = nuevo_nodo
            self.cabeza.previo = self.cabeza
            self.cabeza.siguiente = self.cabeza
        else:
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.previo = self.cabeza.previo
            self.cabeza.previo = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.length += 1

    def buscar_nodo(self,id):
        """
        Retorna el dato en lista con el indicado.
        """
        if self.length == 0:
            return -1
        elif self.cabeza.dato.id == id:
            return self.cabeza
        else:
            puntero_actual = self.cabeza
            for i in range(0,self.length-1):
                puntero_actual = puntero_actual.siguiente
                if puntero_actual.dato.id == id:
                    return puntero_actual
                    break
                if i==self.length-2 and puntero_actual.dato.id != id:
                    return -1
    
    def anadir_despues_de(self,nodo_1, dato):
        """
        Añade un nuevo nodo con el dato indicado después de nodo_1.
        """
        nodo_2 = Nodo(dato)
        nodo_2.siguiente = nodo_1.siguiente
        nodo_2.previo = nodo_1
        nodo_1.siguiente = nodo_2
        nodo_2.siguiente.previo = nodo_2
        self.length += 1

    #Añade un nuevo nodo en el previo a la cabeza
    def empujar_atras(self,dato):
        if self.length==0:
            nuevo_nodo = Nodo(dato)
            self.cabeza = nuevo_nodo
            self.cabeza.previo = self.cabeza
            self.cabeza.siguiente = self.cabeza
            self.length += 1
        else:
            self.anadir_despues_de(self.cabeza.previo,dato)
    
    def eliminar_adelante(self):
        if self.length==1:
            self.cabeza = None
        else:
            aux_previo = self.cabeza.previo
            aux_siguiente = self.cabeza.siguiente
            aux_siguiente.previo = self.cabeza.previo
            aux_previo.siguiente = self.cabeza.siguiente
            self.cabeza = aux_siguiente
        self.length -=1
    
    def eliminar(self,id):
        try:
            nodo_a_borrar = self.buscar_nodo(id)
            if self.cabeza.dato.id == id:
                self.eliminar_adelante()
                self.length +=1
            elif self.length==2:
                self.cabeza.previo = None
                self.cabeza.siguiente = None
            else:
                nodo_a_borrar.siguiente.previo = nodo_a_borrar.previo
                nodo_a_borrar.previo.siguiente = nodo_a_borrar.siguiente
            self.length -=1
        except:
            raise Exception("Nodo no encontrado")
    
    def esta_vacio(self):
        if self.length==0:
            return True
        else:
            return False

#Datos_de_prueba
'''
coleccion_ejemplo = ListaEnlazadaCircularDoble()
usuario_1 = Usuario(1,"Pepito","Alvarez","cliente","amoamimami","ahiguerac@unal.edu.co","Bogotá","CL 197 18 71",
        6013782025,110141,"1,2")
usuario_2 = Usuario(2,"María","Alvarez","cliente","amoamimami","ahiguerac@unal.edu.co","Bogotá","CL 197 18 71",
        6013782025,110141,"1,2")
usuario_3 = Usuario(3,"Juancho","Alvarez","cliente","amoamimami","ahiguerac@unal.edu.co","Bogotá","CL 197 18 71",
        6013782025,110141,"1,2")

coleccion_ejemplo.insertar_con_orden(usuario_3)
coleccion_ejemplo.insertar_con_orden(usuario_2)
coleccion_ejemplo.insertar_con_orden(usuario_1)
print(coleccion_ejemplo.buscar_nodo(2).dato.id)
coleccion_ejemplo.eliminar(1)
'''
