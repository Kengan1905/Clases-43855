# archivo_abierto = open('prueba.txt', 'a')
# archivo_abierto.write('\nEscribiendo mi primera Linea')
# archivo_abierto.close()

# archivo_abierto = open('carpeta/prueba.txt', 'w')
# archivo_abierto.write('Cree una carpeta, un archivo y mi segunda linea')
# archivo_abierto.close()

# archivo = open('miHobbieFavorito.txt', 'w')
# for i in range(1,4):
#     archivo.write(input(f'Ingrese su hobbie numero{i}: ') + '\n')
# archivo.close()

# archivo = open('miHobbieFavorito.txt', 'r')
# texto_del_archivo = archivo.read()
# print(texto_del_archivo)
# archivo.close()
# print(texto_del_archivo)
#nos permite seguir utilizando la lectura ya q lo guardamos en una variable sin importar que este el archivo cerrado

# archivo = open('miHobbieFavorito.txt', 'r')
# linea1_del_archivo = archivo.readline()
# print(linea1_del_archivo)
# linea2_del_archivo = archivo.readline()
# print(linea2_del_archivo)
# linea3_del_archivo = archivo.readline()
# print(linea3_del_archivo)
# archivo.close()
# cada readline nos muestra una linea mas del archivo

archivo = open('miHobbieFavorito.txt', 'r')
# print(archivo.read())
# print('============================')
# print(archivo.read())
# print('============================')
archivo.seek(0)
print(archivo.readlines())
print(archivo.readlines())
archivo.seek(0)
print(archivo.readlines())
archivo.seek(17)
print(archivo.readline())
archivo.close()
# .seek(indice) posiciona el puntero
lista = [1,2,3,4,5,6,7,8,9]
mi_dic = {
    'clave1' : 1,
    'clave2' : 2,
    'clave3' : 3,
    'clave4' : 4,
    'clave5' : 5,
    'clave6' : 6,
    'lista' : lista
}

import json 
# with open('test.json', 'w') as f:
#     json.dump(mi_dic, f, indent=4)


with open('test.json', 'r') as f:
    datos = json.load(f)
    print(datos)
    print(type(datos))