from estruturas.hash_table import HashTable

class Evento:
    def __init__(self):
        self.eventos = HashTable()

    def insertiEvento(self, categoria, nome, descricao):
        return self.eventos.put(categoria, nome, descricao)
    
    def get(self, categoria, evento):
        return self.eventos.get(categoria, evento)
    
    def getCategoria(self, categoria):
        return self.eventos.getCategoria(categoria)
    
    def listarCategorias(self):
        return self.eventos.listarCategorias()
        
