def saludar(titulo, *args, **kwargs):
    print(titulo)

    print("Posicionales:", args)
    print("Con nombre:", kwargs)

saludar(
    "Datos",
    "Ana", "Pedro", "Luis", "Sandra",
    ciudad="Temuco",
    activo=True
)