class lampada :
    def __init__(self,cor,potencia,ligado ):
        self.cor = cor
        self.potencia = potencia
        self.ligado = ligado
    def ligado(self):
        self.ligado = False

    def desligado(self):
        self.desligado = True
    def alternar(self):
        if self.ligado == False:
            self.ligado = True
            self.desligado = False
    def __str__(self):
        estado = 'ligada' if self.ligado else 'desligada'
        return f'sua lampada e da cor {self.cor}, com potencia de {self.potencia}W e esta {estado}'        

lampada1 = lampada(cor=input("informe a cor da lampada:"), potencia=int(input("informe a potencia da lampada:")), ligado=False)
print(lampada1)
lampada1.alternar()
print(lampada1)