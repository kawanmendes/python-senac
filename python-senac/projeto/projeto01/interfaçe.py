from projeto.projeto01.calcular_gasto_calorico import *
from projeto.projeto01.calculo_da_frequencia_cardica import *
from projeto.projeto01.calculo_de_imc import *

# Função de menu principal para escolher cálculo desejado
def menu():
    while True:
        opcoes = int(input('informe qual opcao vc quer fazer : \a [1]calcular gasto calorico \a [2]calcular frequencia cardiaca \a [3]calcular o imc \a[4]sair :'))
        if opcoes == 1:
            opcoes_de_treino()
            break
        elif opcoes == 2:
            frequencia_cardiaca()
            break
        elif opcoes == 3:
            calcular_imc()
            break
        elif opcoes == 4:
            print('saindo....')
            break
        else:
            print(f'resposta invalida')
            break

# Executa o menu principal
menu()

