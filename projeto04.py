class Leitor :
    leitores = []

    def __init__(self, id, nome , telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone
       
    def cadastrar_leitor(self ,id , nome , telefone):
        novo_leitor = Leitor(id , nome , telefone)
        self.leitores.append(novo_leitor)
        for i in self.leitores:
            print(i)
       

    def atualizar_leitor(self, id , nome , telefone):
        for leitor in self.leitores:
            if leitor.id == id:
                leitor.cadastrar_leitor()
               
     
    def deletar_leitor():
        pass
    def consultar_leitor():
        pass


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
leitor01.atualizar_leitor(1, 'marthelo', 6582984)
print(leitor01)