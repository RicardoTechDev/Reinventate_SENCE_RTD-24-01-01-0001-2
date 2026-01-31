'''
1.- *args (argumentos posicionales)

Qué es?
args no es una palabra reservada
El * es lo importante
Todo lo que llega sin nombre se guarda en una tupla
'''
def sumar(*args):
    total = 0
    for n in args:
        total += n
    return total

print(sumar(2, 4))
print(sumar(1, 2, 3, 4))



#=========================================================
'''
2.- **kwargs (argumentos con nombre)

Qué es?
kwargs = keyword arguments
Todo lo que viene como clave=valor se guarda en un diccionario
'''

def mostrar(**kwargs):
    '''
        Internamente:
                        kwargs = {
                    "nombre": "Ana",
                    "edad": 30
                }
    '''
    print(kwargs)

mostrar(nombre="Ana", edad=30)


#Otro ejemplo 
def mostrar_datos(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Ana", ciudad="Temuco", activo=True)


#? ========== Regla de orden (IMPORTANTÍSIMA) ============
#?def funcion(param_normal, *args, **kwargs):

#?Ejemplo combinado
def saludar(titulo, *args, **kwargs):
    print(titulo)

    print("Posicionales:", args)
    print("Con nombre:", kwargs)

saludar(
    "Datos",
    "Ana", "Pedro",
    ciudad="Temuco",
    activo=True
)