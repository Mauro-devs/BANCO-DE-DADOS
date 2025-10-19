from connexion.conexao_oracle import ConexaoOracle
from model.produtos import Produto

class ControllerProduto:
    def __init__(self):
        pass

    def inserir_produto(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        id = input("ID do produto novo: ")
        if not self.existencia_produto(bd, id):
            nome = input("Nome do produto: ")
            preco = float(input("Preco do produto: "))
            descricao = input("Descricao do produto: ")
            categoria = input("Categoria do produto: ")
            bd.write(f"INSERT INTO PRODUTOS (ID_PRODUTO, NOME , PRECO_UNITARIO, DESCRICAO, CATEGORIA) VALUES ({id}, '{nome}', {preco}, '{descricao}', '{categoria}')")

            dados_produto = bd.sqlToTuple(f"SELECT ID_PRODUTO, NOME, PRECO_UNITARIO, DESCRICAO, CATEGORIA FROM PRODUTOS WHERE ID_PRODUTO = {id}")
            if dados_produto:
                produto = Produto(dados_produto[0], dados_produto[1], dados_produto[2], dados_produto[3], dados_produto[4])
                print(f"{produto} cadastrado.")
                return produto
            else:
                print("Erro ao buscar o produto cadastrado!")
        else:
            print("ID já cadastrado!")
            return None

    def excluir_produto(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        id = input("ID do produto a ser excluído: ")
        if self.existencia_produto(bd, id):
            check_fk = f"SELECT 1 FROM PRODUTOS_FORNECEDORES WHERE ID_PRODUTO = {id}"
            if bd.sqlToTuple(check_fk):
               print("Produto não pode ser excluido!\n**Está associada na tabela PRODUTOS_FORNECEDORES") 
               return
                
            dados_produto = bd.sqlToTuple(f"SELECT ID_PRODUTO, NOME, PRECO_UNITARIO, DESCRICAO, CATEGORIA FROM PRODUTOS WHERE ID_PRODUTO = {id}")
            bd.write(f"DELETE FROM PRODUTOS WHERE ID_PRODUTO = {id}")
            if dados_produto:
                produto = Produto(dados_produto[0], dados_produto[1], dados_produto[2], dados_produto[3], dados_produto[4])
                print(f"{produto} excluído.")
            else:
                print("Erro ao buscar o produto excluído!")
        else:
            print("ID não encontrado!")

    def atualizar_produto(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        id = input("ID do produto para atualização: ")
        if self.existencia_produto(bd, id):
            nome = input("Nome novo do produto: ")
            preco = float(input("Preco novo do produto: "))
            descricao = input("Descricao nova do produto: ")
            categoria = input("Categoria nova do produto: ")
            bd.write(f"UPDATE PRODUTOS SET NOME = '{nome}', PRECO_UNITARIO = {preco}, DESCRICAO = '{descricao}', CATEGORIA = '{categoria}' WHERE ID_PRODUTO = {id}")

            dados_produto = bd.sqlToTuple(f"SELECT ID_PRODUTO, NOME, PRECO_UNITARIO, DESCRICAO, CATEGORIA FROM PRODUTOS WHERE ID_PRODUTO = {id}")
            if dados_produto:
                produto = Produto(dados_produto[0], dados_produto[1], dados_produto[2], dados_produto[3], dados_produto[4])
                print(f"{produto} atualizado.")
                return produto
            else:
                print("Erro ao buscar o produto atualizado!")
        else:
            print("ID não encontrado!")
            return None

    def existencia_produto(self, bd:ConexaoOracle, id:int):
        query = f"SELECT 1 FROM PRODUTOS WHERE ID_PRODUTO = {id}"
        return True if bd.sqlToTuple(query) else False
    
    def buscar_produto(self, bd:ConexaoOracle, id:int):
        dados_produto = bd.sqlToTuple(f"SELECT ID_PRODUTO, NOME, PRECO_UNITARIO, DESCRICAO, CATEGORIA FROM PRODUTOS WHERE ID_PRODUTO = {id}")
        if dados_produto:
            produto = Produto(dados_produto[0], dados_produto[1], dados_produto[2], dados_produto[3], dados_produto[4])
            return produto
        else:
            print("ID não encontrado!")
            return None