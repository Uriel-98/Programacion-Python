# Ejercicio 2 - Uriel Diaz

numero_str = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lado_1 = 0
lado_2 = 0
lado_3 = 0
entrar = 1

while entrar != 0:
    if lado_1 == 0:
        lado_1 = input("\ningrese las medidas del primer lado: ")
        for i in lado_1:
            if i in numero_str:
                print("\nPor favor, ingrese solo caracteres numéricos.")
                lado_1 = 0
    elif lado_2 == 0:
        lado_2 = input("\ningrese las medidas del segundo lado: ")
        for x in lado_2:
            if x in numero_str:
                print("\nPor favor, ingrese solo caracteres numéricos.")
                lado_2 = 0
    elif lado_3 == 0:
        lado_3 = input("\ningrese las medidas del tercer lado: ")
        for l in lado_3:
            if l in numero_str:
                print("\nPor favor, ingrese solo caracteres numéricos.")
                lado_3 = 0
    else:
        area = (int(lado_1) * int(lado_2)) / 2
        entrar -= 1
        
print(f"El area del triangulo es: {area}")