import random
import string

def gerar_senha(tamanho=12, usar_letras=True, usar_simbolos=True, usar_numeros=True):
    caracteres = ''

    if usar_letras :
        caracteres += string.ascii_letters
    if usar_simbolos:
        caracteres += string.punctuation
    if usar_numeros:
        caracteres += string.digits



    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print(gerar_senha())
