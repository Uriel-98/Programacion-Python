# Ejercicio 8 - Uriel Diaz

numero_str = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vocales = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
entrar = 2
cuenta_vocales = 0
digitos_aceptables = 4
caracter_especial = ["!", "“", "#", "$", "%", "&", "_", "@", ".", "-", "/"]
año_nacimiento_check = "no"
nombre = 0
apellido = 0
año_nacimiento = 0
todo_ok = 0



while entrar >= 1:
    if nombre == 0:
        nombre = input("\nPor favor, ingrese su nombre: ")
        for x in nombre:
            if x in vocales:      #checks how many vowels there are
                cuenta_vocales += 1
        if cuenta_vocales < 3:
            print("El nombre debe tener al menos 3 vocales.")
            nombre = 0
    elif apellido == 0:
        apellido = input("\nIngrese su apellido: ")
    elif año_nacimiento == 0:
        año_nacimiento = input("\nEscriba, con números, el año en el que nació: ")   
        for x in año_nacimiento:
            if x in numero_str:
                print("\nPor favor, ingrese caracteres numéricos, no letras.")
                año_nacimiento = 0
                continue
            elif len(str(año_nacimiento)) != 4:       #checks whether it is a proper date or not
                print("\nPor favor, ingrese una fecha válida.")
                año_nacimiento = 0
            else:
                año_nacimientoint = 0
                año_nacimientoint = int(año_nacimiento)
                if año_nacimientoint != 0:
                    año_nacimiento_check = "yes"
                    contraseña = input("\nIngrese su contraseña: ")
                
                    if len(str(contraseña)) > 16:
                        print("Ponele menos caracteres a tu contraseña!")
                    elif len(str(contraseña)) <8:
                        print("ponele más caracteres a tu contraseña!")
                    cuenta_caracter_especial = 0
                    for caracter in contraseña:
                        if caracter in caracter_especial:                        #checks whether it contains a special character or not
                            cuenta_caracter_especial += 1
                            if cuenta_caracter_especial == 0:
                                print("Ponele al menos un caracter especial a la contraseña.")
                    if cuenta_vocales >= 3 and año_nacimiento_check == "yes" and cuenta_caracter_especial > 0 and len(str(contraseña)) >= 8 and len(str(contraseña)) <= 16:
                        todo_ok += 1
                        entrar -= 1
    if todo_ok == 1:
        entrar -=1
print(f"Bienvenido, {nombre} {apellido}!")