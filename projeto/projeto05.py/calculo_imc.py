class Calcular_imc :
    def __init__(self, altura, peso):
        self.altura = float(altura)
        self.peso = float(peso)
        self.imc = self.peso /(self.altura*self.altura)


    def __str__(self):
        return f"o seu imc e {self.imc:.2f}"
    
    def clasificacao_imc(self):
        if self.imc < 18.5:
            return f"vc esta muito magro"
        elif self.imc <= 24.9:
            return f'vc esta com o peso normal'
        elif self.imc <= 29.9:
            return f"vc esta com sobrepeso"
        else:
            return f'vc esta obeso'
        
      

