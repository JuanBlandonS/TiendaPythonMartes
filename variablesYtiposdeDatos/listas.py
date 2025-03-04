# Se puedeb agregar cualquier tipo de datos
frutas = ["pera", "manzana", "naranja", "uva", "fresa"]
print (frutas)
print (frutas[2])
print (frutas[0])
print (frutas[-1])
frutas2 = frutas[1:4] # Con los corchetesy el : se agrega el rango que quiro copiar o modificar
print (frutas2)
frutas [1] = "kiwi"
print (frutas[1])

frutas.append(5*4) #Agrega un numero al final
print (frutas)
print(len(frutas))