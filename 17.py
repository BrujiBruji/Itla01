import random
numero_secreto = random.randint(1, 100)

contador = 1

while True:
    contador != numero_secreto
    
    print("Adivina el numero secreto, (recuerda entre el 1 y el 100)")
    intento = int(input("primer intento:"))
    
    if intento < numero_secreto:
        print("El numero secreto es mayor. Intenta de nuevo")
        contador += 1
    elif intento > numero_secreto:
        print("El numero secreto es menor. Intenta de nuevo")
        contador += 1
    else:
        print("felicidades!!, adivinaste el nuemro secreto: ", numero_secreto)
        print("Lo lograstes en", contador, "intentos")
        break