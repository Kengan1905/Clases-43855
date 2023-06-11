#primer_numero = int(input('dame un numero: '))
#segundo_numero = int(input('dame otro numero: '))

#if primer_numero < segundo_numero:
    #print('el primer_numero es menor que segundo_numero')
    #if primer_numero == segundo_numero - 3:
        #print('el primer_numero es igual a segundo_numero -3')
    #print('Sali del if anidado')

#if primer_numero < segundo_numero:
    #print('el primer_numero es menor que el segundo_numero')
#else:
    #print('el primer_numero no es menor al segundo_numero')

#var = 10
#primer_numero = int(input('dame un numero: '))
#segundo_numero = int(input('dame otro numero: '))

#if primer_numero == segundo_numero:
    #print('primer numero es igual al segundo')
    #if primer_numero > var:
        #print('primer numero es mayor a var')
    #else:
        #print('primer numero no es mayor a var')
#else:
    #print('ambos valores no son iguales')

#contrasenia = 'pass123'
#pass_ingresada = input('Ingrese la contraseña: ')

#if contrasenia == pass_ingresada:
    #print('Bien, la contraseña es correcta')
#else:
    #print('la contraseña ingresada es incorrecta')

#print('la contraseña es correcta') if contrasenia == pass_ingresada else print('la contraseña es incorrecta')

#contrasenia = 'pass123'
#pass_ingresada = (input('Ingrese la contraseña: '))

#if contrasenia == pass_ingresada:
    #print('La contraseña es correcta')
#else:
    #print('La contraseña es incorrecta :(')

#variable = 1
#while True:
#    variable += 100
#    print('la variable ahora vale', variable)

repetir_menu = True
while repetir_menu:
    print('''
===============
    MENU
===============
1. Extraer efectivo.
2. Consulta de saldo.
3. Salir    
''')
    opcion_elegida = input('Elija una opcion: ')
    if opcion_elegida == '1':
        extraer = True
        extraer = input('Efectivo que desea extraer: ')
        print('Usted extrajo', extraer)
    elif opcion_elegida == '2':
        print('Su saldo es $550.700')
    elif opcion_elegida == '3':
        print('Hasta luego')
        repetir_menu = False
    else:
        print('Vuelva a intentar con una opcion valida')

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#valor_extraido = 0
#while valor_extraido != 3:
#    valor_extraido = numeros.pop()
#    print(valor_extraido)

# lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# for dato_devuelto in enumerate(lista):
#     print(dato_devuelto)

# lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# for indice, valor in enumerate(lista):
#     print(indice, valor)

# multi = 2
# for numero in range(4, 100000, 2):
#     if multi:
#         print(f'2x{multi} = {numero}')
#         multi += 1

