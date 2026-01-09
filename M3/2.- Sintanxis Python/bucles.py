# ============================================================
# BUCLES EN PYTHON (for / while)
# ============================================================

#*============= Blucle for =================
# for(let indice=0; indice<5; indice++){

# }

for numero in range(5):
    print(f"Hola {numero}")

#? 0 --> 4

#*otro ejemplo
for indice in range(1, 6):
    print(indice)

#? 1 ---> 5

#*============ Con saltos (paso) ===========
for numero in range(1, 11, 2):
    print(numero)

#? Imprime 1,3 , 5, 7, 9
#? range(inicio, fin, paso)

'''
inicio = 1
fin = 11 -> no se incluye
paso = 2 -> avanza de 2 en 2
'''

#*hacia atrás
for numero in range(5, 0, -1):
    print(numero)

#? Imprime 5 ,4 ,3 , 2 , 1
#? range(inicio, fin, paso)

'''
inicio = 5
fin = 0 -> no se incluye
paso = -1 -> avanza de 2 en 2
'''

#*================== Bucle for con listas ============
nombres = ["Ana", "Luis", "Pedro"]

#* Con índice usando range(len(...))
for indice in range(len(nombres)):
    print(f"{indice} - {nombres[indice]}")

#* Recorrer por elementos
nombres = ["Ana", "Luis", "Pedro"]

for nombre in nombres:
    print(nombre)

#*break (detener el bucle)
#* Ejemplo: parar cuando encuentre “Luis”.
nombres = ["Ana", "Pedro", "Luis", "Pedro"]

for nombre in nombres:
    if nombre == "Luis":
        print(nombre)
        break
    
    print("No es Luis")


#* continue (saltar un elemento)
#* Ejemplo: no imprimir “Luis”.
nombres = ["Ana", "Pedro", "Luis", "Sandra", "Roberto", "Luis","Pedro"]

for nombre in nombres:
    if nombre == "Luis":
        continue
    
    print(nombre)


#* Recorrer con enumerate()
'''
enumerate() es una función de Python que permite recorrer una lista (u otro iterable) 
obteniendo al mismo tiempo la posición (índice) y el valor de cada elemento.
'''
nombres = ["Ana", "Pedro", "Luis", "Sandra", "Roberto", "Luis","Pedro"]

for indice, nombre in enumerate(nombres):
    print(f"{indice} - {nombre}")


nombres = ["Ana", "Pedro", "Luis", "Sandra", "Roberto", "Luis","Pedro"]

for indice, nombre in enumerate(nombres, start=15):
    print(f"{indice} - {nombre}")

#*================= Los ciclos anidados ==============
for i in range(1,4):
    for j in range(1,4):
        print(f"i={i}-j={j}")

'''
    [11,12,13]
    [21,22,23]
    [31,32,33]

'''

productos = ["Café", "Té", "Chocolate"]
tamanos = ["Chico", "Mediano", "Grande"]

for producto in productos:
    for tamano in tamanos:
        print(f"{producto} - {tamano}")


#? Matriz

matriz = [
    [1, 2 , 3], #fila 0
    [4, 5 , 6], #fila 1
    [7, 8, 9]   #fila 2
]

print(matriz[1][2])

#? imprimir todos los elementos
for fila in matriz:
    for elemento in fila:
        print(elemento)


#? Imprimir con coordenadas
matriz = [
    [1, 2 , 3], #fila 0
    [4, 5 , 6], #fila 1
    [7, 8, 9]   #fila 2
]

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        print(f"matriz[{fila}][{columna}] = {matriz[fila][columna]}")

#* =================== Optimización de ciclos y mejores prácticas ============
'''
● Evitar bucles innecesarios: No recorrer listas o estructuras de datos si no es necesario.
● Usar comprensiones de listas en lugar de for cuando sea posible.
● Minimizar cálculos dentro del bucle.
● Usar enumerate() en lugar de range(len(lista)) para iterar sobre listas.
'''
cuadrados = []

for i in range(10):
    cuadrados.append(i**2)

#forma optimizada
cuadrados_optimizado = [i**2 for i in range(10)]

print(cuadrados)
print(cuadrados_optimizado)


#*====================== Bucle While =================
contador = 1

while contador <= 5:
    print(contador)
    contador += 1

#*While con validación de entrada
edad = int(input("Ingrese su edad: "))

while edad < 0:
    print("Edad no válida")
    edad = int(input("Ingrese su edad: "))

print("Edad válida")

#* while True + break (simula un do-while)
clave_correcta = "1234"

while True:
    clave = input("Ingrese su clave: ")

    if clave == clave_correcta:
        print("Acceso permitido")
        break
    else:
        print("Clave incorrecta")


#* ejemplo con continue (salta una vuelta)
num = 0

while num < 5:
    num +=1

    if num == 3:
        continue
    
    print(num)


#*while para menús
opcion = ""

while opcion !="3":
    #*Mostrar opciones al usuario
    print("\nMenu")
    print("1) Saludar")
    print("2) Mostrar Fecha")
    print("3) Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Hola usuario")
    elif opcion == "2":
        print("Mostrar Fecha")
    elif opcion == "3":
        print("Saliendo.....")
    else:
        print("Opción no válida")


#* ============================ Estructura match-case ======================
'''
#!Funciona de la versión de Python 3.10 en adelante

🧠 ¿Qué es match-case? 

Es la forma moderna de hacer lo que en otros lenguajes se conoce como switch-case.
Sirve para comparar un valor con varios casos posibles y ejecutar el que corresponda.
'''
'''
match valor:
    case opcion_1:
        # código si valor coincide con opcion_1
    case opcion_2:
        # código si valor coincide con opcion_2
    case _:
        # código por defecto (si no coincide con ningún caso)
'''

edad = int(input("Ingrese su edad: "))

match edad:
    case _ if edad < 0:
        print("edad no válida")
    case _ if edad <= 12:
        print("Niño o Niña")
    case _ if edad <= 17:
        print("Adolecente")
    case _ if edad <= 65:
        print("Adulto")
    case _:
        print("Adulto mayor")

#* Ejemplo del Menú
opcion = ""

while opcion !="3":
    #*Mostrar opciones al usuario
    print("\nMenu")
    print("1) Saludar")
    print("2) Mostrar Fecha")
    print("3) Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            print("Hola usuario")
        case "2":
            print("Mostrar Fecha")
        case "3":
            print("Saliendo.....")
        case _:
            print("Opción no válida")
