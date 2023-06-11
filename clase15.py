# import clase14

#Scripts
#import sys
# #este sys atrapa en el atributo argv todo lo q le pase en la terminal desp de python.

# print(sys.argv)
# print(type(sys.argv))

# argumentos = sys.argv[:]#guardamos en una variable los resultados de sys.argv
# print(argumentos)#por si modificamos algo para no dañar el codigo

# print('AHI TE VA DE QUE GRUPO SOS')
# nombre = sys.argv[1]
# preferencia = sys.argv[2]

# if (preferencia == 'marvel' and nombre < 'm') or (preferencia == 'capcom' and nombre > 'n'):
#     print('Sos del grupo A')
# else:
#     print('Sos del grupo B')

#Modulos. antes de la hora de clase se ve modulos.
#Los import siempre van arriba de todo.
#
# from clase14 import Perro, hablar as voy_hacer_que_perro_ladre

# perro = Perro()
# voy_hacer_que_perro_ladre(perro)

#paquetes: nos permite meter modulos en un paquete y en este paquete saber todo lo que
#se tiene. Los paquetes tienen formato distintos a los modulos. Los paquetes trabajan con
#carpetas. Los paquetes nos permiten crear paquetes que son redistribuibles. 
#Son paquetes que contienen modulos pero que con esto tenemos la posibilidad de subirlo a la internet
#permite que los demas usuarion puedan descargar ese paquete y utilizarlos
#La idea de los paquetes es agrupar modulos que estan relacionados entre si.

#2 posibilidades, son lo mismo. pero esta me funciona:

# from mi_paquete import funciones
# from mi_paquete.funciones import llama_hablar as llama_hablar_funciones
# from mi_paquete.clases import Perro as PerritoLoco

# perro = PerritoLoco()
# perro.caminar()

# llama_hablar_funciones(perro)

# def llama_hablar():
#     print('Mira lo que hago')


# llama_hablar()


#Formula para crear un paquete redistribuible:

# from setuptools import setup

# setup(
#     name='el_paquetito',
#     version= '1.0',
#     description= 'Cree mi primer paquete redistribuible',
#     author= 'Yo',
#     author_email= 'pepito@grillin.io',
#     packages=['mi_paquete']
# )

#=============================         EN TERMINAL:         ===================================              =======================
#python clase15.py sdist (EJECUTO) crea el paquetito y todo y se crean las carpetas
#pip freeze (para ver todos los paquetes que tengo yo instalados en mi entorno)
#para INSTALAR este paquete en la terminal: 
#pip install dist/el_paquetito-1.0.tar.gz(enter)
#pip freeze ahora me figura instalado el_paquetito
#Ahora la carpeta mi_paquete la puedo borrar, pero lo tengo instalado y activado
#puedo ejecutar los codigos de la clase 15 y no me salta error porque utilizo lo que ya esta instado
#ya lo tengo instalado y lo puedo utilizar.
#si en terminal pongo deactivate se desactiva
#ejecuto la clase 15 y ya me genera el error
#ya que no lo tengo en mis archivos y tampoco lo tengo instaldo en mi entorno virtual

# ============================================= CONTINUACION EN CASA==========================================
#Ctrl + click eb 'collections' y navegamos por ahi.

# from collections import namedtuple, Counter #se escribe asi, no es mucha ciencia.
# #Esto nos devuelve en foma de diccionario:
# Key: que serian los elementos que aparecen
# Llaves: la cantidad de veces que aparecen esos elemento

# print(Counter('abcabc123'))
# print(Counter((1,2,3,4,5,3,5,7,8,9,1,1,1,2,2)))

#================= NAMED TUPLE (otro tipo de clases) o Pseudoclase.

# from collections import namedtuple, Counter
# #Pescado con mayuscula como si fuera CLASE
# #     |funcionalidad |La Clase  | key 1   | key 2    | key 3  |
# Pescado = namedtuple('Pescado', ['nombre', 'especie', 'peso'])

# pescado1 = Pescado('pecesin', 'payaso', 200)

# print(Pescado)
# print(pescado1)
# print(pescado1.nombre)
# print(pescado1[0])
# print(pescado1._asdict()) #transformamos a dicc lo q es pescado
# print(list(pescado1._asdict().items())[0]) #acceso?

#una tupla es mas una clase q un diccionario
#porque se puede acceder "pescado1.nombre" como en las clases

#Math nos trae la funcionalidad de pi

# import math

# print(math.pi) #da la funcionalidad de pi
# print(math.sqrt(64)) #sqrt: sacar la raiz
# print(round(3.3)) #roun: redondear
# print(round(3.5))
# print(round(3.8))
# print(math.floor(3.8)) #redonde para arriba sin importar la decimal q tenga
# print(math.ceil(3.3)) #redonde para abajo sin importar la decimal q tenga

#Se usa para matematicas y esta bueno q lo sepamos pero no es importante

# import random
# #nos sirve para obtener cosas RANDOM
# #a random le podemos pedir randrange y nos va a dar un valor random
# #entre el 0 y el tope que le indiquemos aca
# print(random.randrange(15)) 
# print(random.randrange(15, 22))
# print(random.randrange(15, 22, 2))

# lista = ['hoy', 'corri', '4', 'kilometros']
# print(random.choice(lista)) #nos devuelve un valor random de la lista
# print(random.choice(lista)) #nos lo devuelve suelto
# print(random.choice(lista)) #esto esta bueno para los sorteos ej
# print(random.choice(lista))
# print(random.choice(lista))

# print(random.choices(lista, k=3)) #choices es lo mismo pero
# print(random.choices(lista, k=5)) #se le puede pasar por parametro k=x cantidad de valores
# print(random.choices(lista, k=2)) #que queremos que nos devuelva
# print(random.choices(lista))#y si no le pones k=x nos devuelve uno solo pero dentro de lista

#================================= DATE TIME
# from datetime import datetime, timedelta

# dt = datetime.now()
# print(dt)

# dt_custom = datetime(2000, 1, 1) #si apoyamos el mouse en datetime podemos ver los parametros y el orden que tiene.
# print(dt_custom)

# print(dt.strftime("%A %d %B %Y %I:%M")) #date time modulo nos devuelve Sunday 11 June 2023 01:54:13
# print(dt.hour) #podemos acceder a la hora, dia, mes, año, segundos, etc.

# dt1 = dt.replace(day=5) # le digo q de la fecha de ahora, al dia lo cambie por la fecha 5
# print(dt)
# print(dt1)

# td = timedelta(days=15)
# # al dt se le suma o resta el td de timedelta(days=15) se le resta o suma un rango de 15 dias y nos da la fecha
# dato_de_fecha_modificado = dt + td
# dato_de_fecha_modificado = dt - td 

# print(dato_de_fecha_modificado)

#CLASE 16 CON LA MISMA CLASE 15











































