# Pido al usuario que ingrese el espacio libre en disco
espacio_libre_gb = float(input("¿Cuántos GB de espacio libre tiene el disco?: "))

# Analizo el valor ingresado y genero la alerta correspondiente
if espacio_libre_gb < 10:
    print("¡Alerta! El espacio libre en disco es crítico. Requiere limpieza urgente.")
elif 10 <= espacio_libre_gb <= 50:
    print("Advertencia: El espacio libre en disco es bajo. Considere realizar una revisión.")
else:
    print("El espacio libre en disco es adecuado.")


