#Ejercicio1

#Descuentos
#categoria_1: 5 a 14 - 35%
#categoria_2: 15 a 19 - 25%
#categoria_3: 20 a 60 - 0%
#categoria_4: > 60 - 90%

entrada = 10000

aforo = int(input("Ingrese la cantidad total de personas que pueden ingresar: "))
contador = 1

recaudado = 0
descuentos = 0

cat1 = 0
cat2 = 0
cat3 = 0
cat4 = 0

while contador <= aforo:
    edad = int(input("ingrese la edad de la persona: "))
    
    if edad < 5:
        print("¡No puede ingresar!")
    else:
        if edad <= 14:
            descuentos = entrada * 0.35
            cat1 = cat1 + 1
        else:
            if edad <= 19:
                descuentos = entrada * 0.25
                cat2 = cat2 + 1
            else:
                if edad <= 60:
                    descuentos = 0
                    cat3 = cat3 + 1
                else:
                    descuentos = entrada * 0.90
                    cat4 = cat4 + 1
                    
        pago = entrada - descuentos
        recaudado = recaudado + pago
        descuentos = descuentos + descuentos
        
        contador = contador + 1
        
print(f"Total recaudado: {recaudado}")
print(f"Personas en categoria 1 (5-14 años): {cat1}")
print(f"Personas en categoria 2 (15-19 años): {cat2}")
print(f"Personas en categoria 3 (20-60 años): {cat3}")
print(f"Personas en categoria 4 (>60 años): {cat4}")
print(f"Total descuentos otorgados: {descuentos}")