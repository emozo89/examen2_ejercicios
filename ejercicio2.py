#Ejercicio2

serie = int(input("Ingrese hasta donde desea la serie: "))

while serie <= 5:
    print("Ingrese un numero mayor!")
    serie = int(input("Ingrese hasta donde desea la serie: "))

contador = 1
resultado = 0

while contador <= serie:
    if contador == 1:
        print(contador, end="")
        resultado = resultado + contador
    else:
        if contador % 2 == 0:
            print(f"+{contador}", end="")
            resultado = resultado + contador
        else:
            print(f"-{contador}", end="")
            resultado = resultado - contador
    contador = contador + 1

print(f"={resultado}")