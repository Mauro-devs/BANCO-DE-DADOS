from src.conexion.conexao_oracle import ConexaoOracle
from src.model.produtos import Produto

class RepositoryProduto():

    def __init__(self):
        pass
    
    def buscar_produto(self, bd: ConexaoOracle, id: int) -> Produto:
        dados_produto = bd.sqlToTuple(f"SELECT ID_PRODUTO, NOME, PRECO_UNITARIO, DESCRICAO, CATEGORIA FROM PRODUTOS WHERE ID_PRODUTO = {id}")
        
        if dados_produto:
            return Produto(dados_produto[0], dados_produto[1], dados_produto[2], dados_produto[3], dados_produto[4])
        return None

    def inserir_produto(self, bd: ConexaoOracle, nome: str, preco: float, descricao: str, categoria: str) -> Produto:
        query = f"INSERT INTO PRODUTOS (NOME, PRECO_UNITARIO, DESCRICAO, CATEGORIA) VALUES (:1, :2, :3, :4) RETURNING ID_PRODUTO INTO :5"
        params = (nome, preco, descricao, categoria)
        
        # coletar o id gerado
        id_gerado = bd.return_id(query, params)
        if id_gerado:
            return Produto(id_gerado, nome, preco, descricao, categoria)
        return None
    
    def excluir_produto(self, bd: ConexaoOracle, id: int) -> bool:
        check_fk = f"SELECT 1 FROM PRODUTOS_FORNECEDORES WHERE ID_PRODUTO = {id}"
        if bd.sqlToTuple(check_fk):
            return False
        
        bd.write(f"DELETE FROM PRODUTOS WHERE ID_PRODUTO = {id}")

        return True
    
    def atualizar_produto(self, bd: ConexaoOracle, produto: Produto) -> Produto:
        bd.write(f"UPDATE PRODUTOS SET NOME = '{produto.get_nome()}', PRECO_UNITARIO = {produto.get_preco_unitario()}, DESCRICAO = '{produto.get_descricao()}', CATEGORIA = '{produto.get_categoria()}' WHERE ID_PRODUTO = {produto.get_id()}")


    def existencia_produto(self, bd: ConexaoOracle, id: int) -> bool:
        query = f"SELECT 1 FROM PRODUTOS WHERE ID_PRODUTO = {id}"
        
        return True if bd.sqlToTuple(query) else False