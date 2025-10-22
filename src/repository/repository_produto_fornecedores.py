from src.conexion.conexao_oracle import ConexaoOracle
from src.model.produtos_fornecedores import ProdutoFornecedor
from src.repository.repository_produto import RepositoryProduto
from src.repository.repository_fornecedor import RepositoryFornecedor
from src.model.produtos import Produto
from src.model.fornecedores import Fornecedor

class RepositoryProdutoFornecedores():

    def __init__(self):
        self.repository_produto = RepositoryProduto()
        self.repository_fornecedor = RepositoryFornecedor()

    def inserir_produto_fornecedor(self, bd: ConexaoOracle, produto: Produto, fornecedor: Fornecedor) -> ProdutoFornecedor:
        query = "INSERT INTO PRODUTOS_FORNECEDORES (ID_PRODUTO, CNPJ_FORNECEDOR) VALUES (:1, :2) RETURNING ID_PRODUTO_FORNECEDOR INTO :3"
        params = (produto.get_id(), fornecedor.get_cnpj())

        id_produto_forecedor = bd.return_id(query, params)

        if id_produto_forecedor:
            return ProdutoFornecedor(id_produto_forecedor, produto, fornecedor)
        else:
            return None


    def buscar_produto_fornecedor(self, bd: ConexaoOracle, id: int) -> ProdutoFornecedor:
        dados = bd.sqlToTuple(f"SELECT ID_PRODUTO_FORNECEDOR, ID_PRODUTO, CNPJ_FORNECEDOR FROM PRODUTOS_FORNECEDORES WHERE ID_PRODUTO_FORNECEDOR = '{id}'")
        
        if dados:
            obj_produto = self.repository_produto.buscar_produto(bd, dados[1])
            obj_fornecedor = self.repository_fornecedor.buscar_fornecedor(bd, dados[2])
            produto_fornecedor = ProdutoFornecedor(dados[0], obj_produto, obj_fornecedor)
            return produto_fornecedor
        else:
            return None

    def excluir_produto_fornecedor(self, bd: ConexaoOracle, id: int) -> bool:
        check_fk = f"SELECT 1 FROM MOVIMENTACAO_ESTOQUE WHERE ID_PRODUTO_FORNECEDOR = '{id}'"
        
        # Se tiver tabela dependente
        if bd.sqlToTuple(check_fk):
            return False
        
        bd.write(f"DELETE FROM PRODUTOS_FORNECEDORES WHERE ID_PRODUTO_FORNECEDOR = '{id}'")

        return True

    def atualizar_produto_fornecedor(self, bd: ConexaoOracle, produto_fornecedor: ProdutoFornecedor):
        id_produto_fornecedor: int = produto_fornecedor.get_id()
        id_produto: int = produto_fornecedor.get_produto().get_id()
        cnpj: str = produto_fornecedor.get_fornecedor().get_cnpj()

        bd.write(f"UPDATE PRODUTOS_FORNECEDORES SET ID_PRODUTO = '{id_produto}', CNPJ_FORNECEDOR = '{cnpj}' WHERE ID_PRODUTO_FORNECEDOR = '{id_produto_fornecedor}'")

    def existencia_produto_fornecedor(self, bd: ConexaoOracle, id: int) -> bool:
        query = f"SELECT 1 FROM PRODUTOS_FORNECEDORES WHERE ID_PRODUTO_FORNECEDOR = {id}"
        return True if bd.sqlToTuple(query) else False
    
    def existencia_produtos_fornecedores(self, bd: ConexaoOracle) -> bool:
        query = f"SELECT COUNT(1) FROM PRODUTOS_FORNECEDORES"

        result = bd.sqlToTuple(query)[0]

        return True if result else False