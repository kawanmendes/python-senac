class conta:
    def __init__(self, usuario, saldo = 0):
        self.usuario =usuario
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor    
        print(f"o deposito de {valor}, e o saldo atual e de {self.saldo}")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"o saque de {valor} saldo atual : {self.saldo} ")

        else:
            print("saldo invalido")

c1 = conta("João")
c1.depositar(100)
c1.saque(30)
c1.saque(100)        