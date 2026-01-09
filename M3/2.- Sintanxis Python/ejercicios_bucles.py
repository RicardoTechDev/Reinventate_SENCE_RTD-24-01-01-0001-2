'''
1) Suma de múltiplos de 3 (0 a 300)
Enunciado: Suma todos los números entre 0 y 300 que sean múltiplos de 3 
e imprime la suma final.
'''
#1° OPCIÓN
suma = 0
for i in range(0, 301, 3):  
    suma += i 
print("La suma es:", suma) 

#2° Opción
suma = 0
for i in range(301):  # se itera desde la posición 0 a 301
    if i % 3 == 0:    # 
        suma += i     
print("La suma es:", suma)

#3° Opción
suma = 0
i = 0
while i <= 300:
    suma += i
    i += 3   
print("La suma es:", suma)


'''
2) Suma de los números que terminan en 7

Enunciado: Suma los números del 1 al 200 que terminan en 7 (7, 17, 27, …, 197) 
y muestra la suma.
'''
#1° OPCIÓN
suma= 0

for num in range(1, 201):
    if num % 10==7:
        suma +=num
print(suma)

#2° OPCIÓN
suma = 0
for i in range(7,201, 10):
    suma +=i
    print(i)
print("La suma es:", suma)

#3° OPCIÓN
suma = 0
i = 7
while i <= 200:
    suma += i
    print(i)
    i += 10  
print("La suma es:", suma)


'''
3) “Fizz” y “Buzz” (1 a 60)

Enunciado: Imprime del 1 al 60.

Si es divisible por 3, imprime "Fizz"
Si es divisible por 4, imprime "Buzz"
Si es divisible por 3 y 4, imprime "FizzBuzz"
Si no, imprime el número.
'''
#1° OPCIÓN
print("Numeros del 1 al 60")
for numero in range(1, 61):
    if numero % 3 == 0 and numero % 4 == 0:
        print(f"FizzBuuzz {numero}")
    elif numero % 4 == 0:
        print(f"Buzz {numero}")
    elif numero % 3 == 0:
        print(f"Fizz {numero}")
    else:
        print(numero)

#2° OPCIÓN
i = 1

while i <= 60:
    if i % 3 == 0 and i % 4 == 0:
        print("FizzBuzz", i)
    elif i % 4 == 0:
        print("Buzz", i)
    elif i % 3 == 0:
        print("Fizz", i)
    else:
        print(i)
    i += 1

'''
4) Contar cuántos son pares e impares

Enunciado: Recorre del 1 al 100 y cuenta cuántos números son pares 
y cuántos son impares. Muestra los totales.
'''
par = 0
impar = 0

for num in range(1, 101):
    if num %2==0:
        par +=1
    else :
        impar +=1
print(f"cantidad pares {par} cantidad impares {impar}")