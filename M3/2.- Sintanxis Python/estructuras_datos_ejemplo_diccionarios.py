'''
1) Buscar un producto por ID

Enunciado:
Crea una función buscar_producto(productos, id_producto) que reciba un diccionario de productos y un ID.
Debe devolver el diccionario del producto si existe, o None si no existe.
'''

'''
2) Sumar ventas por producto

Enunciado:
Crea una función sumar_venta(ventas, producto, cantidad) que sume la cantidad vendida al diccionario ventas.
Si el producto no existe, debe crearlo con esa cantidad.
'''


'''
3) Calcular el promedio de notas de un alumno

Enunciado:
Crea una función promedio_alumno(alumnos, nombre) que reciba:

alumnos: diccionario donde cada alumno tiene una lista de notas
nombre: el alumno a buscar

Debe devolver el promedio, o -1 si el alumno no existe.
'''


'''
4) Carrito de compras (agregar, total, mostrar)

Enunciado:
Vas a simular un carrito de compras usando un diccionario.

- Crea una función agregar_al_carrito(carrito, producto, precio, cantidad) que:
Si el producto no existe en el carrito, lo agregue.
Si el producto ya existe, solo debe sumar la cantidad (y mantener el precio que ya tenía).

- Crea una función mostrar_carrito(carrito) que imprima cada producto con:
nombre, precio, cantidad, subtotal (precio * cantidad)

- Crea una función calcular_total(carrito) que devuelva el total a pagar (suma de subtotales).
'''