def validar_remocao() -> bool:
    validacao = input(str("Confirme a remoção:\n'SIM'/'NAO'\n>> ")).upper().strip()

    return validacao == 'SIM'