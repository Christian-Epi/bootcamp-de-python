cadena1 = "Hola,soy,Christian"
cadena2 = "Gracias por aprender Python con nosotros"
#print (dir(cadena1))

resultado = cadena1.lower()
print (resultado)

primera_letra_mayuscula = cadena1.capitalize() 
print (primera_letra_mayuscula)

busqueda_find = cadena1.find("Hola")
print (busqueda_find)

busqueda_find = cadena1.find("a")
print (busqueda_find)

busqueda_find = cadena1.find("z")
print (busqueda_find)

busqueda_index = cadena1.index("a")
print (busqueda_index)

#busqueda_index = cadena1.index("z")
#print (busqueda_index) #genera error porque no hay z

# Los objetos estan asociados a metodos: los perros ladran, los gatos hacen miau

es_numerico = cadena1.isnumeric()
print (es_numerico)
#isalnum() permite tanto letras como números, mientras que isalpha() solo permite letras.

contar_coincidencias = cadena1.count("a")
print (contar_coincidencias)

contar_caracteres = len(cadena1)
print (contar_caracteres)

empieza_con = cadena1.startswith("H")
print (empieza_con)

termina_con = cadena1.endswith("n")
print (termina_con)

cadena_nueva = cadena1.replace("soy"," me llamo ")
print (cadena_nueva)

cadena_separada = cadena1.split(",")
print (cadena_separada)
print (type(cadena_separada))
print (cadena_separada [0])
