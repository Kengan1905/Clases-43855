'''
CLASE 
Caracteristicas = Atributos
Funcionalidades = Metodos
'''

# class ClaseAuto:
    
#     tiene_velocimetro = True
    
#     def tocar_bocina(self):       (((#self representa el objeto que lo esta llamando (auto1, auto2). O sea, 
#yo a este self le podria pedir todo lo que tiene el objeto, le podria pedir un describir_auto, tocar_bocina.
#o le puedo preguntar si tiene velocimetro xq self representa el objeto que lo esta llamando.)))

#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este es un auto. {self}'

# auto1 = ClaseAuto()
# auto2 = ClaseAuto()
# auto1.tocar_bocina()
# auto2.tocar_bocina()
# print(auto1.describir_auto())
# print(auto2.describir_auto())

# print(ClaseAuto.tiene_velocimetro)
# print(auto1.tiene_velocimetro)
# print(auto2.tiene_velocimetro)

'''
    Los """ATRIBUTOS""" de clase se distinguen por el hecho de que es una caracteristica que se comparte con 
todos los objetos q se creen con la clase, aparte, no solo se comparten, si no que desde la misma clase
se puede acceder a ese valor.

    Los METODOS son como las funciones.
    LOS ATRIBUTOS serian como las variables, las trabajamos afuera pero relacionadas al objeto en si 
    o a la clase.
    Y los de INSTANCIA debemos identificar a que instancia se lo vamos a dar, para eso usamos el SELF
'''
# class Onix:
#     def __init__(self, color, puertas): #def __init__(self, color='blanco', puertas=2): <-- Tambien se le
#         self.color = color       #puede poner valores por defecto en caso de no indicarle color y puertas
#         self.puertas = puertas

# auto1 = Onix('Negro', 5)
# auto2 = Onix('Blanco', 3)
# print(auto1.color)
# print(auto2.puertas)

#__init__ me va a ejecutar las funcionas por cada objeto que cree en la clase.
'''
class fordk:
    ruedas: 4 # tipo de atributo: CLASE ya que son variables sueltas, que lo comparten todos los obj.

    def ... (): tipó de atributo: INSTANCIAS funciones
    --init__ se ejecuta cuando creamos un objeto.
    
Metodos de instancias necesitan el SELF como primer parametro.
'''

class Fordk:
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas
        self.blindado = True
        self.aviso_de_fabricacion()
    
    def aviso_de_fabricacion(self):
        print('Se fabrico un Ford K')
    
    def tocar_bocina(self):
        print('Pi pi!!')
    
    def describir_auto(self):
        return f'El auto tiene {self.puertas} puertas y es de color {self.color}'

auto1 = Fordk('Negro', 5)
auto2 = Fordk('Gris', 3)
print(auto1)
print(auto2)

#Si queremos que una clase tenga atributos de instancias, generamos un constructor para esa clase donde
#le vamos a definir esos valores, que pueden ser valores como q no se pueden cambiar desde afuera para 
#que se generen, o tambien lo mismo pero le podemos pasar valores por defecto.
#A una funcion no le podes pasar menos parametros de lo que pide.

#=======================================SEGUNDA PARTE================================================================================= EN LO DE ANTO =======

from typing import Any


class Fordk:
    ...
    cantidad_ruedas = 4
 
    def __init__(self, color='verde', puertas=3):
        self.color = color
        self.puertas= puertas
        self.blindado = True
    
    def tocar_bocina(self):
        print('Pi pi!')
    
    def __str__(self):
        return f'El auto es de color {self.color} y tiene {self.puertas} puertas.'

auto1 = Fordk('Rojo', 5)
auto2 = Fordk('Negro', 3)
auto3 = Fordk('amarillo')
auto4 = Fordk()
#Magic/Dunder Methods: importantes(__init__, __str__), __len__,__getitem__,__setitem__,__iter__
class Concesionaria:
#__init__ se va a ejecutar cuando se crea un objeto.    
    def __init__ (self, nombre, autos_en_venta=[]):
        self.nombre = nombre
        self.autos_en_venta = autos_en_venta
#__str__ cuando queremos transformar a string nuestro objeto.   
    def __str__ (self):
        return f'Esta es la concesionaria {self.nombre}.'#SE USA SI O SI RETURN xq nos retorna un valor.
        
#__len__ cuando queremos sacar la cantidad de un objeto.   
    def __len__ (self):
        return len(self.autos_en_venta)#SE USA SI O SI RETURN xq nos retorna un valor.
#__getitem__ se usa para mostrar un objeto dentro de una coleccion de datos como por ej: lista.
    def __getitem__ (self, ubicacion): 
        return self.autos_en_venta [ ubicacion - 1]
#__setitem__ se usa para reemplazar un valor   
    def __setitem__ (self, ubicacion, nuevo_dato):
        self.autos_en_venta [ubicacion - 1] = nuevo_dato
#__iter__ se usa para poder recorrer una coleccion de elementos.   
    def __iter__ (self):#el iter no trabaja con return, se usa YIELD
        for auto in self.autos_en_venta:
            yield auto #yield te muestra el elemento y se pausa ahi, cuando lo llaman de nuevo, continua desde el mismo
                                    #lugar, y sigue recorriendo 1x1, hasta que no haya mas elementos y deje de recorrer.
    
Concesionaria1 = Concesionaria('Grillo',[auto1,auto2])
Concesionaria2 = Concesionaria('Black',[auto3,auto4,auto1,auto2])
print(Concesionaria1)
print(Concesionaria2)
print(len(Concesionaria1))
print(len(Concesionaria2))
print(Concesionaria1[1])
Concesionaria2[1] = auto2
print(Concesionaria2[1])
for elemento in Concesionaria2:
    print(elemento)

'================================================================================================================='
...

class persona:
    
    def __init__ (self, dni, color_de_pelo_, cantidad_de_cirugias):
        self.__dni = dni
        self.color_de_pelo = color_de_pelo_
        self.cantidad_de_cirugias = cantidad_de_cirugias
    
    def mostrar_dni(self):#se crea la funcion para mostrar dni con el self.__dni
        print(self.__dni)#es lo mismo q get_dni solo q si muestra lo que solicitamos xq usa print
    
    def get_dni(self):#no aparece nada xq queremos q muestre por pantalla un dato y se usa print()
        return self.__dni
    
    def set_dni(self, valor_nuevo):
        self.__dni = valor_nuevo
    


persona1 = persona(42682287,'negro',3)
persona2 = persona(42954894,'castaño',1)
persona3 = persona(11222333,'rubio',1)
# print(persona1.color_de_pelo)
# persona1.mostrar_dni()
# persona2.mostrar_dni()
# persona3.mostrar_dni()
# persona1.set_dni(33666777)  #Se llama a la funcion set y se pasa por parametro el valor nuevo.
# persona1.mostrar_dni()      #luego se muestra la funcion mostrar dni sin el print
# persona2.set_dni(11999000)
# persona2.mostrar_dni()
# persona3.set_dni(77999888)
# persona3.mostrar_dni()
# persona1.get_dni()
