from funciones.menu import *
from funciones.login import *

#contraseña y usuarios default:
#usuarios: invitado, empleado y admin
#contraseñas: invitado123, empleado123, admin123

while Menu.eleccion != 1:


    Login.login(str(input("Usuario: ")), str(input("Contraseña: ")))


    while Login.verificado != 0:

        if Login.verificado == 1:

            Menu.desplegar_menu(1)

        elif Login.verificado == 2:

            Menu.desplegar_menu(2)

        elif Login.verificado == 3:

            Menu.desplegar_menu(3)
        