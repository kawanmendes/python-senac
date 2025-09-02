def senha_valida(senha):
    if len(senha) < 8:
        return False

    tem_letra = False
    tem_numero = False

    for caractere in senha:
        if caractere.isalpha():
            tem_letra = True
        elif caractere.isdigit():
            tem_numero = True

    return tem_letra and tem_numero


tentativas = 3

while tentativas > 0:
    senha = input("Digite sua senha: ")

    if senha_valida(senha):
        print("Acesso permitido!")
        break
    else:
        tentativas -= 1
        print("Senha inválida. Ela deve ter pelo MAIS DE 8 caracteres, conter letras e números.")
        if tentativas > 0:
            print(f"Você tem {tentativas} tentativa(s) restante(s).")
        else:
            print("Número de tentativas excedido. Acesso negado.")