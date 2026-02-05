'''
Función suelta #1: mezclar_textos()

Objetivo: practicar *args + defaults + condicionales.

Enunciado
Crea una función mezclar_textos(*args, separador=" ", mayus=False) que:

* Reciba cualquier cantidad de textos (strings) por *args.
* Si no recibe textos, debe retornar "Sin textos".
* Una los textos usando el separador.
* Si mayus=True, el resultado debe quedar en mayúsculas.
* Retorne el texto final.

Casos de prueba esperados:
* mezclar_textos("hola", "mundo") → "hola mundo"
* mezclar_textos("hola", "mundo", separador="-") → "hola-mundo"
* mezclar_textos(mayus=True) → "Sin textos"
'''

'''
Función suelta #2: calcular_area()

Objetivo: practicar “sobrecarga” con **kwargs.

Enunciado

Crea una función calcular_area(**kwargs) que calcule el área según los datos entregados:
* Si llega radio=... → área del círculo.
* Si llega base=... y altura=... → área del triángulo.
* Si llega ancho=... y alto=... → área del rectángulo.
* Si no coincide con ninguno, debe retornar None y mostrar "Datos insuficientes".
* Validar que los valores sean positivos.

Casos de prueba esperados:
* calcular_area(radio=3) → 28.27...
* calcular_area(base=10, altura=5) → 25
* calcular_area(ancho=4,
'''

'''
POO #1: Clase Reproductor (playlist)

Objetivo: composición + “sobrecarga” por *args + __str__.

Enunciado

Crea estas clases:

1) Cancion
* Atributos: titulo, artista, duracion_seg
* Implementa __str__ para mostrar: "Título - Artista (mm:ss)"

2) Playlist (composición)
* Contiene una lista de canciones (parte esencial)
* Método agregar(cancion)

3) Reproductor (colaboración)
* Tiene un método reproducir(playlist, *args) que funcione así:
    - Sin args → reproduce “toda la playlist” (imprime cada canción)
    - 1 arg (n) → reproduce las primeras n canciones
    - 2 args (inicio, fin) → reproduce desde inicio hasta fin (inclusive)
    - Si args inválidos → error

Condiciones
* Validar rangos (inicio/fin no pueden salir del tamaño de la playlist)
* No usar librerías
'''


'''
POO #2: Clase Tarea y Agenda (organizador)

Objetivo: @classmethod, @staticmethod, atributo de clase, “sobrecarga” con defaults + **kwargs.

Enunciado

Crea estas clases:

1) Tarea
* Atributos: titulo, prioridad (1 a 5), hecha (bool)
* Atributo de clase: prioridad_por_defecto = 3
* @staticmethod prioridad_valida(p) → retorna True si está entre 1 y 5
* @classmethod cambiar_prioridad_defecto(nueva) → cambia la prioridad por defecto si es válida
* Implementa __str__ para mostrar:
    - "[ ] Título (prio X)" si no está hecha
    - "[x] Título (prio X)" si está hecha

2) Agenda (composición)
* Contiene una lista de tareas
* Método agregar(titulo, **kwargs) que simule sobrecarga:
    - Si kwargs trae prioridad, úsala (validándola)
    - Si no trae, usar Tarea.prioridad_por_defecto
    - Si trae hecha=True/False, asignarla (si no, False)

* Método marcar_hecha(indice) para marcar una tarea como lista
* Método mostrar() para imprimir todas

Casos de prueba esperados:
* Cambiar prioridad por defecto a 5 y agregar tareas sin prioridad
* Agregar tarea con prioridad inválida (debe rechazar o corregir)
* Mostrar agenda con __str__
'''