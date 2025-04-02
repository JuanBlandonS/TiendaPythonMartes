# Necesito pedir datos por teclado 
# Llamar a la funcion que crea la pieza 
# Llamar a la funcion que agrega la pieza a la lista de piezas
# Llamar a la funcion que muestra la lista de piezas

from fabrica import agregarPieza, pedirCaracteristicas, crearPieza, mostrarPiezas

lista = []

# Menú principal
while True:
    print("\n--- MENU DE OPCIONES ---")
    print("1. Registrar pieza")
    print("2. Mostrar piezas")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        # Primero pedimos las características
        datos_pieza = pedirCaracteristicas()
        # Luego creamos la pieza con esos datos
        nueva_pieza = crearPieza(datos_pieza)
        # Finalmente agregamos a la lista
        lista = agregarPieza(lista, nueva_pieza)
        print("\n¡Pieza registrada exitosamente!")
    
    elif opcion == "2":
        mostrarPiezas(lista)
    
    elif opcion == "3":
        print("¡Gracias por usar el sistema!")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")
