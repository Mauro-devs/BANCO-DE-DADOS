def validar_remocao() -> bool:


    validacao = input(str("Confirme a remoção:\n'SIM'/'NAO'\n>> "))

    if validacao != 'NAO':
        return True

    return False