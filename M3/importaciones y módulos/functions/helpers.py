from tabulate import tabulate


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
    

def imprimir_tabla(datos: dict, headers: list[str] | None = None, formato = "grid"):
    if not datos:
        print("No hay datos para mostrar.")
        return
    
    filas = []

    #caso 1: diccionario simple
    if not isinstance(next(iter(datos.values())), dict):
        if headers is None:
            headers = ["Clave", "Valor"]

        for clave, valor in datos.items():
            filas.append([clave, valor])

    
    #caso 2 diccionario de diccionarios
    else:
        columnas: list(next(iter(datos.value())).keys())

        if headers is None:
            headers = ["Clave"] + columnas

        for clave, subdic in datos.items():
            filas.append([clave] + list(subdic.values()))

    print(tabulate(filas, headers=headers, tablefmt=formato))
