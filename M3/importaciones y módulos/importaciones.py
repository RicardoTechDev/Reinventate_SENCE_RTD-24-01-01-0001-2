import os
import random#--> tiene muchas funciones
from tabulate import tabulate


def limpiar_consola():
    for num in range(1,100):
        print(f"Hola mundo {num}")
    os.system('cls')

#limpiar_consola()
num = random.randint(1, 100)
print(num)


#=================================================================================
colores = ["Rojo", "Azul", "Verde", "Amarillo"]
print(f"Color: {colores[random.randint(0, 3)]}")#1 forma
print(f"Color: {random.choice(colores)}")#1 forma

# import tkinter as tk

# # 1. Crear la ventana principal
# ventana = tk.Tk()
# ventana.title("Ventana de Color")
# ventana.geometry("400x300") # Tamaño inicial de la ventana

# # 2. Configurar el color de fondo
# # Puedes usar nombres de colores (ej. 'blue', 'lightgray')
# # o códigos hexadecimales (ej. '#3498DB')
# ventana.configure(bg='blue') # Fondo gris claro

# # 3. Añadir elementos (opcional)
# # Etiqueta de texto con color
# etiqueta = tk.Label(ventana, text="¡Hola, mundo con color!", fg="navy", bg="lightgray", font=("Arial", 16))
# etiqueta.pack(pady=20) # Empaqueta la etiqueta en la ventana

# # 4. Iniciar el bucle principal para mostrar la ventana
# ventana.mainloop()

#======================================================================
# from pynput import mouse

# def al_hacer_click(x, y, boton, presionado):
#     if presionado:
#         print(f"Click detectado en la posición: ({x}, {y}) con {boton}")

# # Inicia el "escuchador" (listener)
# with mouse.Listener(on_click=al_hacer_click) as listener:
#     listener.join()

#======================================================================


alumnos = {
    "Ana" : 6.5,
    "Juan": 5.8,
    "Pedro": 4.5
}

tabla = []

for nombre, nota in alumnos.items():
    tabla.append([nombre, nota])

print(tabulate(tabla, headers=["Alumno", "Nota"], tablefmt="grid"))

#================================================================
from rich.console import Console
from rich.table import Table

datos = {"Pan": 12, "Leche": 5, "Huevos": 20}
maxv = max(datos.values())

table = Table(title="Stock (barras)")
table.add_column("Producto")
table.add_column("Cantidad")
table.add_column("Barra")

for k, v in datos.items():
    barra = "█" * int((v / maxv) * 20)
    table.add_row(k, str(v), barra)

Console().print(table)


#===================================================================
'''
¿Qué es una librería en Python? (explicado fácil)

👉 Una librería es un conjunto de herramientas ya hechas
que otra persona programó para que tú no tengas que hacerlo desde cero.

Es como una caja de herramientas:

tú no fabricas el martillo,
solo lo usas cuando lo necesitas.

Ejemplo de la vida real 🧰
Imagina que quieres clavar un clavo:

❌ Sin herramientas → tendrías que inventar algo con una piedra
✅ Con un martillo → lo haces rápido y bien

👉 Las librerías son el martillo
👉 Python es la persona que lo usa

Ejemplo en programación (muy simple)
❌ Sin librería

Supongamos que quieres calcular la raíz cuadrada de un número.

Tendrías que:
aprender la fórmula matemática
programarla tú mismo
manejar errores
😵 Mucho trabajo.
'''

#Sin librería
def raiz_cuadrada(n, tolerancia=1e-10, max_iter=1000):
    # Casos especiales
    if n < 0:
        return None  # no existe raíz cuadrada real para negativos
    if n == 0:
        return 0.0

    # Estimación inicial
    x = n if n >= 1 else 1.0

    # Iterar (Newton-Raphson)
    for _ in range(max_iter):
        x_nuevo = 0.5 * (x + n / x)
        if abs(x_nuevo - x) < tolerancia:
            return x_nuevo
        x = x_nuevo

    return x  # por si no converge en max_iter

print(raiz_cuadrada(16))   # 4.0 aprox
print(raiz_cuadrada(2))    # 1.41421356... aprox


#Con una librería
import math
resultado = math.sqrt(16)
print(resultado)
