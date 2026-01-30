'''
Vas a diseñar una clase que modele un empleado, 
incorporando tanto un método de clase como uno estático
para aplicar distintos tipos de comportamiento.

1. Lo que deberá tener la clase:
● Atributos públicos como nombre y salario
● Un atributo de clase llamado aumento_general 
con un valor inicial (ej. 1.05)
● Un método de clase que permita modificar 
el porcentaje de aumento general para
todos los empleados
● Un método estático que reciba un salario y 
verifique si supera un cierto umbral (ej.
sueldo mínimo)
2. Qué se debe probar:
● Crear varios empleados con salarios distintos
● Modificar el aumento general desde la clase
● Usar el método estático para evaluar si un salario es alto o bajo
● Ver cómo el método de clase afecta a todos los objetos
'''

class Empleado:
    """
    Demo: Métodos de clase y métodos estáticos

    - Atributos públicos : nombre y salario
    - Atributo de clase : aumento_general
    - Método de clase: modificar el aumento_general para todos
    - Método estático: verifique si salario supera un cierto umbral
    """

    #?Atributo de clase, lo dejamos como privado en esta ocación
    __aumento_general = 1.05 #5 % de aumento para todos (todas las instancias)
    # ((5/100) * 5000) + 5000 --> 5250 
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    

    @classmethod
    def cambiar_aumento_general(cls, nuevo_factor):
        if nuevo_factor <= 1:
            print("El aumento debe ser mayor a 0. Ej.: 1.05, 1.10, 1.15")
        
        cls.__aumento_general = nuevo_factor
        print(f"Nuevo factor ingresado de manera correcta {cls.__aumento_general}")


    @staticmethod    
    def supera_umbral(salario, umbral):
        '''
            if salario >= umbral:
                return True
            else:
                return False
        '''
        return salario >= umbral
    

    def mostrar_info_empleado(self):
        print(f"Empleado: {self.nombre} | Salario: {self.salario}")    

    
    def aplicar_aumento(self):
        self.salario = self.salario * Empleado.__aumento_general   #self.__aumento_general


    def get_aumento_general(self):
        return Empleado.__aumento_general

#=============== DEMO ===============
empleado1 = Empleado("Luis", 1500000)
empleado2 = Empleado("Ana", 1800000)
empleado3 = Empleado("Sofía", 1200000)

print("=========== Empleado iniciales ============")
empleado1.mostrar_info_empleado()
empleado2.mostrar_info_empleado()
empleado3.mostrar_info_empleado()

print("=========== Evaluar salario vs umbral ============")
umbral = 1250000
empleados = [empleado1, empleado2, empleado3]

for empleado in empleados:
            #Estamos llamando al método estático
    es_alto = Empleado.supera_umbral(empleado.salario, umbral)#True o False

    if es_alto:
        print(f"El salario de {empleado.nombre} es alto respecto del umbral {umbral}")
    
    else:
        print(f"El salario de {empleado.nombre} es bajo respecto del umbral {umbral}")


print("=========== Cambiar aumento general desde la clase ============")
#print(Empleado.__aumento_general)
print(empleado1.get_aumento_general())

Empleado.cambiar_aumento_general(1.25)
print(empleado1.get_aumento_general())
print(empleado2.get_aumento_general())
print(empleado3.get_aumento_general())

print("=========== Aumento de salario ============")
for empleado in empleados:
    empleado.aplicar_aumento()

print("=========== Empleados luego del aumento de salario ============")
empleado1.mostrar_info_empleado()
empleado2.mostrar_info_empleado()
empleado3.mostrar_info_empleado()