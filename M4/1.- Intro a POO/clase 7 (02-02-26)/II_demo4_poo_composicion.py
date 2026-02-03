'''
Vas a diseñar una clase principal que contenga otras clases como parte de su estructura, representando una
relación de composición real.

Qué debe tener cada clase:
➔ Clase Procesador:Atributos: marca, velocidad_ghz
➔ Clase MemoriaRAM:Atributos: capacidad_gb, tipo
➔ Clase DiscoDuro:Atributos: capacidad_gb, tipo (HDD/SSD)
➔ Clase Computadora:Atributos: marca, y objetos de tipo Procesador, MemoriaRAM, DiscoDuro
◆ Método mostrar_info() que imprima todos los datos, incluyendo los de sus componentes
Qué se debe probar:
● Crear instancias individuales de los componentes
● Crear una Computadora pasándole esos objetos
● Usar el método mostrar_info() para mostrar toda la información en conjunto
'''
class Procesador:
    def __init__(self, marca, velocidad_ghz):
        self.marca = marca
        self.velocidad_ghz = velocidad_ghz

    def __str__(self):
        return f"{self.marca} - {self.velocidad_ghz} Ghz"

class MemoriaRAM:
    def __init__(self, capacidad_gb, tipo):
        self.capacidad_gb = capacidad_gb
        self.tipo = tipo

    def __str__(self):
        return f"{self.capacidad_gb} GB - {self.tipo}"


class DiscoDuro:
    def __init__(self, capacidad_gb, tipo): #tipo HDD o SSD
        self.tipo = tipo
        self.capacidad_gb = capacidad_gb

    def __str__(self):
        return f"{self.capacidad_gb} GB - {self.tipo}"


class Computadora:
    def __init__(self, marca, procesador, ram, disco):
        self.marca = marca
        self.procesador = procesador #objeto del tipo Procesador
        self.ram = ram              #objeto del tipo MemoriaRAM
        self.disco = disco          #objeto del tipo DiscoDuro

    def mostrar_info(self):
        print("Información la computadora")
        print(f"Marca: {self.marca}")
        print(f"Procesador: {self.procesador}")
        print(f"Memoria RAM: {self.ram}")
        print(f"Disco: {self.disco}")


#================= DEMO =============
print("==== Creando componentes ====")
cpu = Procesador("Intel", 3.6)
ram = MemoriaRAM(16, "DDR4")
disco = DiscoDuro(512, "SSD")

print("==== Creando la computadora con sus componentes ====")
pc = Computadora("Lenovo", cpu, ram, disco)

pc.mostrar_info()
