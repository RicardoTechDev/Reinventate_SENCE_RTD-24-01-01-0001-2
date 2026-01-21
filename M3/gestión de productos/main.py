'''
Arranca el programa.
Mantiene el “ciclo principal” (while) que muestra el menú y ejecuta opciones.
Importa funciones desde otros módulos.
'''
from app.datos import PRODUCTOS
from app.menu import ejecutar_menu

def main():
    ejecutar_menu(PRODUCTOS)

if __name__ == "__main__":
    main()
