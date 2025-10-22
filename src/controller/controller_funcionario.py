from src.model.funcionarios import Funcionario
from src.conexion.conexao_oracle import ConexaoOracle
from src.repository.repository_funcionario import RepositoryFuncionario
from src.tasks.validacoes import validar_confirmacao, validar_continuacao
from src.reports.relatorios import Relatorio
from src.utils.config import limpar_console

class ControllerFuncionario:
    def __init__(self):
        self.repository_funcionario = RepositoryFuncionario()

    def inserir_funcionario(self):
        while True:
            bd = ConexaoOracle(can_write=True)
            bd.connect()

            print("--------------------------------------------------")
            print("Listagem Funcionários")
            # Se não tiverem registros
            if not Relatorio().get_relatorio_funcionarios():
                print()

            print("--------------------------------------------------")
            cpf = input("CPF do funcionário novo: ")

            #Verifica se já existe pelo cpf
            if not self.repository_funcionario.existencia_funcionario(bd, cpf):
                nome = input("Nome do funcionário: ")
                telefone = input("Telefone do funcionário: ")
            
                funcionarioInserido: Funcionario = self.repository_funcionario.inserir_funcionario(bd, Funcionario(cpf, nome, telefone))

                if funcionarioInserido:
                    print(f"{funcionarioInserido} cadastrado.")

                    if validar_continuacao("Deseja continuar inserindo registros?"):
                        limpar_console()
                    else:
                        limpar_console()
                        break

                else:
                    print("Erro ao inserir o funcionário!")
            else:
                print("CPF já cadastrado!")
                if not validar_continuacao("Deseja continuar inserindo registros?"):
                    break
            print() #Deixa para o visual ficar melhor
        return False

    def excluir_funcionario(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        if not Relatorio().get_relatorio_funcionarios():
            input("Aperte enter para sair...")
            return

        cpf = input("CPF do funcionário a ser excluído: ")
        if self.repository_funcionario.existencia_funcionario(bd, cpf):
            funcionario_excluido: Funcionario = self.repository_funcionario.buscar_funcionario(bd, cpf)
            
            if validar_confirmacao("Deseja realmente excluir este registro?"):
                excluido: bool = self.repository_funcionario.excluir_funcionario(bd, cpf)
                
                if excluido:
                    limpar_console()
                    print(f"{funcionario_excluido} excluído.")
                else:
                    print("Funcionário não pode ser excluído!\n**Está associado na tabela MOVIMENTACAO_ESTOQUE")
            else:
                print("Remoção cancelada pelo usuário.")
        else:
            print("CPF não encontrado!")

        print() #Deixa para o visual ficar melhor

    def atualizar_funcionario(self):
        bd = ConexaoOracle(can_write=True)
        bd.connect()

        if not Relatorio().get_relatorio_funcionarios():
            input("Aperte enter para sair...")
            return

        cpf = input("CPF do funcionário para atualização: ")
        if self.repository_funcionario.existencia_funcionario(bd, cpf):
            nome = input("Nome novo do funcionário: ")
            telefone = input("Telefone novo do funcionário: ")

            funcionario_atualizar = Funcionario(cpf, nome, telefone)

            self.repository_funcionario.atualizar_funcionario(bd, funcionario_atualizar)
                
            print(f"{funcionario_atualizar} atualizado.")

            if validar_continuacao("Deseja alterar mais registros?"):
                limpar_console()
                return True

        else:
            print("CPF não encontrado!")

        print() #Deixa para o visual ficar melhor

        return False

    def buscar_funcionario(self):
        bd = ConexaoOracle(can_write=False)
        bd.connect()

        if not self.repository_funcionario.existencia_funcionarios(bd):
                print("Não há funcionários cadastrados!")
                input("Aperte enter para sair...")
                return

        cpf = input("CPF do funcionário: ")

        funcionario: Funcionario = self.repository_funcionario.buscar_funcionario(bd, cpf)

        if funcionario:
            print(funcionario)

        else:
            print("Usuário não econtrado com este CPF!")

        print() #Deixa para o visual ficar melhor