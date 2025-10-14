soma = 0
cont18 =0
maior_idade = 0
cont5 = 0
for controle in range(1, 11):
    idade=float(input("informe a idade:"))
    soma = soma + idade
    if idade > 18:
        cont18 = cont18 + 1
    elif idade < 5 :
        cont5 = cont5 = 1
    if idade > maior_idade:
        maior_idade = idade

media = soma / 10

print("A média das idades é:", media)

print("A quantidade de pessoas com mais de 18 anos é:", cont18)

print("A quantidade de pessoas com menos de 5 anos é:", cont5)

print("A maior idade é:", maior_idade)