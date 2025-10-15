import re

# Função para calcular o IMC e classificar o resultado
# Solicita altura e peso ao usuário, calcula IMC e exibe classificação
def calcular_imc():
    altura = input("informe a sua altura :")
    altura = re.sub(r"[^0-9.,]", "", altura).replace(",", ".")
    altura = float(altura)
    if altura <= 0 or altura >= 3:
        print("É impossível você ter essa altura")
    peso = input("informe o seu peso :")
    peso = re.sub(r"[^0-9.,]", "", peso).replace(",", ".")
    peso = float(peso)

    if peso <= 0 or peso > 500:
        print("Impossível você ter esse peso")

    imc = peso/ (altura * altura)
    print(imc)
    if imc < 18.5:
        print("Você está muito magro")
    elif imc <= 24.9:
        print("Você está com o peso normal")
    elif imc <= 29.9:
        print("Você está com sobrepeso")
    else:
        print("Você está obeso")
