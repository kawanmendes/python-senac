import re
def frequencia_cardiaca():
        idade = input("Informe sua idade: ")
        idade = re.sub(r"[^0-9]", "", idade)
        if idade.isdigit() and int(idade) > 0:
            idade = int(idade)
        else:
            print("Por favor, digite uma idade válida.")
        bmp = 220 - idade
        print(f"Sua frequência cardíaca máxima é: {bmp} bpm")    
        queima_gordura1 = bmp * 0.5
        queima_gordura2 = bmp * 0.7
        print(f"Sua zona de queima de gordura é entre: {queima_gordura1:} e {queima_gordura2:} bpm")
        zona_cardio1 = bmp * 0.7
        zona_cardio2 = bmp * 0.85 , 
        print(f"Sua zona de queima de gordura é entre: {zona_cardio1:} e {zona_cardio2:} bpm")


