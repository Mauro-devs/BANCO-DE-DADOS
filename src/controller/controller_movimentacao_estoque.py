from src.repository.repository_funcionario import RepositoryFuncionario
from src.repository.repository_produto_fornecedores import RepositoryProdutoFornecedores
from src.repository.repository_movimentacao_estoque import RepositoryMovimentacaoEstoque
from src.conexion.conexao_oracle import ConexaoOracle
from src.model.movimentacoes_estoque import MovimentacaoEstoque
from datetime import date

class ControllerMovimentacaoEstoque:
    def __init__(self):
        self.repository_produto_fornecedores = RepositoryProdutoFornecedores()
        self.repository_funcionario = RepositoryFuncionario()
        self.repository_movimentacao_estoque = RepositoryMovimentacaoEstoque()

    def inserir_movimentacao_estoque(self):
        try:
            bd = ConexaoOracle(can_write=True)
            bd.connect()

            # verificar fk produto_fornecedor
            id_produto_fornecedor = int(input("ID da associação PRODUTO/FORNECEDOR: "))
            obj_produto_fornecedor = self.repository_produto_fornecedores.buscar_produto_fornecedor(bd, id_produto_fornecedor)
            if not obj_produto_fornecedor:
                print("Associação PRODUTO/FORNECEDOR não cadastrada!")
                return None
        
            # verificar fk funcionario
            cpf_funcionario = input("CPF do funcionário: ")
            obj_funcionario = self.repository_funcionario.buscar_funcionario(bd, cpf_funcionario)
            if not obj_funcionario:
                print("Funcionário não cadastrado!")
                return None

            quantidade = int(input("Quantidade: "))
            tipo_movimentacao = input("Tipo de movimentação (ENTRADA/SAÍDA): ")
            if tipo_movimentacao not in ["ENTRADA", "SAÍDA", "SAIDA"]:
                print("Tipo de movimentação inválido! Use 'ENTRADA' ou 'SAÍDA'.")
                return
            
            data_atual = date.today()

            movimentacao_estoque = self.repository_movimentacao_estoque.inserir_movimentacao_estoque(bd, obj_produto_fornecedor, obj_funcionario, quantidade, tipo_movimentacao, data_atual)

            if movimentacao_estoque:
                print(f"Movimentação de estoque com ID {movimentacao_estoque.get_id()} cadastrada.")
            else:
                print("Erro ao Cadastrada!")
        except ValueError:
            print("Quantidade inválida!")
        except Exception as e:
            print(e)
        
    def excluir_movimentacao_estoque(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        try:
            id = int(input("ID da movimentação de estoque a ser excluída: "))
        except ValueError:
            print("ID inválido!")
            return
        
        if self.repository_movimentacao_estoque.existencia_movimentacao_estoque(bd, id):
            
            excluido: bool = self.repository_movimentacao_estoque.excluir_movimentacao_estoque(bd, id)

            if excluido:
                print("Movimentação excluída com sucesso.")
            else:
                print("ID não encontrado!")
    
    def buscar_movimentacao_estoque(self):
        bd = ConexaoOracle(can_write=False)
        bd.connect()

        try:
            id = int(input("ID da movimentação de estoque: "))
        except ValueError:
            print("ID inválido!")
            return None

        movimentacao_estoque = self.repository_movimentacao_estoque.buscar_movimentacao_estoque(bd, id)

        if movimentacao_estoque:
            print(movimentacao_estoque)
        else:
            print("Movimentação não encontrada com este ID!")

    def atualizar_movimentacao_estoque(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        try:
            id = int(input("ID da movimentação de estoque para atualização: "))
        except ValueError:
            print("ID inválido!")
            return None
        
        try:
            if self.repository_movimentacao_estoque.existencia_movimentacao_estoque(bd, id):
                quantidade = int(input("Quantidade nova: "))
                tipo_movimentacao = input("Tipo de movimentação nova (ENTRADA/SAÍDA): ")
                if tipo_movimentacao not in ["ENTRADA", "SAÍDA", "SAIDA"]:
                    print("Tipo de movimentação inválido! Use 'ENTRADA' ou 'SAÍDA'.")
                    return

                movimentacao_antiga = self.repository_movimentacao_estoque.buscar_movimentacao_estoque(bd, id)

                id_produto_fornecedor = movimentacao_antiga.get_produto_fornecedor().get_id()
                self.repository_movimentacao_estoque.atualizar_movimentacao_estoque(bd, id_produto_fornecedor, quantidade, tipo_movimentacao)
                movimentacao_nova = self.repository_movimentacao_estoque.buscar_movimentacao_estoque(bd, id)

                if movimentacao_antiga != movimentacao_nova:
                    print(f"Movimentacao com ID {id} atualizado.")
                else:
                    print("Erro ao atualizar a movimentação de estoque!")
            else:
                print("ID não encontrado!")
        except ValueError:
            print("Quantidade inválida!")
        except Exception as e:
            print(e)