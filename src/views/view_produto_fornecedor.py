from src.controller.controller_produto_fornecedor import ControllerProdutoFornecedor
from src.utils import limpar_console

def view_produto_fornecedor():
    controller = ControllerProdutoFornecedor()

    sair = False

    while not sair:
        print("--------------------")
        print(" MENU FORNECEDOR\n")
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
            controller.inserir_produto_fornecedor()
        
        elif opcao == 2:
            controller.buscar_produto_fornecedor()

        elif opcao == 3:
            controller.atualizar_produto_fornecedor()

        elif opcao == 4:
            controller.excluir_produto_fornecedor()

        elif opcao == 5:
            return True
        
        else:
            print("Insira uma opção válida!")
            return False