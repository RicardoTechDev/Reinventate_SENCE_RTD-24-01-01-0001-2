'''
1. Qué debe tener la clase:
● Atributos: titulo, autor, anio_publicacion
● Método especial __str__() que devuelva una cadena como:
○ " Título: [titulo] – Autor: [autor] – Año: [año]"

2. Qué se debe probar:
● Crear varios objetos con diferentes datos
● Hacer print(objeto) para ver cómo se presenta cada uno
● Comparar contra el comportamiento por defecto sin __str__()
Objetivo: lograr que los objetos tengan una presentación clara y profesional al ser impresos o
registrados en consola.
'''

class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
    

    def __str__(self):
        #Esto se mostrará cuando hagas print(objeto)
        return f"Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio_publicacion}"
    
    def mostrar_info(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio_publicacion}"


#====================== DEMO ================
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("El señor de los anillos (Trilogía)", " J. R. R. Tolkien", 1985)
libro3 = Libro("Un mundo feliz", "Aldous Huxley", 2000)

print(libro1)
print(libro2)
print(libro3)

libros = [libro1, libro2, libro3]

for libro in libros:
    print(libro.mostrar_info())
    print(libro)