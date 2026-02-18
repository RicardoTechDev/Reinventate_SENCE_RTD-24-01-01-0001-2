# inventario_app.py
from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Optional


# ==============================
# MODELO
# ==============================
@dataclass
class Producto:
    sku: str
    nombre: str
    precio: float
    stock: int

    def actualizar(
        self,
        nombre: Optional[str] = None,
        precio: Optional[float] = None,
        stock: Optional[int] = None,
    ) -> None:
        """Actualiza campos del producto (solo los que vengan no-None)."""
        if nombre is not None:
            self.nombre = nombre
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    @staticmethod
    def desde_dict(data: dict) -> "Producto":
        """Crea un Producto desde un diccionario (ej. leído desde JSON)."""
        return Producto(
            sku=str(data["sku"]),
            nombre=str(data["nombre"]),
            precio=float(data["precio"]),
            stock=int(data["stock"]),
        )


# ==============================
# PERSISTENCIA
# ==============================
class RepositorioJSON:
    """Lee y escribe el inventario en un archivo JSON."""

    def __init__(self, ruta_archivo: str = "inventario.json") -> None:
        self.ruta = Path(ruta_archivo)

    def cargar(self) -> Dict[str, Producto]:
        """Retorna un dict sku->Producto. Si el archivo no existe, retorna vacío."""
        if not self.ruta.exists():
            return {}

        try:
            contenido = self.ruta.read_text(encoding="utf-8").strip()
            if not contenido:
                return {}

            data = json.loads(contenido)
            # data esperado: lista de productos o dict sku->dict
            productos: Dict[str, Producto] = {}

            if isinstance(data, list):
                for item in data:
                    p = Producto.desde_dict(item)
                    productos[p.sku] = p
            elif isinstance(data, dict):
                for sku, item in data.items():
                    item["sku"] = sku  # por si viene sin sku dentro
                    p = Producto.desde_dict(item)
                    productos[p.sku] = p
            else:
                return {}

            return productos

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("⚠️  El archivo de inventario está dañado o tiene un formato inválido.")
            print("    Se iniciará con inventario vacío (puedes revisar inventario.json).")
            return {}

    def guardar(self, productos: Dict[str, Producto]) -> None:
        """Guarda el inventario en JSON usando escritura segura (archivo temporal)."""
        data = [asdict(p) for p in productos.values()]
        texto = json.dumps(data, ensure_ascii=False, indent=2)

        tmp = self.ruta.with_suffix(self.ruta.suffix + ".tmp")
        tmp.write_text(texto, encoding="utf-8")
        tmp.replace(self.ruta)


# ==============================
# LÓGICA DE NEGOCIO
# ==============================
class Inventario:
    def __init__(self, repo: RepositorioJSON) -> None:
        self.repo = repo
        self.productos: Dict[str, Producto] = self.repo.cargar()

    def guardar(self) -> None:
        self.repo.guardar(self.productos)

    def listar(self) -> list[Producto]:
        return sorted(self.productos.values(), key=lambda p: p.sku)

    def obtener(self, sku: str) -> Optional[Producto]:
        return self.productos.get(sku)

    def agregar(self, producto: Producto) -> bool:
        """Agrega un producto si el SKU no existe. Retorna True si se agregó."""
        if producto.sku in self.productos:
            return False
        self.productos[producto.sku] = producto
        self.guardar()
        return True

    def eliminar(self, sku: str) -> bool:
        """Elimina un producto por SKU. Retorna True si existía y se eliminó."""
        if sku not in self.productos:
            return False
        del self.productos[sku]
        self.guardar()
        return True

    def modificar(
        self,
        sku: str,
        nombre: Optional[str] = None,
        precio: Optional[float] = None,
        stock: Optional[int] = None,
    ) -> bool:
        """Modifica un producto por SKU. Retorna True si existía y se modificó."""
        p = self.obtener(sku)
        if p is None:
            return False
        p.actualizar(nombre=nombre, precio=precio, stock=stock)
        self.guardar()
        return True


# ==============================
# UTILIDADES DE ENTRADA
# ==============================
def pedir_no_vacio(msg: str) -> str:
    while True:
        valor = input(msg).strip()
        if valor:
            return valor
        print("❌ No puede estar vacío.")


def pedir_int(msg: str, minimo: Optional[int] = None) -> int:
    while True:
        raw = input(msg).strip()
        try:
            n = int(raw)
            if minimo is not None and n < minimo:
                print(f"❌ Debe ser un número >= {minimo}.")
                continue
            return n
        except ValueError:
            print("❌ Ingresa un número entero válido.")


def pedir_float(msg: str, minimo: Optional[float] = None) -> float:
    while True:
        raw = input(msg).strip().replace(",", ".")
        try:
            n = float(raw)
            if minimo is not None and n < minimo:
                print(f"❌ Debe ser un número >= {minimo}.")
                continue
            return n
        except ValueError:
            print("❌ Ingresa un número válido (ej: 12990 o 12.5).")


def pedir_opcional_str(msg: str) -> Optional[str]:
    raw = input(msg).strip()
    return raw if raw != "" else None


def pedir_opcional_int(msg: str, minimo: Optional[int] = None) -> Optional[int]:
    raw = input(msg).strip()
    if raw == "":
        return None
    try:
        n = int(raw)
        if minimo is not None and n < minimo:
            print(f"❌ Debe ser >= {minimo}. Se mantiene el valor anterior.")
            return None
        return n
    except ValueError:
        print("❌ Entero inválido. Se mantiene el valor anterior.")
        return None


def pedir_opcional_float(msg: str, minimo: Optional[float] = None) -> Optional[float]:
    raw = input(msg).strip()
    if raw == "":
        return None
    try:
        n = float(raw.replace(",", "."))
        if minimo is not None and n < minimo:
            print(f"❌ Debe ser >= {minimo}. Se mantiene el valor anterior.")
            return None
        return n
    except ValueError:
        print("❌ Número inválido. Se mantiene el valor anterior.")
        return None


# ==============================
# INTERFAZ (CLI)
# ==============================
def mostrar_producto(p: Producto) -> None:
    print(f"SKU: {p.sku}")
    print(f"Nombre: {p.nombre}")
    print(f"Precio: ${p.precio:,.2f}")
    print(f"Stock: {p.stock}")


def listar_productos(inv: Inventario) -> None:
    productos = inv.listar()
    if not productos:
        print("📦 Inventario vacío.")
        return

    print("\n📋 LISTADO DE PRODUCTOS")
    print("-" * 60)
    print(f"{'SKU':<12} {'NOMBRE':<25} {'PRECIO':>12} {'STOCK':>7}")
    print("-" * 60)
    for p in productos:
        print(f"{p.sku:<12} {p.nombre:<25} {p.precio:>12.2f} {p.stock:>7}")
    print("-" * 60)


def menu() -> None:
    inv = Inventario(RepositorioJSON("inventario.json"))

    while True:
        print("\n=== CONTROL DE INVENTARIO ===")
        print("1) Listar productos")
        print("2) Buscar producto por SKU")
        print("3) Agregar producto")
        print("4) Modificar producto")
        print("5) Eliminar producto")
        print("0) Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            listar_productos(inv)

        elif opcion == "2":
            sku = pedir_no_vacio("SKU a buscar: ")
            p = inv.obtener(sku)
            if p is None:
                print("❌ No existe un producto con ese SKU.")
            else:
                print("\n🔎 PRODUCTO ENCONTRADO")
                mostrar_producto(p)

        elif opcion == "3":
            sku = pedir_no_vacio("SKU: ")
            nombre = pedir_no_vacio("Nombre: ")
            precio = pedir_float("Precio: ", minimo=0.0)
            stock = pedir_int("Stock: ", minimo=0)

            ok = inv.agregar(Producto(sku=sku, nombre=nombre, precio=precio, stock=stock))
            if ok:
                print("✅ Producto agregado y guardado.")
            else:
                print("❌ Ya existe un producto con ese SKU.")

        elif opcion == "4":
            sku = pedir_no_vacio("SKU a modificar: ")
            p = inv.obtener(sku)
            if p is None:
                print("❌ No existe un producto con ese SKU.")
                continue

            print("\n🛠️ Deja vacío para mantener el valor actual.")
            print(f"Actual -> Nombre: {p.nombre} | Precio: {p.precio} | Stock: {p.stock}")

            nuevo_nombre = pedir_opcional_str("Nuevo nombre: ")
            nuevo_precio = pedir_opcional_float("Nuevo precio: ", minimo=0.0)
            nuevo_stock = pedir_opcional_int("Nuevo stock: ", minimo=0)

            ok = inv.modificar(sku, nombre=nuevo_nombre, precio=nuevo_precio, stock=nuevo_stock)
            print("✅ Producto modificado y guardado." if ok else "❌ No se pudo modificar.")

        elif opcion == "5":
            sku = pedir_no_vacio("SKU a eliminar: ")
            ok = inv.eliminar(sku)
            print("✅ Producto eliminado y guardado." if ok else "❌ No existe ese SKU.")

        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    menu()
