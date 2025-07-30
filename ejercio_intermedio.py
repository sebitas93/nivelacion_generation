import string
import getpass  # Importo la librería que oculta la entrada

# Bucle hasta que el usuario cree una contraseña válida
while True:
    # Oculto lo que el usuario escribe
    contrasena = getpass.getpass("Crea una contraseña segura (no se mostrará en pantalla): ")

    # Verificaciones de seguridad
    tiene_longitud = len(contrasena) >= 8
    tiene_numero = any(caracter.isdigit() for caracter in contrasena)
    tiene_mayuscula = any(caracter.isupper() for caracter in contrasena)
    tiene_simbolo = any(caracter in string.punctuation for caracter in contrasena)

    # Validación final
    if tiene_longitud and tiene_numero and tiene_mayuscula and tiene_simbolo:
        print("Contraseña válida. ¡Buen trabajo!")
        break
    else:
        print("\n La contraseña no es válida. Revisa los siguientes puntos:")
        if not tiene_longitud:
            print("- Debe tener al menos 8 caracteres.")
        if not tiene_numero:
            print("- Debe contener al menos un número.")
        if not tiene_mayuscula:
            print("- Debe incluir al menos una letra mayúscula.")
        if not tiene_simbolo:
            print("- Debe tener al menos un símbolo (como !, @, #, $, etc.)")
        print("\nIntenta de nuevo.\n")
