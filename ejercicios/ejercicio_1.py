# Ejercicio 1 - Uriel Diaz

numeros = []
salir = 1

while salir != 0:
    try:
        numeros.append(int(input("Ingrese un número: ")))
        
        if len(numeros) >= 2:
            print(f"De los números ingresados hasta ahora, el mayor es {max(numeros)} y el menor {min(numeros)}.\n")
            print(f"La suma de todos los números ingresados es {sum(numeros)}, y su promedio es {sum(numeros) / len(numeros)}\n")
            try:
                salir = (str(input("Desea continuar ingresando números? Si/No: \n"))).lower()
                if salir == "si":
                    pass
                elif salir == "no":    
                    salir = 0
                else:
                    print("Ingresa solo Si o No!")
            except ValueError:
                print("No ingreses caracteres numéricos/especiales!")
    except ValueError:
        print("Ingresa solo caracteres numéricos!")    
    