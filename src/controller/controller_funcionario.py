from model.funcionarios import Funcionario
from connexion.conexao_oracle import ConexaoOracle

class ControllerFuncionario:
    def __init__(self):
        pass

    def inserir_funcionario(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()
        
        cpf = input("CPF do funcionário novo: ")
        if not self.existencia_funcionario(bd, cpf):
            nome = input("Nome do funcionário: ")
            telefone = input("Telefone do funcionário: ")
            bd.write(f"INSERT INTO FUNCIONARIOS (CPF, NOME , TELEFONE) VALUES ('{cpf}', '{nome}', '{telefone}')")

            dados_funcionario = bd.sqlToTuple(f"SELECT CPF, NOME, TELEFONE FROM FUNCIONARIOS WHERE CPF = '{cpf}'")
            if dados_funcionario:
                funcionario = Funcionario(dados_funcionario[0], dados_funcionario[1], dados_funcionario[2])
                print(f"{funcionario} cadastrado.")
                return funcionario
            else:
                print("Erro ao buscar o funcionário cadastrado!")
        else:
            print("CPF já cadastrado!")
            return None

    def excluir_funcionario(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        cpf = input("CPF do funcionário a ser excluído: ")
        if self.existencia_funcionario(bd, cpf):
            check_fk = f"SELECT 1 FROM MOVIMENTACAO_ESTOQUE WHERE CPF_FUNCIONARIO = '{cpf}'"
            if bd.sqlToTuple(check_fk):
                print("Funcionário não pode ser excluído!\n**Está associado na tabela MOVIMENTACAO_ESTOQUE")
                return
            
            dados_funcionario = bd.sqlToTuple(f"SELECT CPF, NOME, TELEFONE FROM FUNCIONARIOS WHERE CPF = '{cpf}'")
            bd.write(f"DELETE FROM FUNCIONARIOS WHERE CPF = '{cpf}'")
            if dados_funcionario:
                funcionario = Funcionario(dados_funcionario[0], dados_funcionario[1], dados_funcionario[2])
                print(f"{funcionario} excluído.")
            else:
                print("Erro ao buscar o funcionário excluído!")
        else:
            print("CPF não encontrado!")

    def atualizar_funcionario(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        cpf = input("CPF do funcionário para atualização: ")
        if self.existencia_funcionario(bd, cpf):
            nome = input("Nome novo do funcionário: ")
            telefone = input("Telefone novo do funcionário: ")
            bd.write(f"UPDATE FUNCIONARIOS SET NOME = '{nome}', TELEFONE = '{telefone}' WHERE CPF = '{cpf}'")

            dados_funcionario = bd.sqlToTuple(f"SELECT CPF, NOME, TELEFONE FROM FUNCIONARIOS WHERE CPF = '{cpf}'")
            if dados_funcionario:
                funcionario = Funcionario(dados_funcionario[0], dados_funcionario[1], dados_funcionario[2])
                print(f"{funcionario} atualizado.")
                return funcionario
            else:
                print("Erro ao buscar o funcionário atualizado!")
        else:
            print("CPF não encontrado!")
            return None

    def existencia_funcionario(self, bd:ConexaoOracle, cpf:str):
        query = f"SELECT 1 FROM FUNCIONARIOS WHERE CPF = '{cpf}'"
        return True if bd.sqlToTuple(query) else False
    
    def buscar_funcionario(self, bd:ConexaoOracle, cpf:str):
        dados_funcionario = bd.sqlToTuple(f"SELECT CPF, NOME, TELEFONE FROM FUNCIONARIOS WHERE CPF = '{cpf}'")
        if dados_funcionario:
            funcionario = Funcionario(dados_funcionario[0], dados_funcionario[1], dados_funcionario[2])
            return funcionario
        else:
            print("CPF não encontrado!")
            return None