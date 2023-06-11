#PRIMERA ENTREGA

repetir_menu = True
dicc = {
    'Lautaro' : '123',
    'Andres' : '456',
    'Camila' : '111',
}

#Inicio de sesion (login)
def login():
    usr = input('Ingrese su usuario: ')
    psr = input('Ingrese su contraseña: ')
    if usr in dicc:
        if (dicc[usr] == psr):
            print('Bienvenido')
        else:
            print('La contraseña es incorrecta')
    else:
        print('Este usuario no existe')

def mostrar_cuentas():
    registrados = list(dicc.keys())
    return registrados

# 2 Funciones para registrarse:
def usuario():
    user = input ('Ingrese un nombre de usuario: ')
    return user

def contraseña():
    clave = input ('Ingrese una contraseña: ')
    return clave

while repetir_menu:
    print('''
=====================
        MENU
=====================
1. Iniciar sesion.
2. Registrar.
3. Salir.
''')
    opcion_elegida = input('Ingrese una opción: ')
    if opcion_elegida == '1':
        inicio_sesion = login()
    elif opcion_elegida == '2':
        usr = usuario()
        psr = contraseña()
        if usr not in dicc:
            dicc.update({usr:psr})
            print('Usted se ha registrado con exito.')
            print(dicc)
        else:
                print('Este usuario ya existe')
    elif opcion_elegida == '3':
        print('Hasta luego!')
        repetir_menu = False
    else:
        print('Ingrese una opcion valida')

print(mostrar_cuentas())








