to_do = ["alistar la pelicula",
    "Hacer maiz pira",
    "preparar pasabocas"]

print(to_do)

lista_de_actividades_de_hoy = ["Me desperte a la 5 am",
    "Me levante a las 6:10 am",
    "Hice el desayuno"
    "Me duche a las 6:30 am",
    "Me vesti a las 7:00 am",
    "Me puse a estudiar Python - mentiras, me pase el tiempo arreglando la habitacion"]  

numbers = [1, 2 , 3, 4, "cinco"]
print(numbers)
print(type(numbers))
mix = [1, "dos", 3.14, True, {1, 2, 3},"cinco"]
print(mix)
print(len(mix))
print("Elemento 1", mix[0])
print("Elemento 2", mix[1])
print("Elemento 3", mix[2])
print("Elemento 4", mix[3])
print("Ultimo Elemento: ", mix[-1])
# Podemos omitir el elemento inicial de la lista y partir de :
#Recuerde que el ] excluye el ultimo elemento
print(mix[:3])
# Agregar elemnto nuevo a la lista
mix.append("false")
print(mix)
mix.append("Chris")
print(mix)
# Insertar lista en lista
mix.insert(1, ["a", "b", "c"]) # (index, numbers)
print(mix)
print(mix.index(["a", "b", "c"]))
numbers = [1, 2, 100, 90.45, 5, 6, 7, 8, 9, 10]   
print(numbers)
print("Mayor: ", max(numbers))
print("Menor: ", min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers
# print(numbers)
