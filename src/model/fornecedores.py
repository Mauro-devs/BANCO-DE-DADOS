class Fornecedor:
    def __init__(self, CNPJ:str, nome:str):
        self._CNPJ = CNPJ
        self._nome = nome

    def get_cnpj(self):
        return self._CNPJ
    
    def get_nome(self):
        return self._nome

    def set_cnpj(self, CNPJ:str):
        self._CNPJ = CNPJ
        
    def set_nome(self, nome:str):
        self._nome = nome

    def __str__(self):
        return f"Fornecedor: {self._nome} (ID: {self._id}), Cnpj: {self._CNPJ}"
