'''
Reutilizar la clase Persona con atributos nombre y edad
2. Crear dos objetos distintos: persona1 y persona2
3. Ver cómo cada objeto tiene su estado individual
4. Modificar el atributo edad de uno de los objetos
5. Verificar que los cambios en un objeto no afectan al otro

7. Mostrar que no todos los objetos tienen por qué tener los mismos atributos si se agregan
dinámicamente
'''
from objeto_persona import Persona

persona1 = Persona("Luis", 21)
persona2 = Persona("Alberto", 32)

persona1.presentarse()
persona2.presentarse()

persona1.edad += 1
persona1.nombre += " Salazar"
persona1.presentarse()
persona2.presentarse()
