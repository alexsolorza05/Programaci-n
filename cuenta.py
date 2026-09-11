from cliente import Cliente

class Cuenta_bancaria:
    def __init__(self, nro_cuenta, estadodeCuenta, SALDO, titular):
        self.__nro_cuenta = nro_cuenta
        self.__estadoDe_cuenta = estadodeCuenta
        self.__saldo = SALDO
        self.__titular = titular

    @property
    def nro_cuenta(self):
        return self.__nro_cuenta

    @nro_cuenta.setter
    def nro_cuenta(self, nuevo_nro):
        self.__nro_cuenta = nuevo_nro

    @property
    def estadoDe_cuenta(self):
        return self.__estadoDe_cuenta

    @estadoDe_cuenta.setter
    def estadoDe_cuenta(self, nuevo_estado):
        self.__estadoDe_cuenta = nuevo_estado

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("El saldo no puede ser negativo.")

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    def depositar(self, monto):
        if monto > 0 and self.__estadoDe_cuenta.lower() == "activa":
            self.__saldo += monto
            return True
        return False

    def extraer(self, monto):
        if 0 < monto <= self.__saldo and self.__estadoDe_cuenta.lower() == "activa":
            self.__saldo -= monto
            return True
        return False