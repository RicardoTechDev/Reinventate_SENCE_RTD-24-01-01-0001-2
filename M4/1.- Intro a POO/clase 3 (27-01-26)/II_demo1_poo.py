'''
1. Definir la clase Auto con atributos marca, color, velocidad
2. Inicializar el objeto con velocidad en 0
3. Agregar método acelerar() que aumente la velocidad
4. Agregar método frenar() que la disminuya
5. Mostrar el estado del objeto antes y después de ejecutar métodos
6. Ver cómo cada objeto mantiene su propio estado independiente

Objetivo: entender cómo los métodos afectan el estado interno 
de un objeto a través de sus atributos.
'''

'''
self es una palabra que usamos dentro de una clase para referirnos 
al objeto actual (la instancia) que está usando el método.

Cuando haces persona1.presentarse(), por dentro Python llama algo como:
Persona.presentarse(persona1)

Entonces self “apunta” a persona1.

¿Para qué sirve?

1.- Acceder a los atributos del objeto
 * self.nombre, self.edad son los datos de ese objeto.

2.- Modificar el estado del objeto
* self.edad += 1 cambia la edad de ese objeto.

Idea clave
Cada objeto tiene sus propios valores, y self asegura que el método trabaje 
con los datos correctos (los del objeto que llamó al método).
'''

class Auto:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.velocidad = 0


    def acelerar(self,aumento):
        if aumento <= 0:
            print("El aumento de velocidad debe ser mayor a 0.")
            return
        self.velocidad += aumento 


    def frenar(self, disminucion):
        if disminucion <= 0:
            print("La disminución de velocidad debe ser mayor a 0.")
            return
        self.velocidad -= disminucion
        
        if self.velocidad < 0:
            self.velocidad = 0

    def mostrar_estado(self):
        print(f"Marca: {self.marca} | Color: {self.color} | Velocidad: {self.velocidad}")


auto1 = Auto("Toyota", "Blanco")
auto2 = Auto("Nissan", "Negro")

auto1.mostrar_estado()
auto2.mostrar_estado()
print("==================================")
auto1.acelerar(60)
auto2.acelerar(90)

auto1.mostrar_estado()
auto2.mostrar_estado()
print("==================================")
auto1.frenar(30)

auto1.mostrar_estado()
auto2.mostrar_estado()