from src.views.view_funcionario import view_funcionario
from src.views.view_produto import view_produto
from src.views.view_fornecedor import view_fornecedor
from src.views.view_produto_fornecedor import view_produto_fornecedor
from src.utils import limpar_console

def principal_menu():
    print("--------------------")
    print(" MENU PRINCIPAL\n")
    print("1) FUNCIONÁRIOS")
    print("2) PRODUTOS")
    print("3) FORNECEDORES")
    print("4) MOVIMENTAÇÕES")
    print("5) PRODUTO FORNECEDOR")
    print("6) SAIR")

    try:
        opcao = int(input("--: "))
        limpar_console()
        
    
    except ValueError:
        print("Insira um valor válido!")
        print()
        return False

    if opcao == 1:
        view_funcionario()
    
    elif opcao == 2:
        view_produto()

    elif opcao == 3:
        view_fornecedor()

    elif opcao == 4:
        pass

    elif opcao == 5:
        view_produto_fornecedor()
    
    elif opcao == 6:
        return True
    
    else:
        print("Insira uma opção válida!")
        return False