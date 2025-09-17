class cliente:
    def __init__(self,nome,cpf,email):
        self.nome = nome
        self.cpf = cpf
        if "@" not in email:
            raise ValueError("Email inválido")
        elif "." not in email.split("@")[-1]:
            raise ValueError("Email inválido")
        else:
            self.email = email

class conta_bancaria :
    
    def __init__(self,numero,cliente,saldo = 0.0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo 

    def depositar(self,valor):
        self.saldo += valor
        
    def sacar (self,valor):
     if valor <= self.saldo:
         self.saldo -= valor
         return f'o saque de {valor} foi realizado da conta'
     else:
         return f'o valor e insuficiente '
    def exibir_dados(self):
        return f'conta numero: {self.numero}, cliente: {self.cliente.nome}, cpf: {self.cliente.cpf}, email: {self.cliente.email}' 
         
    def __str__(self):
        return f" Saldo: {self.saldo}"
            


conta1 = cliente('kawan', '123.456.789-00', 'kawan@email.com')
conta_bancaria1 = conta_bancaria('001', conta1)
conta_bancaria1.depositar(1000)
print(conta_bancaria1)
print(conta_bancaria1.exibir_dados())
print(conta_bancaria1.sacar(500))
print(conta_bancaria1)

conta2 = cliente('kawan', '123.45688888.789-00', 'kawan@email.com')
conta_bancaria1 = conta_bancaria('002', conta2)
conta_bancaria1.depositar(1000)
print(conta_bancaria1)
print(conta_bancaria1.exibir_dados())
print(conta_bancaria1.sacar(500))
print(conta_bancaria1)