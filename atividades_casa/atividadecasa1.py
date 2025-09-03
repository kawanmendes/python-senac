def cauculadora():
    print("CALCULADORA")
    n1 = float(input("informe o primeiro numero: "))
    n2 = float(input("informe o segundo numero: "))
    operacao = input("informe a operacao (+, -, *, /): ")

    if operacao == "+":
        resultado = n1 + n2
    elif operacao == "-":
        resultado = n1 - n2
    elif operacao == "*":
        resultado = n1 * n2
    elif operacao == "/":
        if n2 != 0:
            resultado = n1 / n2
        else:
             "Erro: Divisao por zero nao e permitida."
    else:
         "Operacao invalida."

    return print(f"O resultado de {n1} {operacao} {n2} e: {resultado}")
cauculadora()