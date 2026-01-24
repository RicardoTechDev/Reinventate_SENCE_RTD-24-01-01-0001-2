def sumar_hasta(n):
    suma = 0
    for _ in range(0, n):#3
        print(n)#1
        suma += n# 9 + 1 --> 10 
        n -= 1#1 - 1 ---> 0 
    return suma

print(sumar_hasta(4)) 