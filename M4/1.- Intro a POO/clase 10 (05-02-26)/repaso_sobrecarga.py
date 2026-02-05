'''
¿Qué es la sobrecarga de métodos o funciones?

Sobrecargar significa:

Usar el mismo nombre de función o método para comportamientos distintos,
según cómo se llama (cantidad o tipo de parámetros).

En lenguajes como Java o C++

1.- sumar(int a, int b)
2.- sumar(int a, int b, int c)
3.- sumar(float a, float b)
4.- sumar(Bool a, Bool b)

sumar(5, 10) --> v1
sumar(1.25, 2.24) --> v3
sumar(5, 78, 26) --> v2
sumar(True, False) --> v4

El lenguaje decide automáticamente cuál usar según la cantidad de parámetros.


En Python (MUY importante)
#!Python NO tiene sobrecarga real por firma.
'''

#!Esto NO funciona:
def sumar(a, b):
    return a + b

def sumar(a, b, c):  # pisa la anterior
    return a + b + c

print(sumar(10, 15, 23))
#! print(sumar(10, 15)) NOS DA ERROR POR FALTA DE UN ARGUMENTO

#?La segunda definición reemplaza a la primera.

'''
Entonces… ¿cómo se hace “sobrecarga” en Python?

En Python se simula la sobrecarga usando:

1️⃣ Parámetros por defecto
2️⃣ *args
3️⃣ **kwargs
4️⃣ Condicionales internas
'''

#? 1️⃣ Sobrecarga con parámetros por defecto

#* Si no llega un parámetro, uso un valor por defecto
def saludar(nombre="Invitado", ciudad=""):
    if ciudad:
        print(f"Hola, {nombre}, estamos en {ciudad}")
    else:
        print(f"Hola, {nombre}")


saludar()
saludar("Arsenio")#Mismo nombre, distinto comportamiento.
saludar("Ana", "Santiago")


#?2️⃣ Sobrecarga con *args

#*Me adapto a la cantidad de argumentos recibidos.
def sumar(*args):#args es una tupla con lo que llegue.
    #! args ES UNA TUPLA EN ESTE PUNTO, NO SE PUEDE MODIFICAR; ES INMUTABLE
    #! soy_una_tupla = ("Hola", 5 , "chao")  --->  soy_una_tupla[2]
    #! args = (5, 4, 7, 15 ,23)
    if len(args) == 2:
        return args[0] + args[1]
    elif len(args) == 3:
        return args[0] + args[1] + args[2]
    elif len(args) == 4:
        return args[0] + args[1] + args[2] + args[3]
    elif len(args) == 5:
        return args[0] + args[1] + args[2] + args[3] + args[4]
    else:
        return 0

    '''
    Otra forma 

    suma = 0
    for numero in args:
        suma = suma + numero
    return suma
    '''
    

print(f"Suma argumentos {sumar(5)}")
print(f"Suma argumentos {sumar(5)}")
print(f"Suma argumentos {sumar(5, 10)}")
print(f"Suma argumentos {sumar(5, 4, 3)}")
print(f"Suma argumentos {sumar(5, 4, 15, 10)}")
print(f"Suma argumentos {sumar(5, 4, 7, 15 ,23)}")


#? 3 Sobrecarga con **kwargs
#!Al pasar los parametros laa función los recibe como un diccionario
def saludar(**kwargs):
    '''
    kwargs = {
        "nombre": VALOR,
        "ciudad": VALOR
    }
    '''
    print("======== Asi llega el diccionario =======")
    print(kwargs)
    print("=========================================")
    
    if kwargs.get("nombre") and kwargs.get("ciudad"):
        print(f"Hola, {kwargs.get("nombre")}, estamos en {kwargs.get("ciudad")}")
    
    elif kwargs.get("nombre"): #retorna None en caso de no encontrar la clave nombre
        print(f"Hola, {kwargs.get("nombre")}")

    else:
        print("Hola, Invitado")


saludar()
saludar(nombre="Ana")
saludar(nombre="Elena", ciudad="Santiago")
saludar(nombre="Luis", ciudad="Santiago", clima="Soleado")


#? 4️⃣ Sobrecarga combinada (la más común)
def procesar(*args, **kwargs):
    if len(args) == 0:
        print("Nada que procesar")
    elif len(args) == 1:
        print("Un dato:", args[0])

    if kwargs.get("debug"):
        print("Modo debug activo")


# 1) Sin argumentos
procesar()
# Nada que procesar

print("-"*15)

# 2) Con 1 argumento posicional
procesar(123)
# Un dato: 123

print("-"*15)

# 3) Con 1 argumento posicional + debug=True
procesar("hola", debug=True)
# Un dato: hola
# Modo debug activo

print("-"*15)

# 4) Solo kwargs (sin args) + debug=True
procesar(debug=True)
# Nada que procesar
# Modo debug activo

print("-"*15)

# 5) Con varios args (ojo: tu función NO hace nada con len(args)>1)
procesar(1, 2, 3)
# (no imprime nada, porque no hay caso para 2 o más args)

print("-"*15)

# 6) Con varios args + debug=True
procesar(1, 2, 3, debug=True)
# Modo debug activo

#===============================================
'''
En POO es exactamente lo mismo

Un método es una función dentro de una clase, así que la idea no cambia:
'''
class Calculadora:
    def sumar(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
