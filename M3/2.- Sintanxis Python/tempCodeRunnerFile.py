ciudades = [
    ("Pucón", (-39.28223, -71.95427)),
    ("Valdivia", (-39.81422, -73.24589)),
    ("Futaleufu", (-43.1858, -71.8667)),
    ("Punta Arenas", (-53.1625, -70.9081)),
]

#*7. Iterar sobre la lista de tuplas y mostrar cada ciudad
print("================= LISTA DE CIUDADES ==================")
for nombre_ciudad, coordenadas_ciudad in ciudades:
    latitud = coordenadas_ciudad[0]
    longitud = coordenadas_ciudad[1]
    print(f"La ciudad {nombre_ciudad} está ubicada en ({latitud}, {longitud})")