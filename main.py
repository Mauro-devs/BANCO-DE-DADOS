from src.model.produtos import Produto
from src.model.categoria import Categoria

categoria = Categoria(1)
print(categoria)

produto = Produto("Razer ViperX", 220.0, categoria)
print(produto)