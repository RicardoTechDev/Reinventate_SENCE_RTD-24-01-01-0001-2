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

def mezclar_textos(*args, separador=" ", mayus=False):
    # Si no se reciben textos
    if len(args) == 0:
        return "Sin textos"

    # Unir los textos usando el separador
    # resultado = separador.join(args)
    resultado = ""
    for i, texto in enumerate(args):
        if i > 0:
            resultado += separador
        resultado += texto

    # Convertir a mayúsculas si corresponde
    if mayus:
        resultado = resultado.upper()

    return resultado



print(mezclar_textos("hola", "mundo")) # hola mundo
print(mezclar_textos("hola", "mundo", separador="-")) # hola-mundo
print(mezclar_textos(mayus=True)) # Sin textos
print(mezclar_textos("python", "es", "genial", mayus=True)) # PYTHON ES GENIAL



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
* calcular_area(ancho=4, alto=6)
'''
def calcular_area(**kwargs):
    import math  # solo para pi

    # Área del círculo
    if "radio" in kwargs:
        radio = kwargs.get("radio")
        if radio <= 0:
            print("El radio debe ser positivo.")
            return None
        return math.pi * radio ** 2

    # Área del triángulo
    elif "base" in kwargs and "altura" in kwargs:
        base = kwargs.get("base")
        altura = kwargs.get("altura")
        if base <= 0 or altura <= 0:
            print("Base y altura deben ser positivas.")
            return None
        return (base * altura) / 2

    # Área del rectángulo
    elif "ancho" in kwargs and "alto" in kwargs:
        ancho = kwargs.get("ancho")
        alto = kwargs.get("alto")
        if ancho <= 0 or alto <= 0:
            print("Ancho y alto deben ser positivos.")
            return None
        return ancho * alto

    # Caso inválido
    else:
        print("Datos insuficientes")
        return None

print(calcular_area(radio=3)) # 28.27...
print(calcular_area(base=10, altura=5)) # 25.0
print(calcular_area(ancho=4, alto=6))# 24
print(calcular_area(base=10))# Datos insuficientes # None
print(calcular_area(radio=-2))# El radio debe ser positivo. # None


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
class Cancion:
    def __init__(self, titulo, artista, duracion_seg):
        self.titulo = titulo
        self.artista = artista
        self.duracion_seg = duracion_seg

    def __str__(self):
        # Convertir segundos a mm:ss (sin librerías)
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{self.titulo} - {self.artista} ({minutos:02d}:{segundos:02d})"


class Playlist:
    # Composición: la playlist "tiene" canciones
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar(self, cancion):
        # Validación simple: debe ser un objeto Cancion
        if not isinstance(cancion, Cancion):
            print("Solo puedes agregar objetos de tipo Canción.")
            return False
        self.canciones.append(cancion)
        return True

    def cantidad(self):
        return len(self.canciones)


class Reproductor:
    # Colaboración: el reproductor "usa" una playlist para reproducir
    def reproducir(self, playlist, *args):
        if not isinstance(playlist, Playlist):
            print("Debes pasar un objeto Playlist.")
            return

        total = playlist.cantidad()

        if total == 0:
            print("Playlist vacía.")
            return

        # Caso A: sin args -> reproduce todo
        if len(args) == 0:
            inicio = 0
            fin = total - 1

        # Caso B: 1 arg -> primeras n canciones
        elif len(args) == 1:
            n = args[0]
            if not isinstance(n, int) or n <= 0:
                print("Error: n debe ser un entero mayor a 0.")
                return

            if n > total:
                n = total  # se ajusta al máximo disponible
            inicio = 0
            fin = n - 1

        # Caso C: 2 args -> rango inicio-fin (inclusive)
        elif len(args) == 2:
            inicio = args[0]
            fin = args[1]

            if not isinstance(inicio, int) or not isinstance(fin, int):
                print("Error: inicio y fin deben ser enteros.")
                return

            if inicio < 0 or fin < 0:
                print("Error: inicio y fin no pueden ser negativos.")
                return

            if inicio > fin:
                print("Error: inicio no puede ser mayor que fin.")
                return

            if fin >= total or inicio >= total:
                print("Error: inicio/fin fuera de rango de la playlist.")
                return

        # Caso D: inválido
        else:
            print("Error: máximo 2 parámetros (n) o (inicio, fin).")
            return

        # Reproducir
        print(f"\nReproduciendo playlist: {playlist.nombre}")
        print(f"Rango: {inicio} a {fin} (total canciones: {total})")
        print("-" * 35)

        for i in range(inicio, fin + 1):
            print(f"{i}. {playlist.canciones[i]}")

        print("-" * 35)
        print("Fin reproducción\n")



# Crear canciones
c1 = Cancion("Blinding Lights", "The Weeknd", 200)
c2 = Cancion("Imagine", "John Lennon", 183)
c3 = Cancion("Shape of You", "Ed Sheeran", 234)
c4 = Cancion("Viva La Vida", "Coldplay", 242)

# Crear playlist y agregar canciones (composición)
pl = Playlist("Favoritas")
pl.agregar(c1)
pl.agregar(c2)
pl.agregar(c3)
pl.agregar(c4)

# Reproductor (colaboración)
r = Reproductor()

# 1) Sin args: todo
r.reproducir(pl)

# 2) Con 1 arg: primeras n
r.reproducir(pl, 2)

# 3) Con 2 args: rango inicio-fin
r.reproducir(pl, 1, 3)

# Errores típicos
r.reproducir(pl, 0)        # n inválido
r.reproducir(pl, 3, 10)    # fuera de rango
r.reproducir(pl, 2, 1)     # inicio > fin
r.reproducir(pl, 1, 2, 3)  # demasiados args





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

class Tarea:
    # Atributo de clase (parámetro de clase)
    prioridad_por_defecto = 3

    def __init__(self, titulo, prioridad=None, hecha=False):
        self.titulo = titulo

        # Si no llega prioridad, usar la de clase
        if prioridad is None:
            prioridad = Tarea.prioridad_por_defecto

        # Validar prioridad
        if not Tarea.prioridad_valida(prioridad):
            # En esta solución rechazamos (también podrían corregir a default)
            raise ValueError("Prioridad inválida. Debe estar entre 1 y 5.")

        self.prioridad = prioridad
        self.hecha = hecha

    @staticmethod
    def prioridad_valida(p):
        return isinstance(p, int) and 1 <= p <= 5

    @classmethod
    def cambiar_prioridad_defecto(cls, nueva):
        if cls.prioridad_valida(nueva):
            cls.prioridad_por_defecto = nueva
            return True
        return False

    def __str__(self):
        marca = "[x]" if self.hecha else "[ ]"
        return f"{marca} {self.titulo} (prio {self.prioridad})"


class Agenda:
    # Composición: una agenda "tiene" tareas
    def __init__(self):
        self.tareas = []

    def agregar(self, titulo, **kwargs):
        """
        Simula sobrecarga con **kwargs:
        - prioridad: opcional (si no, usa Tarea.prioridad_por_defecto)
        - hecha: opcional (si no, False)
        """
        prioridad = kwargs.get("prioridad", None)
        hecha = kwargs.get("hecha", False)

        # Validación básica de hecha (debe ser bool)
        if hecha not in (True, False):
            print("'hecha' debe ser True o False.")
            return False

        # Si viene prioridad, validarla
        if prioridad is not None and not Tarea.prioridad_valida(prioridad):
            print("Prioridad inválida. Debe estar entre 1 y 5. Tarea NO agregada.")
            return False

        # Crear tarea y agregarla
        tarea = Tarea(titulo, prioridad=prioridad, hecha=hecha)
        self.tareas.append(tarea)
        return True

    def marcar_hecha(self, indice):
        """
        Marca una tarea como hecha según su índice.
        """
        if not isinstance(indice, int):
            print("El índice debe ser un entero.")
            return False

        if indice < 0 or indice >= len(self.tareas):
            print("Índice fuera de rango.")
            return False

        self.tareas[indice].hecha = True
        return True

    def mostrar(self):
        """
        Imprime todas las tareas usando __str__ de Tarea.
        """
        if len(self.tareas) == 0:
            print("Agenda vacía.")
            return

        print("Agenda:")
        for i, tarea in enumerate(self.tareas):
            print(f"{i}. {tarea}")


# ---------------------------
# DEMO / CASOS DE PRUEBA
# ---------------------------
if __name__ == "__main__":
    agenda = Agenda()

    # Caso 1: cambiar prioridad por defecto a 5 y agregar tareas sin prioridad
    print("=== Cambiar prioridad por defecto a 5 ===")
    ok = Tarea.cambiar_prioridad_defecto(5)
    print("Cambio realizado:", ok)
    print("Prioridad por defecto actual:", Tarea.prioridad_por_defecto)

    print("\n=== Agregar tareas sin prioridad (usan la por defecto) ===")
    agenda.agregar("Estudiar Python")
    agenda.agregar("Hacer ejercicios de lógica")
    agenda.agregar("Preparar clase")

    # Caso 2: tarea con prioridad inválida
    print("\n=== Intento agregar tarea con prioridad inválida ===")
    agenda.agregar("Esto debería fallar", prioridad=10)

    # Agregar tarea con prioridad válida y hecha=True
    print("\n=== Agregar tarea con prioridad válida y hecha=True ===")
    agenda.agregar("Enviar tarea al profesor", prioridad=2, hecha=True)

    # Caso 3: mostrar agenda con __str__
    print("\n=== Mostrar agenda ===")
    agenda.mostrar()

    # Marcar hecha una tarea
    print("\n=== Marcar hecha la tarea índice 1 ===")
    agenda.marcar_hecha(1)

    print("\n=== Mostrar agenda (actualizada) ===")
    agenda.mostrar()
