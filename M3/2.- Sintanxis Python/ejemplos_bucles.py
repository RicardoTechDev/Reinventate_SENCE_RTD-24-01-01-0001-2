#1.- Básico : imprime todos los enteros del 0 al 150.
print("Enteron del 0 al 150")
for num in range(0, 151):
    print(num)

#2.- Múltiplos de cinco : imprime todos los múltiplos de 5, de 5 a 1,000
print("Múltiplos de 5")
for num in range(5, 1001, 5):
    print(num)

#3.- Contar, Ecas Way - imprime enteros del 1 al 100. Si es divisible por 5, 
# imprima "Ecas" en su lugar. Si es divisible por 10, imprima "Ecas OTEC".
print("Enteros del 1 al 100")
for numero in range(1, 101):
    if numero%10 ==  0 :
        print("Ecas OTEC")
    elif numero%5 ==  0 :
        print("Ecas")
    else :
        print(numero)