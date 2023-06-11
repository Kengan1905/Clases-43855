#POO Programacion orientada a objeto.

#Para identificar entre funcionalidades y metodos:

#Las funcionalidades generalmente se encuentran solas como el print y al lado tienen lo siguiente, estan solos
#Y los metodos somo como el .pop, tienen la variable, y le sigue para odernarles, .len .update .pop, etc.

#COMO SE PIENSA CON POO?
#Elemento Principal ---------> CLASE
#Caracteristicas    ---------> Atributo
#Funcionalidades    ---------> Metodo

#TIPOS DE RELACIONES:
#EXISTEN 3 TIPOS DE RELACIONES:
    #AGREGACION / COMPOSICION.
    #ASOCIACION.
    #GENERALIZACION / ESPECIALIZACION. Herencia simple y Herencia Multiple.

#AGREGACION: es cuando para crear la primer clase no se necesita de otra.
#COMPOSICION: es cuando si se necesita la segunda clase para crear la primera.
#ej 1. la clase empresa no necesita clientes para crear la empresa, los va a necesitar desp.
#ej 2. la clase empresa si necesita de empleados para poder crearse.
#SON COMO RECETAS PARA CREAR UNA CLASE, Y OTRA RECETA PARA CREAR OTRA CLASE.

#ASOCIACION: ej. coche esta en composicion con motor xq dentro de la clase coche figura motor, pero
#persona aparece en coche pero igualmente esta relacionada a coche aunque no pertenezca adentro.

#GENERALIZACION/ESPECIALIZACION: lo que nos permite poo es q de una clase podamos tener otra mas especifica,
#o que de otra clase podamos tener otra mas general.
#EJ. podemos tener una clase que hace autos genericos, pero tambien podriamos tener una clase mas especifico,
#pero que hace lo que hace la clase autos pero especificamente de la marca Ford.

#La estructura de las clases la tiene lo que fabrica cosas...

#LAS CARDINALIDADES EN LAS RELACIONES.

#Nos sirven para indicar cuantos objetos de una clase se pueden relacionar con cuantos objetos de otra clase
#En la cardinalidad lo importante es marcar si la relacion es a muchos objetos ("..*") o si solo es a uno
# (1), incluso a veces puede decir a uno o ninguno (0,1)

#cuando nosotros decimos OBJETOS o INSTANCIAS nos estamos refiriendo a un elemento creado por una clase
#Todos los objetos o instacias creadas por una clase van a tener las mismas funcionalidades.
#A diferencia de los atributos que van a tener los mismos atributos pero la informacion va a variar.

#---------------------------------------------------------
#class ClaseAuto: # PascalCase
... # pass

# auto1 = ClaseAuto()
# auto2 = ClaseAuto()
#---------------------------------------------------------

#Nosotros tenemos que pensar a los metodos como funciones, si nosotros a las funciones le podemos poner if, try, 
#bucles, 30 lines de codigo, nosotros a los metodos les podemos hacer todo lo mismo.

#class NombreClase:
    #def nombre_funcion(self): # self siempre va como primer parametro
...# codigo


#class ClaseAuto: # PascalCase
            
    #def tocar_bocina(self):
        #print('Pi pi!!')  

    #def describir_auto(self):
        # return f'Este es un auto.'
        #return f'Este es un auto. {self}'

#auto1 = ClaseAuto()
#auto2 = ClaseAuto()
#print(auto1)
#print(auto2)
#auto1.tocar_bocina()
#auto2.tocar_bocina()

                                #self va a valer auto1
#print(auto1.describir_auto()) # describir_auto(auto1)

                                #self va a valer auto2
#print(auto2.describir_auto()) # describir_auto(auto2)

#===================================================================================

# Atributos

# De clase

# class ClaseAuto: # PascalCase
    
#     tiene_velocimetro = True
            
#     def tocar_bocina(self):
#         print('Pi pi!!')  

#     def describir_auto(self):
#         # return f'Este es un auto.'
#         return f'Este es un auto. {self}' 

    
# auto1 = ClaseAuto()
# auto2 = ClaseAuto()
# auto1.tocar_bocina()
# auto2.tocar_bocina()
# print(auto1.describir_auto())
# print(auto2.describir_auto())

# print(ClaseAuto.tiene_velocimetro)
# print(auto1.tiene_velocimetro)
# print(auto2.tiene_velocimetro)#les pido q me muestren la info de estos objetos creados.