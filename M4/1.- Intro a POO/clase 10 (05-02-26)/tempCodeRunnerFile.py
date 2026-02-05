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