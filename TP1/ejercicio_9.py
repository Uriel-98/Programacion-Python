# Ejercicio 9 - Uriel Diaz

numero_1 = 1
numero_2 = 1
numero_str = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

while numero_1 and numero_2:
    eleccion = int(input("\nOperaciones disponibles:\n1-> Sumar\n2-> Restar\n3-> Dividir\n4-> Multiplicar\nElija lo que quiera hacer: "))
    if eleccion > 4 or eleccion <= 0:
        print("\nPor favor, elija una opción válida.")
    elif eleccion <= 4 and eleccion > 0:
        numero_1 = (input("\nPor favor, ingrese el número que desea usar: "))
        numero_2 = (input("\nPor favor, ingrese otro número: "))
        if numero_1 in numero_str or numero_2 in numero_str:
            print("\nPor favor, ingrese un número, no una letra.")
        else:
            numero_int = int(numero_1)
            numero_int2 = int(numero_2)
            suma = numero_int + numero_int2
            resta = numero_int - numero_int2 
            division = numero_int / numero_int2 
            multiplicacion = numero_int * numero_int2 
            if eleccion == 1:
                print(f"\nEl resultado es {suma}")
            elif eleccion == 2:
                print(f"\nEl resultado es {resta}")
            elif eleccion == 3:
                print(f"\nEl resultado es {division}")
            elif eleccion == 4:
                print(f"\nEl resultado es {multiplicacion}")
            respuesta = input("\nQuiere realizar otra operación?\n(Si/No): ").lower()
            if respuesta == "si" or respuesta == "s":
                continue
            elif respuesta == "no" or respuesta == "n":
                print("\nFin del programa.")
                break
