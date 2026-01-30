class Celular:
    def __init__(self, marca, modelo, almacenamiento):
        self.marca= marca
        self.modelo, = modelo,
        self.almacenamiento = almacenamiento

    def encender(self):
        print(f"Encendiendo {self.marca} {self.modelo} ")

    def mostrar_info(self):
        
        print(f" {self.marca} {self.modelo} {self.almacenamiento}")

motorola = Celular("Motorola", "X4 ", "256 GB" )
nokia = Celular("Nokia", "gt1", "128 GB" ) 

motorola.encender()
motorola.mostrar_info()

nokia.encender()
nokia.mostrar_info()