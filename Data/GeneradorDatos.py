import random 

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
Los atributos que se tienen para ARTICULOS son : 
    -> id 
    -> Nombres y Apellidos
    -> Stock
    -> url_img
    -> precio_antes_impuesto
    -> impuesto_porcentaje
    -> descuento
'''

# Se tiene una lista de datos base para luego hacer una combinación de estos para cada Dato que se va a crear
nombre_repartidor = 'El Alejo'

lista_nombres = ['Juan','Mateo','Sebastian','Juana','Camila','Diego','Joaquin','Valentina','Diego','Jose','Camilo','Estefani','Diana','Hernan','Martin','Ana','Laura','Lilian','Yuret','Paula','Alejandra','Lorenzo','Andrea','Erika','Alejandro','Carlos','Maria','Juliana','Martha','Matias','Jesus','David','Daniela','Xaira','Danna','Sebastian','Karen','Lorena','Luis','Luisa','Manuel','Manuela','Salome','Salomon','Nicolay']

lista_apellidos = ['Gutierrez','Melo','Herrera','Higuera','Hernadez','Trujillo','Camelo','Sierra','Angarita','Cubillos','Lozano','Sanchez','Nuñez','Osorio','Valenzuela','Venegas','Vanegas','Holguin','Mejia','Maldonado','Pinilla','Delgado','Paez','Espitia','Troncoso','Suarez','Ortiz','Guarin','Montoya','Garcia']

lista_productos = ['Leche','Pasta','Salsa','Crema','Mantequilla','Huevos','Pan','Tostadas','Galletas','Té','Café','Crema Dental','Jabón','Cepillos','Harina']

lista_correo = ['@unal.edu.co','@gmail.com','@hotmail.com','@uniandes.com','@xix.com.co']

lista_ciudad = ['Bogotá','Miami','Cartagena','Madrid','Fusa','Choconta','Yopal','Funza','Facatativa','Cali','Medellin','Santa Marta']

lista_direccion = ['Calle','Transversal','Diagonal','Carrera','Avenida']

lista_estado = ['Cancelado','Pendiente']

id_inicial = 1000000000

archivo = open ('C:/Users/mtgtr/Desktop/cienmillonesUsuarios.txt','w',encoding = "utf-8") # Archivo de usuarios
archivo2 = open ('C:/Users/mtgtr/Desktop/cienmillonesArticulos.txt','w',encoding = "utf-8") # Archivo de Articulos
archivo3 = open ('C:/Users/mtgtr/Desktop/cienmillonesPedidos.txt','w',encoding = "utf-8")  # Archivo de Pedidos

datos_a_crear = 10 + 2
cont = 10230
cont2 = cont + 25

# String_final -> String para Usuarios 
# String_articulos -> String para articulos
# String_pedidos -> String para pedidos

print("Inicio")
string_final = '{\n'
string_final = string_final
string_articulos = '{\n'
string_pedidos = '{\n'


archivo.write(string_final)
archivo2.write(string_articulos)
archivo3.write(string_pedidos)

# Selección aleatoria para Usuarios, Pedidos, Articulos
cont0 = 0 
for i in range(1,datos_a_crear) :
    cont += 1
    cont2 += random.randrange(0,10)

    nombre = random.choice(lista_nombres)
    apellido = random.choice(lista_apellidos) 

    # String para Usuarios
   
    string_final = '"' + str(id_inicial) + '":{\n'
    string_final += '"nombres":"' + nombre + '",\n'
    string_final += '"apellidos":' + apellido + '",\n'
    string_final += '"rol": Cliente' + '",\n'
    
    numero = random.randrange(34,126)
    numero2 = int(random.uniform(1,100000))
    numero3 = list(random.choice(lista_apellidos))
    numero4 = numero3[random.randrange(0,4)]
    numero5 = random.randrange(0,9)
    pedido_padre = str(cont2)
    num_pedido = pedido_padre + "," + str(random.randrange(0,cont2))

    string_final += '"contrasena":"' + str( chr(numero) + chr(numero5) +str(numero3[random.randrange(0,3)] +numero3[random.randrange(0,3)]) + str(numero4) + chr(numero) + chr(numero + 2*(numero)) ) + '",\n'
    string_final += '"correo":"' + str(nombre[0:random.randrange(1,3)] + apellido[0:random.randrange(0,10)] + random.choice(lista_correo)) + '",\n'
    string_final += '"ciudad":"' + random.choice(lista_ciudad) + '",\n'
    string_final += '"direccion":"' + str(random.choice(lista_direccion) + " " +str(numero) +" "+ "#" + " "+  str(numero5) +" "+  random.choice(lista_direccion) ) + '",\n'
    string_final += '"telefono":' + str(random.randrange(1000000000,556789042340)) + '",\n'
    string_final += '"zip":' + str(cont2)  + '",\n'
    string_final += '"pedidos":' + num_pedido + '"\n'
    string_final += '},\n'

    # String para pedidos 

    string_pedidos = '"' + str(id_inicial) + '":{"id":"' + str(id_inicial) +'",\n'
    string_pedidos += '"pedido_padre":"' + pedido_padre + '",\n'
    string_pedidos += '"id_cliente":"' + str(id_inicial) + '",\n'
    string_pedidos += '"id_conductor":"0",\n'
    string_pedidos += '"estado":"' + str(random.choice(lista_estado)) + '",\n'
    string_pedidos += '"frecuencia":' + str(random.randrange(1,10)) + ',\n'
    string_pedidos += '"productos":"' + str(random.randrange(1,15)) + str(random.randrange(1,15)) +str(random.randrange(1,15)) + '",\n'
    string_pedidos += '"cantidades":"' + str(random.randrange(1,15)) + str(random.randrange(1,15)) +str(random.randrange(1,15)) + '",\n' 
    string_pedidos += '"valor_producto_sin_impuestos":"' + str(random.randrange(100,1500)) + str(random.randrange(1,1236)) +str(random.randrange(684,2364)) + '",\n'
    string_pedidos += '"impuestos_productos":"' + str(random.randrange(1,19)) + str(random.randrange(1,18)) +str(random.randrange(1,19)) + '",\n'
    string_pedidos += '"valor_descuentos":"'+ str(random.randrange(1000,15561)) + str(random.randrange(1023,12165)) +str(random.randrange(1000,1569)) + '",\n'
    string_pedidos += '"moneda":"COP",\n'
    string_pedidos += '"subtotal":"' + str(random.randrange(1000,100000)) + '",\n'
    string_pedidos += '"impuestos":"' + str(random.randrange(100,100004)) + '",\n'
    string_pedidos += '"total":"' + str(random.randrange(10000,1000000)) + '",\n'
    string_pedidos += '},\n'

    # String para articulos
    nombre_producto = str(random.choice(lista_productos))
    string_articulos = '"' + str(cont0) + '":{\n'
    string_articulos += '"id":"' + str(cont0) + '",\n'
    string_articulos += '"nombre":"' + nombre_producto + " " + nombre + '",\n'
    string_articulos += '"stock":' + str(random.randrange(0,500)) + '",\n'
    string_articulos += '"url_img":' + '"../img/productos/' + nombre_producto + '.jpg",\n'
    string_articulos += '"precio_antes_impuesto":"' + str(random.randrange(1000,100450)) + '",\n'
    string_articulos += '"impuesto_porcentaje":"' + str(random.randrange(1,19)) +'",\n'
    string_articulos += '"descuento":"' + str(random.randrange(0,100)) + '",\n'
    string_articulos += '},\n'  

    archivo.write(string_final)
    id_inicial += 1
    cont0 += 1

archivo.close()
archivo3.close()
archivo2.close()
print("Finalizo")
