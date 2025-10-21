from src.conexion.conexao_oracle import ConexaoOracle
from src.model.produtos import Produto
from src.repository.repository_produto import RepositoryProduto
class ControllerProduto:
    def __init__(self):
        self.repository_produto = RepositoryProduto()

    def inserir_produto(self):
            try:
                bd = ConexaoOracle(can_write=True)
                bd.connect()

                nome = input("Nome do produto: ")
                preco = float(input("Preco do produto: "))
                descricao = input("Descricao do produto: ")
                categoria = input("Categoria do produto: ")

                if categoria not in ["MOUSE", "TECLADO", "MONITOR", "HEADSET", "MOUSE_PAD"]:
                    print("Categoria inválida -> (MOUSE, TECLADO, MONITOR, HEADSET, MOUSE_PAD)")
                    return

                produto_cadastrado: Produto = self.repository_produto.inserir_produto(bd, nome, preco, descricao, categoria)

                if produto_cadastrado:
                    print(f"Produto cadastrado com ID {produto_cadastrado.get_id()}.")
                else:
                    print(f"Erro ao cadastrar o produto")
                
                print() #Deixa para o visual ficar melhor

            except Exception:
                ...

    def excluir_produto(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        id = input("ID do produto a ser excluído: ")
        if self.repository_produto.existencia_produto(bd, id):
            
            produto_excluido: Produto = self.repository_produto.buscar_produto(bd, id)
            excluido: bool = self.repository_produto.excluir_produto(bd, id)

            if not excluido:
               print("Produto não pode ser excluido!\n**Está associada na tabela PRODUTOS_FORNECEDORES") 
               return
                
            if produto_excluido:
                print(f"{produto_excluido} excluído.")
            else:
                print("Erro ao excluir o produto!")
        else:
            print("ID não encontrado!")
        
        print() #Deixa para o visual ficar melhor

    def atualizar_produto(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        id = input("ID do produto para atualização: ")
        if self.repository_produto.existencia_produto(bd, id):
            nome = input("Nome novo do produto: ")
            preco = float(input("Preco novo do produto: "))
            descricao = input("Descricao nova do produto: ")
            categoria = input("Categoria nova do produto: ")
            
            produto_antigo = self.repository_produto.buscar_produto(bd, id)
            self.repository_produto.atualizar_produto(bd, Produto(id, nome, preco, descricao, categoria))
            produto_novo = self.repository_produto.buscar_produto(bd, id)

            if produto_antigo != produto_novo:
                print(f"{produto_novo} atualizado.")
            else:
                print("Erro ao atualizar o produto!")
        else:
            print("ID não encontrado!")

    print() #Deixa para o visual ficar melhor
    
    def buscar_produto(self):
        bd = ConexaoOracle(can_write=False)
        bd.connect()
        
        id: int = int(input("Id do produto: "))

        produto: Produto = self.repository_produto.buscar_produto(bd, id)

        if produto:
            print(produto)
        else:
            print("ID não encontrado!")
        
        print() #Deixa para o visual ficar melhor

if __name__ == "__main__":
    c = ControllerProduto
    c.inserir_produto()