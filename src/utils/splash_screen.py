from connexion.conexao_oracle import ConexaoOracle

from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_fornecedores = config.QUERY_COUNT.format(tabela="fornecedores")
        self.qry_total_funcionarios = config.QUERY_COUNT.format(tabela="funcionarios")
        self.qry_total_movimentacoes_estoque = config.QUERY_COUNT.format(tabela="movimentacoes_estoque")
        self.qry_total_produtos_fornecedores = config.QUERY_COUNT.format(tabela="produtos_fornecedores")
        self.qry_total_produtos = config.QUERY_COUNT.format(tabela="produtos")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        # Nome(s) do(s) criador(es)
        self.created_by = "Arthur Pomarolli, Davi de Souza, Mauro Barros, Pedro Algusto."
        self.professor = "Prof. M.Sc. Howard Roatti."
        self.disciplina = "Banco de dados"
        self.semestre = "2025/2"

    def get_total_fornecedores(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = ConexaoOracle()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_fornecedores)["total_fornecedores"].values[0]

    def get_total_funcionarios(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = ConexaoOracle()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_funcionarios)["total_funcionarios"].values[0]

    def get_total_movimentacoes_estoque(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = ConexaoOracle()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_movimentacoes_estoque)["total_movimentacoes_estoque"].values[0]

    def get_total_produtos_fornecedores(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = ConexaoOracle()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_produtos_fornecedores)["total_produtos_fornecedores"].values[0]

    def get_total_produtos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = ConexaoOracle()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_produtos)["total_produtos"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                        
        #  TOTAL DE REGISTROS:                                   
        #      1 - FORNECEDORES:       {str(self.get_total_fornecedores()).rjust(5)}
        #      2 - FUNCIONARIOS:       {str(self.get_total_funcionarios()).rjust(5)}
        #      3 - MOV. ESTOQUE:       {str(self.get_total_movimentacoes_estoque()).rjust(5)}
        #      4 - PROD. FORNECEDORES: {str(self.get_total_produtos_fornecedores()).rjust(5)}
        #      5 - PRODUTOS:           {str(self.get_total_produtos()).rjust(5)}
        #
        # DADOS DO GRUPO:
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR: {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """