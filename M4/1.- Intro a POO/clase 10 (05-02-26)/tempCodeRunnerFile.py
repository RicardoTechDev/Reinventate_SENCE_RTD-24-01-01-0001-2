def mezclar_textos(*args, separador=" ", mayus=False):
    # Si no se reciben textos
    if len(args) == 0:
        return "Sin textos"

    # Unir los textos usando el separador
    # resultado = separador.join(args)
    resultado = ""
    for i, texto in enumerate(args):
        if i > 0:
            resultado += separador
        resultado += texto

    # Convertir a mayúsculas si corresponde
    if mayus:
        resultado = resultado.upper()

    return resultado



print(mezclar_textos("hola", "mundo")) # hola mundo
print(mezclar_textos("hola", "mundo", separador="-")) # hola-mundo
print(mezclar_textos(mayus=True)) # Sin textos
print(mezclar_textos("python", "es", "genial", mayus=True)) # PYTHON ES GENIAL