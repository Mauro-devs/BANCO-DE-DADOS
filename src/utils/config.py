import os

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

def limpar_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")