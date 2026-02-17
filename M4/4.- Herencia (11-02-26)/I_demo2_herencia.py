'''
Vas a implementar una clase base con un método común, y dos subclases que sobrescriben ese método de
forma distinta.

Clase base Animal:
● Atributo: nombre
● Método: emitir_sonido() que imprima
"Sonido genérico"
Subclases Perro y Gato:
● Sobrescriben emitir_sonido() para imprimir:
○ "Guau!" en Perro
○ "Miau!" en Gato

Qué se debe probar:
● Crear un objeto de cada subclase
● Llamar a emitir_sonido() desde
cada uno
● Verificar que el comportamiento
es distinto, aunque el método se
llama igual
'''
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def emitir_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def emitir_sonido(self):
        print("Guau!")

class Gato(Animal):
    def emitir_sonido(self):
        print("Miau!")


#==================== Demo ==================
perro = Perro("Firulais")
gato = Gato("Mishi")

perro.emitir_sonido()
gato.emitir_sonido()