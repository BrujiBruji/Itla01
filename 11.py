edad = int(input("Cuantos años tienes?: "))
MiedadEnElFuturo = int(input("Cuanto años en el futuro quieres?"))
def DameMiNuevaEdadMas(edad,MiedadEnElFuturo):
    return edad + MiedadEnElFuturo
MiNuevaEdad = DameMiNuevaEdadMas(edad,MiedadEnElFuturo)
print("En", MiedadEnElFuturo, "años tendras", MiNuevaEdad, "años")