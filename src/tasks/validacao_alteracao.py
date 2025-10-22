def validar_alteracao() -> bool:
    validacao = input(str("Deseja alterar mais algum registro?\n'SIM'/'NAO'\n>> "))

    if validacao != 'SIM':
        return False

    return True