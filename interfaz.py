class Interfaz:
    def __init__(self, cajero):
        self.__cajero = cajero
        self.__cuenta_actual = None

    def iniciar(self):
        while True:
            print("CAJERO: {self.__cajero.idCajero}")
            print("1. Ingresar Número de Cuenta")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                if self._autenticar():
                    self._menu_principal()
            elif opcion == "2":
                print("Operación finalizada")
                break

    def _autenticar(self):
        nro_cuenta = input("Ingrese su Número de Cuenta: ")
        cuenta = self.__cajero.obtener_cuenta(nro_cuenta)

        if not cuenta:
            input("Número de cuenta no encontrado. Ingrese nuevamente")
            return False

        num_cliente = int(input("Ingrese su Número de Cliente: "))

        if cuenta.titular and cuenta.titular.numeroDeCliente == num_cliente:
            self.__cuenta_actual = cuenta
            return True
        else:
            input("Número de cliente incorrecto. Ingrese nuevamente")
            return False

    def _menu_principal(self):
        while True:
            titular = self.__cuenta_actual.titular
            nombre_completo = f"{titular.nombre} {titular.apellido}" if titular else "Cliente"

            print(f"Bienvenido/a, {nombre_completo}")
            print(f"Estado de la cuenta: {self.__cuenta_actual.estadoDe_cuenta}")
            print(f"Saldo actual: ${self.__cuenta_actual.saldo:.2f}")
            print("1. Consultar Saldo")
            print("2. Depositar")
            print("3. Extraer")
            print("4. Salir/Cerrar Sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(f"Su saldo actual es: ${self.__cuenta_actual.saldo:}")
                input("Intente nuevamente")

            elif opcion == "2":
                monto = float(input("Ingrese monto a depositar: $"))
                if self.__cajero.realizar_deposito(self.__cuenta_actual, monto):
                    print("Depósito realizado con éxito")
                else:
                    print("Operación no permitida o monto inválido.")
                input("Intente nuevamente")

            elif opcion == "3":
                monto = float(input("Ingrese monto a extraer: $"))
                if self.__cajero.realizar_extraccion(self.__cuenta_actual, monto):
                    print("Extracción exitosa")
                else:
                    print("Fondos insuficientes en la cuenta o dinero de cajero insuficiente.")
                input("Intente nuevamente")

            elif opcion == "4":
                self.__cuenta_actual = None
                break