'''
1. Qué debe tener cada clase:
Clase Motor:
● Atributos como tipo y potencia
● Método encender() que imprima un mensaje como “Motor encendido”
Clase Coche:
● Atributos como marca, modelo, y un atributo motor que será una instancia de la clase
Motor
● Método arrancar() que utilice el método encender() del motor asociado
2. Qué se debe probar:
● Crear un objeto Motor
● Crear un objeto Coche pasándole el motor como parámetro
● Llamar al método arrancar() y verificar que el coche use su motor correctamente
'''
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def encender(self): 
        print("Motor encendido")

    def __str__(self):
        return f"Motor --> tipo: {self.tipo} | potencia: {self.potencia}"


class Coche:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor #objeto Motor (colaboración)

    
    def arrancar(self):
        print(f"Arrancando coche {self.marca} {self.modelo}...")
        self.motor.encender()

    def __str__(self):
        return f"Coche: {self.marca} {self.modelo}"
    
    
#============== DEMO ==========================
print("==== Crear Motor ====")
motor1 = Motor("Gasolina", 120)

print("==== Crear Coche ====")
coche1 = Coche("Toyota", "Corolla", motor1)

print("==== Arrancar Coche ====")
coche1.arrancar()