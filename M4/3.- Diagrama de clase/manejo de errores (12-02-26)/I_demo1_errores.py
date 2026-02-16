'''
Qué va a ocurrir:
1. Si el usuario ingresa "0" → se lanza ZeroDivisionError
2. Si ingresa texto → se lanza ValueError
3. Python mostrará un traceback completo y detendrá el programa
'''

try:
    numero = int(input("Ingresa un número: "))
    resultado = 10/numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Error: debes ingresar un número entero (no texto)")

except ZeroDivisionError:
    print("Error: no es posible dividir por cero")


print("Continuo.....")