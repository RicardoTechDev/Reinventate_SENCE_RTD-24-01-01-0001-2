class ErrorAplicacion(Exception):
    pass

class ErrorValidacion(ErrorAplicacion):
    pass

class ErrorPermisos(ErrorAplicacion):
    def __init__(self, mensaje, rol, codigo=403):
        super().__init__(mensaje)
        self.rol = rol
        self.codigo = codigo

    def detalle(self):
        return f'[{self.codigo}] "{self.rol}" --> {self}'


def verificar_usurio(rol):
    if rol == "Visitante":
        raise ErrorPermisos("Acceso no autorizado", rol, codigo=500)
    elif rol not in ["admin", "editor"]:
        raise ErrorValidacion("Rol inválido")
    
    print(f"Acceso permitido para el rol {rol}")


roles_a_probar = [
    "Visitante", 
    "SuperAdmin", 
    "admin"
    ]

for rol in roles_a_probar:
    print(f"=== PROBANDO ROL {rol} ===")

    try:
        verificar_usurio(rol)

    except ErrorPermisos as e:
        print("Error: no tienes permisos suficientes")
        print(f"Detalle: {e.detalle()}")
        print(f"Código: {e.codigo}")
        print(f" Rol: {e.rol}")

    except ErrorValidacion:
        print("Error: datos inválidos")

    except ErrorAplicacion:
        print("Otro error general de aplicación")
