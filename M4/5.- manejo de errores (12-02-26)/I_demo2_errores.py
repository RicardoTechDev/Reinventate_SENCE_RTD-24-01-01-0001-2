#1. ZeroDivisionError
try:
    print(10/0)
    print("Luego de ZeroDivisionError")
except ZeroDivisionError:
    print("no es posible dividir por cero")

#2. ValueError
try:
    edad = int("veinticinco")
    print("luego de ValueError")
except ValueError:
    print("Error en el casteo")

#3. IndexError
try:
    lista = [1, 2, 3]
    print(lista[5])
    print("luego de IndexError")
except IndexError:
    print("error de indice")


#4. KeyError
try:
    datos = {
        "nombre": "Ana",
        "edad": 29
        }
    print(datos["apellido"])#datos.get("apellido", None)
    print("KeyError")
except KeyError:
    print("Error de key")

#5 TypeError
try:
    resultado = "10" + 5
    print("luego de TypeError")
except TypeError:
    print("Error de tipos")