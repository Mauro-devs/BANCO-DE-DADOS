from src.conexion.conexao_oracle import ConexaoOracle

class Relatorio:

    def __init__(self):
        self.query_relatorio_movimentacao_estoque = None

        with open("src/sql/relatorio_funcionarios.sql") as f:
            self.query_relatorio_funcionarios = f.read()

        with open("src/sql/relatorio_produtos.sql") as f:
            self.query_relatorio_produtos = f.read()

        with open("src/sql/relatorio_fornecedores.sql") as f:
            self.query_relatorio_fornecedores = f.read()

        with open("src/sql/relatorio_movimentacao_estoque.sql") as f:
            self.query_relatorio_movimentacao_estoque = f.read()

        with open("src/sql/relatorio_produtos_fornecedor.sql") as f:
            self.query_relatorio_produtos_fornecedores = f.read()


    def get_relatorio_funcionarios(self):
        oracle = ConexaoOracle()
        oracle.connect()
        
        relatorio = oracle.sqlToDataFrame(self.query_relatorio_funcionarios)

        if relatorio.empty:
            print("Não há funcionários\n\n")
            return False
        else:
            print(relatorio.to_string(index=False))
            print()
            return True

    def get_relatorio_movimentacoes(self):
        oracle = ConexaoOracle()
        oracle.connect()

        relatorio = oracle.sqlToDataFrame(self.query_relatorio_movimentacao_estoque)

        if relatorio.empty:
            print("Não há movimentações no estoque\n")
            return False
        else:
            print(relatorio.to_string(index=False))
            print()
            return True

    def get_relatorio_produtos(self):
        oracle = ConexaoOracle()
        oracle.connect()

        relatorio = oracle.sqlToDataFrame(self.query_relatorio_produtos)

        if relatorio.empty:
            print("Não há produtos\n")
            return False
        else:
            print(relatorio.to_string(index=False))
            print()
            return True

    def get_relatorio_fornecedores(self):
        oracle = ConexaoOracle()
        oracle.connect()

        relatorio = oracle.sqlToDataFrame(self.query_relatorio_fornecedores)

        if relatorio.empty:
            print("Não há fornecedores\n")
            return False
        else:
            print(relatorio.to_string(index=False))
            print()
            return True
    
    def get_relatorio_produtos_fornecedores(self):
        oracle = ConexaoOracle()
        oracle.connect()

        relatorio = oracle.sqlToDataFrame(self.query_relatorio_produtos_fornecedores)

        if relatorio.empty:
            print("Não há associação de produtos e fornecedores\n")
            return False
        else:
            print(relatorio.to_string(index=False))
            print()
            return True
    