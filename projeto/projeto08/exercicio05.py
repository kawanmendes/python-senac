import datetime
class Autor :
    def __init__(self,nome,nacionalidade,ano_nascimento):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.ano_nascimento = ano_nascimento
    def apresentacao(self):
        return f'Prazer, meu nome é {self.nome}, sou  {self.nacionalidade} e nasci em {self.ano_nascimento}.'
class  Livro:
    def __init__(self,livro,ano_publicacao,autor :Autor):
          self.livro =livro        
          self.ano_publicacao = ano_publicacao        
          self.autor =autor
    def exibir_informacoes(self):
        return f'titulo :{self.livro}, ano publicado : {self.ano_publicacao}, autor :{self.autor.nome}'
    def idade_do_livro(self):
        idade = datetime.datetime.now().year - self.ano_publicacao
        print(f'A idade do livro "{self.livro}" é {idade} anos.')
    
Autor1 = Autor('kawan','brasileiro' ,2009)
Livro1 = Livro('Aprendendo Python', 2020, Autor1)
print(Autor1.apresentacao())
print(Livro1.exibir_informacoes())
print(Livro1.idade_do_livro())
