class Aluno:
    def __init__(self, nome, ra, email, notas=None):
        self.nome = nome
        self.ra = ra
        self.email = email
        self.notas = notas if notas is not None else []  

    def adicionar_nota(self, nota):        
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return f'nao a notas cadastradas para calcular a media'
        else:

            resultado = sum(self.notas) /  len(self.notas)
            return resultado

    def __str__(self):
        return (
            f'Nome: {self.nome}, RA: {self.ra}, Email: {self.email}, '
            f'Notas: {self.notas}, Média: {self.calcular_media():.2f}'
        )


Aluno1 = Aluno('kawan', '01', 'kawan@example.com')
Aluno1.adicionar_nota(10)
Aluno1.adicionar_nota(8)
Aluno1.adicionar_nota(9)
Aluno2 = Aluno('leticia', '02', 'leticia@exemplo.com')
Aluno2.adicionar_nota(9)
Aluno2.adicionar_nota(6)
Aluno2.adicionar_nota(9)

print(Aluno1)
print(Aluno2)
