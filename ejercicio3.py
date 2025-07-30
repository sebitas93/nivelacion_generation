# Solicito al usuario que ingrese una cantidad de bytes
bytes_ingresados = int(input("Ingresa la cantidad de bytes: "))

# Realizo las conversiones
kb = bytes_ingresados / 1024
mb = kb / 1024
gb = mb / 1024

# Muestro los resultados
print(f"{bytes_ingresados} bytes equivalen a:")
print(f"{kb:.2f} KB")
print(f"{mb:.2f} MB")
print(f"{gb:.2f} GB")
