'''
Enunciado (repaso POO completo)

Vas a desarrollar un mini-sistema para una tienda:

1.- Producto
* Tiene atributo público nombre
* Tiene atributo “privado” __precio
* Tiene atributo de clase iva (parámetro de clase) con valor inicial 0.19
* Debe tener get_precio() y set_precio() (solo permite valores positivos)
* Debe tener precio_final() que calcule precio con IVA
* Debe implementar __str__ para que al imprimir el objeto muestre algo legible

2.- Método de clase (@classmethod)
* Debe existir un método cambiar_iva(nuevo_iva) que cambie el IVA para todos los productos

3.- Método estático (@staticmethod)
* Debe existir un método es_precio_valido(precio) que retorne True/False

4.- Carrito (composición)
* Una clase Carrito que “contenga” una lista de productos (parte esencial del carrito)
* Debe tener agregar_producto(producto) y mostrar()

5.- Método con “sobrecarga” simulada
* En Carrito, crea un método calcular_total(*args) que funcione así:
    - Si no recibe nada → total con IVA
    - Si recibe 1 argumento (con_iva) → si es False, calcula sin IVA
    - Si recibe 2 argumentos (con_iva, descuento) → aplica descuento % al final

6.- Colaboración
* Crea una clase Impresora con método imprimir_ticket(carrito)
* El carrito usa la impresora (no la contiene como parte este
'''

class Producto:
    iva = 0.19#Atributo de clase

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = 0 #Atributo privado
        self.set_precio(precio)#validación al crear el objeto

    def set_precio(self, nuevo_precio):
        if not Producto.es_precio_valido(nuevo_precio):
            print("Debe ingresar un precio válido")
            return
        
        self.__precio = nuevo_precio

    def get_precio(self):
        return self.__precio

    def precio_final(self):
        #total = self.__precio * (1 + Producto.iva)
        iva = self.__precio * Producto.iva
        total_con_iva = self.__precio + iva
        return total_con_iva

    @classmethod
    def cambiar_iva(cls, nuevo_iva):
        if not isinstance(nuevo_iva, float) and nuevo_iva < 0:
            print("IVA inválido...")
            return
        
        cls.iva = nuevo_iva
        print("IVA actualizado...")

    @staticmethod
    def es_precio_valido(precio):#5.22
        return isinstance(precio, int) and precio > 0#verificar si es posible con !

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.__precio}"


class Carrito:#Composición
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            print("El producto ingresado no es válido")
            return
        
        self.productos.append(producto)

    def mostrar(self):
        #if not self.productos:
        if len(self.productos) == 0:
            print("Carrito vacío.")
            return
        
        for producto in self.productos:
            print(producto)

    def calcular_total(self, *args):
        '''
        - Si no recibe nada → total con IVA
        - Si recibe 1 argumento (con_iva) → si es False, calcula sin IVA
        - Si recibe 2 argumentos (con_iva, descuento) → aplica descuento % al final
        '''
        #! args es una tupla, para acceder a las posiciones usamos [posición]
        
        #1 elemento
        #args[0] ---> True o False

        #2 elementos
        #args[0] ---> True o False
        #args[1] ---> descuento, porcentaje descuento

        con_iva = True
        descuento = None
        total = 0
            
        if len(args) == 1:
            con_iva = args[0]

        elif len(args) == 2:
            con_iva = args[0]
            descuento = args[1]

        elif len(args) > 2:
            print("Error: máximo 2 parámetros (con_iva, descuento)")
            return
        
        for producto in self.productos:
            if con_iva:
                total += producto.precio_final()#retorna precio con IVA incluido
            else:
                total += producto.get_precio()#el precio sin IVA

        if descuento: #descuento = 10/100 --> 0.10
            descuento = total * (descuento/100)
            total = total - descuento

        return total


class Impresora:#Colaboración
    def imprimir_ticket(self, carrito):
        print("======== TICKET ========")
        carrito.mostrar()
        print("------------------------")
        print(f"TOTAL: ${carrito.calcular_total()}")
        print("========================")


#============================= DEMO ==================
p1 = Producto("Polera", 15000)
p2 = Producto("Pantalón", 25000)
p3 = Producto("Gorro", 8000)

#prueba de __str__
print("==== Productos ===")
print(p1.get_precio())
print(p2)
print(p3)

Producto.cambiar_iva(0.21)

carrito = Carrito()
carrito.agregar_producto(p1)
carrito.agregar_producto(p2)
carrito.agregar_producto(p3)

print(carrito.calcular_total())
print(carrito.calcular_total(False))
print(carrito.calcular_total(False, 10))
print(carrito.calcular_total(True, 10))

print("==== IMPRIMIR TICKET ===")
impresora = Impresora()
impresora.imprimir_ticket(carrito)