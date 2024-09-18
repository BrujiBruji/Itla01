# Inicializar la lista
nombres_estudiantes = []

# Bucle while
while True:
    # Pedimos al usuario que ingrese el nombre de un estudiante
    nombre = input("Ingresa el nombre del estudiante (o escribe 'salir' para terminar): ")

    # Verificamos si el usuario quiere terminar
    if nombre.lower() == 'salir':
        break  # Salimos del bucle si el usuario escribe 'salir'
    
    # Agregamos el nombre a la lista
    nombres_estudiantes.append(nombre)

# Salida: mostramos la lista completa de estudiantes
print("Lista completa de estudiantes:")
for estudiante in nombres_estudiantes:
    print(estudiante)
