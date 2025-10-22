from src.conexion.conexao_oracle import ConexaoOracle
from src.model.produtos_fornecedores import ProdutoFornecedor
from src.repository.repository_produto import RepositoryProduto
from src.repository.repository_funcionario import RepositoryFuncionario
from src.model.produtos import Produto
from src.model.funcionarios import Funcionario
from src.model.movimentacoes_estoque import MovimentacaoEstoque

class RepositoryMovimentacaoEstoque():

    def __init__(self):
        self.repository_produto = RepositoryProduto()
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
            obj_produto = self.repository_produto.buscar_produto(bd, dados[1])
            obj_funcionario = self.repository_funcionario.buscar_funcionario(bd, dados[2])
            quantidade = dados[3]
            tipo_movimentacao = dados[4]
            data_movimentacao = dados[5]

            movimentacao_estoque = MovimentacaoEstoque(dados[0], obj_produto, obj_funcionario, quantidade, tipo_movimentacao, data_movimentacao)

            return movimentacao_estoque
        else:
            return None

    def excluir_movimentacao_estoque(self, bd: ConexaoOracle, id: int) -> bool:
        bd.write(f"DELETE FROM MOVIMENTACAO_ESTOQUE WHERE ID_MOVIMENTACAO = {id}")
        return True

    def atualizar_movimentacao_estoque(self, bd: ConexaoOracle, movimentacao_estoque: MovimentacaoEstoque):
        print(2)
        id_produto_fornecedor: int = movimentacao_estoque.get_produto_fornecedor().get_id()
        print(3)
        id_produto: int = movimentacao_estoque.get_produto_fornecedor().get_produto().get_id()
        print(4)
        cnpj: str = movimentacao_estoque.get_produto_fornecedor().get_fornecedor().get_cnpj()
        print(5)

        bd.write(f"UPDATE PRODUTOS_FORNECEDORES SET ID_PRODUTO = '{id_produto}', CNPJ_FORNECEDOR = '{cnpj}' WHERE ID_PRODUTO_FORNECEDOR = '{id_produto_fornecedor}'")

    def existencia_movimentacao_estoque(self, bd: ConexaoOracle, id: int) -> bool:
        query = f"SELECT 1 FROM MOVIMENTACAO_ESTOQUE WHERE ID_MOVIMENTACAO = {id}"
        return True if bd.sqlToTuple(query) else False