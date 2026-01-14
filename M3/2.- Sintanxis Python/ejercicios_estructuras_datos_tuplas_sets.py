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
'''
Sistema de gestión de estudiantes (listas + tuplas)

Contexto:
Una institución educativa necesita registrar y consultar información de sus estudiantes. Cada estudiante
tiene un nombre, una edad y una ciudad de residencia. Se requiere un sistema básico para almacenar los
datos, listarlos, buscar estudiantes por ciudad y obtener estadísticas.
Consigna:
● Desarrollar un programa que permita:
● Registrar múltiples estudiantes representados por tuplas dentro de una lista.
● Mostrar todos los registros con formato legible.
● Permitir consultar cuántos estudiantes son de una ciudad específica.
● Mostrar la edad promedio de los estudiantes registrados.

Tiempo : 25 Minutos

Sistema de gestión de estudiantes (listas + tuplas)

Paso a paso:
1. Crear una lista vacía llamada estudiantes.
2. Cada entrada será una tupla con 3 datos: (nombre, edad, ciudad).
3. Agregar al menos 5 estudiantes con datos variados.
4. Recorrer la lista e imprimir cada estudiante con el formato:
"Nombre: Ana, Edad: 25, Ciudad: Córdoba"
5. Pedir al usuario que ingrese una ciudad, y contar cuántos estudiantes son de esa ciudad.
6. Calcular la edad promedio de todos los estudiantes (sumar edades / total).
7. Bonus: Permitir agregar un nuevo estudiante desde consola.
'''
alumnos = [
    ("Felipe", 23, "Santiago"),
    ("Ariel", 27, "Talca"),
    ("Maria", 18, "Temuco"),
    ("Juan", 30, "Santiago"),
    ("Leonardo", 26, "Temuco"),
    ("Javiera", 33, "Concepcion")
]
# for datos in alumnos:
#     nombre = datos[0]
#     edad = datos[1]
#     ciudad = datos[2]
#     print(f"Nombre: {nombre}, Edad: {edad} años, Ciudad: {ciudad}")

print("\nBienvenido/a a la demo lista de estudiantes")

opcion = ""

while opcion != "5":
    if not alumnos:
        print("\n")
        print("No hay alumnos en la lista")
    print("")

    #*Mostrar opciones al usuario
    print("\nMenu")
    print("1) Mostrar lista de alumnos")
    print("2) Buscar alumnos por ciudad")
    print("3) Calcular edad promedio")
    print("4) Agregar nuevo estudiante")
    print("5) Salir")

    opcion = input("\nElije una opcion: ")

    match opcion:
        case "1": #Agregar una tarea
            for datos in alumnos:
                nombre = datos[0]
                edad = datos[1]
                ciudad = datos[2]
                print(f"Nombre: {nombre}, Edad: {edad} años, Ciudad: {ciudad}")
            

        case "2":
            por_ciudad = input("Ingrese la ciudad de los alumnos: ")
            alumno_ciudad = 0
            for busqueda in alumnos:
                if busqueda[2] == por_ciudad:
                    alumno_ciudad += 1
                    # print(f"Coincide ciudad {busqueda}")
            print(f"\nLa cantidad de alumnos en la ciudad de {por_ciudad} es de {alumno_ciudad} estudiante(s)")

        case "3":
            edad_total = 0
            for edades in alumnos:
                edad = edades[1]
                edad_total += edad
            print(f"\nLa edad promedio de los estudiantes es de {(edad_total/len(alumnos)):.2f} años")

        case "4":
            add_nombre = str(input("Ingrese el nombre del estudiante: "))
            add_edad = int(input("Ingrese la edad: "))
            add_ciudad = str(input("Ingrese la ciudad: "))
            alumnos.append((add_nombre, add_edad, add_ciudad))

            print(f"El alumno {add_nombre} ha sido agregado correctamente")

        case "5":
            print("\nSaliendo........")
            break
        case _:
            print("\nOpcion no valida")
            print("-----------------------------------------------------\n")
            

#!==============================================================================================
'''
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
6. Mostrar los sets actualizados con mensajes claros.
'''

catalogo_a = ["azul", "verde", "rojo", "amarillo", "rosado", "celeste", "verde"]
catalogo_b = ["celeste", "violeta", "naranjo", "azul", "cafe", "blanco", "rojo"]

set_a = set(catalogo_a)
set_b = set(catalogo_b)

print("\nBienvenido/a a la demo de colores")

opcion = ""

while opcion != "8":

    #*Mostrar opciones al usuario
    print("\nMenu")
    print("1) Mostrar todos los colores")
    print("2) Mostrar interseccion de colores")
    print("3) Mostrar colores unicos del catalogo A")
    print("4) Mostrar colores unicos del catalogo B")
    print("5) Agregar nuevo color al catalogo A")
    print("6) Eliminar color especifico al catalogo B")
    print("7) Mostrar catalogos actualizados")
    print("8) Salir")

    opcion = input("\nElije una opcion: ")

    match opcion:
        case "1": #Unión: todos los colores disponibles sin duplicados
            print(f"Estos son los colores disponibles {set_a | set_b}")

        case "2": #Intersección: colores que están en ambos catálogos
            print(f"Estos colores estan en ambos catalogos {set_a & set_b}")

        case "3": #Diferencia A - B: colores únicos del catálogo A
            print(f"Colores unicos del catalogo A {set_a - set_b}")

        case "4": #Diferencia B - A: colores únicos del catálogo B.
            print(f"Colores unicos del catalogo B {set_b - set_a}")

        case "5": #Agregar un nuevo color al set_a (usando add()).
            add_color = input("Ingrese el color que quiere agregar al catalogo A: ")
            set_a.add(add_color)
            print(f"\nEl color {add_color} ha sido agregado correctamente")

        case "6": #Eliminar un color específico del set_b (usando discard())
            print(f"Colores en B {set_b}")
            eliminar_color = input("Ingrese el color que desea eliminar del catalogo B: ")
            if eliminar_color not in set_b:
                print("\nEl color ingresado no esta en la lista")
                continue

            set_b.discard(eliminar_color)
            print(f"\nEl color {eliminar_color} ha sido eliminado correctamente")

        case "7": #Mostrar los sets actualizados con mensajes claros.
            print(f"\nTodos los colores: {set_a | set_b}")
            print("\nColores por catalogo: ")
            print("\n - Catalogo A")
            for coloresA in set_a:
                print(coloresA)

            print("\n - Catalogo B")
            for coloresB in set_b:
                print(coloresB)

        case "8":
            print("\nSaliendo........")
            break
        case _:
            print("\nOpcion no valida")
            print("-----------------------------------------------------\n")

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
"""Contexto:
Una institución educativa necesita registrar y consultar información de sus estudiantes. Cada estudiante
tiene un nombre, una edad y una ciudad de residencia. Se requiere un sistema básico para almacenar los
datos, listarlos, buscar estudiantes por ciudad y obtener estadísticas.
Consigna:

● Desarrollar un programa que permita:
● Registrar múltiples estudiantes representados por tuplas dentro de una lista.
● Mostrar todos los registros con formato legible.
● Permitir consultar cuántos estudiantes son de una ciudad específica.
● Mostrar la edad promedio de los estudiantes registrados."""

estudiante=[
    ("Ana", 18, "Temuco"),
    ("Luis", 21, "Santiago"),
    ("María", 19, "Temuco"),
    ("Pedro", 22, "Valdivia"),
    ("Carla", 20, "Santiago"),
    ("Diego", 23, "Temuco")
]

opcion=0

while opcion!=8  :

    print("\nMenu")
    print("1) Registrar estudiante")
    print("2) Listar estudiantes")
    print("3) Buscar estudiante por ciudad")
    print("4) Estudiantes por ciudad")
    print("5) Promedio de edad de estudiantes")
    print("6) Modificar alumno")
    print("7) Eliminar alumno")
    print("8) Salir")

    opcion = int(input("Elige una opción: "))

    match opcion:
        case 1: 
            nombre=input("Nombre estudiante: ")
            edad = int(input("Edad: "))
            ciudad=input("Ciudad: ")

            estudiante.append((nombre, edad, ciudad))
        case 2: 
            for nombre, edad, ciudad in estudiante:
                print(f"\nNombre: {nombre}. Edad: {edad}. Ciudad: {ciudad}")
        case 3: 
            buscaCiudad = input("\nIngrese ciudad: ")

            for nombre, edad, ciudad in estudiante:
                if ciudad.lower()==buscaCiudad.lower():
                    print(f"\nNombre: {nombre} Edad:{edad} Ciudad: {ciudad}")   
        case 4:
            contador = 0
            ciudadEstudiante = input("\nIngrese la ciudad a consultar: ")
            for nombre, edad, ciudad in estudiante:
                    if ciudad.lower()==ciudadEstudiante.lower():
                        contador+=1
            
            print(f"\nHay {contador} estudiantes en la ciudad de {ciudadEstudiante}")

        case 5:
            sumaEdad = 0
            for nombre, edad, ciudad in estudiante:
                    sumaEdad +=int(edad)
            promedioEdad = sumaEdad /len(estudiante)

            print(f"\nPromedio edad de todos los estudiantes:{promedioEdad}")
        
        case 6:
            contador = 0
            nombreEstudianteModificar = input("\nIngrese nombre del estudiante a modificar: ")
            print("\nLista de estudiantes\n")
            print("N°    |  Nombre   |  Edad    |  Ciudad  |")
            for index,(nombre, edad, ciudad) in enumerate(estudiante):
                if nombreEstudianteModificar.lower() == nombre.lower():
                    print(f"  \n{index}   -       {nombre}        {edad}       {ciudad}")
                    contador+=1
            
            print(f"\n Se han encontrado {contador} coincidencia(s)")

            indexModificar = int(input("\n¿Qué regitro desea modificar? \nIngrese número de regitro: "))

            for index,(nombre, edad, ciudad) in enumerate(estudiante):
                if indexModificar==index:
                    nombre = input("\nNombre: ")
                    edad = input("\nEdad: ")
                    ciudad = input("\nCiudad: ")
                    estudiante[index]=(nombre, edad, ciudad)

            print("\n Modificación realizada...")
        case 7:
            contador = 0
            nombreEstudianteModificar = input("Ingrese nombre del estudiante a eliminar: ")
            print("\nLista de estudiantes\n")
            print("N°    |  Nombre   |  Edad    |  Ciudad  |")
            for index,(nombre, edad, ciudad) in enumerate(estudiante):
                if nombreEstudianteModificar.lower() == nombre.lower():
                    print(f"  \n{index}   -       {nombre}        {edad}       {ciudad}")
                    contador+=1
            
            print(f"\n Se han encontrado {contador} coincidencia(s)")

            indexModificar = int(input("\n¿Qué regitro desea eliminar? \nIngrese número de regitro: "))

            for index,(nombre, edad, ciudad) in enumerate(estudiante):
                if indexModificar==index:
                    estudiante.pop(index)
            print("\n Registro eliminado exitosamente...")

        case _:
            print("\nNo es una opción válida\n")                       


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
