def validar_insercao() -> bool:
    validacao = input(str("Deseja inserir mais algum registro?\n'SIM'/'NAO'>> ")).upper().strip()

    return validacao == 'NAO'