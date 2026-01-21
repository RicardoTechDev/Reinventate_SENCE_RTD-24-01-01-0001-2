'''
La buena práctica más común es este orden:
Librería estándar de Python
Librerías externas / de terceros
Módulos o paquetes propios del proyecto

Orden alfabético por nombre del módulo
'''
#? ==== EJEMPLO DE IMPORTACIONES USANDO BUENAS PRACTICAS ====
# --- Librería estándar de Python (viene con Python) ---
import math
import random
from pprint import pprint

# --- Librerías externas / de terceros (pip install ...) ---
from tabulate import tabulate


# --- Módulos y paquetes propios del proyecto ---
from functions.helpers import leer_int, imprimir_tabla
from paquetes import saludos

#? =============================================================

import paquetes.saludos #Opción 1
from paquetes import saludos#Opción 2
from paquetes.saludos import saludar#Opción 3

import paquetes.saludos as pq_saludos#Opción 4
from paquetes.saludos import saludar as saludar_usuario#Opción 5

from functions import helpers as functions_helpers

paquetes.saludos.saludar("Luis")#Opción 1
saludos.saludar("Ana")#Opción 2
saludar("Elena")#Opción 3

pq_saludos.saludar("Mario")#Opción 4
saludar_usuario("Sandra")#Opción 5

#======================================
opcion = functions_helpers.leer_int("Selecione una opción", 1, 10)
print(f"Opción selecionada: {opcion}")


productos = {
    "pan": 2000,
    "leche": 900,
    "huevos":400
    }


functions_helpers.imprimir_tabla(productos)

alumnos = {
    "Ana": {"nota": 6.5, "asistencia": 95},
    "Juan": {"nota": 5.8, "asistencia": 88},
    "Pedro": {"nota": 5.5, "asistencia": 76},
}

headers = ["Nombre", "Nota", "Asistencia"]
#Sin encabezados
functions_helpers.imprimir_tabla(alumnos)

#Con encabezados
functions_helpers.imprimir_tabla(alumnos, headers)

#Sin encabezados y con formato de tabla (ver https://pypi.org/project/tabulate/)
functions_helpers.imprimir_tabla(alumnos, None, "double_outline")