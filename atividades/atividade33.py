def imc(a, b):
    return (a/(b*b))

a = float(input("informe o peso"))
b = float(input("informe a altura"))
imc(a, b)
print("o imc é ", imc(a, b))