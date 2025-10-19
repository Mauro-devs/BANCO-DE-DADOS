from src.connexion.conexao_oracle import ConexaoOracle
from src.model.produtos import Produto

class ControllerProduto:
    def __init__(self):
        pass

    def inserir_produto(self) -> Produto:
            
            try:
                bd = ConexaoOracle(can_write=True)
                bd.connect()

                #Lógica de verificar se o produto já existe para adicionar outro não faz sentido, 
                #pois eu posso ter dois produtos iguais, porém o id sempre será diferente

                nome = input("Nome do produto: ")
                preco = float(input("Preco do produto: "))
                descricao = input("Descricao do produto: ")
                categoria = input("Categoria do produto: ")
                sql_insert = bd.write(f"INSERT INTO PRODUTOS (NOME , PRECO_UNITARIO, DESCRICAO, CATEGORIA) VALUES ('{nome}', {preco}, '{descricao}', '{categoria}')")
                params = (nome, preco, descricao, categoria)

                dados_produto = bd.sqlToTuple(sql_insert, params)
                
                if dados_produto:
                    produto = Produto(dados_produto[0], dados_produto[1], dados_produto[2], dados_produto[3], dados_produto[4])
                    print(f"Produto com id {produto[1]} cadastrado.")
                    return produto
                else:
                    print("Erro ao buscar o produto cadastrado!")
            except Exception:
                ...

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
        

if __name__ == "__main__":
    c = ControllerProduto
    c.inserir_produto()