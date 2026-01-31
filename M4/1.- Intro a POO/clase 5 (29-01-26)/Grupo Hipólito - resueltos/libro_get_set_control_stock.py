"""
Una librería necesita un sistema simple para controlar su inventario. 
Cada libro posee un título, un autor, un
precio y una cantidad de stock. Se desea evitar precios negativos y 
gestionar correctamente las ventas.

Modelá una clase Libro que contenga atributos
públicos y privados. Utilizá getters y setters para
proteger el precio, y diseñá un método para realizar
ventas que actualicen el stock.

Paso a paso:
1. Definí los atributos: titulo, autor, stock
(públicos) y __precio (privado)
2. Implementá get_precio() y set_precio()
validando que sea un valor positivo
3. Agregá un método vender(unidades) que
descuente del stock si hay suficiente
4. Creá el método mostrar_info() para
imprimir todos los datos del libro
5. Probá con varios objetos

"""

class Libro:

    def __init__(self, titulo, autor, stock, precio=0):
        self.titulo = titulo
        self.autor= autor
        self.stock= stock
        self.__precio= precio

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio <0:
            print("El precio no debe ser negativo")
            return
        self.__precio = nuevo_precio
    
    def vender(self, unidades):
        if unidades<0:
            print("La cantidad de unidades debe ser mayor a 0")
            return
        self.stock-=unidades
    
    def mostrar_info(self):
        print(f"El libro '{self.titulo}' del {self.autor} tiene {self.stock} unidades a ${self.__precio}")



libros = []

libro_uno= Libro("Fortaleza digital", "Dan Brown", 3, 1400)
libro_dos= Libro("La divina comedia", "Dante Alighieri", 3, 2000)
libro_tres= Libro("El sabueso de los BackerVille", "Conan Doyle", 8, 3800)

libros.append(libro_uno)
libros.append(libro_dos)
libros.append(libro_tres)


print("\n")
print("="*10, "Se muestra la información inicial de cada libro", "="*10)
for libro in libros:
    libro.mostrar_info()

print("\n")
print("="*10, "Se intenta modificar el precio a través del atributo privado __precio", "="*10)
contador_libros = 1
for libro in libros:
    print(f"{contador_libros} - Modificando precio del libro {libro.titulo}... ")
    libro.__precio = 1500
    if libro.get_precio() == libro.__precio:
        print("\tResultado: MODIFICADO")
    else:
        print("\tResultado: NO MODIFICADO")
    contador_libros+=1

print("\n")
print("="*10, "Muestra precio actual de cada libro, a través del método get_precio()", "="*10)
for libro in libros:
    print(f"-Precio {libro.titulo}: {libro.get_precio()}")

print("\n")
print("="*10, "Se modifica el precio de cada libro a través de set_precio()", "="*10)
for libro in libros:
    nuevo_precio=libro.get_precio()*1.05 #valor constante de prueba
    libro.set_precio(nuevo_precio)
    libro.mostrar_info()

print("\n")
print("="*10, "Ingresando precio negativo a cada libro a través de set_precio()", "="*10)
for libro in libros:
    print(f"-Libro {libro.titulo}")
    nuevo_precio=libro.get_precio()*-1.05 #valor constante de prueba
    libro.set_precio(nuevo_precio)
    print("")

print("="*10, "Se simula la venta de libros modificando su stock", "="*10)
unidades_vendidas = -1 
for libro in libros:
    libro.vender(unidades_vendidas)
    libro.mostrar_info()
    unidades_vendidas+=1

print("")