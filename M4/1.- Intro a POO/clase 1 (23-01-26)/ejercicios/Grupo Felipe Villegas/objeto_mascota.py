class Mascota:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo


    def presentarse(self):
        print(f"Soy {self.nombre}, un/a {self.tipo} de {self.edad} años")

        
    def es_joven(self):
        return self.edad < 5
            

mascota1 = Mascota("Daysi", 10, "Perro")
mascota2 = Mascota("Pinky", 3, "Gato")
mascota3 = Mascota("Max", 2, "Caballo")
#======= Presentación=======#
mascota1.presentarse()
mascota2.presentarse()
mascota3.presentarse()
#============Mostrar atributos a través de una lista===========#
lista_mascotas = []
lista_mascotas.append(mascota1)
lista_mascotas.append(mascota2)
lista_mascotas.append(mascota3)
#========= Recorre lista mostranado los atributos de las mascotas=========#
for self in lista_mascotas:
    print(self.nombre, self.edad, self.tipo)
#======== Verificación edad=========#
print(mascota1.es_joven())
print(mascota2.es_joven())
print(mascota3.es_joven())

lista_joven = []

for mascota in lista_mascotas:
    if mascota.es_joven():
        lista_joven.append(mascota)

for self in lista_joven:
    print(self.nombre, self.edad, self.tipo)





    