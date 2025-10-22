from src.conexion.conexao_oracle import ConexaoOracle
from src.model.produtos import Produto
from src.repository.repository_produto import RepositoryProduto
from src.tasks.validacao_insercao import validar_insercao
from src.tasks.validacao_alteracao import validar_alteracao
from src.tasks.validacao_remocao import validar_remocao
from src.reports.relatorios import Relatorio
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

                    if validar_insercao():
                        return True

                else:
                    print(f"Erro ao cadastrar o produto")
                
                print() #Deixa para o visual ficar melhor

            except Exception:
                ...
            
            print()
            return False

    def excluir_produto(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        Relatorio().get_relatorio_produtos()

        id = input("ID do produto a ser excluído: ")
        if self.repository_produto.existencia_produto(bd, id):
            
            produto_excluido: Produto = self.repository_produto.buscar_produto(bd, id)

            if validar_remocao():
                excluido: bool = self.repository_produto.excluir_produto(bd, id)
                print(f"{produto_excluido} excluído.")

            elif not excluido:
               print("Produto não pode ser excluido!\n**Está associada na tabela PRODUTOS_FORNECEDORES")  
        else:
            print("ID não encontrado!")
        
        print() #Deixa para o visual ficar melhor

    def atualizar_produto(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        Relatorio().get_relatorio_produtos()

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

                if validar_alteracao():
                    return True
            else:
                print("Erro ao atualizar o produto!")
        else:
            print("ID não encontrado!")

        print() #Deixa para o visual ficar melhor
        return False
    
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