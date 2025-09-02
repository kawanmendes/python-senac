import re

def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '.','-', cpf)

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (ex: 00000000000, 11111111111)
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10) % 11
    if digito1 == 10:
        digito1 = 0

    # Calcula o segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10) % 11
    if digito2 == 10:
        digito2 = 0

    # Verifica se os dígitos calculados batem com os do CPF
    return cpf[-2:] == f"{digito1}{digito2}"

