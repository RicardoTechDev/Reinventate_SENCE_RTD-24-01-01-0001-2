'''¿Qué es una función lambda?

Una función lambda es una función pequeña, 
rápida y sin nombre, que se escribe en una sola línea.
Se usan cuando la función es muy simple 
y no vale la pena escribir un def.
'''

#? lambda parametros: expresion

#Ejemplo función normal
def sumar(a, b):
    return a + b

print(sumar(3, 5))  # 8

#La misma función con lambda:
sumar = lambda a, b: a + b

print(sumar(3, 5))  # 8


#Otros ejemplos
#? Duplicar un número
def duplicar(x):
    return x * 2

duplicar = lambda x: x * 2
print(duplicar(4))  # 8

#? Ver si un número es par
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

es_par = lambda n: n % 2 == 0
print(es_par(6))  # True

#? Calcular precio con IVA (19%)
def precio_con_iva(precio):
    total = precio * 1.19
    return total

precio_con_iva = lambda precio: precio * 1.19
print(precio_con_iva(1000))  # 1190

hora = 22

mensaje = (lambda h: "Buenas noches" if h >= 20 else "Buen día")(hora)
print(mensaje)


#?Funciones lambda – Resumen

#?Ventajas
'''
* Permiten escribir funciones muy cortas y rápidas
* Reducen código cuando la lógica es simple
* Útiles para usos puntuales y temporales
* Evitan crear funciones con nombre cuando no es necesario
'''

#?Desventajas

'''
* Menor legibilidad si se abusa de ellas
* No son ideales para principiantes
* Difíciles de depurar al no tener nombre
* No permiten explicar la lógica con comentarios
'''

#?Restricciones

'''
Solo permiten una expresión
No pueden tener varias líneas
No admiten estructuras de control complejas
No pueden manejar errores
No permiten asignaciones de variables
'''