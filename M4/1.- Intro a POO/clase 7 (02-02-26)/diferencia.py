'''
🔗 Diferencia entre colaboración y composición

Ambas hablan de cómo se relacionan los objetos, 
pero no es lo mismo “usar” que “estar hecho de”.

🧩 Colaboración (uso)
🧠 Idea clave

👉 Un objeto usa a otro para hacer algo.

El objeto no depende totalmente del otro

Puede funcionar aunque el otro no exista

El objeto colaborador se puede cambiar fácilmente

📦 Ejemplo mental

Un auto y una llave inglesa
El auto usa la llave, pero no está hecho de ella.
'''

class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def arrancar(self, motor):
        motor.encender()

#*📌 El coche recibe el motor y lo usa → colaboración.

'''
🧱 Composición (estructura)
🧠 Idea clave

👉 Un objeto está compuesto por otros objetos.

Las partes son esenciales

Si el objeto principal desaparece, sus partes también

No tiene sentido sin sus componentes

📦 Ejemplo mental

Un auto y su motor
Un auto está hecho de un motor.
'''

class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self):
        self.motor = Motor()  # creado dentro

    def arrancar(self):
        self.motor.encender()

#*📌 El coche contiene el motor → composición.

'''
| Aspecto            | Colaboración     | Composición            |
| ------------------ | ---------------- | ---------------------- |
| Tipo de relación   | Débil / flexible | Fuerte / estructural   |
| Idea               | “Usa a otro”     | “Está hecho de”        |
| Dependencia        | Baja             | Alta                   |
| Vida de las partes | Independiente    | Depende del contenedor |
| Ejemplo            | Auto usa un GPS  | Auto tiene motor       |


🧠 Frase clave para memorizar (💎)

Colaboración = usar
Composición = estar hecho de


🎓 Regla práctica (para pruebas)

Pregúntate:

❓ ¿Este objeto tiene sentido sin el otro?

Sí → colaboración
No → composición


'''

