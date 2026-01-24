'''
¿Qué es la recursividad?

La recursividad es cuando una función se llama a sí misma 
para resolver un problema.

Ojo: siempre debe tener una condición de corte, si no, se ejecuta infinitamente.

-----------------------------------
Partes de una función recursiva

Caso base → cuándo la función se detiene
Llamada recursiva → la función se llama a sí misma
'''

#? Ejemplo clásico: contar hacia atrás
def contar(n):#0
    if n == 0:        # caso base
        print("Fin")
    else:
        print(n)#1
        contar(n - 1)#1-1 = 0 # llamada recursiva

contar(5)


#? Ejemplo muy común: factorial
def factorial(n):#5
    if n == 1:       # caso base
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))  # 120


#? Ejemplo simple con suma de números
def sumar_hasta(n):
    if n == 0:
        return 0
    
    return n + sumar_hasta(n - 1)

print(sumar_hasta(4))  # 10 (4+3+2+1)

def sumar_hasta(n):
    suma = 0
    for _ in range(0, n):#3
        #print(n)#1
        suma += n# 9 + 1 --> 10 
        n -= 1#1 - 1 ---> 0 
    return suma

print(sumar_hasta(4)) 

#===================================================

import tkinter as tk
import time

def actualizar_reloj():
    # Obtener la hora y actualizar la etiqueta
    hora_actual = time.strftime("%H:%M:%S")
    etiqueta.config(text=hora_actual)
    
    # "Recursividad" controlada: se llama a sí misma después de 1000ms
    etiqueta.after(1000, actualizar_reloj)

# Configuración básica de la ventana
ventana = tk.Tk()
ventana.title("Reloj Recursivo")
etiqueta = tk.Label(ventana, font=("Helvetica", 48), fg="blue")
etiqueta.pack()

actualizar_reloj() # Primera llamada
ventana.mainloop()