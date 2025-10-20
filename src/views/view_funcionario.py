from src.controller.controller_funcionario import ControllerFuncionario
from src.utils import limpar_console

def view_funcionario():
    controller = ControllerFuncionario()

    sair = False

    while not sair:
        print("--------------------")
        print(" MENU FUNCIONARIO\n")
        print("1) ADICIONAR")
        print("2) BUSCAR")
        print("3) ATUALIZAR")
        print("4) REMOVER")
        print("5) VOLTAR AO MENU PRINCIPAL")

        try:
            opcao = int(input("--: "))
            limpar_console()
        
        except ValueError:
            print("Insira um valor válido!")
            print()
            return False
        
        if opcao == 1:
            controller.inserir_funcionario()
        
        elif opcao == 2:
            controller.buscar_funcionario()

        elif opcao == 3:
            controller.atualizar_funcionario()

        elif opcao == 4:
            controller.excluir_funcionario()

        elif opcao == 5:
            return True
        
        else:
            print("Insira uma opção válida!")
            return False