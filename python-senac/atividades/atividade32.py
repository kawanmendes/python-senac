def par(numero):
    if numero % 2 == 0:
        print(f"o numero {numero} e par")
    else:
        print(f"o numero {numero} e impar")


numero = int(input("insira o numero"))
par(numero)