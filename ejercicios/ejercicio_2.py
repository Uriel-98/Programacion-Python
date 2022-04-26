#Escribir un código que muestre en orden alfabético las palabras ingresadas.

palabras = []
salir = 1

print("Ingrese las palabras que desee ordenar\nPara dejar de ingresar, escriba Exit")
while salir:
    try:
        palabras.append(str(input()))
        for palabra in palabras:
            if palabra == "exit" or palabra == "Exit":
                salir = 0

    except ValueError:
        print("No ingreses caracteres numéricos/especiales!")

palabras.remove("exit")
print("-".join(sorted(palabras)))