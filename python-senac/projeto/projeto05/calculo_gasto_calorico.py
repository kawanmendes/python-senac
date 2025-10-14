class gasto_calorico :
    def __init__(self, peso,tempo_minutos):
        self.peso = peso
        self.tempo_minutos = tempo_minutos
        self.met = self.opções_de_treino()
        self.tempo_horas = self.tempo_minutos / 60
        self.calorias_queimadas = self.calorias_queimadas()


    
    

    def calorias_queimadas(self):
        calorias_queimada1 = self.met *self.peso*self.tempo_horas
        return calorias_queimada1
    

    def __str__(self):
       return f"Peso: {self.peso} kg, Tempo: {self.tempo_horas:.2f} , Calorias queimadas: {self.calorias_queimadas:.2f}"
    

    def opções_de_treino(self):
     treinos = input("escolha umas das opções\a [1]caminhada leve \a [2]corrida \a [3]pular corda \a [4]sair \a escolha:")
     if treinos == "1":
        self.met = 3.3
        return self.met
     if treinos == "2":
        self.met = 8.3
        return self.met
     if treinos == "3":
        self.met = 12.3
        return self.met
     if treinos == "4":
        print("Saindo...")
    

