# Este módulo gerencia leitores, livros e empréstimos em uma biblioteca

class Leitor:
    leitores = []
    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.leitores.append(self)
    def cadastrar_leitor(self, id, nome, telefone):
        # Adiciona um novo leitor à lista
        novo_leitor = Leitor(id, nome, telefone)
        return novo_leitor
    def atualizar_leitor(self, id, nome, telefone):
        # Atualiza dados de um leitor existente
        for leitor in self.leitores:
            if leitor.id == id:
                leitor.nome = nome
                leitor.telefone = telefone
                return True
        return False
    def listar_leitores(self):
        # Lista todos os leitores
        for leitor in self.leitores:
            print(leitor)
    def deletar_leitor(self, id):
        # Remove um leitor pelo id
        for leitor in Leitor.leitores:
            if leitor.id == id:
                Leitor.leitores.remove(leitor)
                print(f'o usuario com o id {id} foi removido')
                return True
        return False
    def consultar_leitor(self, id):
        # Consulta um leitor pelo id
        for leitor in Leitor.leitores:
            if leitor.id == id:
                print(f'o leitor foi encontrado {leitor}')
                return True
        print(f'o usuario nao foi encontrado')
        return False
    def __str__(self):
        return  f"ID: {self.id}, Nome: {self.nome}, Telefone: {self.telefone}"

class Livro:
    livros = []
    def __init__(self, isbn, titulo, autores, edicao, qtd_exemplar):
        self.isbn = isbn
        self.titulo = titulo
        self.autores = autores
        self.edicao = edicao
        self.qtd_exemplar = qtd_exemplar
        self.livros.append(self)
    def cadastrar_livro(self, isbn, titulo, autores, edicao, qtd_exemplar):
        # Adiciona um novo livro à lista
        novo_livro = Livro(isbn, titulo, autores, edicao, qtd_exemplar)
        return novo_livro
    def atualizar_livro(self, isbn, titulo, autores, edicao, qtd_exemplar):
        # Atualiza dados de um livro existente
        for livro in self.livros:
            if livro.isbn == isbn:
                livro.titulo = titulo
                livro.autores = autores
                livro.edicao = edicao
                livro.qtd_exemplar = qtd_exemplar
                return True
        return False
    def lista_livros(self):
        # Lista todos os livros
        for livro in self.livros:
            print(livro)
    def deletar_livro(self, isbn):
        # Remove um livro pelo ISBN
        for livro in Livro.livros:
            if livro.isbn == isbn:
                Livro.livros.remove(livro)
                print(f'o livro com o livro {livro.titulo} foi removido')
                return True
        return False
    def consultar_livro(self, isbn):
        # Consulta um livro pelo ISBN
        for livro in Livro.livros:
            if livro.isbn == isbn:
                print(f'o livro foi encontrado {livro}')
                return True
        print(f'o livro nao foi encontrado')
        return False
    def __str__(self):
        return f"ISBN: {self.isbn}, Título: {self.titulo}, Autores: {self.autores}, Edição: {self.edicao}, Quantidade de Exemplares: {self.qtd_exemplar}"
    def verificar_disponibilidade(self, isbn):
        # Verifica se o livro está disponível
        for livro in Livro.livros:
            if livro.isbn == isbn:
                if livro.qtd_exemplar > 0:
                    print(f"o livro {livro} esta disponivel")
                    return True
                else:
                    print(f"o livro {livro} nao esta disponivel no momento")
                    return False

class Emprestimo:
    Emprestimos = []
    def __init__(self, data_emprestimo, data_devolucao, livro: Livro, leitor: Leitor):
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.livro = livro
        self.leitor = leitor
        self.Emprestimos.append(self)
    def registrar_emprestimo(self, data_emprestimo, data_devolucao, livro: Livro, leitor: Leitor):
        # Registra um novo empréstimo se houver exemplares disponíveis
        if livro.qtd_exemplar > 0:
            novo_emprestimo = Emprestimo(data_emprestimo, data_devolucao, livro, leitor)
            livro.qtd_exemplar -= 1
            print(f'O livro {livro.titulo} foi emprestado com sucesso para {leitor.nome}.')
            return novo_emprestimo
        else:
            print(f'O livro {livro.titulo} não está disponível para empréstimo.')
            return None
    def registrar_devolucao(self, livro: Livro):
        # Registra a devolução de um livro
        for emprestimo in Emprestimo.Emprestimos:
            if emprestimo.livro.isbn == livro.isbn:
                Emprestimo.Emprestimos.remove(emprestimo)
                livro.qtd_exemplar += 1
                print(f'O livro {livro.titulo} foi devolvido com sucesso.')
                return True
        print(f'Não foi encontrado um empréstimo para o livro {livro.titulo}.')
        return False
    def __str__(self):
        return f"Data de Empréstimo: {self.data_emprestimo}, Data de Devolução: {self.data_devolucao}, Livro: {self.livro.titulo}, Leitor: {self.leitor.nome}"
    def lista_emprestimos(self):
        # Lista todos os empréstimos
        for emprestimo in self.Emprestimos:
            print(emprestimo)

# Exemplos de uso das classes
Livro01 = Livro('1', 'O Senhor dos Anéis', 'J.R.R. Tolkien', '1ª Edição', 5)
Livro01.cadastrar_livro('2', 'O Código Da Vinci', 'Dan Brown', '2ª Edição', 3)
Leitor01 = Leitor(1, 'João Silva', '1234-5678')
Leitor01.cadastrar_leitor(2, 'Maria Souza', '8765-4321')








