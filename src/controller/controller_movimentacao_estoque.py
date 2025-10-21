from src.controller.controller_produto_fornecedor import ControllerProdutoFornecedor
from repository.repository_funcionario import RepositoryFuncionario
from repository.repository_produto_fornecedores import RepositoryProdutoFornecedores
from src.conexion.conexao_oracle import ConexaoOracle
from src.model.movimentacoes_estoque import MovimentacaoEstoque
from datetime import date

class ControllerMovimentacaoEstoque:
    def __init__(self):
        self.repository_produto_fornecedores = ControllerProdutoFornecedor()
        self.repository_funcionario = RepositoryFuncionario()

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
                return None
            data_atual = date.today()

            query = "INSERT INTO MOVIMENTACAO_ESTOQUE (ID_PRODUTO_FORNECEDOR, CPF_FUNCIONARIO, QUANTIDADE, TIPO_MOVIMENTACAO, DATA_MOVIMENTACAO) VALUES (:1, :2, :3, :4, :5) RETURNING ID_MOVIMENTACAO INTO :6"
            params = (id_produto_fornecedor, cpf_funcionario, quantidade, tipo_movimentacao, data_atual)
            id_movimentacao = bd.return_id(query, params)
            if id_movimentacao:
                movimentacao_estoque = MovimentacaoEstoque(id_movimentacao, obj_produto_fornecedor, obj_funcionario, quantidade, tipo_movimentacao, data_atual)
                print(f"Movimentação de estoque com ID {id_movimentacao} cadastrada.")
                return movimentacao_estoque
            else:
                print("Erro ao Cadastrada!")
        except ValueError:
            print("Quantidade inválida!")
        except Exception as e:
            print(e)
            return None
        
    def excluir_movimentacao_estoque(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        try:
            id = int(input("ID da movimentação de estoque a ser excluída: "))
        except ValueError:
            print("ID inválido!")
            return None
        
        if self.existencia_movimentacao_estoque(bd, id):
            bd.write(f"DELETE FROM MOVIMENTACAO_ESTOQUE WHERE ID_MOVIMENTACAO = {id}")
            print(f"Movimentacao com ID {id} excluída.")
        else:
            print("ID não encontrado!")

    def atualizar_movimentacao_estoque(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        try:
            id = int(input("ID da movimentação de estoque para atualização: "))
        except ValueError:
            print("ID inválido!")
            return None
        
        try:
            if self.existencia_movimentacao_estoque(bd, id):
                quantidade = int(input("Quantidade nova: "))
                tipo_movimentacao = input("Tipo de movimentação nova (ENTRADA/SAÍDA): ")
                if tipo_movimentacao not in ["ENTRADA", "SAÍDA", "SAIDA"]:
                    print("Tipo de movimentação inválido! Use 'ENTRADA' ou 'SAÍDA'.")
                    return None
                data_atual = date.today()
                bd.write(f"UPDATE MOVIMENTACAO_ESTOQUE SET QUANTIDADE = {quantidade}, TIPO_MOVIMENTACAO = '{tipo_movimentacao}', DATA_MOVIMENTACAO = '{data_atual}' WHERE ID_MOVIMENTACAO = {id}")

                dados_movimentacao = bd.sqlToTuple(f"SELECT ID_MOVIMENTACAO, ID_PRODUTO_FORNECEDOR, CPF_FUNCIONARIO, QUANTIDADE, TIPO_MOVIMENTACAO, DATA_MOVIMENTACAO FROM MOVIMENTACAO_ESTOQUE WHERE ID_MOVIMENTACAO = {id}")
                if dados_movimentacao:
                    obj_produto_fornecedor = self.ctrl_produto_fornecedor.buscar_produto_fornecedor(bd, dados_movimentacao[1])
                    obj_funcionario = self.repository_funcionario.buscar_funcionario(bd, dados_movimentacao[2])

                    if obj_produto_fornecedor and obj_funcionario:
                        movimentacao_estoque = MovimentacaoEstoque(dados_movimentacao[0], obj_produto_fornecedor, obj_funcionario, dados_movimentacao[3], dados_movimentacao[4], dados_movimentacao[5])
                        print(f"Movimentacao com ID {id} atualizado.")
                        return movimentacao_estoque
                    else:
                        print("Falha ao buscar PRODUTO/FORNECEDOR ou Funcionario após atualização!")
                else:
                    print("Erro ao buscar a movimentação de estoque atualizada!")
            else:
                print("ID não encontrado!")
        except ValueError:
            print("Quantidade inválida!")
        except Exception as e:
            print(e)
            
    def existencia_movimentacao_estoque(self, bd:ConexaoOracle, id:int):
        query = f"SELECT 1 FROM MOVIMENTACAO_ESTOQUE WHERE ID_MOVIMENTACAO = {id}"
        return True if bd.sqlToTuple(query) else False