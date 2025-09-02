n1 = float(input("digite o primeiro valor:"))
n2 = float(input("digite o segundo valor:"))
operacao = str(input("escolha a operacao entre * , -, / ,+ : "))
resposta = 0
if operacao == "*":
    resposta = n1 * n2
elif operacao  == "/":
    resposta = n1 / n2
elif operacao == "-":
    resposta = n1 - n2
elif operacao == "+":
    resposta = n1 + n2

print(resposta)
