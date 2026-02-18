'''
¿En qué consistirá la Demo?
Vas a abrir un archivo nuevo, escribir texto línea por línea 
con write() y luego usar writelines() para agregar más
líneas.
ur
1. Abrir un archivo llamado
"demo_escrita.txt" en modo "w"
2. Escribir un par de líneas usando write()
3. Crear una lista de textos y escribirla
usando writelines()
4. Cerrar automáticamente el archivo usando
with open()

Qué observar:
● write() necesita agregar manualmente \n
para los saltos de línea
● writelines() escribe todos los elementos tal
como están, no agrega saltos de línea
automáticamente
'''

with open("demo_escritura.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Línea 1 escrita con write\n")
    archivo.write("Línea 2 escrita con write\n")

    lineas = [
        "Línea 3 escrita con write\n",
        "Línea 4 escrita con write\n",
        "Línea 5 escrita con write\n"
    ]

    archivo.writelines(lineas)

    print(archivo.closed)