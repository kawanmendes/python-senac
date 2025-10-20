import re
def gasto_calorico(met):
        peso = input("Informe sua peso: ")
        peso = re.sub(r"[^0-9]", "", peso)
        if peso.isdigit() and int(peso) > 0:
            peso = int(peso)
        else:
            print("Por favor, digite uma peso válida.")

        tempo_minutos = input("Informe seu tempo (em minutos) do seu treino: ")
        tempo_minutos = re.sub(r"[^0-9]", "", tempo_minutos)
        if tempo_minutos.isdigit() and float(tempo_minutos) > 0:
            tempo_minutos = float(tempo_minutos)
        else:
            print("Por favor, digite o tempo correto.")  
        tempo_horas = tempo_minutos / 60      
        print(round(tempo_horas, 2))
        calorias_queimadas = met * peso * tempo_horas
        print(round(calorias_queimadas, 5))
        
def opções_de_treino():
     treinos = input("escolha umas das opções\a [1]caminhada leve \a [2]corrida \a [3]pular corda \a [4]sair \a escolha:")
     if treinos == "1":
        gasto_calorico(met=3.3)  
     if treinos == "2":
        gasto_calorico(met=8.3) 
     if treinos == "3":
        gasto_calorico(met=12.3)  
     if treinos == "4":
        print("Saindo...")
    
opções_de_treino()     
            
