from hash import *

print("Inicio")
dicc: Map = Map()

def añadir_usuarios_hash(Name,key):
    dicc.add(Name,key)

def eliminar_usuarios_hash(Name):
    dicc.remove(Name)

def buscar_clave(key): 
    dicc.search_value(key)


dicc.add("this",  1)
print("CCC --> ",dicc.search_value("this"))
dicc.add("code", 2)
dicc.add("this", 4)
dicc.add("hi", 5)
print("Tamaño Diccionario",dicc.getSize())
print()
for x in dicc: 
    print(x)


'''

print(dicc.remove("this"))
print(dicc.remove("this"))
print(dicc.getSize())
print(dicc.isEmpty())
print(dicc.hashFunction(dicc))
'''


print("Acabo")