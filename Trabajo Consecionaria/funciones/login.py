from time import sleep
from funciones.usuarios import *

class Login:
    verificado = 0
    
    def login(usuario, contraseña):
        login_location = 0

        print(f"Iniciando sesión como {usuario}..."), sleep(3)

        for x in lista_invitados:
            if usuario == x.usuario and usuario == x.contraseña:
                print("Sesión iniciada con éxito.")
                Login.verificado = 1
                login_location = 0
            else:
                login_location = 1
                print("no")
        
        for i in lista_empleados:
            if usuario == i.usuario and usuario == i.contraseña:
                print("Sesión iniciada con éxito.")
                Login.verificado = 2
                login_location = 0
            else:
                login_location = 1
                print("no")
            
        if (len(lista_empleados) == 0 or len(lista_invitados) == 0) or login_location == 1:
            if usuario == Invitado.usuario_default:

                if contraseña == Invitado.contraseña_default:
                    print("Sesión iniciada con éxito.")
                    Login.verificado = 1
                    
                else:
                    print("Contraseña incorrecta!")

            elif usuario == Empleado.usuario_default:

                if contraseña == Empleado.contraseña_default:
                    print("Sesión iniciada con éxito.")
                    Login.verificado = 2
                    
                else:
                    print("Contraseña incorrecta!")

            elif usuario == Admin.usuario_default:

                if contraseña == Admin.contraseña_default:
                    print("Sesión iniciada con éxito.")
                    Login.verificado = 3
                    
                else:
                    print("Contraseña incorrecta!")
            
            else:
                print(f"El usuario {usuario} no existe!")