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
        
        print(oracle.sqlToDataFrame(self.query_relatorio_funcionarios).to_string(index=False))

    def get_relatorio_movimentacoes(self):
        oracle = ConexaoOracle()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_movimentacao_estoque).to_string(index=False))

    def get_relatorio_produtos(self):
        oracle = ConexaoOracle()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos).to_string(index=False))

    def get_relatorio_fornecedores(self):
        oracle = ConexaoOracle()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_fornecedores).to_string(index=False))
    
    def get_relatorio_produtos_fornecedores(self):
        oracle = ConexaoOracle()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos_fornecedores).to_string(index=False))
    