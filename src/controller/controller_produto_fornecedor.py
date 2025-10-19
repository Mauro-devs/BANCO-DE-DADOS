from controller_produto import ControllerProduto
from controller.controller_fornecedor import ControllerFornecedor
from connexion.conexao_oracle import ConexaoOracle
from model.produtos_fornecedores import ProdutoFornecedor

class ControllerProdutoFornecedor:
    def __init__ (self):
        self.ctrl_produto = ControllerProduto()
        self.ctrl_fornecedor = ControllerFornecedor()

    def inserir_produto_fornecedor(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        # verificar fk produto
        id_produto = input("ID do produto: ")
        obj_produto = self.ctrl_produto.buscar_produto(bd, id_produto)
        if not obj_produto:
            print("Produto não cadastrado! Cadastre o produto antes de associá-lo a um fornecedor.")
            return None
        
        # verificar fk fornecedor
        cnpj = input("CNPJ do fornecedor: ")
        obj_fornecedor = self.ctrl_fornecedor.buscar_fornecedor(bd, cnpj)
        if not obj_fornecedor:
            print("Fornecedor não cadastrado! Cadastre o fornecedor antes de associá-lo a um produto.")
            return None
        
        id_produto_fornecedor = input("ID para a associação PRODUTO/FORNECEDOR: ")
        if self.existencia_produto_fornecedor(bd, id_produto_fornecedor):
            print("ID já cadastrado!")
            return None

        bd.write(f"INSERT INTO PRODUTOS_FORNECEDORES (ID_PRODUTO_FORNECEDOR, ID_PRODUTO, CNPJ_FORNECEDOR) VALUES ('{id_produto_fornecedor}', '{id_produto}', '{cnpj}')")
        print("Produto associado ao fornecedor com sucesso.")
        produto_fornecedor = ProdutoFornecedor(id_produto_fornecedor, obj_produto, obj_fornecedor)
        print(f"{produto_fornecedor} cadastrado.")
        return produto_fornecedor
    
    def excluir_produto_fornecedor(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        id = input("ID da associação PRODUTO/FORNECEDOR a ser excluída: ")
        if self.existencia_produto_fornecedor(bd, id):
            check_fk = f"SELECT 1 FROM MOVIMENTACAO_ESTOQUE WHERE ID_PRODUTO_FORNECEDOR = '{id}'"
            if bd.sqlToTuple(check_fk):
                print("Associação não pode ser excluída!\n**Está associada na tabela MOVIMENTACAO_ESTOQUE")
                return

            bd.write(f"DELETE FROM PRODUTOS_FORNECEDORES WHERE ID_PRODUTO_FORNECEDOR = '{id}'")
            print(f"A associação com ID {id} excluída.")
        else:
            print("ID não encontrado!")

    def atualizar_produto_fornecedor(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        id = input("ID da associação PRODUTO/FORNECEDOR para atualização: ")
        if self.existencia_produto_fornecedor(bd, id):
            # verificar fk produto
            id_produto = input("ID do produto: ")
            obj_produto = self.ctrl_produto.buscar_produto(bd, id_produto)
            if not obj_produto:
                print("Produto não cadastrado! Cadastre o produto antes de associá-lo a um fornecedor.")
                return None
            
            # verificar fk fornecedor
            cnpj = input("CNPJ do fornecedor: ")
            obj_fornecedor = self.ctrl_fornecedor.buscar_fornecedor(bd, cnpj)
            if not obj_fornecedor:
                print("Fornecedor não cadastrado! Cadastre o fornecedor antes de associá-lo a um produto.")
                return None

            bd.write(f"UPDATE PRODUTOS_FORNECEDORES SET ID_PRODUTO = '{id_produto}', CNPJ_FORNECEDOR = '{cnpj}' WHERE ID_PRODUTO_FORNECEDOR = '{id}'")
            produto_fornecedor = ProdutoFornecedor(id, obj_produto, obj_fornecedor)
            print(f"{produto_fornecedor} atualizado.")
            return produto_fornecedor
        else:
            print("ID não encontrado!")
            return None 

    def existencia_produto_fornecedor(self, bd:ConexaoOracle, id:int):
        query = f"SELECT 1 FROM PRODUTOS_FORNECEDORES WHERE ID_PRODUTO_FORNECEDOR = '{id}'"
        return True if bd.sqlToTuple(query) else False