'''
¿En qué consistirá la Demo?
Vas a trabajar con un archivo existente, primero cambiándole 
el nombre y luego trasladándolo a una carpeta
diferente.

1. Crear un archivo llamado
"demo_archivo.txt" si no existe
2. Usar os.rename() para renombrarlo a
"archivo_renombrado.txt"
3. Crear manualmente una carpeta llamada
"nueva_carpeta"
4. Usar shutil.move() para mover
"archivo_renombrado.txt" a
"nueva_carpeta/"

Qué observar:
El archivo ya no estará en su carpeta
original
Si la carpeta destino no existe,
shutil.move() lanzará un error
'''

import os
import shutil

#1. Crear un archivo llamado "demo_archivo.txt"
archivo_original = "demo_archivo.txt"

if not os.path.exists(archivo_original):
    with open(archivo_original, "w", encoding="utf-8") as archivo:
        archivo.write("Archivo de prueba\n")
    print(f"Archivo creado: {archivo_original}")
else:
    print(f"El archivo ya existe: {archivo_original}")

archivo_renombrado = "archivo_renombrado.txt"

#2. Usar os.rename() para renombrarlo a "archivo_renombrado.txt"
try:
    os.rename(archivo_original, archivo_renombrado)
    print("Archivo renombrado")
except FileNotFoundError:
    print("No se logró renombrar el archivo")


#3. Crear manualmente una carpeta llamada "nueva_carpeta"
carpeta_nueva = "nueva_carpeta"

if not os.path.exists(carpeta_nueva):
    os.mkdir(carpeta_nueva)
    print(f"Carpeta creada: {archivo_original}")
else:
    print(f"La carpeta ya existe: {carpeta_nueva}")


#4. Usar shutil.move() para mover "archivo_renombrado.txt" a "nueva_carpeta/"
try:
    ruta_destino = os.path.join(carpeta_nueva, archivo_renombrado)
    #ruta_destino = f"{carpeta_nueva}/{archivo_renombrado}"
    print(ruta_destino)
    shutil.move(archivo_renombrado, ruta_destino)
except FileNotFoundError:
    print("Archivo no existe para poder moverlo")
except Exception as e:
    print(e)
