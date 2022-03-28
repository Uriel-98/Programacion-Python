# Ejercicio 10 - Uriel Diaz

import random

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
numero_random = 0
numero_elegido = 1
intentos = 5

while numero_random != numero_elegido and intentos != 0:
    numero_random  = random.choice(numeros)
    numero_elegido = int(input("\nElija un número del 0 al 25, solo tiene 5 intentos: "))
    intentos -= 1
if intentos == 0:
    print(f"\nTe quedaste sin intentos!\nEl número era {numero_random}")
else:
    print("\nBien ahi, adivinaste el número.")