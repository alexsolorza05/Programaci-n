from cliente import Cliente
from cuenta import Cuenta_bancaria
from cajero import Cajero
from interfaz import Interfaz

def main():
    c1 = Cliente("Lucas", "Gómez", "40123456", 1001)
    c2 = Cliente("Ana", "Martínez", "38987654", 1002)

    cta1 = Cuenta_bancaria("10001", "Activa", 25000.0, c1)
    cta2 = Cuenta_bancaria("10002", "Activa", 100000.0, c2)

    cajero = Cajero(101, 500000.0)
    cajero.agregar_cuenta(cta1)
    cajero.agregar_cuenta(cta2)

    app = Interfaz(cajero)
    app.iniciar()

if __name__ == "__main__":
    main()