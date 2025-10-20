import os

def limpar_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")