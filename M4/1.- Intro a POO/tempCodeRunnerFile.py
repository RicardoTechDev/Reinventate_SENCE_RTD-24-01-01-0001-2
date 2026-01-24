'''
1. Definir una clase simple llamada Animal con atributo nombre y método hablar()
2. Crear una instancia de Animal llamada mi_gato
3. Ejecutar un método desde la instancia
4. Comprobar con sinstance() ique mi_gato es una instancia de Animal
5. Mostrar que una instancia tiene vida propia y puede almacenarse, pasarse como parámetro, o
guardarse en listas
Objetivo: entender que una instancia es un objeto real creado a partir de una clase, y que puede
verificarse con herramientas como isinstance().
'''
from objeto_persona import Persona

class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo   = tipo
    
    def hablar(self):
        print(f"{self.nombre} hace un sonido.")



mi_gato = Animal("Michi", "Gato")
mi_gato.hablar()

print(isinstance(mi_gato, Animal))#--> True
print(isinstance(mi_gato, Persona))#--> False

animales = []
animales.append(mi_gato)

leon = Animal("Bofi", "León")
animales.append(leon)

print(animales)