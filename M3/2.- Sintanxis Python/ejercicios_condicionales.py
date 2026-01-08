'''
1. Verificar si un número es positivo, negativo o cero
a. Pide al usuario que ingrese un número decimal.
b. Convierte la entrada a número (float).
c. Usa una estructura if para verificar si es mayor a cero.
d. Si no lo es, agrega una condición elif para comprobar si es menor a cero.
e. Si ninguna de las anteriores se cumple, usa else para indicar que el número es cero.
f. Muestra un mensaje apropiado según el caso.
'''

#a. Pide al usuario que ingrese un número decimal.
numero_texto = input("Ingrese un número decimal:")

#b. Convierte la entrada a número (float).
numero = float(numero_texto)#casteo

#c. Usa una estructura if para verificar si es mayor a cero.
if numero > 0:
    print(f"El número {numero} es mayor a cero (positivo)")

#d. Si no lo es, agrega una condición elif para comprobar si es menor a cero.
elif numero < 0:
    print(f"El número {numero} es menor a cero (negativo)")

#e. Si ninguna de las anteriores se cumple, usa else para indicar que el número es cero.
else:
    print("El número es cero")