numero = int(input("digite um numero:"))
while numero >= 0:
    contador = 0
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            contador += 1
    if contador == 2:
            print("numero primo")
    else:
            print("numero nao e primo")
    numero = int(input("digite um numero:"))