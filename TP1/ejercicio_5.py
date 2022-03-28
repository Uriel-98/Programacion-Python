# Ejercicio 5 - Uriel Diaz

numeros = []
print("Por favor, ingrese 3 números\n")

for x in range(3):
    numeros.append(int(input("Números a ingresar: ")))
print("El mayor numero ingresado es:", max(numeros))