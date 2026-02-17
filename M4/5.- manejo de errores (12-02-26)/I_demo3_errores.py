
try:
    print("=== Caso 1 Error de sintaxis ===")
    if True
        print("Esto no se ejecutará")
except Exception as e:
    print("Error", e)

def mi_funcion():
    try:
        print("=== Caso 2 Excepción en tiempo de ejecución ===")
        print("Inicio del programa")
        numero = int("abc")
        print("Esto no se verá")

    except ValueError as e:
        print(f"se capturo un ValueError: {e}, ubicación: mi_funcion() --> I_demo3_erroes.py")

    except Exception as e:
        print("Error", e)


mi_funcion()