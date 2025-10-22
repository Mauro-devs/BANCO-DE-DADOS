from src.model.produtos import Produto
from src.views.view_principal import principal_menu
from src.utils.config import limpar_console

sair = False

limpar_console()

while not sair:
    sair = principal_menu()