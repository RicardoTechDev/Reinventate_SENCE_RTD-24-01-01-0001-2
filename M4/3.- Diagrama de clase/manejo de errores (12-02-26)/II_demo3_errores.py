class ErrorAplicacion(Exception):
    pass

class ErrorValidacion(ErrorAplicacion):
    pass

class ErrorPermisos(ErrorAplicacion):
    pass


def verificar_usurio(rol):
    if rol == "Visitante":
        raise ErrorPermisos("Acceso no autorizado")
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

    except ErrorPermisos:
        print("Error: no tienes permisos suficientes")

    except ErrorValidacion:
        print("Error: datos inválidos")

    except ErrorAplicacion:
        print("Otro error general de aplicación")
