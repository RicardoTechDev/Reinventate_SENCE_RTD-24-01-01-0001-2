def leer_int(mensaje: str, minimo=None, maximo=None):
    while True:
        dato = input(mensaje).strip()
        if not dato.isdigit():#isdigit para verificar si es entero
            print("Debes ingresar un número entero.")
            continue

        num = int(dato)

        if minimo is not None and num < minimo:
            print(f"Debe ser un número >= {minimo}")
            continue
        
        # 0--> False,  "" ---> False , None ---> False
        # 1 ---> True, "hola" --->True, "8" ---> True
        if maximo and num > maximo:
            print(f"Debe ser un número <= {maximo}")
            continue

        return num
    

leer_int("Ingrese un opción")