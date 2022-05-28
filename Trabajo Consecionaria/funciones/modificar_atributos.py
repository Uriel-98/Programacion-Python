
from funciones.mostrar_vehiculos import *
from funciones.vehiculos import *
from funciones.usuarios import *
from funciones.menu import *

def modificar_km(vehiculo, num_vehiculo, km, permiso):  # 1 = Auto, 2 = Moto, 3 = Camioneta, 4 = Camion, 5 = Colectivo, 6 = Acoplado

    if vehiculo == 1:
        mostrar_autos(permiso)
        for auto in lista_autos:
            if auto.numero == num_vehiculo:
                auto.kilometros = km
                print(f"Los nuevos datos del vehiculo son:\n----------\nkilometros: {auto.kilometros}(modificado)\nprecio: {auto.precio}\n----------")
    elif vehiculo == 2:
        mostrar_motos(permiso)
        for moto in lista_motos:
            if moto.numero == num_vehiculo:
                moto.kilometros = km
                print(f"Los nuevos datos del vehiculo son:\n----------\nkilometros: {moto.kilometros}(modificado)\nprecio: {moto.precio}\n----------")
    elif vehiculo == 3:
        mostrar_camionetas(permiso)
        for camioneta in lista_camionetas:
            if camioneta.numero == num_vehiculo:
                camioneta.kilometros = km
                print(f"Los nuevos datos del vehiculo son:\n----------\nkilometros: {camioneta.kilometros}(modificado)\nprecio: {camioneta.precio}\n----------")
    elif vehiculo == 4:
        mostrar_Camiones(permiso)
        for camion in lista_camiones:
            if camion.numero == num_vehiculo:
                camion.kilometros = km
                print(f"Los nuevos datos del vehiculo son:\n----------\nkilometros: {camion.kilometros}(modificado)\nprecio: {camion.precio}\n----------")
    elif vehiculo == 5:
        mostrar_colectivos(permiso)
        for colectivo in lista_colectivos:
            if colectivo.numero == num_vehiculo:
                colectivo.kilometros = km
                print(f"Los nuevos datos del vehiculo son:\n----------\nkilometros: {colectivo.kilometros}(modificado)\nprecio: {colectivo.precio}\n----------")
    elif vehiculo == 6:
        mostrar_acoplados(permiso)
        for acoplado in lista_acoplados:
            if acoplado.numero == num_vehiculo:
                acoplado.kilometros = km
                print(f"Los nuevos datos del vehiculo son:\n----------\nkilometros: {acoplado.kilometros}(modificado)\nprecio: {acoplado.precio}\n----------")
                

def agregar_detalles(vehiculo, num_vehiculo, detalle, permiso):

    if vehiculo == 1:
        mostrar_autos(permiso)
        for auto in lista_autos:
            if auto.numero == num_vehiculo:
                auto.detalle = detalle
                print(f"Los nuevos detalles del vehiculo son:\n----------\ndetalles: {auto.detalle}(modificado)\n----------")
                break
    elif vehiculo == 2:
        mostrar_motos(permiso)
        for moto in lista_motos:
            if moto.numero == num_vehiculo:
                moto.detalle = detalle
                print(f"Los nuevos detalles del vehiculo son:\n----------\ndetalles: {moto.detalle}(modificado)\n----------")
    elif vehiculo == 3:
        mostrar_camionetas(permiso)
        for camioneta in lista_camionetas:
            if camioneta.numero == num_vehiculo:
                camioneta.detalle = detalle
                print(f"Los nuevos detalles del vehiculo son:\n----------\ndetalles: {camioneta.detalle}(modificado)\n----------")
    elif vehiculo == 4:
        mostrar_Camiones(permiso)
        for camion in lista_camiones:
            if camion.numero == num_vehiculo:
                camion.detalle = detalle
                print(f"Los nuevos detalles del vehiculo son:\n----------\ndetalles: {camion.detalle}(modificado)\n----------")
    elif vehiculo == 5:
        mostrar_colectivos(permiso)
        for colectivo in lista_colectivos:
            if colectivo.numero == num_vehiculo:
                colectivo.detalle = detalle
                print(f"Los nuevos detalles del vehiculo son:\n----------\ndetalles: {colectivo.detalle}(modificado)\n----------")
    elif vehiculo == 6:
        mostrar_acoplados(permiso)
        for acoplado in lista_acoplados:
            if acoplado.numero == num_vehiculo:
                acoplado.detalle = detalle
                print(f"Los nuevos detalles del vehiculo son:\n----------\ndetalles: {acoplado.detalle}(modificado)\n----------")


def agregar_vehiculo(vehiculo):
    if vehiculo == 1:
        lista_autos.append(Autos(input("Marca: "), input("Color: "), input("Modelo: "), int(input("Kilometros: ")), int(input("Precio: ")), input("Detalles (ingresar 0 para dejarlo vacio): ")))
    if vehiculo == 2:
        lista_motos.append(Motos(input("Marca: "), input("Color: "), int(input("Kilometros: ")), int(input("Precio: ")), input("Detalles (ingresar 0 para dejarlo vacio): ")))
    if vehiculo == 3:
        lista_bicicletas.append(Bicicletas(input("Marca: "), input("Color: "), int(input("Rodado: ")), int(input("Precio: ")), input("Detalles (ingresar 0 para dejarlo vacio): ")))
    if vehiculo == 4:
        lista_camionetas.append(Camionetas(input("Marca: "), input("Color: "), input("Modelo: "), int(input("Kilometros: ")), int(input("Precio: ")), input("Detalles (ingresar 0 para dejarlo vacio): ")))
    if vehiculo == 5:
        lista_camiones.append(Camiones(input("Marca: "), input("Color: "), input("Modelo: "), int(input("Kilometros: ")), int(input("Precio: ")), input("Detalles (ingresar 0 para dejarlo vacio): ")))
    if vehiculo == 6:
        lista_colectivos.append(Colectivos(input("Marca: "), int(input("Cantidad de pasajeros soportados: ")), input("Color: "), input("Modelo: "), int(input("Kilometros: ")), int(input("Precio: ")), input("Detalles (ingresar 0 para dejarlo vacio): ")))
    if vehiculo == 7:
        lista_acoplados.append(Acoplados(input("Marca: "), input("Color: "), int(input("Precio: ")), input("Detalles (ingresar 0 para dejarlo vacio): ")))


def cambiar_precio(vehiculo, num_vehiculo, precio, permiso):
    if vehiculo == 1:
        mostrar_autos(permiso)
        for auto in lista_autos:
            if auto.numero == num_vehiculo:
                auto.precio = precio
                print(f"Los nuevos detalles del vehiculo son:\n----------\nprecio: {auto.precio}(modificado)\n----------")
    elif vehiculo == 2:
        mostrar_motos(permiso)
        for moto in lista_motos:
            if moto.numero == num_vehiculo:
                moto.precio = precio
                print(f"Los nuevos detalles del vehiculo son:\n----------\nprecio: {moto.precio}(modificado)\n----------")
    elif vehiculo == 3:
        mostrar_camionetas(permiso)
        for camioneta in lista_camionetas:
            if camioneta.numero == num_vehiculo:
                camioneta.precio = precio
                print(f"Los nuevos detalles del vehiculo son:\n----------\nprecio: {camioneta.precio}(modificado)\n----------")
    elif vehiculo == 4:
        mostrar_Camiones(permiso)
        for camion in lista_camiones:
            if camion.numero == num_vehiculo:
                camion.precio = precio
                print(f"El nuevo precio del vehiculo es:\n----------\nprecio: {camion.precio}(modificado)\n----------")
    elif vehiculo == 5:
        mostrar_colectivos(permiso)
        for colectivo in lista_colectivos:
            if colectivo.numero == num_vehiculo:
                colectivo.precio = precio
                print(f"Los nuevos detalles del vehiculo son:\n----------\nprecio: {colectivo.precio}(modificado)\n----------")
    elif vehiculo == 6:
        mostrar_acoplados(permiso)
        for acoplado in lista_acoplados:
            if acoplado.numero == num_vehiculo:
                acoplado.precio = precio
                print(f"Los nuevos detalles del vehiculo son:\n----------\nprecio: {acoplado.precio}(modificado)\n----------")

def agregar_usuario(nombre, contraseña, permiso):
    if permiso == 1:
        lista_invitados.append(Invitado(nombre, contraseña))
        print("Agregando usuario..."), sleep(1)
        print("Usuario agregado con éxito.")
    if permiso == 2:
        lista_empleados.append(Empleado(nombre, contraseña))
        print("Agregando usuario..."), sleep(1)
        print("Usuario agregado con éxito.")
