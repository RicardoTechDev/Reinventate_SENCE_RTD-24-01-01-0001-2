'''
1. Crear la clase Automovil con atributos internos: encendido, combustible, velocidad
2. Definir método encender() que:
● Verifique si hay combustible
● Cambie el estado encendido a True
● Muestre un mensaje al usuario
3. Definir método acelerar() que:
● Aumente la velocidad
● Reste combustible
● Muestre un mensaje amigable
4. Ocultar detalles internos (cálculos, chequeos, lógica condicional)
'''

class Automovil:
    def __init__(self, combustible):
        self.encendido = False
        self.combustible = combustible
        self.velocidad = 0

    def encender(self):
        if self.encendido:
            print("Ya estoy encendido...")
            return

        if self.combustible <= 0:
            print("No puedo encender: no hay combustible")
            return
        
        self.encendido = True
        print("brum brummmm: Automóvil encendido...")


    def acelerar(self, aumento):
        if not self.encendido:
            print("No estoy encendido, no puedo aumentar velocidad...")
            return
        
        if self.combustible <= 0:
            print("Sin combustible, no puedo acelerar...")
            self.encendido = False
            return

        if aumento <= 0:
            print("El aumento de velocidad debe ser mayor a 0.")
            return
        
        velocidad_aux = self.velocidad
        self.velocidad += aumento
        combustible_aux = self.combustible
        self.combustible -= 18

        if self.combustible <= 0:
            print("Sin combustible suficiente, no puedo acelerar...")
            print(f"Se intento acelerar {aumento} pero sólo había {combustible_aux} de combustible")
            self.combustible = combustible_aux
            self.velocidad = velocidad_aux
            return

        print(f"Acelerando... Velocidad actual: {self.velocidad} k/m | Combustible: {self.combustible}")
        


auto1 = Automovil(20)
auto1.encender()
auto1.acelerar(80)
auto1.encender()     
auto1.acelerar(50)   
        

auto1.velocidad(200)