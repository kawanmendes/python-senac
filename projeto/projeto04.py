class Leitor :
    
    leitores = []


    def __init__(self, id, nome , telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.leitores.append(self)

       
    def cadastrar_leitor(self ,id , nome , telefone):
        novo_leitor = Leitor(id , nome , telefone)
        return novo_leitor
    
    def atualizar_leitor(self, id, nome, telefone):
        for leitor in self.leitores:
            if leitor.id == id:
                leitor.nome = nome
                leitor.telefone = telefone
                return True
        return False
                
    def listar_leitores(self):
        for leitor in self.leitores:
            print(leitor)


    def deletar_leitor(self, id ):
        for leitor in Leitor.leitores:
            if leitor.id == id :
                Leitor.leitores.remove(leitor)
                print(f'o usuario com o id {id} foi removido')
                return True
        return False    
       
           

    def consultar_leitor(self , id):
        for leitor in Leitor.leitores:
            if leitor.id == id :
                print(f'o leitor foi encontrado {leitor}')
                return True
        print(f'o usuario nao foi encontrado')
        return False

    def __str__(self):
        return  f"ID: {self.id}, Nome: {self.nome}, Telefone: {self.telefone}"
class Livro:
   def __init__(self,isbn,titulo,autores,edicao,qtd_exemplar):
       self.isbn = isbn
       self.titulo = titulo
       self.autores = autores
       self.edicao = edicao
       self.qtd_exemplar = qtd_exemplar
       pass
   

class Emprestimo :
     def __init__(self, data_emprestimo, data_devolucao, livro : Livro ,leitor : Leitor):
       self.data_emprestimo = data_emprestimo
       self.data_devolucao = data_devolucao
       self.livro = livro
       self.leitor = leitor


leitor01 = Leitor(1,'rubinho marthelo', 6666666)
leitor01.cadastrar_leitor(2 ,'kawan' , 545454)
leitor01.consultar_leitor(2)


    