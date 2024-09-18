import random

opciones = ["piedra", "papel", "tijera"]

while True:
    jugador = input("Elige: piedra, papel o tijera: ").lower()
    computadora = random.choice(opciones)
    
    print("Tu elegiste:", jugador)
    print("La computadora eligio:", computadora)
    
    if jugador == computadora:
        print("Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "tijera" and computadora == "papel") or \
         (jugador == "papel" and computadora == "piedra"):
         print("Ganaste!")
    else:
        print("Perdiste!")
        
jugar_de_nuevo = input("Quieres jugar de nuevo (s/n): ").lower()

if jugar_de_nuevo != "s":
    Break