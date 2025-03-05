nombreVendedor = None
productos = []
producto = {}
contador_id = 1  # Variable para generar IDs únicos

opcion = 100

print("Mercado")
print("*****")
print("1. Crear lista de mercado")
print("2. Ver lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("Presiona 5 para salir")

while opcion != 5:
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("Estoy en la 1")

        # Creando claves y valores de un diccionario
        producto["id"] = contador_id  # Asignar ID único
        producto["nombre"] = input("Ingrese el nombre del producto: ")
        producto["precio"] = int(input("Ingrese el precio del producto: "))
        producto["cantidad"] = int(input("Ingrese la cantidad del producto: "))
        producto["presentacion"] = input("Ingrese la presentación del producto: ")

        # Mostrando mi diccionario
        print(producto)

        # Poblando una lista (Agregando los datos a la lista)
        productos.append(producto.copy())

        # Incrementar el contador de ID para el próximo producto
        contador_id += 1

    elif opcion == 2:
        print("Estoy en la 2")
        # Mostrar la lista de productos
        for p in productos:
            print(p)

    elif opcion == 3:
        print("Estoy en la 3")
        # Editar un producto por ID
        id_editar = int(input("Ingrese el ID del producto a editar: "))
        for p in productos:
            if p["id"] == id_editar:
                p["nombre"] = input("Nuevo nombre: ")
                p["precio"] = int(input("Nuevo precio: "))
                p["cantidad"] = int(input("Nueva cantidad: "))
                p["presentacion"] = input("Nueva presentación: ")
                print("Producto actualizado:", p)
                break
        else:
            print("Producto no encontrado.")

    elif opcion == 4:
        print("Estoy en la 4")
        # Retirar un producto por ID
        id_retirar = int(input("Ingrese el ID del producto a retirar: "))
        for p in productos:
            if p["id"] == id_retirar:
                productos.remove(p)
                print("Producto retirado.")
                break
        else:
            print("Producto no encontrado.")

    else:
        print("Opción no válida")