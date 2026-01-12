"""
Vamos a simular un sistema que guarda coordenadas geográficas 
usando tuplas para asegurar que no se
modifiquen accidentalmente.

1. Crear una tupla con las coordenadas de una ciudad
2. Mostrar las coordenadas por pantalla
3. Acceder al valor de latitud y longitud por índice
4. Intentar modificar la tupla (y provocar un error)
5. Reemplazar la tupla completa si es necesario (no un solo valor)
6. Usar tuplas dentro de una lista para múltiples registros
7. Iterar sobre la lista de tuplas y mostrar cada ciudad
8. Imprimir mensajes como: "La ciudad está ubicada en (lat, long)"la
"""

#? 1. Crear una tupla con las coordenadas de una ciudad (Temuco  latitud -38.73628 y longitud -72.59738)
ciudad = "Temuco"
coordenadas = (-38.73628, -72.59738)

#? 2. Mostrar las coordenadas por pantalla

print(f"Ciudad : {ciudad}")
print(f"Coordenadas : {coordenadas}")

#? 3. Acceder al valor de latitud y longitud por índice
latitud = coordenadas[0]
longitud = coordenadas[1]

print(f"Latitud (indice 0): {latitud}")
print(f"Longitud (indice 1): {longitud}")

#? 4. Intentar modificar la tupla (y provocar un error)
try:
    coordenadas[1] = -33.451265
except TypeError as e:
    print(f"Ocurrio un error: {e}")

#? 5. Reemplazar la tupla completa si es necesario (no un solo valor)
coordenadas = (-38.67687167, -72.6546874684)#nueva tupla completa
print(f"Nuevas coordenas para la ciudad {ciudad} : {coordenadas}")

#? 6. Usar tuplas dentro de una lista para múltiples registros

ciudades = [
    ("Pucón", (-39.28223, -71.95427)),
    ("Valdivia", (-39.81422, -73.24589)),
    ("Futaleufu", (-43.1858, -71.8667)),
    ("Punta Arenas", (-53.1625, -70.9081)),
]

#? 7. Iterar sobre la lista de tuplas y mostrar cada ciudad
print("================= LISTA DE CIUDADES ==================")
for nombre_ciudad, coordenadas_ciudad in ciudades:
    latitud = coordenadas_ciudad[0]
    longitud = coordenadas_ciudad[1]
    #? 8. Imprimir mensajes como: "La ciudad está ubicada en (lat, long)"
    print(f"La ciudad {nombre_ciudad} está ubicada en ({latitud}, {longitud})")
