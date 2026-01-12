#=====================================================================
#                 Estructuras de Datos en Python
#=====================================================================
#*=========================== Listas --> list =======================
"""
¿Qué es una lista?

Una lista es una estructura de datos ordenada y mutable que permite almacenar múltiples elementos, incluso
de tipos distintos.

Características clave:
● Se define con corchetes: []
● Permite duplicados
● Los elementos son accesibles por índice
● Puede contener otros objetos (listas, diccionarios, etc.)


👉 En palabras simples:

Una lista es una caja grande donde puedes guardar muchas cosas ordenadas.


Ejemplo de la vida real:

Lista de compras
Lista de nombres del curso
Lista de notas
"""

nombres = ["Ana", "Luis", "Pedro", "Sofía"]
notas = [6.0, 5.5, 4.2, 7.0]
numeros= [1, 7, 4, 8, 5]
datos = ["Juan", 18, True, 5.8]

matriz = [[1,2,3], [4,5,6], [7,8,9]]


#* ==== Acceder a los elementos de la lista ====
alumnos = ["Ana", "Luis", "Pedro", "Sofía"]

print(alumnos[1])#Luis
print(alumnos[2])#Pedro
print(alumnos[3])#Sofía

#? Indices negativos
print(alumnos[-1])#Sofía
print(alumnos[-2])#Pedro

#* ==== Modificación de una lista ====
#? Cambiar valor
alumnos[2] = "Lucas"
print(alumnos)

#? Agregar elementos
alumnos.append("Camila")#agregar al final de la lista
print(alumnos)

alumnos.insert(2, "Mateo")#agregar en una posición especifica
print(alumnos)

#? Eliminar elementos
alumnos.pop() #elimina el último
print(alumnos) 

#? Eliminar un el elemento por valor
alumnos.remove("Luis")#Elimina por valor
print(alumnos) 

#? Eliminar por el índice
alumnos.pop(2)
print(alumnos) 

#*==== Tamaño de una lista ====
print(len(alumnos))

#*==== Recorrer una lista ====
#con for
for nombre in alumnos:
    print(nombre)

#con for con enumerate()
alumnos = ["Ana", "Luis", "Pedro", "Sofía"]
for indice, nombre in enumerate(alumnos, start=37):
    print(f"{indice} - {nombre}") 

#con while

indice = 0 #indice inicial

while indice < len(alumnos):
    print(f"{indice} - {alumnos[indice]}")
    indice += 1 #!IMPORTANTE: avanzar para no quedar en un bucle infinito

#*==== Buscar elementos en una lista ====
alumnos = ["Ana", "Luis", "Pedro", "Sofía"]
if "Sandra" in alumnos:
    print("Sandra esta en la lista alumnos")
else:
    print("Sandra no esta en la lista alumnos")


if "Juan" not in alumnos:
    print("Juan no esta en la lista alumnos")

#*======================= Tuplas --> tuple =========================