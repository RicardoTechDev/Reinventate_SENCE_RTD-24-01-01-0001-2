"""
Queremos representar productos de un sistema de stock, controlando el precio mediante métodos y
gestionando un descuento común para todos. Además, el sistema debe validar precios antes de aceptarlos.

Consigna:
Creá una clase Producto con precio encapsulado,
un descuento común para todas las instancias, y
un validador independiente que confirme si un
precio ingresado es correcto.

Tiempo : 25 Minutos

Paso a paso:
1. Atributos: nombre (público), __precio
(privado), y descuento (atributo de clase)
2. Método aplicar_descuento() para obtener
el precio final
3. @classmethod set_descuento() para
actualizar el valor general
4. @staticmethod validar_precio(precio) para
verificar si es mayor que cero
5. Creá 2 productos distintos y usá todos los
métodos creados
"""

class Producto:

    __descuento=0

    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.__precio = 0
        self.set_precio(precio)

    def aplicar_descuento(self):
        #self.__precio = self.__precio-(self.__precio * Productos.__descuento)/100
        self.__precio  = self.__precio * (1 - Producto.__descuento/100)
    
    def set_precio(self, precio):
        if not Producto.validar_precio(precio):
            print("El precio debe ser mayor a 0")
            return
        self.__precio = precio
    
    @classmethod
    def set_descuento(cls, nuevo_descuento):
        if not (nuevo_descuento > 0 and nuevo_descuento <=100):
            print("El descuento debe ser mayor a 0 y menor o igual a 100")
            return
        cls.__descuento = nuevo_descuento
        print("El descuento ha sido actualizado exitosamente")
    
    @staticmethod
    def validar_precio(precio):
        return precio>0
    
    def mostrar_info(self):
        print(f"Producto {self.nombre},  precio: {self.__precio}")


producto_uno = Producto("Libro", -2000)
producto_dos = Producto("Lámpara", 4500)
producto_tres = Producto("Reloj mural", 10000)

productos = []

productos.append(producto_uno)
productos.append(producto_dos)
productos.append(producto_tres)


print("="*10,"Lista de productos","="*10)

for producto in productos:
    producto.mostrar_info()


print("")
print("="*10,"Lista de productos","="*10)
Producto.set_descuento(20)
for producto in productos:
    producto.aplicar_descuento()
    producto.mostrar_info()

print("")
print("="*10,"Ingreso descuento negativo","="*10)
Producto.set_descuento(-20)
Producto.set_descuento(120)
