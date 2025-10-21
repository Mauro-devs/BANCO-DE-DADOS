from conexion.conexao_oracle import ConexaoOracle

class Relatorio:

    def _init_(self):
        with open("sql/relatorio_funcionarios.sql") as f:
            self.query_relatorio_funcionarios = f.read()

        with open("sql/relatorio_produtos.sql") as f:
            self.query_relatorio_produtos = f.read()

        with open("sql/relatorio_fornecedores.sql") as f:
            self.query_relatorio_fornecedores = f.read()

        with open("sql/relatorio_movimentacao_estoque.sql") as f:
            self.query_relatorio_movimentacao_estoque = f.read()

        with open("sql/relatorio_produtos_fornecedores.sql") as f:
            self.query_relatorio_produtos_fornecedores = f.read()


    def get_relatorio_funcionarios(self):
        oracle = ConexaoOracle()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_funcionarios))
        input("Pressione Enter para sair do Relatório de Funcionários")

    def get_relatorio_movimentacoes(self):
        oracle = ConexaoOracle()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_movimentacao_estoque))
        input("Pressione Enter para sair do Relatório de Movimentações de Estoque")

    def get_relatorio_produtos(self):
        oracle = ConexaoOracle()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos))
        input("Pressione Enter para sair do Relatório de Produtos")

    def get_relatorio_fornecedores(self):
        oracle = ConexaoOracle()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_fornecedores))
        input("Pressione Enter para sair do Relatório de Fornecedores")
    
    def get_relatorio_produtos_fornecedores(self):
        oracle = ConexaoOracle()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos_fornecedores))
        input("Pressione Enter para sair do Relatório de ")
    