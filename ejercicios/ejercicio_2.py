# Ejercicio 2 - Uriel Diaz
palabras = []
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
salir = 1

print("Ingrese las palabras que desee ordenar\nPara dejar de ingresar, escriba Exit")
while salir:
    palabras.append(input())
    for palabra in palabras:
        if palabra in numeros:
            print("No ingreses caracteres numéricos/especiales!")
            palabras.remove(palabra)
        elif palabra == "exit" or palabra == "Exit":
            salir = 0

palabras.remove("exit")
print("-".join(sorted(palabras)))