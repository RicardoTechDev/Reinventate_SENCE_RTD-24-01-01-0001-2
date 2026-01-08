# ============================================================
# CONDICIONALES EN PYTHON (if / elif / else)
# ============================================================
'''
Las condicionales permiten a los programas tomar
decisiones y ejecutar diferentes acciones en función de
ciertas condiciones. Estas condiciones se expresan en
forma de expresiones booleanas que se evalúan como
VERDADERO o FALSO.
'''

'''
¿Qué es una condición?
Una condición es una expresión que se evalúa como:

True (verdadero)
False (falso)
'''

edad = 18
print(edad>=18) #True

#* ====== Estructura if ===================
edad = 20

if edad >= 18:
    print("Eres mayor de edad")    

#?📌 Reglas clave:
''' 
- if termina con :
- El bloque va indentado
- Se ejecuta solo si la condición es verdadera
'''

#* ============ if – else =================
edad = 15

if edad >= 18:
    print("Eres mayor de edad") 
else:
    print("Eres menor de edad")       

#* =========== if – elif – else ==================
nota = 5.5

if nota >= 6.0:
    print("Exceclente Nota")
elif nota >= 5.0:
    print("Aprobado")
elif nota >= 5.5:
    print("Aprobado")
elif nota >= 4.0:
    print("Apenas aprobado")
else:
    print("Reprobado")

#? 📌 Python evalúa de arriba hacia abajo y entra solo en un bloque

#* ================ Condiciones con operadores lógicos ===============
edad = 20
tiene_permiso = True

#? and → ambas verdaderas
if edad >= 18 and tiene_permiso:
    print("Es mayor de edad y tiene permiso, puede ingresar")
else:
    print("no puede ingresar")

edad = 16
tiene_permiso = True

#? or → al menos una verdadera
if edad >=18 or tiene_permiso:
    print("Puede ingresar")

tiene_permiso = False

if (not tiene_permiso): # ---> True
    print("No tiene permiso para ingresar")

#* Ejemplo combinado (and + or + not)
edad = 17
tiene_permiso = True
esta_suspendido = False
#!      F      or   T   = True   and   ~F --> True  ======> True
if (edad >= 18 or tiene_permiso) and not esta_suspendido:
    print("Puede ingresar")