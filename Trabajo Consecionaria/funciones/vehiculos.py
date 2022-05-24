
import random

vehiculos_a_la_venta = ["auto", "moto", "bicicleta", "camioneta", "colectivo", "camion", "acoplado"]
marcas = ["Ford", "VW", "Mercedes"]
marcas_bicicletas = ["BMX", "Olmo", "BMC"]
rodado = ["24", "26", "29"]
marcas_motos = ["Yamaha", "Honda", "Suzuki"]
colores = ["Azul", "Verde", "Rojo", "Amarillo", "Naranja", "Gris", "Marron"]

class Bicicletas:
    def __init__(self, numero, marca, color, rodado, precio, detalle=0, ):
        self.numero = numero
        self.marca = marca
        self.color = color
        self.rodado = rodado
        self.precio = precio
        self.detalle = detalle

class Motos:
    def __init__(self, numero, marca, color, kilometros, precio, detalle=0): 
        self.numero = numero
        self.marca = marca
        self.color = color
        self.kilometros = kilometros
        self.precio = precio
        self.detalle = detalle

class Autos:
    def __init__(self, numero, marca, color, modelo, kilometros, precio, detalle=0): 
        self.numero = numero
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.kilometros = kilometros
        self.precio = precio
        self.detalle = detalle

class Camionetas:
    def __init__(self, numero, marca, color, modelo, kilometros, precio, detalle=0): 
        self.numero = numero
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.kilometros = kilometros
        self.precio = precio
        self.detalle = detalle

class Colectivos:
    def __init__(self, numero, marca, pasajeros, color, modelo, kilometros, precio, detalle=0): 
        self.numero = numero
        self.marca = marca
        self.pasajeros = pasajeros
        self.color = color
        self.modelo = modelo
        self.kilometros = kilometros
        self.precio = precio
        self.detalle = detalle

class Camiones:
    def __init__(self, numero, marca, color, modelo, kilometros, precio, detalle=0): 
        self.numero = numero
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.kilometros = kilometros
        self.precio = precio
        self.detalle = detalle

class Acoplados:
    def __init__(self, numero, marca, color, precio, detalle=0):
        self.numero = numero
        self.marca = marca
        self.color = color
        self.precio = precio
        self.detalle = detalle