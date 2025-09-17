from projeto.projeto04.projeto04 import *

class Menu:
    def mostrar_menu(self):
        while True:
            print("\n--- MENU PRINCIPAL ---")
            print("1. Cadastrar Leitor")
            print("2. Listar Leitores")
            print("3. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                id = input("ID do leitor: ")
                nome = input("Nome do leitor: ")
                telefone = input("Telefone do leitor: ")
                Leitor.cadastrar_leitor(id, nome, telefone)
            elif escolha == "2":
                Leitor.listar_leitores()
            elif escolha == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    