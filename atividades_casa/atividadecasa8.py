def jogo_da_forca():
    import random

    palavras = ['python', 'java', 'kotlin', 'javascript']
    palavra = random.choice(palavras)
    letras_descobertas = ['_'] * len(palavra)
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0 and '_' in letras_descobertas:
        print("\n" + " ".join(letras_descobertas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        letra = input("Digite uma letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue
        
        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if letra in palavra:
            for idx, char in enumerate(palavra):
                if char == letra:
                    letras_descobertas[idx] = letra
        else:
            tentativas -= 1
            letras_erradas.append(letra)
            print(f"A letra '{letra}' não está na palavra.")
    
    if '_' not in letras_descobertas:
        print(f"\nParabéns! Você adivinhou a palavra: {palavra}")
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")
jogo_da_forca()        