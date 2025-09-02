import random


def jogo_adivinhacaoFacil():

    numero = random.randint(1,100)
    print(numero)
    n1 = 0

    while n1 != numero:
        n1 = int(input("informe um numero"))
        if n1 == numero:
            print("VC ACERTOU")
            break
        if n1 < numero:
            print("um pouco maior")
        if n1 > numero:
            print("um pouco menor")
        
        
def jogo_adivinhacaoDificil():
    numero = random.randint(1, 300)
    contador = 5        
    while contador > 0:
        n1 = int(input(f"informe um numero (tentativas restantes: {contador}): "))

        if n1 == numero:
            print("VC ACERTOU")
            break
        if n1 < numero:
            print("um pouco maior")
        if n1 > numero:
            print("um pouco menor")
        contador -= 1    
       
    while contador == 0:
        print(f"GAME OVER! o numero era {numero}")
        break           
                
    
def dificuldade():
    opcao = input("escolha uma opcao [1] nivel facil [2] nivel dificil [3] sair: ")
    if opcao == "1":
        jogo_adivinhacaoFacil()
    elif opcao == "2":
        jogo_adivinhacaoDificil()
    elif opcao == "3":
        print("JOGO ENCERRADO")
        exit()
    else:
        print("Opcao invalida")
        exit()

dificuldade()
     


