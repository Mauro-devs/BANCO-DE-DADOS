from model.fornecedores import Fornecedor
from connexion.conexao_oracle import ConexaoOracle

class ControllerFornecedor:
    def __init__(self):
        pass

    def inserir_fornecedor(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()
        
        cnpj = input("CNPJ do fornecedor novo: ")
        if not self.existencia_fornecedor(bd, cnpj):
            nome = input("Nome do fornecedor: ")
            telefone = input("Telefone do fornecedor: ")
            bd.write(f"INSERT INTO FORNECEDORES (CNPJ, NOME, TELEFONE) VALUES ('{cnpj}', '{nome}', '{telefone}')")

            dados_fornecedor = bd.sqlToTuple(f"SELECT CNPJ, NOME, TELEFONE FROM FORNECEDORES WHERE CNPJ = '{cnpj}'")
            if dados_fornecedor:
                fornecedor = Fornecedor(dados_fornecedor[0], dados_fornecedor[1], dados_fornecedor[2])
                print(f"{fornecedor} cadastrado.")
                return fornecedor
            else:
                print("Erro ao buscar o fornecedor cadastrado!")
        else:
            print("CNPJ já cadastrado!")
            return None

    def excluir_fornecedor(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        cnpj = input("CNPJ do fornecedor a ser excluído: ")
        if self.existencia_fornecedor(bd, cnpj):
            check_fk = f"SELECT 1 FROM PRODUTOS_FORNECEDORES WHERE CNPJ_FORNECEDOR = '{cnpj}'"
            if bd.sqlToTuple(check_fk):
                print("Fornecedor não pode ser excluído!\n**Está associado na tabela PRODUTOS_FORNECEDORES")
                return
            
            dados_fornecedor = bd.sqlToTuple(f"SELECT CNPJ, NOME, TELEFONE FROM FORNECEDORES WHERE CNPJ = '{cnpj}'")
            bd.write(f"DELETE FROM FORNECEDORES WHERE CNPJ = '{cnpj}'")
            if dados_fornecedor:
                fornecedor = Fornecedor(dados_fornecedor[0], dados_fornecedor[1], dados_fornecedor[2])
                print(f"{fornecedor} excluído.")
            else:
                print("Erro ao buscar o fornecedor excluído!")
        else:
            print("CNPJ não encontrado!")

    def atualizar_fornecedor(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        cnpj = input("CNPJ do fornecedor para atualização: ")
        if self.existencia_fornecedor(bd, cnpj):
            nome = input("Nome novo do fornecedor: ")
            telefone = input("Telefone novo do fornecedor: ")
            bd.write(f"UPDATE FORNECEDORES SET NOME = '{nome}', TELEFONE = '{telefone}' WHERE CNPJ = '{cnpj}'")

            dados_fornecedor = bd.sqlToTuple(f"SELECT CNPJ, NOME, TELEFONE FROM FORNECEDORES WHERE CNPJ = '{cnpj}'")
            if dados_fornecedor:
                fornecedor = Fornecedor(dados_fornecedor[0], dados_fornecedor[1], dados_fornecedor[2])
                print(f"{fornecedor} atualizado.")
                return fornecedor
            else:
                print("Erro ao buscar o fornecedor atualizado!")
        else:
            print("CNPJ não encontrado!")
            return None

    def existencia_fornecedor(self, bd:ConexaoOracle, cnpj:str):
        query = f"SELECT 1 FROM FORNECEDORES WHERE CNPJ = '{cnpj}'"
        return True if bd.sqlToTuple(query) else False
    
    def buscar_fornecedor(self, bd:ConexaoOracle, cnpj:str):
            dados_fornecedor = bd.sqlToTuple(f"SELECT CNPJ, NOME, TELEFONE FROM FORNECEDORES WHERE CNPJ = '{cnpj}'")
            if dados_fornecedor:
                fornecedor = Fornecedor(dados_fornecedor[0], dados_fornecedor[1], dados_fornecedor[2])
                return fornecedor   
            else:
                print("CNPJ não encontrado!")
                return None