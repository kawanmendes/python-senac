# Converte temperatura de Celsius para Fahrenheit
# Solicita temperatura em Celsius ao usuário
tc = input("informe a temperatura em ceusos")

c1 = 32
c2 = 1.8

# Realiza o cálculo da conversão
# Fórmula: F = C * 1.8 + 32
tf = float(tc) * c2 + c1

print("o valor em F é", tf)
