'''
FUNCIONES EN PYTHON
¿Qué es una función?

Una función es un bloque de código que:
- tiene un nombre
- realiza una tarea específica
- se puede usar muchas veces

En palabras simples:
Una función es como una receta: la escribes una vez y la puedes usar cuando quieras.
'''

'''
¿Para qué sirven las funciones?

Evitar repetir código
Ordenar el programa
Hacer el código más claro
Facilitar cambios y mantenimiento
'''

#*==== Estructura básica de un afunción ===
def nombre_funcion():
    print("Hola desde la función")

'''
Partes importantes

def → palabra reservada para crear funciones
nombre_funcion → nombre en snake_case
() → aquí van los parámetros (si los hay)
: → inicia el bloque
indentación → obligatoria
'''


#*=== Llamar o usar una función
nombre_funcion()

def saludar():
    print("Hola mundo")

saludar()#llamado a la función

#* === Funciones sin parámetros ===
def mostrar_menu():
    print("1) Listar productos")
    print("2) Agregar producto")
    print("3) Eliminar producto")
    print("4) Salir")

mostrar_menu()

#* === Funciónes con parámetros ===
def saludar(nombre):
    print(f"Hola {nombre}")


alumno = "Ana"
saludar(alumno)
saludar("Pedro")

#* === Funciones con más de un parámetro ===
def sumar(num_1, num_2):
    print(num_1 + num_2)

sumar(5, 10)

#*==== Funciones que devuelven un valor (return) ====
def multiplicar(num_1, num_2):
    result = num_1 * num_2
    return result

resultado = multiplicar(5, 10)# ---> 50
print(f"print desde acá: {resultado}")


#* ==== Funciones con lógica (if) ====
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True

    return False

print(es_mayor_de_edad(20))  # True

#* === Valores por defecto ==
#Si no se envía el argumento, se usa el valor por defecto
def saludar(nombre="Invitado"):
    print(f"Hola {nombre}")

saludar()
saludar("Luis")


#*==== Funciones y estructuras de datos ====
#*Ej. con listas:
def mostrar_nombres(lista):
    for nombre in lista:
        print(f"Nombre: {nombre}")

nombres_alumnos = ["Ana", "Luis", "Pedro"]
mostrar_nombres(nombres_alumnos)

nombre_usuarios = ["Sandra", "Alejandro", "Viviana"]
mostrar_nombres(nombre_usuarios)

productos = ["Sal", "Azucar", "Bebida"]
mostrar_nombres(productos)

#*Ej. diccionarios
LIBROS = {
    "B001": {
        "titulo": "Cien años de soledad",
        "autor": ("Gabriel García Márquez", 1927),
        "genero": "Realismo mágico",
        "stock": 5
    },
    "B002": {
        "titulo": "1984",
        "autor": ("George Orwell", 1903),
        "genero": "Distopía",
        "stock": 8
    },
    "B003": {
        "titulo": "El principito",
        "autor": ("Antoine de Saint-Exupéry", 1900),
        "genero": "Fábula",
        "stock": 12
    },
    "B004": {
        "titulo": "Don Quijote de la Mancha",
        "autor": ("Miguel de Cervantes", 1547),
        "genero": "Novela clásica",
        "stock": 3
    },
    "B005": {
        "titulo": "Orgullo y prejuicio",
        "autor": ("Jane Austen", 1775),
        "genero": "Romance",
        "stock": 6
    },
    "B006": {
        "titulo": "Crimen y castigo",
        "autor": ("Fiódor Dostoyevski", 1821),
        "genero": "Novela psicológica",
        "stock": 4
    },
    "B007": {
        "titulo": "Fahrenheit 451",
        "autor": ("Ray Bradbury", 1920),
        "genero": "Ciencia ficción",
        "stock": 7
    },
    "B008": {
        "titulo": "La metamorfosis",
        "autor": ("Franz Kafka", 1883),
        "genero": "Ficción",
        "stock": 9
    },
    "B009": {
        "titulo": "Matar a un ruiseñor",
        "autor": ("Harper Lee", 1926),
        "genero": "Drama",
        "stock": 5
    },
    "B010": {
        "titulo": "El hobbit",
        "autor": ("J. R. R. Tolkien", 1892),
        "genero": "Fantasía",
        "stock": 10
    },
    "B011": {
        "titulo": "El nombre de la rosa",
        "autor": ("Umberto Eco", 1932),
        "genero": "Misterio",
        "stock": 4
    },
    "B012": {
        "titulo": "Rayuela",
        "autor": ("Julio Cortázar", 1914),
        "genero": "Novela experimental",
        "stock": 2
    },
    "B013": {
        "titulo": "La ciudad y los perros",
        "autor": ("Mario Vargas Llosa", 1936),
        "genero": "Novela",
        "stock": 6
    },
    "B014": {
        "titulo": "Pedro Páramo",
        "autor": ("Juan Rulfo", 1917),
        "genero": "Realismo mágico",
        "stock": 3
    },
    "B015": {
        "titulo": "Los juegos del hambre",
        "autor": ("Suzanne Collins", 1962),
        "genero": "Distopía",
        "stock": 11
    },
    "B016": {
        "titulo": "Harry Potter y la piedra filosofal",
        "autor": ("J. K. Rowling", 1965),
        "genero": "Fantasía",
        "stock": 14
    },
    "B017": {
        "titulo": "El alquimista",
        "autor": ("Paulo Coelho", 1947),
        "genero": "Ficción",
        "stock": 8
    },
    "B018": {
        "titulo": "La sombra del viento",
        "autor": ("Carlos Ruiz Zafón", 1964),
        "genero": "Misterio",
        "stock": 5
    },
    "B019": {
        "titulo": "El viejo y el mar",
        "autor": ("Ernest Hemingway", 1899),
        "genero": "Novela",
        "stock": 7
    },
    "B020": {
        "titulo": "El perfume",
        "autor": ("Patrick Süskind", 1949),
        "genero": "Suspenso",
        "stock": 4
    }
}



def imprimir_tabla_libros(dic_libros, mostrar):
    
    ancho = 105
    print(f"{'ID':<5} | {'TÍTULO':<50} | {'AUTOR':<35} | {'STOCK':>5}" )
    print("-" * ancho)

    for id_libro, datos in dic_libros.items():
        stock = datos.get("stock")
        texto = f"{id_libro:<5} | {stock:>5}" 
        
        if mostrar:
            titulo = datos.get("titulo")
            autor = datos.get("autor")[0]
            texto += f"| {titulo:<50} | {autor:<35}" 

        print(texto)

imprimir_tabla_libros(LIBROS, False)

'''
Buenas prácticas

✔ Nombres claros y descriptivos de lo que hacen
✔ Una función = una tarea, realiza al en específico 
✔ Usar return cuando sea necesario
✔ No hacer funciones demasiado largas

“Una función es una herramienta que escribimos una vez y usamos muchas veces.”
'''

#* =================== Funciones nativas ======================
# 1) print() -> imprime en pantalla
print("Hola mundo")  # Muestra texto en la consola

# 2) input() -> pide un dato al usuario (siempre llega como texto str)
nombre = input("Ingresa tu nombre: ")
print("Tu nombre es:", nombre)

# 3) str() -> convierte a texto
edad_num = 15
edad_texto = str(edad_num)
print("Edad en texto:", edad_texto)       # "15"
print(type(edad_texto))                   # <class 'str'>

# 4) int() -> convierte a entero
# (si el usuario escribe algo que no es número, dará error)
edad = int(input("Ingresa tu edad (entero): "))
print("Edad + 1 =", edad + 1)

# 5) float() -> convierte a decimal
altura = float(input("Ingresa tu altura (ej: 1.70): "))
print("Altura:", altura)

# 6) bool() -> convierte a booleano
# OJO: bool("hola") es True porque NO está vacío
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False (texto vacío)
print(bool("Hola"))   # True

# 7) type() -> muestra el tipo de dato
precio = 9990
print(type(precio))  # <class 'int'>

# 8) isinstance() -> verifica si una variable es de un tipo
nota = 6.5
print(isinstance(nota, float))  # True
print(isinstance(nota, int))    # False

# 9) len() -> largo de una lista o string
palabra = "Python"
print(len(palabra))  # 6 (cantidad de letras)

nombres = ["Ana", "Luis", "Pedro"]
print(len(nombres))  # 3 (cantidad de elementos)

# 10) list() -> convierte a lista
# Convierte un texto en lista de caracteres
letras = list("Hola")
print(letras)  # ['H', 'o', 'l', 'a']

# 11) tuple() -> convierte a tupla
nombres_tupla = tuple(nombres)
print(nombres_tupla)  # ('Ana', 'Luis', 'Pedro')

# 12) dict() -> crea/convierte a diccionario
# Se puede crear desde pares (clave, valor)
pares = [("nombre", "Sofía"), ("edad", 11)]
alumno = dict(pares)
print(alumno)  # {'nombre': 'Sofía', 'edad': 11}

# 13) range() -> genera un rango de números (muy usado en for)
for i in range(1, 6):
    print(i)  # 1 2 3 4 5


# 14) round() -> redondea decimales
promedio = 5.6789
print(round(promedio, 2))  # 5.68


# 15) format() -> dar formato a strings (alternativa a f-strings)
precio = 12500
texto = "El precio es ${}".format(precio)
print(texto)

# También se puede con decimales:
pi = 3.14159
print("Pi con 2 decimales: {:.2f}".format(pi))  # 3.14