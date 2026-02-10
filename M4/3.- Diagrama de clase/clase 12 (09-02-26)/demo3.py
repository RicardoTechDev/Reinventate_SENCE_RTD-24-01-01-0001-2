class Usuario:
    def __init__(self, nombre, email, carrito):
        self.nombre = nombre
        self.email = email
        self.carrito = None #Usar un carrito
        #self.carrito = Carrito()#Tiene un carrito

    def agregar_carrito(self, carrito):
        pass
    
    def login():
        pass

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.__productos = [] # o así --> self.productos: list[Producto] = []

    def agregar_producto(self, producto):
        pass
    

    def calcular_total(self):
        pass