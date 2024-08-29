#Ejemplo de como funcionan los iteradores
#Crear una lista con algunos números
my_list = [1, 2, 3, 4]
#Obtener el iteador de la lista
#Uni iterador es un objeto que nos permite recorrer una colección (como una lista) uno por uno
my_iter = iter(my_list)
#Usar el iterador para acceder a los elementos de la lista
#la función next() nos da el siguiente elemento en la colección cada vez que se llama
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))
# Iterar cadenas de texto usando un iterador
text = "Hola Mundo"
# Crear un iterador para la cadena de texto
# El iterador nos mostraria cada elemento de la cadena de texto
iter_text = iter(text)
# Iterar sobre cada caracter de la cadena usando el bucle for
for char in iter_text: 
    print(char)
    