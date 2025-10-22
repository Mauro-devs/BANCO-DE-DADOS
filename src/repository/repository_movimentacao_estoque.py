from src.conexion.conexao_oracle import ConexaoOracle
from src.model.produtos_fornecedores import ProdutoFornecedor
from src.repository.repository_produto_fornecedores import RepositoryProdutoFornecedores
from src.repository.repository_funcionario import RepositoryFuncionario
from src.model.produtos import Produto
from src.model.funcionarios import Funcionario
from src.model.movimentacoes_estoque import MovimentacaoEstoque

class RepositoryMovimentacaoEstoque():

    def __init__(self):
        self.repository_produto_fornecedores = RepositoryProdutoFornecedores()
        self.repository_funcionario = RepositoryFuncionario()

    def inserir_movimentacao_estoque(self, bd: ConexaoOracle, produto_fornecedor: ProdutoFornecedor, funcionario: Funcionario, quantidade, tipo_movimentacao, data_atual) -> MovimentacaoEstoque:
        id_produto_fornecedor = produto_fornecedor.get_id()
        cpf_funcionario = funcionario.get_cpf()
        
        query = "INSERT INTO MOVIMENTACAO_ESTOQUE (ID_PRODUTO_FORNECEDOR, CPF_FUNCIONARIO, QUANTIDADE, TIPO_MOVIMENTACAO, DATA_MOVIMENTACAO) VALUES (:1, :2, :3, :4, :5) RETURNING ID_MOVIMENTACAO INTO :6"
        params = (id_produto_fornecedor, cpf_funcionario, quantidade, tipo_movimentacao, data_atual)
        
        id_movimentacao = bd.return_id(query, params)
        if id_movimentacao:
            return MovimentacaoEstoque(id_movimentacao, produto_fornecedor, funcionario, quantidade, tipo_movimentacao, data_atual)

    def buscar_movimentacao_estoque(self, bd: ConexaoOracle, id: int) -> MovimentacaoEstoque:
        dados = bd.sqlToTuple(f"SELECT ID_MOVIMENTACAO, ID_PRODUTO_FORNECEDOR, CPF_FUNCIONARIO, QUANTIDADE, TIPO_MOVIMENTACAO, DATA_MOVIMENTACAO FROM MOVIMENTACAO_ESTOQUE WHERE ID_MOVIMENTACAO = '{id}'")

        if dados:
            obj_produto_fornecedor = self.repository_produto_fornecedores.buscar_produto_fornecedor(bd, dados[1])
            obj_funcionario = self.repository_funcionario.buscar_funcionario(bd, dados[2])
            quantidade = dados[3]
            tipo_movimentacao = dados[4]
            data_movimentacao = dados[5]

            movimentacao_estoque = MovimentacaoEstoque(dados[0], obj_produto_fornecedor, obj_funcionario, quantidade, tipo_movimentacao, data_movimentacao)

            return movimentacao_estoque
        else:
            return None

    def listar_movimentacao_estoque(self, bd: ConexaoOracle):
        with open('src/sql/relatorio_movimentacao_estoque.sql', 'r') as f:
            query = f.read()

            movimentacoes = bd.sqlToTuple(query)
        
        return movimentacoes

    def excluir_movimentacao_estoque(self, bd: ConexaoOracle, id: int) -> bool:
        bd.write(f"DELETE FROM MOVIMENTACAO_ESTOQUE WHERE ID_MOVIMENTACAO = {id}")
        return True

    def atualizar_movimentacao_estoque(self, bd: ConexaoOracle, id_produto_fornecedor: int, quantidade: int, tipo: str): 
        bd.write(f"UPDATE MOVIMENTACAO_ESTOQUE SET QUANTIDADE = '{quantidade}', TIPO_MOVIMENTACAO = '{tipo}' WHERE ID_PRODUTO_FORNECEDOR = '{id_produto_fornecedor}'")

    def existencia_movimentacao_estoque(self, bd: ConexaoOracle, id: int) -> bool:
        query = f"SELECT 1 FROM MOVIMENTACAO_ESTOQUE WHERE ID_MOVIMENTACAO = {id}"
        return True if bd.sqlToTuple(query) else False
    
    def existencia_movimentacoes_estoque(self, bd: ConexaoOracle) -> bool:
        query = f"SELECT COUNT(1) FROM MOVIMENTACAO_ESTOQUE"
        return True if bd.sqlToTuple(query) else False