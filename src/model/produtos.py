from src.model.categoria import Categoria
class Produto:
    def __init__(self, nome, preco_unitario, categoria: Categoria, id=None, descricao=None):
        self._id = id
        self._nome = nome
        self._preco_unitario = preco_unitario
        self._descricao = descricao
        self._categoria = categoria

    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_preco_unitario(self):
        return self._preco_unitario
    
    def get_descricao(self):
        return self._descricao
    
    def get_categoria(self):
        return self._categoria
    
    def get_categoria(self):
        return self._categoria.get_nome()
    
    def set_nome(self, nome):
        self._nome = nome

    def set_preco_unitario(self, preco_unitario):
        self._preco_unitario = preco_unitario

    def set_descricao(self, descricao):
        self._descricao = descricao

    def set_categoria(self, categoria):
        self._categoria = categoria

    def __str__(self):
        return f"Produto: {self._nome} (ID: {self._id}), Preço Unitário: {self._preco_unitario}, Descrição: {self._descricao}, Categoria: {self._categoria.get_nome()}"