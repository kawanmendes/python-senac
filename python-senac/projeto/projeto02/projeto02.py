import datetime

# Classe que representa um item de compra
class Item:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
    
    def __str__(self):
        return f'{self.nome} - {self.quantidade}'

# Classe que representa uma lista de compras
class ListaCompras:
    def __init__(self, nome_lista):
        self.nome_lista = nome_lista
        self.data = datetime.date.today() # Data atual
        self.itens = [] # Lista de itens
    
    def adicionar_item(self, obj_item: Item):
        self.itens.append(obj_item)

    def remover_item(self, nome_item):
        for i in self.itens:
            if i.nome == nome_item:
                self.itens.remove(i)
    
    def listar_itens(self):
        for i in self.itens:
            print(i) # imprime o item (chama o método __str__ da classe Item)

    # Salva a lista em um arquivo de texto
    def salvar_em_arquivo(self):
        # cria o nome do arquivo com base no nome da lista e na data
        nome_arquivo = f'{self.nome_lista}_{self.data}.txt'
        # abre o arquivo em modo de escrita parâmetro 'w' (cria o arquivo se não existir)
        with open (nome_arquivo, 'w', encoding='utf-8') as arquivo:
            # percorre a lista de itens e escreve cada item no arquivo
            for i in self.itens:
                arquivo.write(f'{i.nome} - {i.quantidade}\n')

# Criação e manipulação de listas de compras
lista01 = ListaCompras('Churrasco')
lista01.adicionar_item(Item('Carne', 5))
lista01.adicionar_item(Item('Carvão', 1))
lista01.adicionar_item(Item('Cerveja', 24))
lista01.adicionar_item(Item('Refrigerante', 6))
lista01.adicionar_item(Item('Pão de Alho', 10))
# salva a lista em um arquivo de texto
lista01.salvar_em_arquivo()

lista02 = ListaCompras('Festa Aniversário')
lista02.adicionar_item(Item('Bolo', 1))
lista02.adicionar_item(Item('Doces', 50))
lista02.adicionar_item(Item('Refrigerante', 10))
lista02.adicionar_item(Item('Salgadinho', 100))
# salva a lista em um arquivo de texto
lista02.salvar_em_arquivo()