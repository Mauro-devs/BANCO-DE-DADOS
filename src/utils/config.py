# src/utils/config.py

MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

# ATUALIZADO COM BASE NOS SEUS ARQUIVOS .sql
MENU_RELATORIOS = """Relatórios
1 - Relatório de Funcionários
2 - Relatório de Movimentação de Estoque
3 - Relatório de Produtos por Fornecedor
4 - Relatório de Produtos
5 - Relatório de Fornecedores 
0 - Sair
"""

# ATUALIZADO COM BASE NAS SUAS TABELAS
MENU_ENTIDADES = """Entidades
1 - PRODUTOS
2 - FORNECEDORES
3 - FUNCIONARIOS
4 - MOVIMENTACOES ESTOQUE
5 - PRODUTOS FORNECEDORES
"""

# NÃO MEXA NISSO!
# A SplashScreen DEPENDE EXATAMENTE DESTE FORMATO.
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    '''
        Esse método limpa a tela após alguns segundos
        wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    
    # CORRIGIDO: "cls" é o comando para limpar a tela no Windows.
    # "clear" (do professor) é para Linux/Mac.
    os.system("cls")