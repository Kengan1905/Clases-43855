#ejemplo 2

a = 5
b = 1
c = 0
try:
    try:
        valor = a/b
    except:
        valor = a/c
        print('No se puede dividir por 0.')
    else:
        valor /= c
        print(f'La division dio como resultado {valor}.')
    
    print(int(input('Ingrese un numero: ')))
except:
    print('Exploto despues del try.')