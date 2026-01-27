'''
1. Definir una clase Persona con el método especial __init__()
2. Asignar atributos: nombre, edad
3. Crear el método presentarse() que imprima una presentación
4. Instanciar dos objetos diferentes con datos propios
5. Ejecutar el método presentarse() desde cada objeto
6. Ver cómo cada objeto mantiene su propio estado
7. Bonus: Agregar otro método, como cumplir_anios() que sume 1 a la edad
Objetivo: visualizar cómo una clase puede generar múltiples objetos, cada uno con su identidad y
comportamiento.
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Mi edad actual es de {self.edad}")


#------------- DEMO ----------------
ana = Persona("Ana", 15)#una instancia
carlos = Persona("Carlos", 20)#una segunda instancia
persona3 = Persona("Sandra", 25)

print("Presentación inicial")
ana.presentarse()
carlos.presentarse()
persona3.presentarse()

ana.cumplir_anios()
ana.variable




    