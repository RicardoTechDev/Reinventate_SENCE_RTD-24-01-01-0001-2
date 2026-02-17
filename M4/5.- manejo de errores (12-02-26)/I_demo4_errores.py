'''
Vas a solicitar al usuario que ingrese un número, y vas a manejar posibles errores para evitar que el programa
se rompa.

Objetivo funcional:
● Solicitar un número entero
● Detectar si el usuario escribe texto o caracteres inválidos
● Mostrar un mensaje amigable en lugar de un traceback
Variantes para probar:
● Ingresar "25" → válido
● Ingresar "abc" → ValueError
● Ingresar "10.5" → ValueError (por ser float)
'''

entrada = input("Ingresa un número entero: ")

try:
    numero = int(entrada)#tratar de castear
    print(f"Número ingresado: {numero}")
except ValueError:
    print("Error: debes ingresar un número válido")



