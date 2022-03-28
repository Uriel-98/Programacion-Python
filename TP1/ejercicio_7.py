# Ejercicio 7 - Uriel Diaz

nombre = input("\nPor favor, ingrese su nombre: ")
apellido = input("\nIngrese su apellido: ")
edad = int(input("\nIngrese su edad: "))
dinero = int(input("\nIngrese el dinero que tiene en su billetera: "))
hambre = int(input("\nEn escala del 1 al 10, ingrese el hambre que tiene: "))


if edad >= 34 and dinero >= 500 and hambre >= 5:
    print(f"Hola, {nombre} {apellido}, ¿hoy hay asado?")
elif hambre >= 7 or (dinero <= 100 and edad <= 18):
    print(f"Hola, {nombre} {apellido}, ¿vas a comer a lo de tus padres?") 
elif edad <= 35:
    print(f"\nHola, {nombre}. Eres una persona joven ya que tu edad es {edad}")