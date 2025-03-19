helados = []

while True:
    print("\n--- Gestión de Helados ---")
    print("1. Crear un helado")
    print("2. Ver lista de helados")
    print("3. Modificar un helado")
    print("4. Eliminar un helado")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Crear un helado ---")
        nombre = input("Nombre del helado: ")
        descripcion = input("Descripción: ")
        precio = float(input("Precio unitario: "))

        id_helado = len(helados) + 1

        helado = {
            "id": id_helado,
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio
        }

        helados.append(helado)
        print(f"Helado '{nombre}' creado con éxito.\n")

    elif opcion == "2":
        print("\n--- Lista de helados ---")
        if not helados:
            print("No hay helados registrados.\n")
        else:
            for helado in helados:
                print(f"ID: {helado['id']}")
                print(f"Nombre: {helado['nombre']}")
                print(f"Descripción: {helado['descripcion']}")
                print(f"Precio: ${helado['precio']:.2f}")
                print("-" * 30)

    elif opcion == "3":
        print("\n--- Modificar un helado ---")
        id_helado = int(input("Ingrese el ID del helado a modificar: "))

        encontrado = False
        for helado in helados:
            if helado["id"] == id_helado:
                print(f"Modificando helado: {helado['nombre']}")
                helado["nombre"] = input("Nuevo nombre: ")
                helado["descripcion"] = input("Nueva descripción: ")
                helado["precio"] = float(input("Nuevo precio: "))
                print("Helado modificado con éxito.\n")
                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró un helado con ID {id_helado}.\n")

    elif opcion == "4":
        print("\n--- Eliminar un helado ---")
        id_helado = int(input("Ingrese el ID del helado a eliminar: "))

        encontrado = False
        for helado in helados:
            if helado["id"] == id_helado:
                helados.remove(helado)
                print(f"Helado '{helado['nombre']}' eliminado con éxito.\n")
                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró un helado con ID {id_helado}.\n")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente de nuevo.\n")