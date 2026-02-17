'''
¿En qué consistirá la Demo?
Vas a abrir un archivo de texto y leerlo usando los tres métodos principales, 
observando qué devuelve cada uno.

1. Abrí el archivo "prueba.txt" en modo
lectura ("r")
2. Probá cada método por separado:
● Usá read() y mostrale el contenido
completo
● Volvé a abrir el archivo y usá readline()
para leer línea por línea
● Volvé a abrirlo y usá readlines() para
guardar todas las líneas en una lista
3. Mostrá los resultados por consola

Qué observar:
● read() trae todo como un solo
string
● readline() devuelve una línea a la
vez (se puede iterar)
● readlines() devuelve una lista de
líneas
'''

archivo = None

try:
    #!Probando read()
    archivo = open("prueba.txt", "r")
    contenido = archivo.read()
    archivo.close()
    print("¿Archivo cerrado?: ", archivo.closed)
    print("====== CONTENIDO DEL ARCHIVO ======")
    print(contenido)
except FileNotFoundError:
    print("Error: No se logró leer el archivo...")

print("=" * 40)

#!Prueba de readline()
try:
    archivo = open("prueba.txt", "r")
    linea1 = archivo.readline()
    linea2 = archivo.readline()
    linea3 = archivo.readline()

    print(archivo.name)
    print(archivo.mode)
    print(archivo.closed)

    archivo.close()
    print("Primera línea")
    print(linea1)

    print("Segunda línea")
    print(linea2)

    print("Tercera línea")
    print(linea3)

except FileNotFoundError:
    print("Error: No se logró leer el archivo...")

print("=" * 40)
#!Prueba de readlines()
try:
    archivo = open("prueba.txt", "r")
    lista_lineas = archivo.readlines()#todas las líneas en una lista[]
    archivo.close()

    print("Lista de líneas")
    print(lista_lineas)

    print("Cantidad de líneas")
    print(len(lista_lineas))

    print("Tipo devuelto")
    print(type(lista_lineas))

except FileNotFoundError:
    print("Error: No se logró leer el archivo...")