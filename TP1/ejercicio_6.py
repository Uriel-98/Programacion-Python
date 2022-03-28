# Ejercicio 6 - Uriel Diaz


nombres = [""]

for x in nombres:
    if x == "exit":
        break
    nombres.append(input("Para salir del programa, ingrese la palabra exit\nPor favor, ingrese los nombres de sus amigos:\n"))
nombres.remove("")
nombres.remove("exit")
print("-".join(nombres))