'''
Crearemos una pequeña aplicación de consola que permita gestionar 
una lista de tareas. Aplicaremos
operaciones básicas de listas como agregar, eliminar e iterar.

1. Crear una lista inicial con tareas
2. Mostrar todas las tareas actuales
3. Agregar una nueva tarea a la lista
4. Marcar una tarea como completada (eliminarla)
5. Recorrer e imprimir la lista de tareas con un for
6. Usar pop() para eliminar tareas por índice
7. Validar si la lista está vacía
8. Mostrar mensaje de cierre: "¡Todas las tareas completadas!"
'''
tareas = [
    "Estudiar Python", 
    "Hacer Ejercicios de Python", 
    "Soñar con Python", 
    "Leer 50 páginas de Documentación de Python"
    ]

print("Bienvenido/a a la demo de lista de Tareas")

opcion = ""

while opcion !="4":
    print("\n")
    if not tareas:
        print("No hay tareas en la lista")
        print("¡Todas las tareas completadas!")
    
    else:
        for indice, tarea in enumerate(tareas):
            print(f"{indice}-{tarea}")
    
    
    #*Mostrar opciones al usuario
    print("\nMenu")#\n salto de línea
    print("1) Agregar nueva tarea")
    print("2) Marcar tarea completada (eliminarla)")
    print("3) Eliminar tarea (con pop)")
    print("4) Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            #Agregar nueva tarea
            nueva_tarea = input("Ingrese nueva tarea: ")
        
            if not nueva_tarea:
                print("Debe ingresar una tarea válida")
                continue
            
            tareas.append(nueva_tarea)
            print("Tarea agregada correctamente")

        case "2":
            marcar_completada = input("Ingrese tarea completada: ")

            if marcar_completada in tareas:
                tareas.remove(marcar_completada)
                print("Tarea marcada correctamente")
                continue

            print("Esa tarea no esta en la lista")
            
        case "3":
            indice_eliminar = int(input("Ingrese número de tarea a eliminar: "))

            if indice_eliminar == "":
                print("Debe ingresar un número valido")
                continue

            tarea_eliminada = tareas.pop(indice_eliminar)
            print(f"Tarea : {tarea_eliminada} eliminada  de manera correcta")

        case "4":
            print("Saliendo.....")
            break
        case _:
            print("Opción no válida")