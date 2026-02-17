'''
¿En qué consistirá la Demo?
Vas a abrir un archivo de texto en modo lectura, leer todo su contenido 
y luego cerrarlo manualmente.

1. Usar open() en modo "r" para abrir un archivo llamado "prueba.txt"
2. Leer el contenido usando read()
3. Imprimir el contenido en consola
4. Cerrar el archivo usando close()
Observaciones importantes:
➢ Si el archivo no existe, Python lanzará un FileNotFoundError
➢ Verificar si el archivo realmente se cerró con archivo.closed
'''
archivo = None

try:
    #! 1)Abrir en modo lectura
    archivo = open("prueba2.txt", "r")

    #! 2)Leer el contenido
    contenido = archivo.read()

    #! 3)Imprimir por consola
    print("====== CONTENIDO DEL ARCHIVO ======")
    print(contenido)
except FileNotFoundError:
    print("Error: No se logró leer el archivo...")

except FileExistsError:
    print("Error: El archivo no xiste...")

finally:
    if archivo is not None:
        archivo.close()
        print("¿Archivo cerrado?: ", archivo.closed)#Verificación de si el archivo se cerro
    else:
        print("No se abrió ningún archivo")