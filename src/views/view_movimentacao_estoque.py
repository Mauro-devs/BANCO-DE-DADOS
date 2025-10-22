from src.controller.controller_movimentacao_estoque import ControllerMovimentacaoEstoque
from src.utils.config import limpar_console

def view_movimentacao_estoque():
    controller = ControllerMovimentacaoEstoque()

    sair = False

    while not sair:
        print("--------------------")
        print(" MENU MOVIMENTACAO/ESTOQUE\n")
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
            controller.inserir_movimentacao_estoque()
        
        elif opcao == 2:
            controller.buscar_movimentacao_estoque()

        elif opcao == 3:
            controller.atualizar_movimentacao_estoque()

        elif opcao == 4:
            controller.excluir_movimentacao_estoque()

        elif opcao == 5:
            return True
        
        else:
            print("Insira uma opção válida!")
            return False