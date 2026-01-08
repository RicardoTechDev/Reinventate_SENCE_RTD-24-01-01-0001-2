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


"""2. Determinar si un número es par, impar o múltiplo de 3
a. Pide al usuario un número entero.
b. Convierte la entrada con int.
c. Usa una condición if con un operador lógico (and) para verificar si el número es divisible por
2 y por 3.
d. Si no se cumple, agrega más condiciones para verificar si es par solamente, o si es impar y
múltiplo de 3.
e. En el caso contrario, indica que es impar y no múltiplo de 3.
f. Usa mod (%) para evaluar divisibilidad."""


numero_entero = input("Ingrese un numero entero:")
numero = int(numero_entero)
if numero % 2 == 0   and  numero % 3 == 0 :
    print("El numero es divisible por 2 y 3 ")
elif numero % 2 == 0 :
    print("El numero es par")
elif numero % 2 > 0 and numero % 3 == 0 :
    print("El numero es impar y multiplo de 3")
else :
    print("El numero es impar y no es multiplo de 3")




"""3. Clasificación de edades
a. Pide al usuario que ingrese su edad.
b. Convierte la entrada a entero (int).
c. Verifica que sea un número válido (mayor o igual a cero).
d. Si la edad es de 0 a 12, imprime que es un niño o niña.
e. Si está entre 13 y 17, indica que es adolescente.
f. Si está entre 18 y 64, que es adulto.
g. Si tiene 65 años o más, clasificalo como adulto mayor.
h. Muestra el resultado final en pantalla."""


edad = input("Ingrese edad:")
numero = int(edad)

if numero < 0:
    print("Ingrese edad mayor a 0")
else:
    if numero<=12:
        print ("Eres un niñ@")
    elif numero<=17:
        print ("Eres un adolescente")
    elif numero<=64:
        print("Eres un adulto")
    else:
        print ("Eres un adulto mayor")