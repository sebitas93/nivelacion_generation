# Sistema básico para gestionar un inventario de equipos informáticos
# Permite agregar, buscar, ver estadísticas e imprimir informe general

inventario = []

def agregar_equipo():
    print("\n Agregar equipo")
    tipo = input("Tipo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    serial = input("Número de serie: ")
    ubicacion = input("Ubicación: ")

    equipo = {
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "serial": serial,
        "ubicacion": ubicacion
    }

    inventario.append(equipo)
    print(" Equipo agregado.")

def buscar_equipo():
    print("\n Buscar equipo")
    campo = input("Buscar por (marca/tipo/ubicacion): ").lower()
    valor = input(f"Ingrese el valor de {campo}: ").lower()

    encontrados = []
    for equipo in inventario:
        if equipo.get(campo, "").lower() == valor:
            encontrados.append(equipo)

    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} equipo(s):")
        for eq in encontrados:
            print(eq)
    else:
        print(" No se encontraron coincidencias.")

def ver_estadisticas():
    print("\n Estadísticas")
    por_tipo = {}
    por_ubicacion = {}

    for equipo in inventario:
        por_tipo[equipo["tipo"]] = por_tipo.get(equipo["tipo"], 0) + 1
        por_ubicacion[equipo["ubicacion"]] = por_ubicacion.get(equipo["ubicacion"], 0) + 1

    print("Equipos por tipo:")
    for tipo, cantidad in por_tipo.items():
        print(f"- {tipo}: {cantidad}")

    print("\nEquipos por ubicación:")
    for ubi, cantidad in por_ubicacion.items():
        print(f"- {ubi}: {cantidad}")

def generar_informe():
    print("\n Informe del inventario completo")
    if not inventario:
        print("Inventario vacío.")
        return
    for i, equipo in enumerate(inventario, 1):
        print(f"\nEquipo #{i}")
        for k, v in equipo.items():
            print(f"{k.capitalize()}: {v}")

def menu():
    while True:
        print("\n========== Menú ==========")
        print("1. Agregar equipo")
        print("2. Buscar equipo")
        print("3. Ver estadísticas")
        print("4. Generar informe")
        print("5. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            agregar_equipo()
        elif opcion == "2":
            buscar_equipo()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            generar_informe()
        elif opcion == "5":
            print(" Cerrando el sistema.")
            break
        else:
            print(" Opción inválida.")

# Inicio del programa
menu()
