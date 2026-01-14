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
'''
¿Qué es una tupla?

Una tupla es una estructura de datos que guarda varios valores, igual que una lista, 
pero con una diferencia clave:

✅ Una tupla es inmutable
👉 Esto significa que no se puede modificar (no se puede cambiar, agregar ni eliminar elementos).
'''

#*crear tupla
dias = ("lunes", "martes", "viernes")
numeros = (1, 2, 3 , 4, 5)
mezcla = ("Ana", 6.5, 12, True)

#lista = ["Luis"] 
#no_tupla = ("Luis") No es una tupla, string
tupla = ("Luis", )

#*Acceder a los elementos de una tupla
dias = ("lunes", "martes", "viernes")
print(dias[1])#acceder igual que en las listas
print(dias[0])
print(dias[-1])

#*Correr una tupla
#?con for
dias = ("lunes", "martes", "viernes")

for dia in dias:
    print(dia)


for indice, dia in enumerate(dias, start=1):
    print(f"{indice} - {dia}")

#* Que no podemos hacer
dias = ("lunes", "martes", "viernes")
#dias[0] = "Sábado"
#print(dias) 

#? Creamos una nueva tupla (reemplazando la variable)
dias2 = ("domingo", ) + dias
print(dias2)

#!No puedo modificar los elementos
#!No puedo agregar
#!No puedo eliminar

#*Eliminar tupla
variable_tupla=(1,2,3,4)
print(variable_tupla)


del variable_tupla
print(variable_tupla)

#* Cambiar tipo o convertir
dias = ("lunes", "martes", "viernes")
print(dias)
dias_lista = list(dias) #convertir a lista
dias_lista.remove("lunes")
print(dias_lista)
dias = tuple(dias_lista) #volver a tupla
print(dias)



#* ============================= SETS ==================================
''' 
¿Qué es un set?

Un set es una colección de elementos:
sin orden
sin elementos repetidos
sirve mucho para eliminar duplicados y para comparar conjuntos
'''
numeros = {3, 2, 1, 2, 3, 3, 3}
print(numeros)

numeros = {} #No es un set, es un diccionario
numeros = set()#Para declarar set vacíos

#*==== Operaciones básicas ====
frutas = {"Manzana", "Sandía", "Pera"}
print(frutas)
frutas.add("Uva")
print(frutas)
frutas.remove("Pera")
print(frutas)
frutas.pop()
print(frutas)
frutas.discard("Frutilla")#elimina, sin error si elemento no está
print(frutas)

#*El lugar lo decide Python, porque es un set sin orden

#* Recorrer
frutas = {"Manzana", "Sandía", "Pera", "Uvas"}
for fruta in frutas:
    print(fruta)


#*Verificar si está
print("Uvas" in frutas)
print("Kiwi" not in frutas)

#*Operaciones de conjuntos
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B) #Unión --> {1 , 2, 3, 4, 5}
print(A & B) #Intersección --> {3}
print(A - B) #Diferencia --> {1, 2}
print(B - A)
print(A ^ B) #Diferecia simétrica --> {1, 2 , 4, 5} 

#!==== IMPORTANTE ====
#! No hay índices
#! No hay primero ni último
#! No se puede elegir posición  

#*========================= DICCIONARIOS (dict) ========================
'''
✅ ¿Qué es un diccionario?

Un diccionario guarda datos en pares:

👉 clave : valor

✅ rápido para buscar por clave
✅ ideal para representar “fichas” o “registros”
✅ se usa mucho en inventarios, usuarios, datos de alumnos, etc.
'''
#*Crear un diccionario
alumno = {
    "nombre": "Ana",
    "edad": 27,
    "ciudad": "Temuco"
}

#*Acceder 
print(alumno["nombre"])

#*Modificar
alumno["edad"] = 28 

#*Agregar nueva clave
alumno["curso"] = "Fundamentos de Python"
print(alumno)

print("nombre" in alumno)
print("direccion" not in alumno)

#! Esto nos da error
#direccion = alumno["direccion"]#no es una forma segura si no tenemos certeza de que existe la clave


alumno = {
    "nombre": "Ana",
    "edad": 27,
    "ciudad": "Temuco"
}
direccion = alumno.get("direccion")#Devuelve por Default None cuando encuentra la key o no existe la key 

if direccion:
    print("La key existe")
else:
    print("La key no existe")


#Otro ejemplo
direccion = alumno.get("direccion", "La key no existe")
print(direccion)


#* ==== Eliminar por key ====
alumno = {
    "nombre": "Ana",
    "edad": 27,
    "ciudad": "Temuco"
}
del alumno["ciudad"]
print(alumno)

#Otra alternativa
alumno.pop("edad")
print(alumno)

#* ==== Recorrer diccionarios ====
alumno = {
    "nombre": "Ana",
    "edad": 27,
    "ciudad": "Temuco"
}
for clave in alumno:#recuperar sólo las claves
    print(clave)

for valor in alumno.values():#recupera el valor sin la clave o key
    print(valor)

for clave, valor in alumno.items():#recupera la clave y el valor
    print(f"{clave}: {valor}")


#* Ejemplos con con más de un elemento
alumnos = {
    "Ana":   {  
                "edad": 11, 
                "curso": "6°A", 
                "promedio": 6.2
            },
    "Luis":  {
                "edad": 12, 
                "curso": "6°A", 
                "promedio": 5.4
            },
    "Pedro": {"edad": 11, "curso": "6°B", "promedio": 6.8},
    "Sofía": {"edad": 12, "curso": "6°B", "promedio": 6.0}
}

#Acceder a un alumno
print(alumnos["Ana"])
print(alumnos.get("Pedro"))

#Acceder a un dato en especifíco
print(alumnos["Ana"]["curso"])
print(alumnos.get("Pedro").get("curso"))

#Modificar un dato
alumnos["Ana"]["curso"] = "6°B"

#Agregar un nuevo dato
alumnos["Ana"]["asistencia"] = 70
print(alumnos["Ana"])

#Agregar nuevo alumno
alumnos["Camila"] = {"edad": 13, "curso": "6°A", "promedio": 6.1}
print(alumnos)
#eliminar
print("======= Eliminar ========")

del alumnos["Camila"]
print(alumnos)
alumnos.pop("Camila")
print(alumnos)

#Buscar alumno (sin error)
nombre_buscar = "Camila"

if nombre_buscar in alumnos:
    alumnos.pop("Camila")
else:
    print(f"No existe alumno {nombre_buscar}")

#*Métodos importantes de diccionarios
productos = {
    "pan" : {"precio": 2000, "stock": 100},
    "leche" : {"precio": 1000, "stock": 35}
}

#*Alternativa al método get
try:
    print(productos["jugo"])
except:
    print("No existe el producto")

#*Recupera y si no existe lo crea
arroz = productos.setdefault("arroz", {"precio": 1990, "stock": 30})
print(productos)

pescado = productos.setdefault("pescado")
print(pescado)

#*Actualizar (con otro diccionario)
nuevos = {
    "pescado":  {"precio": 3500, "stock": 35},
    "huevos":  {"precio": 400, "stock": 35}
}

productos.update(nuevos)
print(productos)

#* Borrar todo el diccionario
productos.clear()
print(productos)


