import random 
import os.path

# Generador de datos para trabajo DS 
'''
Los atributos que se tienen para USUARIOS son : 
    -> id 
    -> nombres
    -> apellidos 
    -> rol 
    -> contrasena 
    -> correo 
    -> ciudad
    -> direccion 
    -> telefono
    -> zip
    -> pedidos 

'''

# Se tiene una lista de datos base para luego hacer una combinación de estos para cada Dato que se va a crear

lista_nombres = ['Juan','Mateo','Sebastian','Juana','Camila','Diego','Joaquin','Valentina','Diego','Jose','Camilo','Estefani','Diana','Hernan','Martin','Ana','Laura','Lilian','Yuret','Paula','Alejandra','Lorenzo','Andrea','Erika','Alejandro','Carlos','Maria','Juliana','Martha','Matias','Jesus','David','Daniela','Xaira','Danna','Sebastian','Karen','Lorena','Luis','Luisa','Manuel','Manuela','Salome','Salomon','Nicolay']

lista_apellidos = ['Gutierrez','Melo','Herrera','Higuera','Hernadez','Trujillo','Camelo','Sierra','Angarita','Cubillos','Lozano','Sanchez','Nuñez','Osorio','Valenzuela','Venegas','Vanegas','Holguin','Mejia','Maldonado','Pinilla','Delgado','Paez','Espitia','Troncoso','Suarez','Ortiz','Guarin','Montoya','Garcia']

lista_rol = ['Funcionario','Cliente']

lista_correo = ['@unal.edu.co','@gmail.com','@hotmail.com','@uniandes.com','@xix.com.co']

lista_ciudad = ['Bogotá','Miami','Cartagena','Madrid','Fusa','Choconta','Yopal','Funza','Facatativa','Cali','Medellin','Santa Marta']

lista_direccion = ['Calle','Transversal','Diagonal','Carrera','Avenida']


id_inicial = 1000000000
direccion = os.path.dirname(os.path.abspath(__file__))
archivo = open (os.path.join(direccion, f"usuario.json"),'w',encoding = "utf-8")

datos_a_crear = 1000 + 2
cont = 10230
cont2 = cont + 25
print("Inicio")
string_final = '{\n'
string_final = string_final

archivo.write(string_final)

for i in range(1,datos_a_crear) :
    cont += 1
    cont2 += random.randrange(0,10)

    nombre = random.choice(lista_nombres)
    apellido = random.choice(lista_apellidos) 
    string_final = '"' + str(id_inicial) + '":{\n'
    string_final += '"nombre":"' + nombre + '",\n'
    string_final += '"apellido":"' + apellido + '",\n'
    string_final += '"rol":"' + random.choice(lista_rol) + '",\n'
    
    if random.randrange(0, 1):
        numero = random.randrange(35,91)
    else:
        numero = random.randrange(93, 124)
    numero2 = int(random.uniform(1,100000))
    numero3 = list(random.choice(lista_apellidos))
    numero4 = numero3[random.randrange(0,4)]
    numero5 = random.randrange(0,9)

    string_final += '"contrasena":"' + str( chr(numero) + chr(numero) +str(numero3[random.randrange(0,3)] +numero3[random.randrange(0,3)]) + str(numero4) + chr(numero) + chr(numero + 2*(numero)) ) + '",\n'
    string_final += '"correo":"' + str(nombre[0:random.randrange(1,3)] + apellido[0:random.randrange(0,10)] + random.choice(lista_correo)) + '",\n'
    string_final += '"ciudad":"' + random.choice(lista_ciudad) + '",\n'
    string_final += '"direccion":"' + str(random.choice(lista_direccion) + " " +str(numero) +" "+ "#" + " "+  str(numero5) +" "+  random.choice(lista_direccion) ) + '",\n'
    string_final += '"telefono":' + str(random.randrange(1000000000,556789042340)) + ',\n'
    string_final += '"zip":"' + str(cont2)  + '"\n'
    string_final += '},\n'
    string_final = string_final

    archivo.write(string_final)
    id_inicial += 1

string_final = '\n}'
archivo.write(string_final)
archivo.close()

print("Finalizo")