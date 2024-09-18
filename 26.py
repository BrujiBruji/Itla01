numeros = float(input("Dame un numero"))
numeros2 = float(input("Dame otro numero"))
numeros3 = float(input("Dame otro numero"))

if numeros < numeros2 and numeros3:
    print(numeros , "Este es el numero mas pequeño")
elif numeros2 < numeros and numeros3:
    print(numeros2 , "Este es el numero mas pequeño")
elif numeros3 < numeros and numeros2:
    print(numeros , "Este es el numero mas pequeño")
else:
    print("Son iguales")