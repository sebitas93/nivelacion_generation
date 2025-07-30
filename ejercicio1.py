# Guardo la contraseña que considero correcta
mi_contraseña = "admin123"

# Le pido al usuario que ingrese la contraseña
entrada = input("Introduce tu contraseña: ")

# Compruebo si lo que ingresó coincide con lo que guardé
if entrada == mi_contraseña:
    print("¡Bien! La contraseña es correcta, puedes acceder.")
else:
    print("Lo siento, la contraseña no es válida. Acceso denegado.")