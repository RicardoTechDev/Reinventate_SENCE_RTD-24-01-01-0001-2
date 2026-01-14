#* =======================================================
#*              PRESENTACIÓN FELIPE VILLEGAS
#* =======================================================
print("=== Sistema de Gestión de Estudiantes ===")

# Lista de estudiantes
estudiantes = [
    ("Ana", 25, "Santiago"),
    ("Luis", 30, "Rancagua"),
    ("María", 22, "Pichilemu"),
    ("Pedro", 28, "Antofagasta"),
    ("Sofía", 27, "Iquique")
]

# Mostrar registros
for nombre, edad, ciudad in estudiantes:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# Buscar por ciudad
ciudad_buscar = input("\nIngrese una ciudad: ")
contador = 0
for _, _, ciudad in estudiantes:
    if ciudad.lower() == ciudad_buscar.lower():
        contador += 1
print(f"Cantidad de estudiantes en {ciudad_buscar}: {contador}")

# Edad promedio
suma = 0
for _, edad, _ in estudiantes:
    suma += edad
promedio = suma / len(estudiantes)
print(f"Edad promedio: {promedio:.2f}")

# Bonus: agregar estudiante
opcion = input("\n¿Desea agregar un nuevo estudiante? (s/n): ")
if opcion.lower() == "s":
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")
    estudiantes.append((nombre, edad, ciudad))
    print("\nEstudiante agregado correctamente")
for nombre, edad, ciudad in estudiantes:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# Modificar estudiante 

opcion_modificar = input("\n¿Desea modificar un estudiante existente? (s/n): ") 
if opcion_modificar.lower() == "s": 
    nombre_buscar = input("Ingrese el nombre del estudiante a modificar: ") 
    for i, (nombre, edad, ciudad) in enumerate(estudiantes): #tuppla - lista
        if nombre.lower() == nombre_buscar.lower(): 
            print(f"\nEstudiante encontrado: {nombre}, {edad}, {ciudad}") 
            nuevo_nombre = input("Nuevo nombre: ") 
            nueva_edad = int(input("Nueva edad: ")) 
            nueva_ciudad = input("Nueva ciudad: ") 
            estudiantes[i] = (nuevo_nombre, nueva_edad, nueva_ciudad) 
            print("\nEstudiante modificado correctamente") 
            break 
        else: print("\nNo se encontró un estudiante con ese nombre.") 
        # Mostrar lista final 
    print("\nLista final de estudiantes:") 
    for nombre, edad, ciudad in estudiantes: print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}") 
    print("\nPrograma finalizado")
#-----------------------------------------------------------------------------------------------------------------------------------#
                                                        #Tarea 2#
#-----------------------------------------------------------------------------------------------------------------------------------#

# Dos listas con colores (con duplicados)
catalogo_a = ["rojo", "azul", "verde", "rojo", "amarillo", "negro"]
catalogo_b = ["azul", "blanco", "verde", "gris", "negro", "negro"]

# Convertir listas a sets (eliminan duplicados automáticamente)
set_a = set(catalogo_a)
set_b = set(catalogo_b)

print("=== Comparador de Catálogos ===")

# Unión: todos los colores sin duplicados
print(f"Unión: {set_a | set_b}")

# Intersección: colores en ambos catálogos
print(f"Intersección: {set_a & set_b}")

# Diferencia A - B: todo los que no estan en b pero si en A
print(f"Diferencia A - B: {set_a - set_b}")

# Diferencia B - A: todos los que no estan en A PERO SI EN B
print(f"Diferencia B - A: {set_b - set_a}")

# Modificar sets
set_a.add("violeta")       # agregar color a catálogo A
set_b.discard("gris")      # eliminar color de catálogo B

print("\nSets actualizados:")
print(f"Catálogo A: {set_a}")
print(f"Catálogo B: {set_b}")

#* =======================================================
#*            PRESENTACIÓN EXEQUIEL URIBE
#* =======================================================


#* =======================================================
#*            PRESENTACIÓN MARJORIE AGUILERA
#* =======================================================
'''Desarrollar un programa que permita:
 ● Registrar múltiples estudiantes representados por tuplas dentro de una lista.
 ● Mostrar todos los registros con formato legible.
 ● Permitir consultar cuántos estudiantes son de una ciudad específica.
 ● Mostrar la edad promedio de los estudiantes registrados.

 1. Crear una lista vacía llamada estudiantes.
 2. Cada entrada será una tupla con 3 datos: (nombre, edad, ciudad).
 3. Agregar al menos 5 estudiantes con datos variados.
 4. Recorrer la lista e imprimir cada estudiante con el formato:
 "Nombre: Ana, Edad: 25, Ciudad: Córdoba"
 5. Pedir al usuario que ingrese una ciudad, y contar cuántos estudiantes son de esa ciudad.
 6. Calcular la edad promedio de todos los estudiantes (sumar edades / total).
 7. Bonus: Permitir agregar un nuevo estudiante desde consola.'''


estudiantes = []

estudiantes = [
    ("Anais", 28, "santiago"),
    ("Franco", 32, "valdivia"),
    ("Marion", 30, "coquimbo"),
    ("Joaquin", 19, "valdivia"),
    ("Laura", 29, "puerto montt"),
]

for nombre, edad, ciudad in estudiantes:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

input_localidad = input("Ingrese ciudad a consultar: ")

contador = 0
for ciudad in estudiantes:
    if ciudad[2] == input_localidad:
        contador += 1


print(f"La cantidad de estudiantes de {input_localidad} es: {contador}")

suma_edades = 0
contador2 = 0
for edad in estudiantes:
    suma_edades += edad[1]
    contador2 +=1

promedio = suma_edades / contador2
print(f"La edad promedio de los estudiantes es: {promedio}")

nuevo_ingreso_nombre = input("Ingrese nombre estudiante ")
nuevo_ingreso_edad = input("Ingrese edad estudiante ")
nuevo_ingreso_ciudad = input("Ingrese ciudad estudiante ")

ingreso_nuevo = (nuevo_ingreso_nombre, int(nuevo_ingreso_edad), nuevo_ingreso_ciudad)
estudiantes.append (ingreso_nuevo)
for nombre, edad, ciudad in estudiantes:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")



''' Compare dos listas de colores y elimine duplicados.
● Informe qué colores están en ambos catálogos.
● Determine qué colores son exclusivos de cada uno.
● Permita agregar un nuevo color al catálogo A y eliminar uno del catálogo B.
● Presente todos los resultados de manera clara.

Paso a paso:
1. Crear dos listas: catalogo_a = [...] y catalogo_b = [...] con al menos 6 colores cada una (incluyendo
duplicados).
2. Convertir ambas listas a sets: set_a y set_b.
3. Mostrar los siguientes resultados:
● Unión: todos los colores disponibles sin duplicados.
● Intersección: colores que están en ambos catálogos.
● Diferencia A - B: colores únicos del catálogo A.
● Diferencia B - A: colores únicos del catálogo B.
4. Agregar un nuevo color al set_a (usando add()).
5. Eliminar un color específico del set_b (usando discard()).
6. Mostrar los sets actualizados con mensajes claros.'''


catalogo_a = ["azul", "negro", "celeste", "blanco", "cafe", "blanco"]
catalogo_b = ["calipso", "blanco", "azul", "violeta", "rojo","gris"]
print("Catalogo A:", catalogo_a)
set_a= set(catalogo_a)
print("Set A:", set_a)
set_b= set(catalogo_b)
print(set_a | set_b)
print("colores ambos catalogos:", set_a & set_b)
print("colores unicos catalogo_a:", set_a - set_b)
print("colores unicos catalogo_b:", set_b - set_a)
set_a.add("verde")
print("set_a actualizado:", set_a)
set_b.discard("rojo")
print("set_b actualizado:", set_b)

print("============= Listado de colores actualizados:==============")

for color in set_a:
    print("colores catalogo a son:", color)
print("\n")
for color in set_b:
    print("colores catalogo b son:", color)


#* =======================================================
#*            PRESENTACIÓN HIPÓLITO CAYUPI
#* =======================================================




#* =======================================================
#*            PRESENTACIÓN VICTOR ANABALON
#* =======================================================
"""
Comparador de catálogos de diseño (sets)
Contexto:
Una agencia de diseño gráfico está integrando productos de dos catálogos distintos. Necesitan identificar
los colores que se repiten, los únicos de cada catálogo y todos los colores disponibles sin duplicados.
Además, desean poder agregar y quitar colores según decisiones del equipo creativo.
Consigna:
Construir un programa que:
● Compare dos listas de colores y elimine duplicados.
● Informe qué colores están en ambos catálogos.
● Determine qué colores son exclusivos de cada uno.
● Permita agregar un nuevo color al catálogo A y eliminar uno del catálogo B.
● Presente todos los resultados de manera clara.
Tiempo : 25 Minutos
Comparador de catálogos de diseño (sets)
Paso a paso:
1. Crear dos listas: catalogo_a = [...] y catalogo_b = [...] con al menos 6 colores cada una (incluyendo
duplicados).
2. Convertir ambas listas a sets: set_a y set_b.
3. Mostrar los siguientes resultados:
● Unión: todos los colores disponibles sin duplicados.
● Intersección: colores que están en ambos catálogos.
● Diferencia A - B: colores únicos del catálogo A.
● Diferencia B - A: colores únicos del catálogo B.
4. Agregar un nuevo color al set_a (usando add()).
5. Eliminar un color específico del set_b (usando discard()).
6. Mostrar los sets actualizados con mensajes claros."""


# ? 1. Crear dos listas: catalogo_a = [...] y catalogo_b = [...] con al menos 6 colores cada una (incluyendo duplicados)

catalogo_a = ["Rojo", "Cafe", "Amarillo", "Verde", "Cafe", "Morado", "Negro"]
catalogo_b = ["Azul",  "Celeste", "Negro", "Violeta", "Cafe", "Blanco", "Azul"]

"""
print(catalogo_a)
print(catalogo_b)
"""

# ? 2. Convertir ambas listas a sets: set_a y set_b.

set_a = set(catalogo_a)
set_b = set(catalogo_b)

"""
print(set_a)
print(set_b)
"""

# ?3. Mostrar los siguientes resultados:

# ● Unión: todos los colores disponibles sin duplicados.

print(f"Unión: {set_a | set_b}")


# ● Intersección: colores que están en ambos catálogos.

print(f"Interseccion: {set_a & set_b}")

# ● Diferencia A - B: colores únicos del catálogo A.


print(f"Diferencia A - B: {set_a - set_b}")

# ● Diferencia B - A: colores únicos del catálogo B.

print(f"Diferencia B - A: {set_b - set_a}")


# ? 4. Agregar un nuevo color al set_a (usando add()).
set_a.add("Fucsia")

# ? 5. Eliminar un color específico del set_b (usando discard()).

set_b.discard("Negro")

# ? 6. Mostrar los sets actualizados con mensajes claros.

print(f"set_a actualizado: {set_a}")
print(f"set_b actualizado: {set_b}")
