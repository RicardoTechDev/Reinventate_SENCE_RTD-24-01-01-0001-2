'''
Objetivo funcional:
● Controlar que la edad sea un número positivo
● Lanzar una excepción con un mensaje personalizado si no se cumple
Pasos esperados:
1. Definí una función validar_edad(edad)
2. Usá raise ValueError("La edad no puede ser negativa") si la edad es menor a 0
3. Si la edad es válida, imprimí un mensaje como “Edad válida: X años”
4. Probalo con validar_edad(25) y luego con validar_edad(-3)
'''
class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa")
    print(f"Edad válida: {edad} años")

try:
    validar_edad(25)
    validar_edad(-3)
except EdadInvalidaError as e:
    print("ERROR: ", e)