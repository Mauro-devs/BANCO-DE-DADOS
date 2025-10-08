import enum
class CategoriaEnum(enum.Enum):
    MOUSE = 1
    TECLADO = 2
    HEADSET = 3
    MOUSEPAD = 4

class Categoria:
    def __init__(self, id):
        self._id = id
        self._nome = CategoriaEnum(id).name

    def get_nome(self):
        return self._nome

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
        self._nome = CategoriaEnum(id).name

    def __str__(self):
        return f"Categoria: {self._nome} (ID: {self._id})"