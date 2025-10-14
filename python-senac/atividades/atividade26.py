import random
numero = random.randint(1,100)
print(numero)

n1 = int(input("informe um numero"))

while n1 == numero:
    if n1 == numero:
        print("VC ACERTOU")
        exit()
    if n1 < numero:
        print("um pouco maior")
    if n1 > numero:
        print("um pouco menor")
    n1 = int(input("informe um numero"))