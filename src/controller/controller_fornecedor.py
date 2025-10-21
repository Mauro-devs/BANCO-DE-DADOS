from src.model.fornecedores import Fornecedor
from src.conexion.conexao_oracle import ConexaoOracle
from src.repository.repository_fornecedor import RepositoryFornecedor

class ControllerFornecedor:
    def __init__(self):
        self.repository_fornecedor = RepositoryFornecedor()

    def inserir_fornecedor(self):        
        bd = ConexaoOracle(can_write=True)
        bd.connect()
        
        cnpj = input("CNPJ do fornecedor novo: ")
        if not self.repository_fornecedor.existencia_fornecedor(bd, cnpj):
            nome = input("Nome do fornecedor: ")
            telefone = input("Telefone do fornecedor: ")
        
            fornecedor: Fornecedor = self.repository_fornecedor.inserir_fornecedor(bd, Fornecedor(cnpj, nome, telefone))

            if fornecedor:
                print(f"{fornecedor} cadastrado.")
            else:
                print("Erro ao cadastrar o Fornecedor!")
        else:
            print("CNPJ já cadastrado!")

    def excluir_fornecedor(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        cnpj = input("CNPJ do fornecedor a ser excluído: ")
        if self.repository_fornecedor.existencia_fornecedor(bd, cnpj):
            
            fornecedor: Fornecedor = self.repository_fornecedor.buscar_fornecedor(bd, cnpj)
            excluido: bool = self.repository_fornecedor.excluir_fornecedor(bd, cnpj)

            if not excluido:
                print("Fornecedor não pode ser excluído!\n**Está associado na tabela PRODUTOS_FORNECEDORES")
                return
            
            print(f"{fornecedor} excluído.")
        else:
            print("CNPJ não encontrado!")

    def atualizar_fornecedor(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        cnpj = input("CNPJ do fornecedor para atualização: ")
        if self.repository_fornecedor.existencia_fornecedor(bd, cnpj):
            nome = input("Nome novo do fornecedor: ")
            telefone = input("Telefone novo do fornecedor: ")
            
            fornecedor_antigo = self.repository_fornecedor.buscar_fornecedor(bd, cnpj)
            self.repository_fornecedor.atualizar_fornecedor(bd, Fornecedor(cnpj, nome, telefone))
            fornecedor_novo = self.repository_fornecedor.buscar_fornecedor(bd, cnpj)

            if fornecedor_antigo != fornecedor_novo:
                print(f"{fornecedor_antigo} atualizado.")
            else:
                print("Erro ao atualizar o fornecedor!")
        else:
            print("CNPJ não encontrado!")
    
    def buscar_fornecedor(self):
            bd = ConexaoOracle(can_write=False)
            bd.connect()

            cnpj: str = input("cnpj do fornecedor: ")

            fornecedor: Fornecedor = self.repository_fornecedor.buscar_fornecedor(bd, cnpj)
            
            if fornecedor:
                print(fornecedor)
            else:
                print("Fornecedor não encontrado pelo CNPJ")