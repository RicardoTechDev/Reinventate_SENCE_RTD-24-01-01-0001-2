#python -m pip install requests

import requests

def get_pokedata(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    print("No fue posible recuperar la data")
    return None


def get_pokeinfo(data):
    name = data["name"]
    height = data["height"]
    weight = data["weight"]
    types = [t["type"]["name"] for t in data["types"]]

    print(f"\n___ información de {name} ___")
    print(f"Altura {height}")
    print(f"Peso {weight}")
    print(f"Tipos {', '.join(types)}")

    sprites = data["sprites"]

    # Imágenes básicas
    front_default = sprites.get("front_default")
    back_default = sprites.get("back_default")
    front_shiny = sprites.get("front_shiny")
    back_shiny = sprites.get("back_shiny")

    # Imagen "oficial" (suele ser la mejor)
    official_artwork = (
        sprites.get("other", {})
               .get("official-artwork", {})
               .get("front_default")
    )

    print(f"\nImágenes de {name}")
    print("Frontal (normal):", front_default)
    print("Trasera (normal):", back_default)
    print("Frontal (shiny):", front_shiny)
    print("Trasera (shiny):", back_shiny)
    print("Oficial:", official_artwork)


def main():
    print("Bienvenidos a la Pokedex")

    pokemon = input("Ingresa el nombre el número del pokemón: ")
    data = get_pokedata(pokemon)#Todo el json

    if data:
        get_pokeinfo(data)



if __name__== "__main__":
    main()