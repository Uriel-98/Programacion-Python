
import random
from funciones.login import *
from funciones.modificar_atributos import agregar_detalles, agregar_usuario, agregar_vehiculo, cambiar_precio, modificar_km
from funciones.vehiculos import *
from funciones.mostrar_vehiculos import *



acciones = [ ["1 -> Cerrar el programa.", "2 -> Cerrar sesión e ingresar como otro usuario.","3 -> Ver lista de vehiculos a la venta y sus detalles."], 
            ["4 -> Ver precios y modificar kilómetros de los automóviles.", "5 -> Agregar detalles sobre vehículos."], 
            ["6 -> Agregar nuevos vehículos.", "7 -> Modificar precios.", "8 -> Crear nuevo nuevo usuario invitado/empleado."]
            ]

class Menu():
    eleccion = 0
    accion_realizada = False
    def desplegar_menu(permiso):
        while Menu.accion_realizada is False:
            if permiso == 1 or permiso == 2 or permiso == 3:
                for accion in acciones[0]:        
                    print(accion, sep="\n")

                if permiso == 2 or permiso == 3:
                    for accion in acciones[1]:
                        print(accion, sep="\n")

                    if permiso == 3:
                        for accion in acciones[2]:
                            print(accion, sep="\n")
            Menu.accion_realizada = True

        def elegir_opcion():
                try:
                    eleccion = int(input("Qué desea hacer?: "))
                    
                    if eleccion > 0 and eleccion <= 8:

                        if eleccion == 1:
                            Login.verificado = 0
                            Menu.eleccion = 1 # 2 = salir del programa
                        if eleccion == 2: # 1 = cerrar sesion
                            Menu.accion_realizada = False
                            Login.verificado = 0
                            print(f"Cerrando sesión..."), sleep(3)

                        elif eleccion == 3:
                    
                            try:
                                eleccion_ver = int(input("1 -> Autos\n2 -> Motos\n3 -> Bicicletas\n4 -> Camionetas\n5 -> Camiones\n6 -> Colectivos\n7 -> Acoplados\nQué tipo de vehículo desea ver?: "))

                                if eleccion_ver == 1:
                                    mostrar_autos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_ver == 2:
                                    mostrar_motos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_ver == 3:
                                    mostrar_bicicletas(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_ver == 4:
                                    mostrar_camionetas(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_ver == 5:
                                    mostrar_Camiones(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_ver == 6:
                                    mostrar_colectivos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_ver == 7:
                                    mostrar_acoplados(permiso)
                                    Menu.accion_realizada = False

                            except ValueError:
                                print("Solo podés ingresar números.")

                        elif eleccion == 4 and (permiso == 2 or permiso == 3):
                            try:
                                eleccion_modificar = int(input("1 -> Autos\n2 -> Motos\n3 -> Camionetas\n4 -> Camiones\n5 -> Colectivos\n6 -> Acoplados\nA qué tipo de vehículo quiere cambiarle los km/ver precio?: "))

                                if eleccion_modificar == 1:
                                    mostrar_autos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_modificar == 2:
                                    mostrar_motos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_modificar == 4:
                                    mostrar_camionetas(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_modificar == 5:
                                    mostrar_Camiones(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_modificar == 6:
                                    mostrar_colectivos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_modificar == 7:
                                    mostrar_acoplados(permiso)
                                    Menu.accion_realizada = False

                                try:
                                    numero_de_vehiculo = int(input("Qué vehículo desea modificar? (escriba el número): "))
                                    modificar_km(eleccion_modificar, numero_de_vehiculo, int(input("Nuevo kilometraje:")), permiso)

                                except ValueError:
                                    print("Solamente podés poner números!")

                            except ValueError:
                                print("Ingresá una opción válida!")
                            
                        elif eleccion == 5 and (permiso == 2 or permiso == 3):
                            try:
                                eleccion_detalles = int(input("1 -> Autos\n2 -> Motos\n3 -> Bicicletas\n4 -> Camionetas\n5 -> Colectivos\n6 -> Camiones\n7 -> Acoplados\nA qué tipo de vehículo quiere cambiarle los detalles?: "))
                                if eleccion_detalles == 1:
                                    mostrar_autos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 2:
                                    mostrar_motos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 3:
                                    mostrar_bicicletas(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 4:
                                    mostrar_camionetas(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 6:
                                    mostrar_Camiones(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 5:
                                    mostrar_colectivos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 7:
                                    mostrar_acoplados(permiso)
                                    Menu.accion_realizada = False
                                try:

                                    vehiculo_agregar_detalles = int(input("Qué vehículo desea modificar? (escriba el número): "))
                                    agregar_detalles(eleccion_detalles, vehiculo_agregar_detalles, input("Ingrese el/los detalle/s: "), permiso)
                                    Menu.accion_realizada = False
                                
                                except ValueError:
                                    print("No pongas letas!")
                            
                            except ValueError:
                                print("No pongas letas!")
                        
                        elif eleccion == 6 and  permiso == 3:
                            try:
                                eleccion_agregar= int(input("1 -> Autos\n2 -> Motos\n3 -> Bicicletas\n4 -> Camionetas\n5 -> Camiones\n6 -> Colectivos\n7 -> Acoplados\nQué tipo de vehículo desea agregar?: "))
                                agregar_vehiculo(eleccion_agregar)
                                Menu.accion_realizada = False
                            except ValueError:
                                print("No pongas letras!")
                        
                        elif eleccion == 7 and permiso == 3:
                            try:
                                eleccion_precios = int(input("1 -> Autos\n2 -> Motos\n3 -> Bicicletas\n4 -> Camionetas\n5 -> Camiones\n6 -> Colectivos\n7 -> Acoplados\nA qué tipo de vehículo quiere cambiarle el precio?: "))
                                
                                if eleccion_detalles == 1:
                                    mostrar_autos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 2:
                                    mostrar_motos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 3:
                                    mostrar_bicicletas(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 4:
                                    mostrar_camionetas(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 6:
                                    mostrar_Camiones(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 5:
                                    mostrar_colectivos(permiso)
                                    Menu.accion_realizada = False
                                elif eleccion_detalles == 7:
                                    mostrar_acoplados(permiso)
                                    Menu.accion_realizada = False
                                
                                try:
                                    numero_de_vehiculo = int(input("Qué vehículo desea modificar? (escriba el número): "))
                                    cambiar_precio(eleccion_precios, numero_de_vehiculo, int(input("Precio nuevo: ")), permiso)
                                    Menu.accion_realizada = False
                                except ValueError:
                                    print("Solo podés ingresar números.")
                            except ValueError:
                                print("No pongas letras!")
                        
                        elif eleccion == 8 and permiso == 3:
                            agregar_usuario(input("Ingrese nombre de usuario: "), input("Ingrese contraseña: "), int(input("1 -> Invitado\n2 -> Empleado\nDefina el permiso del usuario: ")))
                            Menu.accion_realizada = False
                        
                        if (permiso == 1 and eleccion >= 4) or (permiso == 2 and eleccion >= 6):
                            print("No tenés permisos para hacer eso!")

                    else:
                        print("Elegí una opción válida2!")

                except ValueError:
                    print("Elegí una opción válida1!")
        elegir_opcion()