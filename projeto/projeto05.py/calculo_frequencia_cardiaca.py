class Frequencia_cardiaca :
    def __init__(self,idade , queima_gordura,zona_cardio):
        self.idade = idade
        self.queima_gordura = queima_gordura
        self.zona_cardio = zona_cardio
        self.bmp = 220 - self.idade


    def __str__(self):
        return f'seu bmp e {self.bmp}'
    
    def calculo_queima_gordura(self,):
       queima_gordura1 = self.bmp * 0.5
       queima_gordura2 = self.bmp * 0.7
       return f'sua queima de gordura e entre {queima_gordura1} e {queima_gordura2}'
    
    def calculo_gasto_calorico(self):
        gasto_calorioco1 = self.bmp * 0.7
        gasto_calorioco2 = self.bmp * 0.85
        return f'seu gasto calorico e entre {gasto_calorioco1}  e  {gasto_calorioco2}'
    



