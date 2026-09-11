from cuenta import Cuenta_bancaria

class Cajero:
    def __init__(self, idCajero, dineroDisponible):
        self.__idCajero = idCajero
        self.__dineroDisponible = dineroDisponible
        self.__cuentas = {}

    @property
    def idCajero(self):
        return self.__idCajero

    @idCajero.setter
    def idCajero(self, nuevo_id):
        self.__idCajero = nuevo_id

    @property 
    def dineroDisponible(self):
        return self.__dineroDisponible

    @dineroDisponible.setter
    def dineroDisponible(self, dinero_disponible):
        if dinero_disponible >= 0:
            self.__dineroDisponible = dinero_disponible
        else:
            print("El dinero disponible no puede ser negativo")

    def agregar_cuenta(self, cuenta):
        self.__cuentas[cuenta.nro_cuenta] = cuenta

    def obtener_cuenta(self, nro_cuenta):
        return self.__cuentas.get(nro_cuenta)

    def realizar_extraccion(self, cuenta, monto):
        if monto > self.__dineroDisponible:
            return False
        
        if cuenta.extraer(monto):
            self.__dineroDisponible -= monto
            return True
        return False

    def realizar_deposito(self, cuenta, monto):
        if cuenta.depositar(monto):
            self.__dineroDisponible += monto
            return True
        return False