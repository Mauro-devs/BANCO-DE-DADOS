from src.model.funcionarios import Funcionario
from src.conexion.conexao_oracle import ConexaoOracle
from src.repository.repository_funcionario import RepositoryFuncionario
from src.tasks.validacao_insercao import validar_insercao
from src.tasks.validacao_alteracao import validar_alteracao
from src.tasks.validacao_remocao import validar_remocao
from src.reports.relatorios import Relatorio

class ControllerFuncionario:
    def __init__(self):
        self.repository_funcionario = RepositoryFuncionario()

    def inserir_funcionario(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        cpf = input("CPF do funcionário novo: ")

        #Verifica se já existe pelo cpf
        if not self.repository_funcionario.existencia_funcionario(bd, cpf):
            nome = input("Nome do funcionário: ")
            telefone = input("Telefone do funcionário: ")

            
            funcionarioInserido: Funcionario = self.repository_funcionario.inserir_funcionario(bd, Funcionario(cpf, nome, telefone))

            if funcionarioInserido:
                print(f"{funcionarioInserido} cadastrado.")

                if validar_insercao():
                    return True

            else:
                print("Erro ao inserir o funcionário!")
        else:
            print("CPF já cadastrado!")

        print() #Deixa para o visual ficar melhor
        return False

    def excluir_funcionario(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        Relatorio().get_relatorio_funcionarios()

        cpf = input("CPF do funcionário a ser excluído: ")
        if self.repository_funcionario.existencia_funcionario(bd, cpf):
            funcionario_excluido: Funcionario = self.repository_funcionario.buscar_funcionario(bd, cpf)
            
            if validar_remocao():
                excluido: bool = self.repository_funcionario.excluir_funcionario(bd, cpf)
                
                if funcionario_excluido:
                    print(f"{funcionario_excluido} excluído.")
                    
                elif not excluido:
                    print("Funcionário não pode ser excluído!\n**Está associado na tabela MOVIMENTACAO_ESTOQUE")
        else:
            print("CPF não encontrado!")

        print() #Deixa para o visual ficar melhor

    def atualizar_funcionario(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        Relatorio().get_relatorio_funcionarios()

        cpf = input("CPF do funcionário para atualização: ")
        if self.repository_funcionario.existencia_funcionario(bd, cpf):
            nome = input("Nome novo do funcionário: ")
            telefone = input("Telefone novo do funcionário: ")

            funcionario_atualizar = Funcionario(cpf, nome, telefone)

            self.repository_funcionario.atualizar_funcionario(bd, funcionario_atualizar)
                
            print(f"{funcionario_atualizar} atualizado.")

            if validar_alteracao():
                return True

        else:
            print("CPF não encontrado!")

        print() #Deixa para o visual ficar melhor

        return False

    def buscar_funcionario(self):
        bd = ConexaoOracle(can_write=False)
        bd.connect()

        cpf = input("CPF do funcionário: ")

        funcionario: Funcionario = self.repository_funcionario.buscar_funcionario(bd, cpf)

        if funcionario:
            print(funcionario)

        else:
            print("Usuário não econtrado com este CPF!")

        print() #Deixa para o visual ficar melhor