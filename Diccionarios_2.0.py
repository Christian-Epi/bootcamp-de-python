numbers = {1:"Uno", 2:"Dos", 3: "Tres"}
print (numbers)
print (numbers[1])
print (numbers[2])
print (numbers [3])
information = { "nombre" : "Christian",
               "apellido" : "Gonzalez",
               "estatura" : 1.70,
               "cena" : False}
print (information)
#del information ["apellido"]
print (information)
claves = information.keys()
print (claves)
print (type(claves))
valus = information.values()
print (valus)
pairs = information.items()
print (pairs)

contacts = {"Christian": {"Apellido" : "Gonzalez",
                        "Estatura" : 1.70,
                        "Telefono" : 55555555,
                        "Cenar" : False,
                        "Signo" : "Acuario",
                        "Serie" : "Hobbit",
                        "Cancion" : "Todo ira bien",
                        "Comida" : "Frijoles",
                        "Lugar" : "Silicon Valley",
                        "Habilidad" : "Con los numeros",
                        "Talento" : "Cantar",
                        "Pasatiempo" : "Cocinar",
                        "Persona_que_admiras" : "Jesus",
                        "Libro_favorito" : "Harry Potter",
                        "cena_favorita" : "pizzas",
                        "superpoder" : "Super fuerza",
                        "logro_personal" : "aprender a programar"},
            "Sofia" : {"Apellido" : "Gonzalez",
                        "Estatura" : 1.50,
                        "Telefono" : 55555555,
                        "Cenar" : False,
                        "Signo" : "Piscis",
                        "Serie" : "House of cards",
                        "Cancion" : "Imagine",
                        "comida" : "frutas",
                        "Lugar" : "Cartagena",
                        "Habilidad" : "Traducir",
                        "Talento" : "Cantar",
                        "Pasatiempo" : "Cocinar",
                        "Persona_que_admiras" : "Jesus",
                        "Libro_favorito" : "Harry Potter",
                        "cena_favorita" : "pizzas",
                        "superpoder" : "Super fuerza",
                        "logro_personal" : "aprender a programar"}}

print (contacts)