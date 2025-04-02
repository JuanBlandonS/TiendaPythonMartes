# Una fabrica de productos ceramicos
# Elabora 10 producotos para corona Cada producto esta identificado por 
# ID, referencia(8 caracteres), descripcion, precio de fabricacion individual , numero de piezas fabricadas 
# Numero de piezas defectuosas, fecha de envio las piezas

# Construya una funcion par agregar piezas al pedido
# Construya una funcion par aver el pedido

piezas = []

def agregarPieza(lista, pieza):
    lista.append(pieza)
    return lista

def crearPieza():
    """Función que pide los datos y crea una nueva pieza"""
    print("\n--- REGISTRO DE PIEZA ---")
    
    # Generar ID automáticamente
    id = len(piezas) + 1
    
    referencia = input("Referencia (Por lo menos 8 caracteres): ").upper()
    while len(referencia) != 8:
        print("¡La referencia debe tener por lo menos 8 caracteres!")
        referencia = input("Referencia (8 caracteres): ").upper()
    
    descripcion = input("Descripción del producto: ")
    precio = float(input("Precio unitario de fabricación: $"))
    numeroFabricadas = int(input("Número de piezas fabricadas: "))
    
    numeroDefectuosas = int(input("Número de piezas defectuosas: "))
    while numeroDefectuosas > numeroFabricadas:
        print("¡No puede haber más defectuosas que piezas fabricadas!")
        numeroDefectuosas = int(input("Número de piezas defectuosas: "))
    
    fechaEnvio = input("Fecha de envío (dd/mm/aaaa): ")
    
    pieza = {
        "id": id,
        "referencia": referencia,
        "descripcion": descripcion,
        "precio": precio,
        "numeroFabricadas": numeroFabricadas,
        "numeroDefectuosas": numeroDefectuosas,
        "fechaEnvio": fechaEnvio,
        "piezasAptas": numeroFabricadas - numeroDefectuosas,
        "costoTotal": precio * numeroFabricadas
    }
    return pieza

def mostrarPiezas(lista_piezas):
    """Muestra todas las piezas registradas"""
    print("\n--- MOSTRAR PEDIDOS ---")
    
    if not lista_piezas:
        print("No hay piezas registradas")
        return
    
    print("\n--- LISTADO DE PIEZAS ---")
    for pieza in lista_piezas:
        print(f"\nID: {pieza['id']} | Ref: {pieza['referencia']}")
        print(f"Descripción: {pieza['descripcion']}")
        print(f"Producción: {pieza['numeroFabricadas']} unidades")
        print(f"Defectuosas: {pieza['numeroDefectuosas']}")
        print(f"Fecha envío: {pieza['fechaEnvio']}")
        print(f"Costo total: ${pieza['costoTotal']:.2f}")

# Menú principal
while True:
    print("\n--- MENU DE OPCIONES ---")
    print("1. Registrar pieza")
    print("2. Mostrar piezas")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        nueva_pieza = crearPieza()
        piezas = agregarPieza(piezas, nueva_pieza)
        print("¡Pieza registrada exitosamente!")
    
    elif opcion == "2":
        mostrarPiezas(piezas)
    
    elif opcion == "3":
        print("¡Gracias por usar el sistema!")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")
