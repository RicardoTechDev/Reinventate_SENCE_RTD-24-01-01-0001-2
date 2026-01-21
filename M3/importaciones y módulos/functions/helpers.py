'''
helpers (o utils) suele ser el archivo donde 
pones funciones reutilizables y “genéricas” 
que ayudan al resto del programa, 
pero que no son la lógica principal.
'''

from tabulate import tabulate


def leer_int(mensaje: str, minimo=None, maximo=None):
    """
    Lee un número entero desde consola y lo valida antes de retornarlo.

    La función muestra un mensaje, recibe texto con `input()`, elimina espacios con `strip()`
    y verifica que el dato sea un entero válido (solo dígitos). Opcionalmente, valida que el
    número esté dentro de un rango definido por `minimo` y/o `maximo`.

    Parámetros
    ----------
    mensaje : str
        Texto que se muestra al usuario al pedir el número.
    minimo : int | None, opcional
        Límite inferior permitido (inclusive). Si es None, no se valida límite inferior.
    maximo : int | None, opcional
        Límite superior permitido (inclusive). Si es None, no se valida límite superior.

    Retorna
    -------
    int
        Un entero válido ingresado por el usuario (cumple tipo y rango si corresponde).
    """
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
    """
    Imprime un diccionario como tabla en consola usando la librería tabulate.

    La función recibe un diccionario simple o un diccionario de diccionarios y
    lo transforma en una tabla legible para mostrar en consola.

    Parámetros
    ----------
    datos : dict
        Diccionario a mostrar. Ejemplos válidos:
        - {"Ana": 6.5, "Juan": 5.8}
        - {"Ana": {"nota": 6.5, "asistencia": 95}}
    headers : list[str] | None, opcional
        Encabezados de la tabla. Si es None, se generan automáticamente.
    formato : str, opcional
        Estilo de la tabla (por defecto "grid").
        Ejemplos: "grid", "simple", "github", "fancy_grid".

    Retorna
    -------
    None
        La función solo imprime la tabla, no retorna valores.

    Requiere
    --------
    tabulate (librería externa)
    Instalar con: python -m pip install tabulate
    """
    if not datos:
        print("No hay datos para mostrar.")
        return

    filas = []

    # Caso 1: diccionario simple
    if not isinstance(next(iter(datos.values())), dict):
        if headers is None:
            headers = ["Clave", "Valor"]

        for clave, valor in datos.items():
            filas.append([clave, valor])

    # Caso 2: diccionario de diccionarios
    else:
        columnas = list(next(iter(datos.values())).keys())

        if headers is None:
            headers = ["Clave"] + columnas

        for clave, subdic in datos.items():
            filas.append([clave] + list(subdic.values()))

    print(tabulate(filas, headers=headers, tablefmt=formato))
