import sys

class Nodo:
    def __init__(self, dato = None):
        self.dato = dato
        self.hijo_izq = None
        self.hijo_der = None
        sys.setrecursionlimit(10**9)
        
#La clase ArbolBST implementa un árbol de búsqueda binario
class ArbolBST:
    def __init__(self):
        self.raiz = None

    #Método recursivo para insertar en un subárbol cuya raíz es nodo
    #Ordenamos en base al id de dato
    def insertar_recursivo(self,nodo,dato):
        if nodo == None:
            return Nodo(dato)
        elif dato.id<nodo.dato.id:
            nodo.hijo_izq = self.insertar_recursivo(nodo.hijo_izq,dato)
        elif dato.id>nodo.dato.id:
            nodo.hijo_der = self.insertar_recursivo(nodo.hijo_der,dato)
        return nodo

    #Método para añadir un nuevo nodo al árbol
    def insertar(self,dato):
        self.raiz = self.insertar_recursivo(self.raiz,dato)

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
    def buscar_nodo(self,id):
        return self.buscar_recursivo(id,self.raiz)

    #Busca el dato del nodo mínimo de un subárbol de manera recursiva
    def buscar_min_recursivo(self,nodo):
        if nodo.hijo_izq == None:
            return nodo
        else:
            return self.buscar_min_recursivo(nodo.hijo_izq)
    
    #Método que elimina el nodo con el id buscado
    def eliminar_recursivo(self,nodo,id):
        if nodo == None:
            return None
        if nodo.hijo_der==None and nodo.hijo_izq==None:
            nodo = None
        elif id<nodo.dato.id:
            nodo.hijo_izq = self.eliminar_recursivo(nodo.hijo_izq,id)
        elif id>nodo.dato.id:
            nodo.hijo_der = self.eliminar_recursivo(nodo.hijo_der,id)
        elif nodo.hijo_izq!=None and nodo.hijo_der!=None:
            nodo.dato = self.buscar_min_recursivo(nodo.hijo_der).dato
            nodo.hijo_der = self.eliminar_recursivo(nodo.hijo_der, id)
        else:
            nodo = nodo.hijo_der if nodo.hijo_der!=None else nodo.hijo_izq
        return nodo

    def eliminar(self,id):
        try:
            self.raiz = self.eliminar_recursivo(self.raiz,id)
        except:
            self.raiz = None
    
    #Método para encontrar la altura de un subárbol de manera recursiva
    def altura_subarbol(self,nodo):
        if nodo == None:
            return -1
        else:
            return 1 + max(self.altura_subarbol(nodo.hijo_der),self.altura_subarbol(nodo.hijo_izq))
    
    def altura(self):
        return self.altura_subarbol(self.raiz)
