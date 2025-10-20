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
        
        query = "INSERT INTO PRODUTOS_FORNECEDORES (ID_PRODUTO, CNPJ_FORNECEDOR) VALUES (:1, :2) RETURNING ID_PRODUTO_FORNECEDOR INTO :3"
        params = (id_produto, cnpj)
        id_produto_forecedor = bd.return_id(query, params)
        if id_produto_forecedor:
            produto_fornecedor = ProdutoFornecedor(id_produto_forecedor, obj_produto, obj_fornecedor)
            print(f"Associação  PRODUTO_FORNECEDOR com ID {id_produto_forecedor} cadastrada.")
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
                print("Produto não cadastrado!")
                return None
            
            # verificar fk fornecedor
            cnpj = input("CNPJ do fornecedor: ")
            obj_fornecedor = self.ctrl_fornecedor.buscar_fornecedor(bd, cnpj)
            if not obj_fornecedor:
                print("Fornecedor não cadastrado!")
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
    
    def buscar_produto_fornecedor(self, bd:ConexaoOracle, id:int):
        dados = bd.sqlToTuple(f"SELECT ID_PRODUTO_FORNECEDOR, ID_PRODUTO, CNPJ_FORNECEDOR FROM PRODUTOS_FORNECEDORES WHERE ID_PRODUTO_FORNECEDOR = '{id}'")
        if dados:
            obj_produto = self.ctrl_produto.buscar_produto(bd, dados[1])
            obj_fornecedor = self.ctrl_fornecedor.buscar_fornecedor(bd, dados[2])
            produto_fornecedor = ProdutoFornecedor(dados[0], obj_produto, obj_fornecedor)
            return produto_fornecedor
        else:
            return None