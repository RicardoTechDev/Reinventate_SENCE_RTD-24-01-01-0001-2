'''
Funciones para:

-mostrar el menú
-pedir una opción
-imprimir mensajes bonitos

No debería tener lógica de negocio (no calcular totales, modificar productos).
'''
# --- Librería estándar ---


# --- Librerías externas / de terceros ---


# --- Módulos y paquetes propios del proyecto ---
from app import productos as functions_productos
from app.functions import helpers as functions_helpers


def mostrar_menu():
    print("\n" + "=" * 30)
    print("     GESTIÓN DE PRODUCTOS")
    print("=" * 30)
    print("1) Listar productos")
    print("2) Agregar producto")
    print("3) Buscar producto por ID")
    print("4) Editar producto")
    print("5) Eliminar producto")
    print("0) Salir")
    print("=" * 30)


def ejecutar_menu(productos):
    while True:
        mostrar_menu()
        opcion = functions_helpers.leer_int("Elige una opción: ", minimo=0, maximo=5)
        print("\n")

        match opcion:
            case 1:
                functions_productos.listar_productos(productos)
                functions_helpers.pausa()
                functions_helpers.limpiar_consola()

            case 2:
                functions_productos.agregar_producto(productos)
                functions_helpers.pausa()
                functions_helpers.limpiar_consola()

            case 3:
                functions_productos.buscar_producto_por_id(productos)
                functions_helpers.pausa()
                functions_helpers.limpiar_consola()

            case 4:
                functions_productos.editar_producto(productos)
                functions_helpers.pausa()
                functions_helpers.limpiar_consola()

            case 5:
                functions_productos.eliminar_producto(productos)
                functions_helpers.pausa()
                functions_helpers.limpiar_consola()

            #case 6 : GENERAR VENTA
            case 0:
                print("Saliendo del sistema...")
                break
