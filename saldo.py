class Conta():
    def __init__(self, _numeros, _titular, __saldo):
        self._numeros = _numeros
        self._titular = _titular
        self.__saldo = __saldo
    def depositar(self, valor):
        self.__saldo += valor
        print(f"o salvo atual de conta {self._numeros} e de r$ {self.__saldo}")
    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"o __saldo atual de conta {self._numeros} e de R$ {self.__saldo}")
        else:
            print("__saldo insuficiente")
    def mostrar(self):
        print(f"o saldo atual da conta {self._numeros} e de R$ {self.__saldo}")
if __name__ == "__main__":
    conta1 = Conta(1234, "edril", 1000)
    conta1.depositar(1240)
    conta1.sacar (200)
    conta1.mostrar