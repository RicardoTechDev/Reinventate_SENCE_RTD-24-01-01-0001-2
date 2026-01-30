'''Define la clase y sus métodos
Creá una lista de 3 o más mascotas
Recorrelas con un for y:
Mostrá su presentación
Indicá si es joven o no
Bonus: Filtrá solo las mascotas jóvenes en una nueva lista'''


class Mascota:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad

    def presentarse(self):
        print(f"Soy {self.nombre}, un/a {self.tipo}, de {self.edad} años ")

    def es_joven(self):
        if(self.edad < 5):
            return True
        else:
            return False
        
mi_gato = Mascota("Garfield", 4, "Gato")
mi_perro = Mascota("Firulais", 8, "Perro")
mi_tortuga = Mascota("Carlota", 10, "Tortuga")

        
lista = []
lista.append(mi_gato)
lista.append(mi_perro)
lista.append(mi_tortuga)

lista_jovenes = []
for i in lista:
    if i.es_joven():
        lista_jovenes.append(i)

for i in lista:
    i.presentarse()
    print(i.es_joven())


print("\nSolo mascotas jóvenes:")
for i in lista_jovenes:
    i.presentarse()