from produtos import Produto
from fornecedores import Fornecedor

class ProdutoFornecedor:
    def __init__(self, id:int=None, produto:Produto=None, fornecedor:Fornecedor=None):
        self._id = id
        self._produto = produto
        self._fornecedor = fornecedor

    def get_id(self):
        return self._id

    def get_produto(self):
        return self._produto

    def get_fornecedor(self):
        return self._fornecedor

    def set_id(self, id:int):
        self._id = id

    def set_produto(self, produto:Produto):
        self._produto = produto
    
    def set_fornecedor(self, fornecedor:Fornecedor):
        self._fornecedor = fornecedor

    def __str__(self):
        return f"Fornecedor/Produto: (ID: {self._id}), Produto: [{self._produto}], Fornecedor: [{self._fornecedor}]"