opcion = ""

while opcion !="3":
    #*Mostrar opciones al usuario
    print("\nMenu")#\n salto de línea
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