from src.repository.repository_produto import RepositoryProduto
from src.repository.repository_fornecedor import RepositoryFornecedor
from src.repository.repository_produto_fornecedores import RepositoryProdutoFornecedores
from src.conexion.conexao_oracle import ConexaoOracle
from src.model.produtos_fornecedores import ProdutoFornecedor
from src.tasks.validacoes import validar_confirmacao, validar_continuacao
from src.reports.relatorios import Relatorio
from src.utils.config import limpar_console

class ControllerProdutoFornecedor:
    def __init__ (self):
        self.repository_produto = RepositoryProduto()
        self.repository_fornecedor = RepositoryFornecedor()
        self.repository_produto_fornecedor = RepositoryProdutoFornecedores()

    def inserir_produto_fornecedor(self):
        while True:
            bd = ConexaoOracle(can_write=True)
            bd.connect()

            if not Relatorio().get_relatorio_produtos_fornecedores():
                input("Aperte enter para sair...")
                return

            # verificar fk produto
            id_produto = input("ID do produto: ")
            produto = self.repository_produto.buscar_produto(bd, id_produto)
            if not produto:
                print("Produto não cadastrado! Cadastre o produto antes de associá-lo a um fornecedor.")
        
            # verificar fk fornecedor
            cnpj = input("CNPJ do fornecedor: ")
            fornecedor = self.repository_fornecedor.buscar_fornecedor(bd, cnpj)
            if not fornecedor:
                print("Fornecedor não cadastrado! Cadastre o fornecedor antes de associá-lo a um produto.")
                return None

            produto_fornecedor: ProdutoFornecedor = self.repository_produto_fornecedor.inserir_produto_fornecedor(bd, produto, fornecedor)
            if produto_fornecedor:
                print(f"Associação PRODUTO/FORNECEDOR com ID {produto_fornecedor.get_id()} cadastrada.")

                if validar_continuacao("Deseja continuar inserindo registros?"):
                    limpar_console()
                else:
                    limpar_console()
                    break
            else:
                print("Erro ao inserir a associação PRODUTO/FORNECEDOR!")
                if not validar_continuacao("Deseja continuar inserindo registros?"):
                    limpar_console()
                    break
        
        print()
        return False
    
    def excluir_produto_fornecedor(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        if not Relatorio().get_relatorio_produtos_fornecedores():
            input("Aperte enter para sair...")
            return

        id = input("ID da associação PRODUTO/FORNECEDOR a ser excluída: ")
        if self.repository_produto_fornecedor.existencia_produto_fornecedor(bd, id):
            
            if validar_confirmacao("Deseja realmente excluir este registro?"):
                excluido: bool = self.repository_produto_fornecedor.excluir_produto_fornecedor(bd, id)
            
                if excluido:
                    print(f"A associação com ID {id} excluída.")
                else:
                    print("Associação PRODUTO/FORNECEDOR não pode ser excluída!\n**Está associada na tabela MOVIMENTACAO_ESTOQUE")
            else:
                print("Remoção cancelada pelo usuário.")
        else:
            print("ID não encontrado!")
        
        print()

    def atualizar_produto_fornecedor(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        if not Relatorio().get_relatorio_produtos_fornecedores():
            input("Aperte enter para sair...")
            return

        id = input("ID da associação PRODUTO/FORNECEDOR para atualização: ")
        if self.repository_produto_fornecedor.existencia_produto_fornecedor(bd, id):
            # verificar fk produto
            id_produto = input("ID do produto: ")
            produto = self.repository_produto.buscar_produto(bd, id_produto)
            if not produto:
                print("Produto não cadastrado!")
                return
            
            # verificar fk fornecedor
            cnpj = input("CNPJ do fornecedor: ")
            fornecedor = self.repository_fornecedor.buscar_fornecedor(bd, cnpj)
            if not fornecedor:
                print("Fornecedor não cadastrado!")
                return

            produto_fornecedor_antigo = ProdutoFornecedor(id, produto, fornecedor)
            self.repository_produto_fornecedor.atualizar_produto_fornecedor(bd, produto_fornecedor_antigo)
            produto_fornecedor_novo: ProdutoFornecedor = self.repository_produto_fornecedor.buscar_produto_fornecedor(bd, id)

            if produto_fornecedor_antigo != produto_fornecedor_novo:
                print(f"{produto_fornecedor_novo} atualizado.")

                if validar_continuacao("Deseja alterar mais registros?"):
                    limpar_console()
                    return True

            else:
                print("Erro ao atualizar produto_fornecedor")
        else:
            print("ID não encontrado!")
            return None 
        
        print()
        return False
    
    def buscar_produto_fornecedor(self):
        bd = ConexaoOracle(can_write = False)
        bd.connect()

        id: str = input("id produto_fornecedor: ")

        produto_fornecedor: ProdutoFornecedor = self.repository_produto_fornecedor.buscar_produto_fornecedor(bd, id)

        if produto_fornecedor:
            print(produto_fornecedor)
        else:
            print("produto_fornecedor não encontrado para esse id.")