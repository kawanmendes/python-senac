valorp = float(input("informe o valor do produto"))

if valorp <= 100:
    print("produto sem desconto")

else:
    valorf = (valorp) -(valorp * 0.1 )
    print("o valor e de" ,valorf)
