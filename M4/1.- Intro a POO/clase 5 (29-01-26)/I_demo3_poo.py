'''
Vas a diseñar una clase que represente un producto de tienda, 
controlando el acceso y modificación del precio a
través de métodos específicos.

1. Qué debe tener la clase:
● Un atributo público para el nombre del producto
● Un atributo privado para el precio (__precio)
● Un método para ver el precio (getter)
● Un método para modificar el precio (setter), 
que solo permita valores positivos
● En el constructor (__init__), usar el setter 
para validar el precio desde el inicio
2. Qué se debe probar con objetos:
● Crear un producto con precio válido
● Mostrar el precio usando el getter
● Intentar cambiar el precio a un valor negativo (debe mostrar un error)
● Modificar correctamente el precio y verificar el nuevo valor
'''
class  Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = 0 # self._Producto__precio
        self.set_precio(precio)


    def set_precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            print("Error: el precio debe ser mayor a cero")
            return False
        
        self.__precio = nuevo_precio
        return True

    
    def get_precio(self):
        return self.__precio
    

    def get_mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: {self.__precio}")
        

#========== DEMO =========
producto1 = Producto("Polera", 15000)
print(producto1.get_precio())

producto1.set_precio(-16990)
print(producto1.get_precio())

producto1.set_precio(16990)
print(producto1.get_precio())


#print(f"COPIA: {producto1.__precio}")

producto1.__precio = 23990#Nuevo atributo

print(f"COPIA: {producto1.__precio}")
print(f"REAL: {producto1.get_precio()}")

producto1.get_mostrar_info()
producto1.nombre = "Zapato"
producto1.get_mostrar_info()