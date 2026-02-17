def validar_email(email):
    if "@" not in email:
        raise ValueError("Email inválido")
    

def registrar_usuario(email):
    try:
        validar_email(email)
    except ValueError as e:
        print("Error interno: ", e)
        raise


try:
    registrar_usuario("usuario_sin_arroba.com")

except ValueError:
    print("Error detectado en el sistema") 