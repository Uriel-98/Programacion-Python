
lista_invitados = []
lista_empleados = []

class Invitado:
    usuario_default = "invitado"
    contraseña_default = "invitado123"
    
    def __init__(self, nombre_usuario, contraseña):
        self.usuario = nombre_usuario
        self.contraseña = contraseña
        
    
class Empleado:
    usuario_default = "empleado"
    contraseña_default = "empleado123"

    def __init__(self, nombre_usuario, contraseña):
        self.usuario = nombre_usuario
        self.contraseña = contraseña
        


class Admin:
    usuario_default = "admin"
    contraseña_default = "admin123"

    def __init__(self, nombre_usuario, contraseña):
        self.usuario = nombre_usuario
        self.contraseña = contraseña

