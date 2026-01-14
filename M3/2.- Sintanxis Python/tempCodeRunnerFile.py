#*Métodos importantes de diccionarios
productos = {
    "pan" : {"precio": 2000, "stock": 100},
    "leche" : {"precio": 1000, "stock": 35}
}

#*Alternativa al método get
try:
    print(productos["jugo"])
except:
    print("No existe el producto")

#*Recupera y si no existe lo crea
arroz = productos.setdefault("arroz", {"precio": 1990, "stock": 30})
print(productos)

pescado = productos.setdefault("pescado")
print(pescado)

#*Actualizar (con otro diccionario)
nuevos = {
    "pescado":  {"precio": 3500, "stock": 35},
    "huevos":  {"precio": 400, "stock": 35}
}

productos.update(nuevos)
print(productos)

#* Borrar todo el diccionario
productos.clear()
print(productos)