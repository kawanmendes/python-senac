salario = float(input("informe o salario"))

if salario <= 1900:
    imposto = ("isento ")

elif salario <= 2800:
    imposto = salario * 0.075
elif salario <= 3700:
    imposto = salario * 0.15
else:
    imposto = salario * 0.225

print("o imposto e ", imposto)