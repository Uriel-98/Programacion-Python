# Ejercicio 4 - Uriel Diaz

numero_str = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numero_1 = 0
numero_2 = 0
entrar = 1

while entrar != 0:
    if numero_1 == 0:
        numero_1 = input("\nPara saber si los números son divisibles o no, ingrese el primer número: ")
        for i in numero_1:
            if i in numero_str:
                print("Por favor, ingrese caracteres numéricos.")
    elif numero_2 == 0:
        numero_2 = input("\nAhora ingrese el segundo número: ")
        for x in numero_2:
            if x in numero_str:
                print("Por favor, ingrese caracteres numéricos.")
                numero_2 = 0
    else:
        resultado = int(numero_1) / int(numero_2)
        entrar -= 1

if resultado == (int(resultado)):
    print(f"Es divisible, el resultado es {resultado}")
elif resultado == float(resultado):
    print("No es divisible")