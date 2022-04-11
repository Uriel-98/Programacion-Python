# Ejercicio 9 - Uriel Diaz

entrar = 1
eleccion = 0
seguir = 0

from funciones import *

while entrar != 0:
    try:
        eleccion = int(input("\nOperaciones disponibles:\n1-> Sumar\n2-> Restar\n3-> Dividir\n4-> Multiplicar\nElija lo que quiera hacer: "))
        if eleccion > 4 or eleccion <= 0:
            print("Elija una opción correcta!")
        else:
            try:
                numero_1 = int(input("\nIngrese el número que desea usar: "))
                numero_2 = int(input("\nIngrese otro número: "))
                if eleccion == 1:
                    print(f"\nEl resultado es {sumar(numero_1, numero_2)}")
                    seguir += 1
                elif eleccion == 2:
                    print(f"\nEl resultado es {restar(numero_1, numero_2)}")
                    seguir += 1
                elif eleccion == 3:
                    print(f"\nEl resultado es {dividir(numero_1, numero_2)}")
                    seguir += 1
                elif eleccion == 4:
                    print(f"\nEl resultado es {multiplicar(numero_1, numero_2)}")
                    seguir += 1
                
                if seguir:
                    salir_o_no = (input("Desea seguir usando el programa? Si/No\nSu respuesta: ")).lower()
                    if salir_o_no == "no":
                        entrar -= 1
                    else:
                        continue

            except ValueError:
                print("Ingrese un número, no una letra!.")

    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue