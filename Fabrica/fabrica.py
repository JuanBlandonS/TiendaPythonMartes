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

def pedirCaracteristicas():
    """Función que pide al usuario las características de la pieza"""
    print("\n--- INGRESO DE CARACTERÍSTICAS ---")
    
    # Generar ID automático
    id = len(piezas) + 1
    
    # Validar referencia
    referencia = input("Referencia (8 caracteres): ").upper()
    while len(referencia) != 8:
        print("¡La referencia debe tener exactamente 8 caracteres!")
        referencia = input("Referencia (8 caracteres): ").upper()
    
    descripcion = input("Descripción del producto: ")
    
    # Validar precios y cantidades
    while True:
        try:
            precio = float(input("Precio unitario de fabricación: $"))
            if precio > 0:
                break
            print("El precio debe ser mayor a 0")
        except ValueError:
            print("Ingrese un valor numérico válido")
    
    while True:
        try:
            piezasFabricadas = int(input("Número de piezas fabricadas: "))
            if piezasFabricadas > 0:
                break
            print("Debe fabricarse al menos 1 pieza")
        except ValueError:
            print("Ingrese un número entero válido")
    
    while True:
        try:
            piezasDefectuosas = int(input("Número de piezas defectuosas: "))
            if 0 <= piezasDefectuosas <= piezasFabricadas:
                break
            print(f"Debe ser entre 0 y {piezasFabricadas}")
        except ValueError:
            print("Ingrese un número entero válido")
    
    fechaEnvio = input("Fecha de envío (dd/mm/aaaa): ")
    
    return {
        'id': id,
        'referencia': referencia,
        'descripcion': descripcion,
        'precio': precio,
        'piezasFabricadas': piezasFabricadas,
        'piezasDefectuosas': piezasDefectuosas,
        'fechaEnvio': fechaEnvio
    }

def crearPieza(caracteristicas):
    """Crea una pieza con las características proporcionadas"""
    pieza = {
        "id": caracteristicas['id'],
        "referencia": caracteristicas['referencia'],
        "descripcion": caracteristicas['descripcion'],
        "precio": caracteristicas['precio'],
        "numeroFabricadas": caracteristicas['piezasFabricadas'],
        "numeroDefectuosas": caracteristicas['piezasDefectuosas'],
        "fechaEnvio": caracteristicas['fechaEnvio'],
        "piezasAptas": caracteristicas['piezasFabricadas'] - caracteristicas['piezasDefectuosas'],
        "costoTotal": caracteristicas['precio'] * caracteristicas['piezasFabricadas']
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
        print(f"Defectuosas: {pieza['numeroDefectuosas']} ({(pieza['numeroDefectuosas']/pieza['numeroFabricadas']):.1%})")
        print(f"Fecha envío: {pieza['fechaEnvio']}")
        print(f"Costo total: ${pieza['costoTotal']:.2f}")

