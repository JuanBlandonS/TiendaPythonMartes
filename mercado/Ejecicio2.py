frutas = []

print("--- Registro de frutas para el salpicón ---")
for i in range(10):
    print(f"\n--- Fruta {i + 1} ---")
    nombre = input("Nombre de la fruta: ")
    precio = float(input("Precio de la fruta: "))
    frutas.append((nombre, precio))

for i in range(len(frutas)):
    for j in range(i + 1, len(frutas)):
        if frutas[i][1] < frutas[j][1]:
            frutas[i], frutas[j] = frutas[j], frutas[i]

print("\n--- Frutas ordenadas por precio (de mayor a menor) ---")
for fruta in frutas:
    print(f"Fruta: {fruta[0]}, Precio: ${fruta[1]:.2f}")