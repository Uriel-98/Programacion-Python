import random
from funciones.vehiculos import *


lista_autos = []
lista_motos = []
lista_bicicletas = []
lista_camionetas = []
lista_colectivos = []
lista_camiones = []
lista_acoplados = []

def mostrar_autos(permiso):
    permiso = permiso
    cantidad_autos = random.randrange(1, 6)
    for i in range(cantidad_autos):
        lista_autos.append(Autos(i, random.choice(marcas), random.choice(colores), random.randrange(1985, 2022), random.randrange(3000, 350000), random.randrange(200000, 3000000), 0))

    for auto in lista_autos:
        print(f"---- {auto.numero} ----")
        print("Marca:", auto.marca)
        print("Modelo:", auto.modelo)
        print("Color:", auto.color)
        print("Kilómetros:", auto.kilometros)
        if auto.detalle == 0:
            print("Sin detalles.")
        else:
            print("Detalles:", auto.detalle)
        if permiso == 2 or permiso == 3:
            print("Precio: $", auto.precio)
        print("-------------------------------------------------------------")

def mostrar_motos(permiso):
    cantidad_motos = random.randrange(1, 6)
    for i in range(cantidad_motos):
        lista_motos.append(Motos(i, random.choice(marcas), random.choice(colores), random.randrange(3000, 350000), random.randrange(200000, 3000000), 0))

    for moto in lista_motos:
        print(f"---- {moto.numero} ----")
        print("Marca:", moto.marca)
        print("Color:", moto.color)
        print("Kilómetros:", moto.kilometros)
        if moto.detalle == 0:
            print("Sin detalles.")
        else:
            print("Detalles:", moto.detalle)
        if permiso == 2 or permiso == 3:
            print("Precio: $", moto.precio)
        print("-------------------------------------------------------------")

def mostrar_bicicletas(permiso):
    cantidad_bicicletas = random.randrange(1, 6)
    for i in range(cantidad_bicicletas):
        lista_bicicletas.append(Bicicletas(i, random.choice(marcas), random.choice(colores), random.choice(rodado), random.randrange(3000, 350000), 0))
        
    for bicicleta in lista_bicicletas:
        print(f"---- {bicicleta.numero} ----")    
        print("Marca:", bicicleta.marca)
        print("Color:", bicicleta.color)
        print("Kilómetros:", bicicleta.rodado)
        if bicicleta.detalle == 0:
            print("Sin detalles.")
        else:
            print("Detalles:", bicicleta.detalle)
        if permiso == 2 or permiso == 3:
            print("Precio: $", bicicleta.precio)
        print("-------------------------------------------------------------")

def mostrar_camionetas(permiso):
    cantidad_camionetas = random.randrange(1, 6)
    for i in range(cantidad_camionetas):
        lista_camionetas.append(Camionetas(i, random.choice(marcas), random.choice(colores), random.randrange(1985, 2022), random.randrange(3000, 350000), random.randrange(200000, 3000000), 0))

    for camioneta in lista_camionetas:
        print(f"---- {camioneta.numero} ----")
        print("Marca:", camioneta.marca)
        print("Color:", camioneta.color)
        print("Kilómetros:", camioneta.modelo)
        print("Kilómetros:", camioneta.kilometros)
        if camioneta.detalle == 0:
            print("Sin detalles.")
        else:
            print("Detalles:", camioneta.detalle)
        if permiso == 2 or permiso == 3:
            print("Precio: $", camioneta.precio)
        print("-------------------------------------------------------------")

def mostrar_colectivos(permiso):
    cantidad_colectivos = random.randrange(1, 6)
    for i in range(cantidad_colectivos):
        lista_colectivos.append(Colectivos(i, random.choice(marcas), random.randrange(10, 200) ,random.choice(colores), random.randrange(1985, 2022), random.randrange(3000, 350000), random.randrange(200000, 3000000), 0))

    for colectivo in lista_colectivos:
        print(f"---- {colectivo.numero} ----")
        print("Marca:", colectivo.marca)
        print("Color:", colectivo.color)
        print("Pasajeros:", colectivo.pasajeros)
        print("Kilómetros:", colectivo.modelo)
        print("Kilómetros:", colectivo.kilometros)
        if colectivo.detalle == 0:
            print("Sin detalles.")
        else:
            print("Detalles:", colectivo.detalle)
        if permiso == 2 or permiso == 3:
            print("Precio: $", colectivo.precio)
        print("-------------------------------------------------------------")

def mostrar_Camiones(permiso):
    cantidad_camiones = random.randrange(1, 6)
    for i in range(cantidad_camiones):
        lista_camiones.append(Camiones(i, random.choice(marcas), random.choice(colores), random.randrange(1985, 2022), random.randrange(3000, 350000), random.randrange(200000, 3000000), 0))
    
    for camion in lista_camiones:
        print(f"---- {camion.numero} ----")
        print("Marca:", camion.marca)
        print("Color:", camion.color)
        print("Kilómetros:", camion.modelo)
        print("Kilómetros:", camion.kilometros)
        if camion.detalle == 0:
            print("Sin detalles.")
        else:
            print("Detalles:", camion.detalle)
        if permiso == 2 or permiso == 3:
            print("Precio: $", camion.precio)
        print("-------------------------------------------------------------")

def mostrar_acoplados(permiso):
    cantidad_acoplados = random.randrange(1, 6)
    
    for i in range(cantidad_acoplados):
        lista_acoplados.append(Acoplados(i, random.choice(marcas), random.choice(colores), random.randrange(200000, 3000000), 0))

    for acoplado in lista_acoplados:
        print(f"---- {acoplado.numero} ----")
        print("Marca:", acoplado.marca)
        print("Color:", acoplado.color)
        if acoplado.detalle == 0:
            print("Sin detalles.")
        else:
            print("Detalles:", acoplado.detalle)
        if permiso == 2 or permiso == 3:
            print("Precio: $", acoplado.precio)
        print("-------------------------------------------------------------")