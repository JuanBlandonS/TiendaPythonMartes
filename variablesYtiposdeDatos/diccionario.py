# Diccionario simple
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Medellín"
}

print(persona)  
# {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Medellín'}

print(persona["nombre"])  # Juan
print(persona.get("edad"))  # 25

#modificar datos
persona["edad"] = 26
print(persona)  # {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Medellín'}

#Agregar y eliminar elementos
persona["profesion"] = "Ingeniero"
print(persona)  
# {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Medellín', 'profesion': 'Ingeniero'}

del persona["ciudad"]  # Eliminar por clave
print(persona)  
# {'nombre': 'Juan', 'edad': 26, 'profesion': 'Ingeniero'}

#Recorrer un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

#Metodosd utiles
print(persona.keys())   # dict_keys(['nombre', 'edad', 'profesion'])
print(persona.values()) # dict_values(['Juan', 26, 'Ingeniero'])
print(persona.items())  # dict_items([('nombre', 'Juan'), ('edad', 26), ('profesion', 'Ingeniero')])

#diccionario con listas y diccionarios anidados
empresa = {
    "nombre": "TechCorp",
    "empleados": ["Ana", "Carlos", "Luis"],
    "ubicaciones": {
        "sede1": "Bogotá",
        "sede2": "Medellín"
    }
}

print(empresa["ubicaciones"]["sede1"])  # Bogotá

#Verificar si una clave existe
if "edad" in persona:
    print("La clave 'edad' existe")

#copiar un diccionario
persona_copia = persona.copy()
persona_copia["nombre"] = "Pedro"
print(persona)         # {'nombre': 'Juan', 'edad': 26, 'profesion': 'Ingeniero'}
print(persona_copia)   # {'nombre': 'Pedro', 'edad': 26, 'profesion': 'Ingeniero'}

