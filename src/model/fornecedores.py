class Fornecedores:
    def __init__(self, nome:str, CNPJ:str, id=None):
        self._id = id
        self._nome = nome
        self._CNPJ = CNPJ

    def get_nome(self):
        return self._nome
    
    def get_cnpj(self):
        return self._CNPJ
    
    def get_id(self):
        return self._id

    def set_nome(self, nome:str):
        self._nome = nome

    def set_cnpj(self, CNPJ:str):
        self._CNPJ = CNPJ

    def __str__(self):
        return f"Fornecedor: {self._nome} (ID: {self._id}), Cnpj: {self._CNPJ}"
