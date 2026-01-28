"""
Demo de ENCAPSULAMIENTO:
El saldo se protege usando un atributo "privado" (__saldo) y solo
se puede modificar con métodos seguros.
"""

'''
Vamos a crear una clase que proteja el saldo del usuario 
y permita manipularlo solo mediante métodos seguros.

1. Definir clase CuentaBancaria con:
● Atributo privado __saldo
● Atributo público titular
● Atributo protegido _direccion
2. Crear métodos:
● depositar(monto): suma si el monto es válido
● retirar(monto): resta si hay suficiente saldo
● ver_saldo(): muestra el saldo actual
3. Mostrar que no se puede acceder a __saldo directamente
4. Usar los métodos para operar con seguridad
Objetivo: entender cómo proteger los datos internos del objeto y operar sobre ellos de forma
controlada.
'''

class CuentaBancaria:
    def __init__(self, titular, direccion, saldo=0):
        '''
        Atributo protegido (convención)

        ¿Qué significa?
        -NO es una protección real
        -Es una señal para el desarrollador tenga cuidado 
        al manipular este atributo
        '''
        self.titular = titular      #Público
        self._direccion = direccion #Protegido
        self.__saldo = saldo        #Privado  --> self._CuentaBancaria__saldo


    def depositar(self, monto):
        if monto <= 0:
            print("Monto inválido. Debe ser mayor a 0")
            return
        
        self.__saldo += monto
        print(f"Depósito realizado de manera correcta. Nuevo saldo: {self.__saldo}")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto inválido. Debe ser mayor a 0")
            return
        
        '''
        Opción 1:
            if monto <= self.__saldo:
                self.__saldo -= monto
                print(f"Retiro realizado de manera correcta. Nuevo saldo: {self.__saldo}")

            else:
                print(f"Saldo insuficiente, saldo actual: {self.__saldo}")
        '''

        '''
        Opción 2:
            if monto <= self.__saldo:
                self.__saldo -= monto
                print(f"Retiro realizado de manera correcta. Nuevo saldo: {self.__saldo}")
                return
        
            print(f"Saldo insuficiente, saldo actual: {self.__saldo}")
        '''

        if monto > self.__saldo:
            print(f"Saldo insuficiente, saldo actual: {self.__saldo}")
            return
        
        self.__saldo -= monto
        print(f"Retiro realizado de manera correcta. Nuevo saldo: {self.__saldo}")
            
        
    def ver_saldo(self):
        print(f"Saldo actual es de: {self.__saldo}")


cuenta1 = CuentaBancaria("Luis", "Avenida Siempreviva 742, Springfield")
cuenta1.depositar(100000)


#! PRUEBA DE atributos privados y protegidos
#print(cuenta1.__saldo)
cuenta1.__saldo = 350000 #Literalmente estamos creando un nuevo atributo
print(cuenta1.__saldo)

cuenta1.ver_saldo()

print(cuenta1._direccion)

'''
En Python, __saldo no es “privado de verdad” como en Java/C#. 
Es un mecanismo para evitar accesos accidentales, 
llamado name mangling (cambio de nombre).

Qué pasa realmente con __saldo

Cuando tú escribes dentro de la clase self.__saldo, 
Python lo renombra internamente a algo como:

self._CuentaBancaria__saldo

O sea, el atributo real se guarda con ese nombre “mangliado”.


cuenta.__saldo = 20000
print(cuenta.__saldo)


✅ NO da error, pero no estás modificando el saldo real.

Se crea un nuevo atributo llamado literalmente __saldo en el objeto, 
distinto del interno _CuentaBancaria__saldo.

Resultado:
cuenta.__saldo → es el “nuevo” que creamos
self.__saldo dentro de métodos → sigue usando _CuentaBancaria__saldo (el verdadero)

'''
#!============================================================================
print("============================")
cuenta1.retirar(200000)#supera el saldo
cuenta1.retirar(-200000)#monto inválido
cuenta1.retirar(35000)#retiro correcto