# Calcula o preço final de um produto com desconto
# Solicita o valor do desconto e o valor do produto ao usuário
des = input("informe o desconto")
n1 = input("informe o valor ")

# Calcula o valor descontado e o preço final
n2 = float(des) * float(n1)
n3 = n2 - (n2 / 100)

print("o preco final sera", n3)