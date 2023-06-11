# cadena1 = 'hOlAa ComO EsTasS'
# cadena2 = cadena1.upper()
# print(cadena2)



# cadena1 = 'hola todo bien'
# cadena_spliteada = cadena1.split()
# print(cadena_spliteada)
# print('____'.join(cadena_spliteada))

# print('arte. hola como estas. rtea'.strip('aert'))

# lista1 = ['hola', 'como', 1, 23]
# lista2 = ['primero', True, 00]
# lista1.extend(lista2)
# print(lista1)
# """Ejercicio - colecciones 1

# Utilizando todo lo que sabes sobre cadenas, listas y
# sus métodos internos, transforma este texto:

# texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies 
# -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

# En este:

# Gordon lanzó su curva...
# - Strawberry ha fallado por un pie! -gritó Joe Castiglione.
# - Dos pies -le corrigió Troop.
# - Strawberry menea la cabeza como disgustado… -agrega el comentarista.
# """

# texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'
# lista = texto.split('&')
# lista[0] += '..'
# lista2 = []
# for oracion in lista:
#     lista2.append(oracion[0].upper() + oracion[1:])
# texto2 = '.\n -'.join(lista2)
# texto2 += '.'
# print(texto2)

# auto = {
#     'nombre' : 'Lautaro',
#     'nombre2' : 'Ramiro',
#     'apellido' : 'Bravo',
#     'DNI' : 42682287,
# }
# print(auto.keys()) #nos muestra todas las llaves
# print(list(auto.keys())) #o para transformarlo en lista

# auto = {
#     'nombre' : 'Lautaro',
#     'nombre2' : 'Ramiro',
#     'apellido' : 'Bravo',
#     'DNI' : 42682287,
# }
# print(auto.items())
# for llave, valor in auto.items():
#     print(llave)
#     print(valor)
#     print()

# Descripción de la actividad. 

# Escribir un programa que guarde en una variable en un diccionario {'Dolar':'$','Euro':'€', 'Libra':'£'}. 

# Luego se le deberá solicitar al usuario que ingrese la divisa que desea visualizar. 

# En el caso de ingresar una divisa no existente en nuestro diccionario, 
# deberemos indicarle con un mensaje de notificación que la divisa no se encuentra disponible.

# dicc = {'dolar':'$','euro':'€', 'libra':'£'}
# divisa = input('Ingrese divisa a visualizar: ').lower()#me transforma el str del usuario todo minuscula 
# print(dicc.get(divisa, 'La divisa que ingresada no se encuentra en el dicc'))

"""### Ejercicio - colecciones

A partir de una lista realizar las siguientes tareas sin modificar la lista original:
1. Borrar los elementos duplicados
2. Ordenar la lista de mayor a menor
3. Eliminar todos los números impares
4. Realizar una suma de todos los números que quedan
5. Añadir como primer elemento de la lista la suma realizada
6. Devolver la lista modificada
7. Finalmente, después de ejecutar la función, comprueba que la suma de todos 
los números a partir del segundo, concuerda con el primer número de la lista

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
"""
{}
[]
{}













lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
# 1. Borrar los elementos duplicados
sin_duplicados = list(set(lista))

# 2. Ordenar la lista de mayor a menor
sin_duplicados.sort(reverse=True)

# 3. Eliminar todos los números impares
sin_impares = []
for valor in sin_duplicados:
    if valor % 2 == 0:
        sin_impares.append(valor)
        
# 4. Realizar una suma de todos los números que quedan
suma = sum(sin_impares)

# 5. Añadir como primer elemento de la lista la suma realizada
sin_impares.insert(0, suma)

# 6. Devolver la lista modificada
print(sin_impares)

# 7. Finalmente, comprueba que la suma de todos  
# los números a partir del segundo, concuerda con el primer número de la lista
print(f'La suma es {suma} y la suma de los elementos de la lista es {sum(sin_impares[1:])}')