"""
ANTES QUE TODO CÓMO CORRER UN CÓDIGO PYTHON 

IMPORTANTE (VS Code):
Si tu programa usa input(), debes ejecutar en TERMINAL.
- Activa: Code Runner: Run In Terminal
- O usa: Python: Run Python File in Terminal


Configurar Code Runner para usar Terminal

Ve a Settings (Ctrl + ,)
Busca: Code Runner: Run In Terminal
Actívalo ✅

File → Preferences → Settings

(Alternativa: en settings.json)
"code-runner.runInTerminal": true
"""

#Clase: Sintaxis de Python

#Objetivos:
#- Comprender reglas básicas de escritura de Python
#- Usar comentarios, indentación y variables 
#- Reconocer tipos de datos y conversiones (parseo/casteo)
#- Operadores


# ============================================================
# 0) RECORDATORIOS IMPORTANTES (TEORÍA)
# ============================================================

"""
1) Lenguaje interpretado: se ejecuta línea a línea (sin compilar).
2) Multiparadigma: estructurada, POO y funcional.
3) Sintaxis simple y legible: fácil de leer y aprender.
4) Tipado dinámico: no declaras tipos, Python los asigna según el valor.
5) Bloques con indentación (en vez de llaves {}).
6) Convención snake_case para variables/funciones. (nombre_variable)
7) Comentarios con # para documentar.
8) Estructuras de control simples: if, for, while.
"""

# ============================================================
# 1) ¿QUÉ ES SINTAXIS?
# ============================================================
"""
La sintaxis de un lenguaje de programación es el conjunto de reglas 
que indican cómo se debe escribir correctamente el código 
para que el computador lo pueda entender y ejecutar.

👉 Es muy parecido a las reglas de la gramática en un idioma.
📘 Ejemplo con lenguaje humano

Ejemplo (idea):
✅ “Yo estudio Python.”
❌ “Estudio yo Python.” (suena raro o confuso)
"""

# ============================================================
# 2) PYTHON VS OTROS LENGUAJES (EJ. JavaScript)
# =======================================================

'''
Ejemplo Js

let num = 5

if(num < 10){
    console.log("El número es mayor a 10");
}else{
    console.log("El número no es mayor a 10);
}

'''

num = 5

if num < 10:
    print("El número es mayor a 10")
    if num > 15:
        print("")
        if num < 8: 
            print("")
else:
    print("El número no es mayor a 10")

# ============================================================
# 3) COMENTARIOS
# ============================================================
"""
Un comentario en Python es un texto que el programador escribe dentro 
del código para explicar lo que hace, pero que Python no ejecuta ni toma en cuenta.

👉 Sirve para entender el código, no para que el programa haga algo.

Un comentario es una nota dentro del código, como escribir algo al margen del cuaderno.
El computador lo lee pero lo ignora.


Tipos:
- 1 línea: # comentario
- “multilínea”: usando triple comillas (""" """ o ''' '''),
Se usa para explicar bloques grandes de código. (técnicamente es un string, pero se usa para explicar)
"""

#Comentario de una línea
print("Hola")#comentario final de línea

"""
Cometario multilínea
lo podemos excribir
de esta forma
"""

'''
Cometario multilínea
lo podemos excribir
de esta forma
'''

'''
✅ ¿Para qué sirven los comentarios?

Explicar qué hace el código
Recordar para qué sirve una parte
Ayudar a otros (o a ti mismo en el futuro)
Enseñar programación
'''

# --- Extensiones útiles (VS Code) ---
#1.- Better Comments (visual): TODO, !, ?, *...
# TODO: Validar que la edad sea mayor a 0
# ! OJO: Esto puede fallar si el usuario escribe texto
# ? Pregunta: ¿Qué pasa si no escribe nada?
# * Tip: Usa int() para convertir a número
# // Nota: Esto es un comentario normal (depende de tu config)
# FIX: Corregir el cálculo del descuento

#2.- Python extension: ejecutar, autocompletar, debug, etc.
#3.- SonarLint O SonarQube: calidad del código 
#    (revisa tu código mientras lo escribes y te avisa de malas prácticas, seguridad, código poco claro o desordenado)
#4.- Error Lens: errores visibles en la misma línea
#5.- Indent-Rainbow: colorea niveles de indentación

# ============================================================
# 4) INDENTACIÓN (MUY IMPORTANTE EN PYTHON)
# ============================================================
'''
La indentación en Python es fundamental para estructurar el código, ya que reemplaza el uso de
llaves {} o palabras clave. Cada bloque de código dentro de estructuras como funciones, bucles y
condiciones debe estar correctamente indentado para que el intérprete entienda la jerarquía de
instrucciones.

Reglas de Indentación
✔ Definición de bloques con indentación en lugar de llaves {}.
✔ Se recomienda usar cuatro espacios por nivel de indentación.
✔ Evitar mezclar espacios y tabulaciones, ya que puede generar errores de sintaxis.
✔ La indentación mejora la claridad, legibilidad y mantenimiento del código.

'''

#* ✅ Indentación correcta
edad = 17

if edad >= 18:
    print("Es mayor de edad")
    print("Puede entrar")
else:
    print("Es menor de edad")
    print("NO puede entrar")

#! ❌ Indentación errónea (NO ejecutar: ejemplo para mostrar el error)
edad = 17

# if edad >= 18:
# print("Es mayor de edad")
#     print("Puede entrar")
# else:
# print("Es menor de edad")
#     print("NO puede entrar")

# ============================================================
# 5) VARIABLES
# ============================================================
"""
Qué son las variables en Python?

Las variables en Python son espacios en la memoria donde se guardan datos, 
y a esos espacios les damos un nombre para poder usarlos después.

👉 En palabras simples:
una variable es una cajita con nombre que guarda información.

Imagina una caja con una etiqueta.
La etiqueta es el nombre de la variable y lo que hay dentro es el dato.


✅ Nombres de Variables en Python


En Python, los nombres de las variables deben seguir ciertas reglas y convenciones para garantizar
un código claro, compatible y fácil de entender.

Reglas y buenas prácticas

→ Inicio válido: Debe comenzar con una letra o _, pero no con un número.
→ Caracteres permitidos : Puede contener letras, números y _, pero no espacios ni caracteres especiales.
→ Sensibilidad a mayúsculas y minúsculas : variable y Variable son diferentes.
→ Convención snake_case: Se recomienda usar nombres descriptivos (nombre_variable).
→ Evitar palabras reservadas : No usar nombres como if, for, while, return, etc.

"""

# --- Declaración (opcional con type hints), inicialización y asignación ---
#*Declaración: no es necesario/obligatorio indicar el tipo de dato, 
#* pero podemos hacer un simulación de declaración

altura : float
altura = 1.67

#* Inicialización: Asignar un valor inicial al momento de crear la variable
nombre = "Ana"
edad = 29

#* Asignación: Cambiar el valor de una variable ya existente
altura = 1.78

#? Otra forma de inicializar
hobby1, hobby2, hobby3 = "Leer", "Dormir", "Comer"
nombre, edad, direccion = "Luis", 31, "Siempre viva"

'''
hobby1 = "Leer"
hobby2 = "Dormir"
hobby3 = "Comer"
'''

nombre_usuario = nombre_cliente = nombre_venta = "Ricardo"

print(hobby1, hobby2, hobby3)
print(nombre, edad, direccion)
print(nombre_usuario, nombre_cliente, nombre_venta)


#* ✅ Ejemplos de variables en Python

#* 🔹 1. Inicio válido (letra o _)
edad = 12
nombre = "Ana"
_altura = 1.68
contador1 = 0

#! Incorrectos
1edad = 12
2nombre = "Ana"

#* 🔹 2. Caracteres permitidos (letras, números y _)
nombre_alumno = "Pedro"
nota_final = 6.7
total_puntos_paes = 825

#! Incorrecta
nombre-alumno = "Pedro"
nota final = 6.5
total$puntos = 120

#* 🔹 3. Sensibilidad a mayúsculas y minúsculas
edad = 10
Edad = 15 #mala práctica primera letra mayúscula

#? Nota: para declarar variables globales es buena práctica usar sólo mayúsculas
PESO_EN_MARTE = 0.81

#* 🔹 4. Convención snake_case (recomendada)
#*Usar nombres claros y descriptivos de lo que almacenan
nombre_estudiante = "Camila"
promedio_notas = 6.2
cantidad_asistencias = 18
es_mayor_de_edad = False
precio_total_compra = 12500

#! Poco recomendada
n = "Camila"
x1 = 6.2
e = 25

#* 🔹 5. Evitar palabras reservadas
#! No se puede usar
# if = 10
# for = "Hola mundo"
# while = "569123456678"
# retunr = "dato"        

'''
================== 🧩 Resumen corto nombre de variables =====================
📌 Buenas prácticas al nombrar variables en Python:

Usar letras, números y _
No comenzar con números
Usar minúsculas y snake_case
Usar nombres claros y descriptivos
No usar palabras reservadas
'''

# ============================================================
# 6) TIPOS DE DATOS (BÁSICOS Y OTROS)
# ============================================================
#* Básicos
nombre = "Diego"     #str
edad = 12            #int
altura = 1.62        #float
es_estudiante = True #bool

#* Avanzados
#* Lista -> list
# - Guarda varios datos en una sola variable
# - Es ordenada (mantiene el orden de los elementos)
# - Es modificable (se pueden agregar, cambiar o eliminar elementos)
notas = [6.0, 5.4, 4.0, "hola"]

#* Diccionario -> dict
# - Guarda datos en pares clave : valor
# - Permite acceder a los valores usando la clave
# - Es muy útil para representar objetos o personas
alumnos = {
    "nombre": "Sofia",
    "edad": 28,
    "direccion": "lasdasdlasd"
}

print(alumnos["nombre"])

#* Tupla -> tuple
# - Guarda varios datos como una lista
# - No se puede modificar (es inmutable)
# - Se usa cuando los datos no deben cambiar
dias = ("lunes", "martes")# 🔹 Similar a lista, pero no se modifica ES INMUTABLE.

#* Conjunto -> set
# - No permite elementos repetidos
# - No mantiene un orden fijo
# - Es útil para eliminar duplicados
numeros = {1,2, 3, 3, 3}
print(numeros)

#* Valor vacío -> NoneType
# - Representa la ausencia de un valor
# - Se usa cuando una variable aún no tiene dato
# - No es lo mismo que 0 ni una cadena vacía
resultado = None # != 0 y != ""

#* Número complejo -> complex
# - Tiene una parte real y una imaginaria
# - Se escribe usando la letra j
# - Se usa en cálculos matemáticos avanzados
valor = 2 + 3j

print(type(notas))
print(type(alumnos))
print(type(dias))
print(type(numeros))
print(type(resultado))
print(type(valor))

# ============================================================
# 7) PARSEO VS CASTEO
# ============================================================
"""
🧠 Diferencia entre parseo y casteo
Parseo: convertir TEXTO a un valor interpretable.
Ej: "12" -> 12 (int)

Casteo: convertir un tipo a otro.
Ej: 3 (int) -> "3" (str) o 3 -> 3.0 (float)
"""

#* Parseo
#*El parseo ocurre cuando tomamos un texto (str) 
#* y lo interpretamos para obtener un valor con significado (número, fecha, etc.).'''
edad_texto = "12"
edad_num = int(edad_texto)
print(edad_texto, type(edad_texto))
print(edad_num, type(edad_num))

#* Casteo
#* El casteo es cambiar el tipo de un dato a otro, aunque ya sea un valor válido.
texto_x = str(3)
print(texto_x, type(texto_x))

# ============================================================
# 8) ENTRADA Y SALIDA DE DATOS (input / print)
# ============================================================
edad_usuario = int(input("Ingrese la edad :"))
print(edad_usuario, type(edad_usuario))


# ============================================================
# 9) OPERADORES (pendiente para la siguiente parte)
# ============================================================

#* 1. Operadores Aritméticos
a = 10
b = 3

print(a + b) # Suma → 13
print(a - b) # Resta → 7
print(a * b) # Multiplicación → 30
print(a / b) # División → 3.333...
print(a // b) # División entera → 3
print(a % b) # Módulo (resto) → 1
print(a ** b) # Potencia → 1000

#* 2. Operadores Relacionales (o de comparación)
x = 5
y = 10

print(x == y) # Igualdad → False
print(x != y) # Distinto → True
print(x > y )  # Mayor que → False
print(x < y) # Menor que → True
print(x >= 5) # Mayor o igual → True
print(y <= 8) # Menor o igual → False


#* 3. Operadores Lógicos
edad = 20 
tiene_permiso = True

print(edad >= 18 and tiene_permiso) #True
print(edad >= 18 or tiene_permiso) #True
print(not tiene_permiso) #False

#* 4. Operadores de Asignación
num = 10
num += 5 #num +5 -> 10+5= 15
num -= 3 # 15-3 = 12
num *= 2 # num * 2 -> 12 * 2= 24
num /= 4 # num = num / 4 -> 24/4 = 6

print(num)

#* 5. Operadores de Incremento / Decremento
#! Incorrecto en Python
# i++
# i--

i = 5

#incremento
i += 1

#decremento
i -= 1

#* 6. Operadores de Concatenación
#*Se usan para unir textos (strings).
nombre = "Ana"
apellido = "Perez"

nombre_completo = nombre + " " + apellido
print(nombre_completo)

mensaje = "Hola"
mensaje += " mundo"
print(mensaje)

#f-string (interpolación)
nombre_comple_alumno = f"{mensaje} mundo"
print(nombre_comple_alumno)
