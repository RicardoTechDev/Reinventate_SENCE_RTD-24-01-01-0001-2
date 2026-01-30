'''
Métodos de clase y métodos estáticos en Python

En Python, además de los métodos normales (que usan self), 
existen dos tipos especiales de métodos:

Métodos de clase → @classmethod
Métodos estáticos → @staticmethod

Se usan cuando no queremos trabajar con una instancia específica.
'''
#?==============================================================
'''
Método de instancia (repaso rápido)

👉 Es el que usa self
👉 Trabaja con los datos del objeto
'''
class Auto:
    def __init__(self, marca):
        self.marca = marca

    def mostrar(self):
        print(self.marca)

#? ✔ Necesita un objeto para ejecutarse
#? ✔ Modifica el estado del objeto


'''
2️⃣ Método de clase (@classmethod)
📌 Qué es

Está vinculado a la clase, no al objeto
Recibe cls en vez de self
Puede acceder a atributos de clase

📌 Para qué se usa

✔ Crear objetos de forma alternativa
✔ Modificar configuraciones comunes de los objetos
✔ Contar instancias
✔ Cambiar valores globales de la clase
'''
class Producto:
    impuesto = 0.19  # atributo de clase

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @classmethod
    def cambiar_impuesto(cls, nuevo_impuesto):
        cls.impuesto = nuevo_impuesto

Producto.cambiar_impuesto(0.21)


'''
3️⃣ Método estático (@staticmethod)
📌 Qué es

No usa self
No usa cls
No depende del estado del objeto ni de la clase

📌 Para qué se usa
✔ Validaciones
✔ Cálculos
✔ Funciones auxiliares relacionadas a la clase
'''
class Producto:

    @staticmethod
    def es_precio_valido(precio):
        return precio > 0

print(Producto.es_precio_valido(1000))
print(Producto.es_precio_valido(-500))

#?=================================================================

'''
¿cómo se cuando usar uno u otro?

🎯 La IDEA REAL (en simple)

Cuando estás escribiendo un método, pregúntate:

¿Este comportamiento pertenece a un objeto, a todos los objetos juntos, 
o a nadie en particular?

Según esa respuesta, eliges el tipo de método.
'''

'''

1️⃣ Método de instancia (self)

👉 Pertenece a UN objeto

Pregunta clave: “¿Necesito los datos de este objeto en particular?”

Si la respuesta es sí → método de instancia

Ejemplos

- Depositar en esta cuenta
- Acelerar este auto
- Calcular el precio final de este producto

📌 Usa self porque modifica ese objeto, no otro.
'''
def depositar(self, monto):
    self.saldo += monto



'''
2️⃣ Método de clase (cls)

👉 Pertenece a la CLASE completa

Pregunta clave: “¿Esto afecta o representa algo común a TODOS los objetos?”

Si la respuesta es sí → método de clase

Ejemplos

- Cambiar el IVA para todos los productos
- Llevar la cuenta de cuántos objetos existen
- Crear objetos de una forma alternativa

📌 No le hablas a un producto, le hablas al concepto Producto.
'''
@classmethod
def cambiar_iva(cls, nuevo_iva):
    cls.iva = nuevo_iva



'''

3️⃣ Método estático

👉 No pertenece a ningún objeto ni a la clase como estado

Pregunta clave: “¿Esto es solo una función útil relacionada con esta clase?”

Si la respuesta es sí → método estático

Ejemplos

- Validar si un precio es correcto
- Calcular descuento
- Revisar formato de datos

📌 No necesita self ni cls.
'''
@staticmethod
def precio_valido(precio):
    return precio > 0


#?====================== EJEMPLO COMPLETO ====================

class Producto:
    iva = 0.19

    def __init__(self, precio):
        self.precio = precio

    def precio_final(self):              # instancia
        return self.precio * (1 + Producto.iva)

    @classmethod
    def cambiar_iva(cls, nuevo_iva):     # clase
        cls.iva = nuevo_iva

    @staticmethod
    def precio_valido(precio):           # estático
        return precio > 0


'''
Cómo lo lees en voz alta:

precio_final → “el precio de ESTE producto”
cambiar_iva → “el IVA de TODOS los productos”
precio_valido → “una regla general”
'''