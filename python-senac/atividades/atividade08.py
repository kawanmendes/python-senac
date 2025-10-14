salario = float(input("digite seu sarario"))

if salario < 1500:
    aumento = 0.2

else:
    aumento = 0.1


salariofinal = (salario) +((salario) * aumento)

print("o valor foi de" ,salariofinal)