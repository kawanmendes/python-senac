import re
def calcular_imc():
    altura = input("informe a sua altura :")
    altura = re.sub(r"[^0-9.,]", "", altura).replace(",", ".")
    altura = float(altura)
    if altura <= 0 or altura >= 3:
        print("e impossivel vc ter essa altura")    
    peso = input("informe o seu peso :")
    peso = re.sub(r"[^0-9.,]", "", peso).replace(",", ".")
    peso = float(peso)

    if peso <= 0 or peso > 500:
        print("impossivel vc ter esse peso")

    imc = peso/ (altura * altura)
    print(imc)
    if imc < 18.5 :
        print("vc esta muito magro")
    elif imc <= 24.9 :
        print("vc esta com o peso normal")
    elif imc <= 29.9:
        print("vc esta com sobrepeso")
    else:
        print("vc esta obeso")    
calcular_imc()
