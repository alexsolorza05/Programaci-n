class Cliente:
    def __init__(self, nombre ,apellido, DNI, numeroDeCliente):
        self._nombre = nombre  
        self._apellido = apellido
        self.__DNI = DNI
        self.__numeroDeCliente = numeroDeCliente

@property
def nombre(self):
    return self.nombre

@nombre.setter
def nombre(self, nuevo_nombre):
    if nuevo_nombre != "":
            self._nombre = nuevo_nombre
    else:
        print("El nombre no puede estar vacío")

@property
def apellido(self):
    return self._apellido

@apellido.setter
def apellido(self, nuevo_apellido):
    if nuevo_apellido != "":
        self._apellido = nuevo_apellido
    else:
        print("El apellido no puede estar vacío")

@property
def DNI(self):
    return self.__DNI

@DNI.setter
def dni(self, nuevo_dni):
    if nuevo_dni.isdigit() and len(nuevo_dni) >= 7:
        self._dni = nuevo_dni
    else:
        print("DNI inválido")

@property
def numeroDeCliente(self):
    return self.__numeroDeCliente

@numeroDeCliente.setter
def numeroDeCliente(self, nuevo_numero: int):
    if nuevo_numero > 0:
        self._numero_de_cliente = nuevo_numero
    else:
        print("El número de cliente debe ser mayor a 0.")