
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

print(carrito)

#Mostrar carrito
print("============== CARRITO ===============")
mostrar_carrito(carrito)

print(carrito)


total = calcular_total(carrito)
print(f"TOTAL A PAGAR: {total}")