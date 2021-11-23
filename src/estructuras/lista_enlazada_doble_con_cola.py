# LinkedList Doble con cola
# Por Samuel Alvarez

class Nodo:
  def __init__(self, dato = None):
    self.dato = dato
    self.siguiente = None # Nodo siguiente
    self.previo = None # Nodo anterior

class ListaEnlazadaDoble:
  """
  Una lista enlazada donde cada nodo
  tiene un puntero al nodo siguiente
  y al nodo anterior.
  
  Atributos:
  self.cabeza := Cabeza de la lista
  self.cola := Cola de la lista
  """
  
  def __init__(self, cabeza = None):
    if cabeza is None:
      cabeza = Nodo()
      cola = cabeza
    else:
      nod = cabeza
      while nod.siguiente is not None:
        nod = nod.siguiente
      cola = nod
    self.cabeza = cabeza
    self.cola = cola
  
  def anadir_antes_o_despues_de(self, nodo, dato, antes = True):
    # Anade el dato antes o despues del nodo dado
    # si antes = True, anade el dato antes. De lo contrario lo anade despues
    nuevo_nodo = Nodo(dato)
    if antes:
      previo = nodo.previo
      nuevo_nodo.siguiente = nodo
      nodo.previo = nuevo_nodo
      if previo is not None:
        previo.siguiente = nuevo_nodo
        nuevo_nodo.previo = previo
    else:
      siguiente = nodo.siguiente
      nuevo_nodo.previo = nodo
      nodo.siguiente = nuevo_nodo
      if siguiente is not None:
        siguiente.previo = nuevo_nodo
        nuevo_nodo.siguiente = siguiente
    
    return nuevo_nodo
  
  def empujar_adelante(self, dato):
    # Añade un nuevo dato al principio de la lista
    if self.cabeza.dato is None:
      self.cabeza.dato = dato
    else:
      nuevo = self.anadir_antes_o_despues_de(self.cabeza, dato)
      self.cabeza = nuevo
  
  def empujar_atras(self, dato):
    # Añade un nuevo dato al final de la lista
    if self.cabeza.dato is None:
      self.cabeza.dato = dato
    else:
      nuevo = self.anadir_antes_o_despues_de(self.cola, dato, False)
      self.cola = nuevo

  def insertar_con_orden(self, dato):
    # Inserta ordenando de menor a mayor en la lista.
    # El orden viene dado por la id de los datos
    if self.cabeza.dato is None:
      self.cabeza.dato = dato
    elif self.cabeza.dato.id > dato.id:
      self.empujar_adelante(dato)
    elif self.cola.dato.id < dato.id:
      self.empujar_atras(dato)
    else:
      nodo = self.cabeza
      
      while (nodo.siguiente is not None) and (nodo.dato.id < dato.id):
        nodo = nodo.siguiente
      
      # Cuando el anterior while se detenga
      # nodo.previo.dato.id < dato.id <= nodo.dato.id
      # Es decir, el nuevo id va entre nodo y nodo.previo
      
      if nodo.dato.id == dato.id:
        raise Exception("El id ya se encuentra en la lista")
      else:
        self.anadir_antes_o_despues_de(nodo, dato)
        
  def eliminar_cabeza(self):
    """
    Elimina el dato de la cabeza de la lista
    y mueve la cabeza a su nuevo lugar
    """
    dato_eliminado = self.head.dato
    if self.head.siguiente is None:
      self.head.dato = None
    else:
      self.head = self.head.siguiente
      self.head.previo = None
    return dato_eliminado

  def eliminar_cola(self):
    """
    Elimina el dato de la cola de la lista
    y mueve la cola a su nuevo lugar
    """
    dato_eliminado = self.cola.dato
    if self.head.dato == dato_eliminado:
      # Como asumimos que el unico modo
      # de insersion es el insertar_con_orden
      # Si el dato en la cabeza es igual al dato
      # en la cola, entones ambos datos deben tener el mismo id.
      # Es decir que estamos lidiando con una lista que solo tiene un dato
      self.cola.dato = None
    else:
      self.cola = self.cola.previo
      self.cola.siguiente = None
    return dato_eliminado
    
  def buscar_nodo(self, id):
        """
        Retorna el nodo en la lista con el id.
        """
        if self.head.dato is None:
          raise Exception("No encontrado")
        elif self.cola.dato.id == id:
          return self.cola
        else:
          nodo = self.cabeza
          while nodo.siguiente is not None:
            if nodo.dato.id == id:
              break
            nodo = nodo.siguiente
          
          if nodo == self.cola:
            raise Exception("No encontrado")
          
          return nodo
        
  
  def eliminar(self, id):
    try:
      nodo_a_borrar = None
      if id == self.cabeza.dato.id:
        nodo_a_borrar = self.cabeza
        self.eliminar_cabeza()
      elif id == self.cola.dato.id:
        nodo_a_borrar = self.cola
        self.eliminar_cola()
      else:
        nodo_a_borrar = self.buscar_nodo(id)
        previo = nodo.previo
        siguiente = nodo.siguiente
        
        previo.siguiente = siguiente
        siguiente.previo = previo
        
      dato_a_borrar = nodo_a_borrar.dato
      return dato_a_borrar
    except:
        raise Exception("No encontrado")
  
  def esta_vacio(self):
        if self.head.dato is None:
            return True
        else:
            return False
