"""
Un singleton es una clase que solo tiene una instancia.
Esta clase permite crear clases singleton del siguiente modo:

class MiClase(metaclass=Singleton):

La idea es que si se intenta guardar en dos variables una clase de estas,
todas las variables guardaran la misma instancia.

var1 = MiClase()
var2 = MiClase()

if id(var1) == id(var2):
    print("Las dos variables apuntan a la misma direccion :O")

"""

class Singleton(type):

    _instancias = {}

    def __call__(self, *args, **kwds):
        if self not in self._instancias:
            instancia = super().__call__(*args, **kwds)
            self._instancias[self] = instancia
        return self._instancias[self]