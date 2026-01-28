"""
Diseñá tu propia clase
Contexto:
Imaginá que tenés que modelar un objeto del mundo real en código. Queremos representar un celular como
clase, con su información principal y funciones básicas.
Consigna:
Creá una clase Celular que tenga los siguientes elementos:
● Atributos: marca, modelo, almacenamiento
● Método encender() que imprima "Encendiendo {marca} {modelo}..."
● Método mostrar_info() que muestre todos los atributos
Tiempo : 20 Minutos
Diseñá tu propia clase
Paso a paso sugerido:
1. Definí la clase Celular
2. Agregá el constructor __init__() con los tres atributos
3. Implementá los métodos encender() y mostrar_info()
4. Creá al menos dos objetos distintos
5. Mostrá los datos de cada uno y ejecutá sus métodos
"""
print("EJERCICIO 1 \n")

class Celular:
    def __init__(self, marca, modelo, almacenamiento, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.sistema_operativo = sistema_operativo
    
    def encender(self):
        print(f" Encendiendo {self.marca} {self.modelo} ...")
    
    def mostrar_info(self):
        print(f"- Marca: {self.marca}.")
        print(f"- Modelo: {self.modelo}.")
        print(f"- Almacenamiento: {self.almacenamiento}")
        print(f"- Sistema operativo: {self.sistema_operativo}")

    def activar_camara ():
        print("\n Activando cámara...")

celular_uno = Celular("Samsung", "Galaxy S25 Ultra", "128GB", "Android")
celular_dos = Celular("Iphone", "16 Pro Max", "512 GB", "iOS")

celular_uno.encender()
celular_uno.mostrar_info()
print("="*40)
celular_dos.encender()
celular_dos.mostrar_info()
print("."*40)
""""
Lista de instancias y métodos personalizados
Contexto:
Queremos simular un grupo de mascotas, cada una representada por un objeto. Las mascotas pueden tener
distintas edades, y vamos a clasificarlas.
Consigna:
Creá una clase Mascota con:
● Atributos: nombre, edad, tipo
● Método presentarse() que diga "Soy {nombre}, un/a {tipo} de {edad} años."
● Método es_joven() que devuelva True si tiene menos de 5 años
Tiempo : 20 Minutos
Lista de instancias y métodos personalizados
Paso a paso:
1. Definí la clase y sus métodos
2. Creá una lista de 3 o más mascotas
3. Recorrelas con un for y:
4. Mostrá su presentación
5. Indicá si es joven o no
6. Bonus: Filtrá solo las mascotas jóvenes en una nueva lista
"""
print("EJERCICIO 2\n")

class Mascota:

    def __init__(self, nombre, edad, tipo, raza):
        self.nombre=nombre
        self.edad=edad
        self.tipo=tipo
        self.raza = raza

    def presentarse(self):
        print(f"Soy {self.nombre}, un/a {self.tipo} de {self.edad} años")

    def es_joven(self):
        return self.edad<=5
        # if self.edad > 5:
        #    return False

        #return True

lista_mascotas = []

mascota = Mascota("Boby", 3,"Perro", "Poodle Toy")
mascota_dos = Mascota("Tadeo", 5 ,"Perro", "Boxer")
mascota_tres = Mascota("Algodón", 2 , "Conejo", "Angora")
mascota_cuatro = Mascota("GuruGuru", 8 , "Ave autóctona", "Desconocido")

lista_mascotas.append(mascota)
lista_mascotas.append(mascota_dos)
lista_mascotas.append(mascota_tres)
lista_mascotas.append(mascota_cuatro)

lista_jovenes = []

for mascota in lista_mascotas:
    mascota.presentarse()
    if mascota.es_joven():
        lista_jovenes.append(mascota)
        print ("- Mascota Joven \n")
    else:
        print("- Mascota adulta \n")

print("-"*30)
print("\t\t\tMASCOTAS JOVENES")
print("-"*30)

for jovenes in lista_jovenes:
    jovenes.presentarse()


'''
Enunciado

Crea una clase Producto con los atributos: nombre, precio y stock.
Luego crea una función llamada aplicar_descuento(producto, porcentaje) que 
reciba un objeto Producto como parámetro y un porcentaje de descuento.

La función debe:
* Validar que el porcentaje esté entre 0 y 100.
* Calcular el nuevo precio con descuento.
* Modificar el precio del producto.
* Mostrar el precio antes y después.
* Finalmente, crea 3 producto y llama a la función para probarlo.

Nota: puedes crear una lista de productos simulando que es una venta y aplicar el mismo
porcentaje de descuento a los 3 productos, en este caso aplicar descuento por 
separado a cada producto
'''

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio= precio
        self.stock=stock
        
    #def modificar_precio (self, nuevo_precio):
    #       self.precio = nuevo_precio

    def mostrar_producto(self):
        print(f"-Nombre: {self.nombre} \n-Precio:  {self.precio} \n-Stock: {self.stock}")



def aplicar_descuento (producto, porcentaje):
        precio_descuento = producto.precio
        if porcentaje<0 and porcentaje >100:
            print("\n El porcentaje debe ser entre 0% y 100%")
        else:
            precio_descuento = producto.precio - (producto.precio * porcentaje)/100
            return producto.precio - precio_descuento

producto = Producto("Cubo Rubik", 50, 3)
producto_dos = Producto("Trompeta", 1000, 2)
producto_tres = Producto("Sombrero", 20, 10)

lista_productos = []

lista_productos.append(producto)
lista_productos.append(producto_dos)
lista_productos.append(producto_tres)

porcentaje = -130
for producto in lista_productos:
    producto.mostrar_producto()
    con_descuento = aplicar_descuento(producto, porcentaje)
    print(f"    -Precio: {producto.precio}")
    print(f"    -Descuento {porcentaje}%: {con_descuento}")
    print(f"    -Nuevo precio: {producto.precio-con_descuento}")
    print("="*30)
