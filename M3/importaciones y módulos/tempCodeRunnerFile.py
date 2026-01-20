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
#opcion = functions_helpers.leer_int("Selecione una opción", 1, 10)
#print(f"Opción selecionada: {opcion}")


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
functions_helpers.imprimir_tabla(alumnos, headers)