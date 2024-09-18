peso = float(input("Dame tu peso en kilogramos: " "kg:"))
altura = float(input("Dame tu altura en metros: " "Metros:"))

IMC = peso / (altura ** 2)

if IMC <= 18.5:
    print("Bajo peso")
elif 18.5 <= IMC <= 24.9:
    print("Peso normal")
elif 25 <= IMC <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")

print("Su IMC es: ", IMC)