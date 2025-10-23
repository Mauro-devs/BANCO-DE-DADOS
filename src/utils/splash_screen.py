from src.conexion.conexao_oracle import ConexaoOracle

from src.utils import config

class SplashScreen:
    def __init__(self):
        self.qry_total_fornecedores = config.QUERY_COUNT.format(tabela="fornecedores")
        self.qry_total_funcionarios = config.QUERY_COUNT.format(tabela="funcionarios")
        self.qry_total_movimentacoes_estoque = config.QUERY_COUNT.format(tabela="movimentacao_estoque")
        self.qry_total_produtos_fornecedores = config.QUERY_COUNT.format(tabela="produtos_fornecedores")
        self.qry_total_produtos = config.QUERY_COUNT.format(tabela="produtos")

    def get_total_fornecedores(self):
        oracle = ConexaoOracle()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_fornecedores)["total_fornecedores"].values[0]

    def get_total_funcionarios(self):
        oracle = ConexaoOracle()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_funcionarios)["total_funcionarios"].values[0]

    def get_total_movimentacoes_estoque(self):
        oracle = ConexaoOracle()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_movimentacoes_estoque)["total_movimentacao_estoque"].values[0]

    def get_total_produtos_fornecedores(self):
        oracle = ConexaoOracle()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_produtos_fornecedores)["total_produtos_fornecedores"].values[0]

    def get_total_produtos(self):
        oracle = ConexaoOracle()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_produtos)["total_produtos"].values[0]

    def get_updated_screen(self):
        largura = 70
        borda_linha = "#" * largura

        criadores = [
            "Arthur Pomarolli",
            "Davi de Souza",
            "Mauro Barros",
            "Pedro Augusto"
        ]
        professor = "Prof. M.Sc. Howard Roatti."
        disciplina = "Banco de dados"
        semestre = "2025/2"
        
        def format_line(content=""):
            return f"#{content.ljust(largura - 2)}#"
        
        criadores_str = ""
        for i, nome in enumerate(criadores):
            prefixo = "   CRIADO POR: " if i == 0 else "               "
            criadores_str += format_line(f"{prefixo}{nome}") + "\n"
        criadores_str = criadores_str.rstrip("\n")

        return f"""
{borda_linha}
{format_line("SISTEMA DE VENDAS".center(largura - 2))}
{format_line()}
{format_line("   TOTAL DE REGISTROS:")}
{format_line(f"   1 - FORNECEDORES:".ljust(30) + str(self.get_total_fornecedores()).rjust(5))}
{format_line(f"   2 - FUNCIONARIOS:".ljust(30) + str(self.get_total_funcionarios()).rjust(5))}
{format_line(f"   3 - MOV. ESTOQUE:".ljust(30) + str(self.get_total_movimentacoes_estoque()).rjust(5))}
{format_line(f"   4 - PROD. FORNECEDORES:".ljust(30) + str(self.get_total_produtos_fornecedores()).rjust(5))}
{format_line(f"   5 - PRODUTOS:".ljust(30) + str(self.get_total_produtos()).rjust(5))}
{format_line()}
{format_line("   DADOS DO GRUPO:")}
{format_line()}
{criadores_str}
{format_line()}
{format_line(f"   PROFESSOR:".ljust(15) + professor)}
{format_line()}
{format_line(f"   DISCIPLINA:".ljust(15) + disciplina)}
{format_line(f"   SEMESTRE:".ljust(15) + semestre)}
{borda_linha}
    """