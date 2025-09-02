contador = 0
nota = 0
resposta = 0
media = 0
while contador != 4:
    nota = int(input("informe a nota:"))
    if nota > 0 and nota <=10:
        resposta = resposta + nota
        contador += 1

    else:
        print("resposta invalida")

media = resposta / 4
print("a media é", media)