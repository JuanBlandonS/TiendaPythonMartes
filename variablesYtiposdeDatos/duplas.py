# Tupla con diferentes tipos de datos
mi_tupla = (1, 2, 3, "Hola", True)

print(mi_tupla)  # (1, 2, 3, 'Hola', True)

mi_tupla = (1, 2, 3, 2, 4, 2)

print(mi_tupla.count(2))  # 3 (cuenta cuántas veces aparece el 2)
print(mi_tupla.index(4))  # 4 (posición del primer 4)

#Duplas anidadas
tupla_anidada = ((1, 2, 3), ("a", "b", "c"))
print(tupla_anidada[1][2])  # "c"
