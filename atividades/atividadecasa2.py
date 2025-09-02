def contar_quantas_vogais(texto):
    contador = 0
    vogais = "aeiouAEIOU"
    for char in texto:
        if char in vogais:
            contador += 1
    return contador
texto = input("Digite um texto: ")
print(f"a {contar_quantas_vogais(texto)} vogais na frase {texto}")
