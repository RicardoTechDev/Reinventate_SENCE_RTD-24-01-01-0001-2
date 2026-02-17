'''
Vas a crear una clase Pato que herede métodos de dos clases distintas, 
y observarás cómo Python decide cuál
método usar si hay conflicto.

Clase Volador:
● Método: moverse() imprime "El pato vuela"
Clase Nadador:
● Método: moverse() imprime "El pato nada"
Clase Pato:
● Hereda de ambas: class Pato(Volador,
Nadador)
● No implementa moverse()

Qué se debe probar:
1. Crear un objeto Pato
2. Llamar a moverse()
3. Usar Pato.__mro__ o help(Pato)
para inspeccionar el orden de
búsqueda
4. Cambiar el orden de herencia
(class Pato(Nadador, Volador)) y
repetir
'''
class Volador:
    def moverse(self):
        print("El pato vuela")


class Nadador:
    def moverse(self):
        print("El pato nada")


class Pato(Nadador, Volador):
    pass


class Pato2(Volador, Nadador):
    pass

#=================== DEMO ============
pato = Pato()
pato.moverse()

print(Pato.__mro__) 
print(help(Pato))

pato2 = Pato2()
pato2.moverse()

print(Pato2.__mro__)