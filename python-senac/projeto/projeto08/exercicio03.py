class produto :
    def __init__(self, nome , preco):
        self.nome = nome 
        self.preco = preco
   
    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"    
class carrinho :
    def __init__(self,lista_produtos = None):
        self.lista_produtos = lista_produtos if lista_produtos is not None else [] 

    def adicionar_produto(self, produto:produto):
        self.lista_produtos.append(produto)

    def total(self):
        if len(self.lista_produtos) == 0:
            return 0  
        
        soma = sum(produto.preco for produto in self.lista_produtos)
        return soma
    def __str__(self):
        produtos_str = ", ".join(str(p) for p in self.lista_produtos)
        return f'carrinho esta com os produtos: {produtos_str} | Total: R${self.total():.2f}'
    
carrinho1 = carrinho()
carrinho1.adicionar_produto(produto('arroz', 10))
    
carrinho1.adicionar_produto(produto('feijao', 8))
print(carrinho1)

carrinho2 = carrinho()
carrinho2.adicionar_produto(produto('macarrao', 5))
carrinho2.adicionar_produto(produto('molho', 7))
print(carrinho2)
