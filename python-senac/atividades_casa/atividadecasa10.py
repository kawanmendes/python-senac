class carro:
    def __init__(self, medole, velocidade):
        self.medole = medole
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10
        print(f'o carro {self.medole} esta a {self.velocidade} km/h')

carro1 = carro("porche", 270)
carro1.acelerar()        