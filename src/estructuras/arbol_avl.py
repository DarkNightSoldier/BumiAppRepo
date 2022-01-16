class Nodo:
    def __init__(self, dato = None):
        self.dato = dato
        self.altura = 0
        self.hijo_izq = None
        self.hijo_der = None

#La clase ArbolAVL implementa un árbol de búsqueda binario
class ArbolAVL:
    def __init__(self):
        self.raiz = None

    #Para valores menores a -1 significa que está desbalanceado por izquierda
    #Para valores mayores a 1 significa que está desbalandeado por derecha
    #Para valores entre -1 y 1 (-1,0,1) significa que está balanceado
    def obtener_desbalanceo(self,nodo):
        if nodo == None:
            return 0
        return self.altura_subarbol(nodo.hijo_der)-self.altura_subarbol(nodo.hijo_izq)

    #Método para una rotación simple a izquierda
    def rotacion_izquierda(self,nodo):
        nodo_rota = nodo.hijo_der
        nodo_subarbol = nodo_rota.izq

        #Se hace la rotación
        nodo_rota.hijo_izq = nodo
        nodo.hijo_der = nodo_subarbol

        #Actualizamos las alturas
        nodo.altura = max(self.altura_recursivo(nodo.hijo_izq),self.altura_recursivo(nodo.hijo_der))+1
        nodo_rota.altura = max(self.altura_recursivo(nodo_rota.hijo_izq),self.altura_recursivo(nodo_rota.hijo_der))+1

        return nodo_rota

    #Método para una rotación simple a derecha
    def rotacion_derecha(self,nodo):
        nodo_rota = nodo.hijo_izq
        nodo_subarbol = nodo_rota.hijo_der

        #Se hace la rotación
        nodo_rota.hijo_der = nodo
        nodo.hijo_izq = nodo_subarbol

        #Actualizamos las alturas
        nodo.altura = max(self.altura_recursivo(nodo.hijo_izq),self.altura_recursivo(nodo.hijo_der))+1
        nodo_rota.altura = max(self.altura_recursivo(nodo_rota.hijo_izq),self.altura_recursivo(nodo_rota.hijo_der))+1

        return nodo_rota
    

    def balanceo(self,nodo,dato):
        #Obtenemos el desbalanceo
        desbalanceo = self.obtener_desbalanceo(nodo)

        #Desbalanceo LL
        if desbalanceo<-1 and dato.id < nodo.hijo_izq.dato.id:
            return self.rotacion_izquierda(nodo)

        #Desbalanceo RR
        if desbalanceo>1 and dato.id > nodo.hijo_izq.dato.id:
            return self.rotacion_derecha(nodo)

        #Desbalanceo LR
        if desbalanceo<-1 and dato.id > nodo.hijo_izq.dato.id:
            nodo.hijo_izq = self.rotacion_izquierda(nodo.hijo_izq)
            return self.rotacion_derecha(nodo)

        #Desbalanceo RL
        if desbalanceo>1 and dato.id < nodo.hijo_izq.dato.id:
            nodo.hijo_der = self.rotacion_izquierda(nodo.hijo_izq)
            return self.rotacion_derecha(nodo)

        return nodo


    #Método recursivo para insertar en un subárbol cuya raíz es nodo
    #Ordenamos en base al id de dato
    def insertar_recursivo(self,nodo,dato):
        if nodo == None:
            return Nodo(dato)
        elif dato.id<nodo.dato.id:
            nodo.hijo_izq = self.insertar_recursivo(self,nodo.hijo_izq,dato)
        elif dato.id>nodo.dato.id:
            nodo.hijo_der = self.insertar_recursivo(self,nodo.hijo_der,dato)

        #Actualizamos la actura del nodo
        nodo.altura = max(self.altura_subarbol(nodo.hijo_izq),self.altura_subarbol(nodo.hijo_der))+1
        nodo = self.balanceo(nodo,dato)
        return nodo

    #Método que elimina el nodo con el id buscado
    def eliminar_recursivo(self,nodo,id):
        nodo_a_eliminar = self.buscar_recursivo(id,nodo)
        if nodo_a_eliminar==-1:
            pass
        elif nodo_a_eliminar.hijo_izq == None and nodo_a_eliminar.hijo_der==None:
            nodo_a_eliminar = None
        elif nodo_a_eliminar.hijo_der==None:
            nodo_a_eliminar = nodo_a_eliminar.hijo_izq
        else:
            nodo_menor = self.buscar_min_recursivo(nodo_a_eliminar.hijo_der)
            nodo_a_eliminar.dato = nodo_menor.dato
            self.eliminar_recursivo(nodo_a_eliminar.hijo_der,nodo_menor.id)
        
        #Actualizamos la actura del nodo
        nodo.altura = max(self.altura_subarbol(nodo.hijo_izq),self.altura_subarbol(nodo.hijo_der))-1
        nodo = self.balanceo(nodo,id)
        return nodo


    #Método para añadir un nuevo nodo al árbol
    def insertar(self,dato):
        self.raiz = self.insertar(self,self.raiz,dato)

    #Busca el dato del nodo con el id buscado de manera recursiva en el subárbol de nodo
    def buscar_recursivo(self,id,nodo):
        if nodo == None:
            return -1
        elif id == nodo.dato.id:
            return nodo
        elif id < nodo.dato.id:
            return self.buscar_recursivo(id,nodo.hijo_izq)
        elif id > nodo.dato.id:
            return self.buscar_recursivo(id,nodo.hijo_der)
        return -1
   
    #Implementar buscar_recursivo para encontrar el nodo cuyo id coincida con el id buscado
    def buscar(self,id):
        return self.buscar_recursivo(self,id,self.raiz).dato

    #Busca el dato del nodo mínimo de un subárbol de manera recursiva
    def buscar_min_recursivo(self,nodo):
        if nodo.hijo_izq == None:
            return nodo
        else:
            return self.buscar_min_recursivo(nodo.hijo_izq)
    
    def eliminar(self,id):
        self.eliminar_recursivo(self.raiz,id)
    
    #Método para encontrar la altura de un subárbol de manera recursiva
    def altura_subarbol(self,nodo):
        if nodo == None:
            return -1
        else:
            return 1 + max(self.altura_subarbol(nodo.hijo_der),self.altura_subarbol(nodo.hijo_izq))
    
    def altura(self):
        return self.altura_subarbol(self.raiz)
