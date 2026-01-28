class Celular:
    def __init__(self, marca, modelo, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento


    def encender(self):
        print(f"Se ha encendido el telefono {self.marca} {self.modelo}")


    def mostrar_info(self):
        print(f"Información de Celular {self.marca} || {self.modelo} || {self.almacenamiento} ")