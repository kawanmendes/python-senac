from projeto04 import *

class Menu:
    def mostrar_menu(self):

        while True:
            print("\n-------------MENU----------")
            print(" menu livros [1]")
            print("menu leitores [2]")
            print("menu emprestimos[3]")       
          
            menu_global = input("escolha a opção:")

            if menu_global == '2' :
                    print("\n--- MENU LEITORES ---")
                    print("1. Cadastrar Leitor")
                    print("2. Listar Leitores")
                    print("3. atualizar leitor")
                    print("4. deletar leitor")
                    print("5. consultar leitor")
                    print("6. Sair")
                    escolha = input("Escolha uma opção: ")

                    if escolha == '1':
                        id = input("ID do leitor: ")
                        nome = input("Nome do leitor: ")
                        telefone = input("Telefone do leitor: ")
                        Leitor.cadastrar_leitor(Leitor,id, nome, telefone)
            
                    elif escolha == "2":
                        Leitor.listar_leitores(Leitor)
                    elif escolha == '3':
                        id = input("qual o id do leitor q deseja atualizar: ")
                        nome = input("Nome do leitor: ")
                        telefone = input("Telefone do leitor: ")
                        Leitor.atualizar_leitor(Leitor,id, nome, telefone)   
                    elif escolha == "4":
                        id = input("informe o id do leitor desejado deletar :")
                        Leitor.deletar_leitor(Leitor,id)
                    elif escolha == "5":
                        id = input("informe o id do leitor desejado consultar :")
                        Leitor.consultar_leitor(Leitor, id)
                    elif escolha == '6':
                         print("saindo......")
                         break    
            if menu_global == '1' :
                print("\n--- MENU LIVROS ---")
                print("1. Cadastrar livro")
                print("2. Listar livros")
                print("3. atualizar livros")
                print("4. deletar livros")
                print("5. consultar livros")
                print("6. verificar disponibilidade")
                print("7. Sair")
                escolha = input("Escolha uma opção: ")
                if escolha == '1':
                        isbn = input("isbn do livro: ")
                        titulo = input("titulo do livro: ")
                        autores = input("autores do livro: ")
                        edicao = input("edicao do livro: ")
                        qtd_exemplar = input("qtd_exemplar do livro: ")
                        Livro.cadastrar_livro(Livro,isbn,titulo,autores,edicao,qtd_exemplar)
            
                elif escolha == "2":
                        Livro.lista_livros(Livro)
                elif escolha == '3':
                        isbn = input("isbn do livro q vc deseja atualizar: ")
                        titulo = input("titulo do livro: ")
                        autores = input("autores do livro: ")
                        edicao = input("edicao do livro: ")
                        qtd_exemplar = input("qtd_exemplar do livro: ")
                        Livro.atualizar_livro(Livro,isbn,titulo,autores,edicao,qtd_exemplar)  


                elif escolha == "4":
                        isbn = input("informe o isbn do livro desejado deletar :")
                        Livro.deletar_livro(Livro,isbn)
                elif escolha == "5":
                        isbn = input("informe o isbn do leitor desejado consultar :")
                        Livro.consultar_livro(Livro,isbn)
                elif escolha == '6' :
                        isbn = input("informe o isbn do livro para verificar a disponibilidade :")
                        Livro.verificar_disponibilidade(Livro,isbn)
                elif escolha == '7':
                         print("saindo......")
            if menu_global =='3':   
                    print("\n--- MENU EMPRESTIMOS ---")
                    print("1. registrar emprestimo")
                    print("2. registrar devolucao")
                    print("3. listar emprestimos")
                    print("4. sair")
                    escolha = input("Escolha uma opção: ")   

                    if escolha == '1':
                        id_leitor = int(input("Digite o ID do leitor: "))
                        isbn_livro = input("Digite o ISBN do livro: ")
                        data_emprestimo = input("Data do empréstimo (dd/mm/aaaa): ")
                        data_devolucao = input("Data de devolução (dd/mm/aaaa): ")
                            
                        leitor = next((l for l in Leitor.leitores if l.id == id_leitor), None)
                        
                        livro = next((l for l in Livro.livros if l.isbn == isbn_livro), None)

                        if leitor and livro:
                                Emprestimo.registrar_emprestimo(Emprestimo,data_emprestimo, data_devolucao, livro, leitor)
                        else:
                                print("Leitor ou livro não encontrado.")

                    if escolha == '2':
                        isbn_livro = input("Digite o ISBN do livro a ser devolvido: ")
                        livro = next((l for l in Livro.livros if l.isbn == isbn_livro), None)
                        if livro:
                            Emprestimo.registrar_devolucao(Emprestimo,livro)
                        else:
                            print("Livro não encontrado.")          

                    if escolha == '3':
                          Emprestimo.lista_emprestimos(Emprestimo)  
                    if escolha == '4':
                          print("saindo...")
                          break                
Menu().mostrar_menu()