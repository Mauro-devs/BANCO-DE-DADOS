from src.controller.controller_produto import ControllerProduto
from src.utils.config import limpar_console

def view_produto():
    controller = ControllerProduto()

    sair = False

    while not sair:
        print("--------------------")
        print(" MENU PRODUTO\n")
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
            controller.inserir_produto()
        
        elif opcao == 2:
            controller.buscar_produto()

        elif opcao == 3:
            controller.atualizar_produto()

        elif opcao == 4:
            controller.excluir_produto()

        elif opcao == 5:
            return True
        
        else:
            print("Insira uma opção válida!")
            return False