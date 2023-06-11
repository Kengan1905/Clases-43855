# class Onix:
#     def __init__(self, color, puertas): #def __init__(self, color='blanco', puertas=2): <-- Tambien se le
#         self.color = color       #puede poner valores por defecto en caso de no indicarle color y puertas
#         self.puertas = puertas

# auto1 = Onix('Negro', 5)
# auto2 = Onix('Blanco', 3)
# print(auto1.color)
# print(auto2.puertas)

# #__init__ me va a ejecutar las funcionas por cada objeto que cree en la clase.
# '''
# class fordk:
#     ruedas: 4 # tipo de atributo: CLASE ya que son variables sueltas, que lo comparten todos los obj.
# '''

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



auto1 = Fordk('blanco', 5)
auto2 = Fordk('azul', 3)
print(auto1)
print(auto2)
print(auto1.describir_auto())
print(auto2.describir_auto())
print(auto1.blindado)