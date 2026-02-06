'''
1) Función: calculadora de propina y total
Enunciado

Crea una función calcular_propina_total(monto_cuenta, porcentaje_propina=10) que:

* Reciba el monto de la cuenta y el porcentaje de propina (opcional).
* Valide que monto_cuenta > 0 y porcentaje_propina >= 0.
* Retorne una tupla: (propina, total).

Ejemplos de uso:

calcular_propina_total(20000)          # propina 10% por defecto
calcular_propina_total(20000, 15)      # propina 15%

'''


'''
2) Función: dividir cuenta entre amigos
Enunciado

Crea una función dividir_cuenta(total, personas) que:

* Reciba el total a pagar y la cantidad de personas.
* Valide que total > 0 y personas >= 1
* Retorne cuánto paga cada persona.

Ejemplos de uso:

dividir_cuenta(45000, 3)   # 15000
dividir_cuenta(10000, 1)   # 10000

'''


'''
3) Función: precio final con descuento
Enunciado

Crea una función aplicar_descuento(precio, porcentaje_descuento) que:

* Valide que precio > 0 y 0 <= porcentaje_descuento <= 100.
* Calcule el precio final y lo retorne.
* (Opcional) Retorne también el monto descontado.

Ejemplos de uso:

aplicar_descuento(20000, 25)
aplicar_descuento(10000, 0)

'''

'''
4) Función: convertir minutos a formato hh:mm
Enunciado

Crea una función minutos_a_hhmm(minutos) que:

* Reciba un entero minutos (>= 0).
* Convierta a horas y minutos.
* Retorne un string con formato "hh:mm" (dos dígitos).

Ejemplos de uso:

minutos_a_hhmm(135)   # "02:15"
minutos_a_hhmm(5)     # "00:05"

'''

'''
5) Función: prioridad de atención (triage básico)
Enunciado

Crea una función prioridad_atencion(temperatura, dificultad_respiratoria) que:

* Reciba temperatura (float) y dificultad respiratoria (bool).
* Retorne "ALTA", "MEDIA" o "BAJA" según reglas:
    - ALTA si dificultad_respiratoria es True o temperatura >= 39
    - MEDIA si 37.5 <= temperatura < 39
    - BAJA si temperatura < 37.5 y sin dificultad respiratoria

Ejemplos de uso:

prioridad_atencion(39.2, False)  # "ALTA"
prioridad_atencion(38.0, False)  # "MEDIA"
prioridad_atencion(36.8, False)  # "BAJA"
prioridad_atencion(36.8, True)   # "ALTA"

'''

'''
6) Función: calcular IMC y categoría
Enunciado

Crea una función calcular_imc(peso_kg, altura_m) que:

* Valide peso_kg > 0 y altura_m > 0.
* Calcule el IMC.
* Retorne una tupla (imc, categoria) con categorías:
    Bajo peso: < 18.5
    Normal: 18.5 a < 25
    Sobrepeso: 25 a < 30
    Obesidad: >= 30

Ejemplos de uso:

calcular_imc(70, 1.75)
calcular_imc(50, 1.70)

'''

'''
7) Función: detectar palíndromo (versión simple)
Enunciado

Crea una función es_palindromo(texto) que:

* Reciba un texto.
* Compare ignorando mayúsculas/minúsculas.
* Retorne True si es palíndromo, False si no.
* (Versión simple) No eliminar espacios ni tildes.

Ejemplos de uso:

es_palindromo("Radar")      # True
es_palindromo("Python")     # False

'''