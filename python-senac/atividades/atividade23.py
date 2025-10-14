par = 0
impar = 0
for controle in range(1, 7):
    numero = float(input("digite o numero"))
    if numero % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print("A quantidade de numero par é:", par)
print("A quantidade de numero impar é:", impar)

