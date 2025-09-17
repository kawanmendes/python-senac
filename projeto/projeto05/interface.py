from calculo_imc import *
from calculo_frequencia_cardiaca import *
from calculo_gasto_calorico import *


class Menu :
   
    def menu(self):
        print ('informe qual opcao vc quer fazer : \a [1]calcular gasto calorico \a [2]calcular frequencia cardiaca \a [3]calcular o imc \a[4]sair :')
        opcoes = input('informe oq deseja fazer :')

        while True:
            
            if opcoes == "1":
               gasto_calorico1 = gasto_calorico(peso=float(input("informe seu peso em kg:")), tempo_minutos=float(input("informe o tempo em minutos:")))
               print(gasto_calorico1)
            elif opcoes == "2":
               Frequencia_cardiaca1 = Frequencia_cardiaca(idade=int(input("informe sua idade:")), queima_gordura=0, zona_cardio=0)
               print(Frequencia_cardiaca1)
               print(Frequencia_cardiaca1.calculo_queima_gordura())
               print(Frequencia_cardiaca1.calculo_gasto_calorico())
            elif opcoes == "3":
               imc1 = Calcular_imc(altura=float(input("informe sua altura em metros:")), peso=float(input("informe seu peso em kg:")))
               print(imc1)
               print(imc1.clasificacao_imc())

            elif opcoes == "4":
               print("Saindo...")
               break
            else:
               print("Opção inválida. Tente novamente.")
Menu().menu()