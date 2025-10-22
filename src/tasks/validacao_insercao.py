def validar_insercao() -> bool:
    validacao = input(str("Deseja inserir mais algum registro?\n'SIM'/'NAO'>> "))

    if validacao != 'SIM':
        return False

    return True