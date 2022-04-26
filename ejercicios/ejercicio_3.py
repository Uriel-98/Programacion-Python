
import random
from time import sleep

salir = 1
eleccion_cpu = ["Piedra", "Papel", "Tijera"]
eleccion_jugador = 0  # 1 = piedra, 2 = papel, 3 = tijera
contador_ganadas_cpu = 0
contador_ganadas_jugador = 0

while salir:
    try:
        eleccion_jugador = int(input("1 -> Piedra\n2 -> Papel\n3 -> Tijera\nSu eleccion: "))
        
        if eleccion_jugador >= 4:
            print("Solamente hay 3 opciones!")
        
        else:
            eleccion = random.choice(eleccion_cpu)

            if (eleccion_jugador == 1 and eleccion == "Tijera") or \
            (eleccion_jugador == 2 and eleccion == "Piedra") or \
            (eleccion_jugador == 3 and eleccion == "Papel"):
                contador_ganadas_jugador += 1
                print(f"Ganaste!\nJugador: {contador_ganadas_jugador}             CPU: {contador_ganadas_cpu}")
            
            elif (eleccion_jugador == 1 and eleccion == "Papel") or \
            (eleccion_jugador == 2 and eleccion == "Tijera") or \
            (eleccion_jugador == 3 and eleccion == "Piedra"):
                contador_ganadas_cpu += 1
                print(f"Perdiste :(\nJugador: {contador_ganadas_jugador}             CPU: {contador_ganadas_cpu}")
            else:
                print(f"Empate!\nJugador: {contador_ganadas_jugador}             CPU: {contador_ganadas_cpu}")

            if contador_ganadas_jugador == 3:
                print("El ganador es")
                sleep(1), print(".")
                sleep(1), print("..")
                sleep(1), print("...")
                sleep(1), print("Jugador")
                salir -= 1
            
            elif contador_ganadas_cpu == 3:
                print("El ganador es")
                sleep(1), print(".")
                sleep(1), print("..")
                sleep(1), print("...")
                sleep(1), print("CPU")
                salir -= 1
            
            else:
                pass
    except ValueError:
        print("Ingresa números, no letras!")