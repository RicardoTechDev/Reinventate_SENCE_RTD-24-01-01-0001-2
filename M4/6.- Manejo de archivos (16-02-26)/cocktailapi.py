import requests

def buscar_coctel(nombre: str):
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
    r = requests.get(url, params={"s": nombre}, timeout=10)

    if r.status_code != 200:
        print("❌ Error al consultar la API")
        return

    data = r.json()
    tragos = data.get("drinks")

    if not tragos:
        print("❌ No se encontraron cócteles con ese nombre.")
        return

    trago = tragos[0]  # el primero
    print(f"\n🍸 Nombre: {trago['strDrink']}")
    print(f"📌 Categoría: {trago['strCategory']}")
    print(f"🥃 Vaso: {trago['strGlass']}")
    print(f"🧾 Instrucciones: {trago['strInstructions']}")
    print(f"🖼️ Imagen: {trago['strDrinkThumb']}")

buscar_coctel("margarita")