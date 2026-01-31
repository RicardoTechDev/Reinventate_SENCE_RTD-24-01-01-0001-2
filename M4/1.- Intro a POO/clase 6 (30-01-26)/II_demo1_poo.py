'''
Vas a crear una clase donde el método saludar() pueda comportarse de distintas formas según cuántos
parámetros reciba.

1. Qué debe tener la clase:
a. Atributo público: nombre
b. Método saludar() que:
c. Si no recibe parámetros → imprime: "Hola"
d. Si recibe 1 parámetro → imprime: "Hola, [nombre]"
e. Si recibe 2 parámetros → imprime: "Hola, [nombre] de [ciudad]"
f. Usar *args y condicionales para manejar los diferentes casos
2. Qué se debe probar:
a. Llamar a saludar() sin argumentos
b. Llamar a saludar("Lucía")
c. Llamar a saludar("Lucía", "Córdoba")
d. Manejar correctamente si se pasan más de 2 argumentos (opcional)
'''

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre #atributo público

    
    def saludar(self, *args, **kwargs):#*args lo recibe como tupla con ()
        largo = len(args)
        
        if largo == 0:
            print("Hola")

        elif largo == 1:
            print(f"Hola, {args[0]}")

        elif largo == 2:
            print(f"Hola, {args[0]} de {args[1]}")

        else:
            print("Máximo 2 argumentos")

        print(kwargs)

#?===================== DEMO ===========================
persona = Persona("Arsenio")

print("==== Sin argumentos ===")
persona.saludar()

print("==== con un argumento ===")
persona.saludar("Ana")

print("==== con dos argumentos ===")
persona.saludar("Lucía", "Córdoba")

print("==== prueba con más de 2 ===")
persona.saludar("Lucía", "Córdoba", nombre2 = "Ana", edad=25)