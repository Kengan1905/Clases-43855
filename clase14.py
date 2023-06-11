# #HERENCIAS:
# #DRY Don't Repeat Yourself
# class Animal:
#     def tipo_animal(self):#para simplificar y no repetir esta funcion en la clase perro y gato
#         print(f'Yo soy un', type(self).__name__)#creamos esta clase padre
#                                     #.__name__ nos da el nombre de la clase especifica en string.

# class Perro(Animal):#entre parentesis le indiciamos su clase padre.

#     def hablar(self):
#         print('Guau guau!!')
        
#     def caminar(self):
#         return 'Perro caminando'

# class Gato(Animal):#entre parentesis le indiciamos su clase padre.
    
#     def hablar(self):
#         print('Miau miau!!')

# class Abeja(Animal):#aca creo una clase vacia, pero que tiene como padre la clase Animal.
#     ...#por lo tanto puede pedirle el tipo de animal.

# gato = Gato()
# perro = Perro()
# abeja = Abeja()

# gato.tipo_animal()
# gato.hablar()

# perro.tipo_animal()
# perro.hablar()

# abeja.tipo_animal()
#============================================================================================================
#============================================================================================================
#============================================================================================================

# class Vehiculo:
#     def __init__ (self,marca):
#         self.marca = marca
        
#     def descripcion(self):
#         return f'{type(self).__name__} marca: {self.marca}'

# class Auto(Vehiculo):
#     ...

# class Lancha(Vehiculo):
# # #     # v1
# # #     # def __init__(self, tipo_ancla, marca):          #creo un init aca porque primero se fija si tiene un atributo de instancia
# # #     #     self.tipo_ancla = tipo_ancla                #en su clase, si no la tiene, se fija en el padre.
# # #     #     self.marca = marca
    
# # #     #v2: super: llama al magic methods(__init__) del padre y le pasamos la variable marca.
#     def __init__(self, tipo_ancla, marca):
#         super().__init__(marca)
#         self.tipo_ancla = tipo_ancla
# #                                                                #cuando se llama a lancha, viene a su clase y sus codigos, hace el init, cuando llega a super le dice que 
# # #                                                                #haga el init del padre y le pasa "marca" para que lo haga, sube al padre lo hace, vuelve y continua
# # #                                                                #la siguiente linea de codigos.
#     def descripcion(self):
#         return super().descripcion() + f'. Ancla {self.tipo_ancla}.' 

# class Moto(Vehiculo):
#     ...

# auto = Auto('Ford')
# print(auto.descripcion())

# lancha = Lancha('sin cepo','Bermuda')
# print(lancha.descripcion())

# moto = Moto('Yamaha')
# print(moto.descripcion())

# EXISTE UN TIPO DE CLASE QUE SE LLAMA "CLASE ABSTRACTA" que es una clase hecha para ser de tipo padre                                                                                                                       traje una funcion afuera de la clase para poder ser "exportado" a la clase 15
#Por lo tanto en esa clase se usa para generalidades y no se puede crear objetos mediante esa clase, para q sepamos.

#Si en la clase hija le ponemos un atributo q es igual a la clase padre, la hija va a ser prioridad.
#para usar el atributo de la clase Padre se usa el super().
#==============================POST BREAK

class Animal:
    def tipo_animal(self):
        print(f'Yo soy un', type(self).__name__)

class Terrestre(Animal):
    def caminar(self):
        print(f'{type(self).__name__} esta caminando.')
    
    def tiene_cola(self):
        print('Soy terrestre y no tengo cola.')

class Acuatico(Animal):
    def nadar(self):
        print(f'{type(self).__name__} esta nadando.')

    def tiene_cola(self):
        print('Soy acuatico y no tengo cola.')

class Perro(Terrestre):
    def hablar(self):
        print('Guau guau!!')

class Delfin(Acuatico):
    ...

class Pato(Acuatico, Terrestre): #puede tener varias HERENCIAS o clases padres
    def hablar(self):            #por lo tanto puede tener todo lo q tiene los demas
        print('Cuak cuak!!')

# perro = Perro()
# perro.caminar()
# perro.hablar()
# perro.tipo_animal()
# print(f'\n')
# delfin = Delfin()
# delfin.nadar()
# delfin.tipo_animal()
# print('\n')
# pato = Pato()
# pato.caminar()
# pato.hablar()
# pato.nadar()
# pato.tipo_animal()

# pato.tiene_cola() #Cual buscara Terrestre o Acuatico (?.
#print(Pato.__mro__) CODIGO PARA SABER EN QUE ORDEN BUSCA. #Nos devuelve el orden de ejecucion de lo que yo le pida a la clase Pato.

#POLIMORFISMO es que nos permita utilizar algo con el mismo nombre
#pero que tenga diferentes funcionalidades dependiendo de a quien se lo pedimos

# Hablar() en Pato y Perro es Polimorfico, porque estan escritos igual y ambos hablan
# dice algo depende de a que funcionalidad se la pedimos

#============================ EJEMPLO DE POLIMORFISMO, usar funciones llamadas iguales pero nos devuelve un valor dependiendo de quien las llame ==========
# lista_de_animales1 = [Pato(), Perro(), Delfin(), Pato(), Perro(), Perro(), Delfin()] #Se puede crear objetos en listas como este ejemplo

# for animal in lista_de_animales1:
#     animal.tipo_animal()

# lista_de_animales2 = [Pato(), Perro(), Pato(), Perro(), Perro()]

# for animal in lista_de_animales2:
#     animal.hablar()

#dUCK TYPING pensar los codigos o los objetos como si fuesen lo que realizan, si camina como un pato y hace cuack! como un pato para mi tiene que ser un pato.

# ENCAPSULAMIENTO, si nosotros queremos que la clase hija no pueda acceder a un elemento de la clase padre le ponemos 2ble ion bajo "__funcion()".











