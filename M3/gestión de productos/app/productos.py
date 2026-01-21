'''
Funciones del CRUD:

-agregar_producto(...)
-listar_productos(...)
-buscar_producto(...)
-editar_producto(...)
-eliminar_producto(...)

Aquí vive “lo importante” del sistema, lógica del negocio
'''
from functions.helpers import imprimir_tabla


def listar_productos(productos):
    headers = ["ID", "nombre", "descripcion", "precio", "stock"]
    imprimir_tabla(productos, headers=headers, formato="double_outline")

def agregar_producto(productos):
    print("Desde agregar_producto")
    pass

def buscar_producto_por_id(productos):
    print("Desde buscar_producto_por_id")
    pass

def editar_producto(productos):
    print("Desde editar_producto")
    pass

def eliminar_producto(productos):
    print("Desde eliminar_producto")
    pass