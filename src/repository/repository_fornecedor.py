from src.conexion.conexao_oracle import ConexaoOracle
from src.model.fornecedores import Fornecedor

class RepositoryFornecedor():

    def __init__(self):
        pass
    
    def buscar_fornecedor(self, bd: ConexaoOracle, cnpj: str) -> Fornecedor:
        dados_fornecedor = bd.sqlToTuple(f"SELECT CNPJ, NOME, TELEFONE FROM FORNECEDORES WHERE CNPJ = '{cnpj}'")
        if dados_fornecedor:
            fornecedor = Fornecedor(dados_fornecedor[0], dados_fornecedor[1], dados_fornecedor[2])
            return fornecedor
        return None

    def inserir_fornecedor(self, bd: ConexaoOracle, fornecedor: Fornecedor) -> Fornecedor:
        bd.write(f"INSERT INTO FORNECEDORES (CNPJ, NOME, TELEFONE) VALUES ('{fornecedor.get_cnpj()}', '{fornecedor.get_nome()}', '{fornecedor.get_telefone()}')")

        dados_fornecedor = bd.sqlToTuple(f"SELECT CNPJ, NOME, TELEFONE FROM FORNECEDORES WHERE CNPJ = '{fornecedor.get_cnpj()}'")

        if dados_fornecedor:
            return fornecedor
        return None
    
    def excluir_fornecedor(self, bd: ConexaoOracle, cnpj: str) -> bool:
        check_fk = f"SELECT 1 FROM PRODUTOS_FORNECEDORES WHERE CNPJ_FORNECEDOR = '{cnpj}'"
        if bd.sqlToTuple(check_fk):
            return False
        
        bd.write(f"DELETE FROM FORNECEDORES WHERE CNPJ = '{cnpj}'")
        return True
    
    def atualizar_fornecedor(self, bd: ConexaoOracle, fornecedor: Fornecedor):
        bd.write(f"UPDATE FORNECEDORES SET NOME = '{fornecedor.get_nome()}', TELEFONE = '{fornecedor.get_telefone()}' WHERE CNPJ = '{fornecedor.get_cnpj()}'")

    def existencia_fornecedor(self, bd: ConexaoOracle, cnpj: str) -> bool:
        query = f"SELECT 1 FROM FORNECEDORES WHERE CNPJ = '{cnpj}'"

        return True if bd.sqlToTuple(query) else False