class jogador:
    def __init__(self, nome, posicao, idade):
        self.nome = nome
        self.posicao = posicao
        self.idade = idade

class time:
    def __init__(self,nome,cidade,jogadores):
        self.nome =nome
        self.cidade =cidade
        self.jogadores =jogadores if jogadores is not None else []  
        
    def adicionar_jogador(self,jogador):
        self.jogadores.append(jogador)
        
    def total_jogadores(self,jogadores):
        total = len(jogadores)
        return total 
    def media_idades(self):
        if not self.jogadores:  
            return 0
        soma_idades = sum(jogador.idade for jogador in self.jogadores)
        media = soma_idades / len(self.jogadores)
        return media
    def lista_jogadores(self,jogadores):
        for jogador in jogadores:
            print(f'Nome: {jogador.nome}, Posição: {jogador.posicao}, Idade: {jogador.idade}')
    def __str__(self):
        return f'Time: {self.nome}, Cidade: {self.cidade}, Jogadores: {len(self.jogadores)}'
        
time1 = time('flamengo','rio de janeiro',[])
jogador1 = jogador('kawan','atacante',20)       
time1.adicionar_jogador(jogador1)
jogador2 = jogador('leticia','zagueira',22)
time1.adicionar_jogador(jogador2)
print(time1)
print(f'o total de jogadores e: {time1.total_jogadores(time1.jogadores)}')
time1.lista_jogadores(time1.jogadores)
print(f'a media de idades e: {time1.media_idades()}')
jogador3 = jogador('maria','meio-campo',21)
time1.adicionar_jogador(jogador3)   

