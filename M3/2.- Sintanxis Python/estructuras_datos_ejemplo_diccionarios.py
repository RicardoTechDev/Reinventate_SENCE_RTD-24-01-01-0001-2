'''
1) Sumar ventas por producto
Si el producto no exis
Enunciado:
Crea una función sumar_venta(ventas, producto, cantidad) que sume la cantidad vendida al diccionario ventas.
te, debe crearlo con esa cantidad.
'''
def sumar_venta(vts, producto, cantidad):
    """
    Suma una cantidad vendida a un diccionario de ventas por producto.

    Parámetros:
    - ventas (dict): Diccionario deonde la clave es el nombre del producto (str)
    y el valor es la cantidad vendida acumulada (int o float).
    - producto (str): Nombre del producto a registrar.
    - cantidad (int|float): Cantidad vendida a sumar (debe ser > 0)

    Retorna:
    - dict:  El mismo diccionario 'ventas' actualizado.
    """
    if producto in vts:
        vts[producto] += cantidad #--> ventas{ "leche": 3 }
    else:
        vts[producto] = cantidad

#*=============== FIN FUNCIÓN =================

ventas = {}
producto = "sandia"
sumar_venta(ventas, "leche", 3)
sumar_venta(ventas, "leche", 5)
sumar_venta(ventas, "pan", 5)

print(ventas)
print(producto)

'''
2) Calcular el promedio de notas de un alumno

Enunciado:
Crea una función promedio_alumno(alumnos, nombre) que reciba:

alumnos: diccionario donde cada alumno tiene una lista de notas
nombre: el alumno a buscar

Debe devolver el promedio, o -1 si el alumno no existe.
'''
def promedio_alumno(alumnos, nombre):
    """
    Calcula el promedio de notas de un alumno existente y si no exite el alumno retorna -1

    Parámetros:
    - alumnos (dict): Diccionario donde:
                        - la clave es el nombre del alumno (str)
                        - el valor es una lista de notas (list) con números (int o float)
    - nombre (str): Nombre del alumno a buscar.

    Retorna:
    - int : -1 si el alumno no existe en el diccionario
    - float: el promedio de las notas del alumno, si existe y si tiene notas
    """
    if nombre not in alumnos:
        return -1
    
    notas = alumnos[nombre]
    suma_notas = 0

    for nota in notas:
        suma_notas += nota
    
    promedio = suma_notas / len(notas)

    return promedio


alumnos = {
    "Ana" : [6.0, 5.5, 5.7],
    "Luis": [4.8, 5.0, 6.4]
}

nombre_alumno = "Sandra"
promedio = promedio_alumno(alumnos, nombre_alumno)

if promedio == -1:
    print("Alumno no encontrado.")
else:
    print(f"Promedio de notas de {nombre_alumno} es {promedio:.2f}")


'''
3) Carrito de compras (agregar, total, mostrar)

Enunciado:
Vas a simular un carrito de compras usando un diccionario.

- Crea una función agregar_al_carrito(carrito, producto, precio, cantidad) que:
Si el producto no existe en el carrito, lo agregue.
Si el producto ya existe, solo debe sumar la cantidad (y mantener el precio que ya tenía).

- Crea una función mostrar_carrito(carrito) que imprima cada producto con:
nombre, precio, cantidad, subtotal (precio * cantidad)

- Crea una función calcular_total(carrito) que devuelva el total a pagar (suma de subtotales).

carrito = {
            "pan": {"precio": 1200, "cantidad": 2, "subtotal": 2400},
            "leche": {"precio": 2000, "cantidad": 1}
}

'''

def agregar_al_carrito(carrito, nombre_producto, precio, cantidad):
    if nombre_producto in carrito:
        carrito[nombre_producto]["Cantidad"] += cantidad
    else:
        carrito[nombre_producto] = {"Precio": precio, "Cantidad": cantidad}


def mostrar_carrito(carrito):
    if len(carrito) == 0:
        print("Carrito vacío")
    else:
        for nombre_producto, datos_producto in carrito.items():
            #datos_producto  ---> {"precio": 1200, "cantidad": 2}
            precio = datos_producto["Precio"]
            cantidad = datos_producto["Cantidad"]
            subtotal = precio * cantidad
            carrito[nombre_producto]["Subtotal"] = subtotal
            print(f"{nombre_producto} | precio: ${precio} | cantidad: {cantidad} | subtotal: ${subtotal}")


def calcular_total(carrito):
    total_carrito = 0

    for datos in carrito.values():
        total_carrito += datos["Subtotal"]

    return total_carrito


carrito = {}

#Agregar los productos al carrito
agregar_al_carrito(carrito, "pan", 2000, 2)
agregar_al_carrito(carrito, "leche", 1200, 1)
agregar_al_carrito(carrito, "huevos", 400, 12)
agregar_al_carrito(carrito, "bebida", 2600, 1)
agregar_al_carrito(carrito, "pan", 2000, 2)

#Mostrar carrito
print("============== CARRITO ===============")
mostrar_carrito(carrito)


total = calcular_total(carrito)
print(f"TOTAL A PAGAR: {total}")

