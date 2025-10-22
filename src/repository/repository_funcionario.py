
from src.conexion.conexao_oracle import ConexaoOracle
from src.model.funcionarios import Funcionario

class RepositoryFuncionario():

    def __init__(self):
        pass

    def inserir_funcionario(self, bd: ConexaoOracle, funcionario: Funcionario) -> Funcionario:
        bd.write(f"INSERT INTO FUNCIONARIOS (CPF, NOME , TELEFONE) VALUES ('{funcionario.get_cpf()}', '{funcionario.get_nome()}', '{funcionario.get_telefone()}')")
        dados_funcionario = bd.sqlToTuple(f"SELECT CPF, NOME, TELEFONE FROM FUNCIONARIOS WHERE CPF = '{funcionario.get_cpf()}'")

        #Caso tenha retornado algo
        if dados_funcionario:
            return funcionario
        #Se não retornou nada
        return None
    
    def buscar_funcionario(self, bd: ConexaoOracle, cpf: str) -> Funcionario:
        dados_funcionario = bd.sqlToTuple(f"SELECT CPF, NOME, TELEFONE FROM FUNCIONARIOS WHERE CPF = '{cpf}'")
        
        if dados_funcionario:
            funcionario = Funcionario(dados_funcionario[0], dados_funcionario[1], dados_funcionario[2])
            return funcionario
        else:
            #CPF não encontrado
            return None
        
    def atualizar_funcionario(self, bd: ConexaoOracle, funcionario: Funcionario):
        bd.write(f"UPDATE FUNCIONARIOS SET NOME = '{funcionario.get_nome()}', TELEFONE = '{funcionario.get_telefone()}' WHERE CPF = '{funcionario.get_cpf()}'")
    
    def excluir_funcionario(self, bd: ConexaoOracle, cpf: str) -> bool:
        check_fk = f"SELECT 1 FROM MOVIMENTACAO_ESTOQUE WHERE CPF_FUNCIONARIO = '{cpf}'"
        if bd.sqlToTuple(check_fk):
            return False
        
        bd.write(f"DELETE FROM FUNCIONARIOS WHERE CPF = '{cpf}'")

        return True


    def existencia_funcionario(self, bd: ConexaoOracle, cpf: str) -> bool:
        # Retorna 1 se achar e None se não achar
        query = f"SELECT 1 FROM FUNCIONARIOS WHERE CPF = '{cpf}'"
        
        return True if bd.sqlToTuple(query) else False
    
    def existencia_funcionarios(self, bd: ConexaoOracle) -> bool:
        # Retorna 1 se achar e None se não achar
        query = f"SELECT COUNT(1) FROM FUNCIONARIOS"
        
        return True if bd.sqlToTuple(query) else False
