class HashTable:
    def __init__(self):
        self.tamanho_categorias = 11
        self.qtd_eventos_categoria = 3
        self.categoria = [None] * self.tamanho_categorias
        self.eventos = [[None] * self.qtd_eventos_categoria] * self.tamanho_categorias 

    def hashfunction(self, palavra):
        valor_categoria = 0
        for letra in palavra:
            valor_categoria += ord(letra)
        valor_hash = valor_categoria%self.tamanho_categorias
        return valor_hash
        # return chave%self.tamanho

    def rehashing(self, oldhash):
        return (oldhash+1)%self.tamanho_categorias
        # return (oldhash+1)%self.tamanho

    def put(self, categoria, evento):
        if categoria in self.categoria:
            valor_hash_categoria = self.hashfunction(categoria)
            valor_hash_evento = self.hashfunction(evento)
            if self.eventos[valor_hash_categoria][valor_hash_evento] == None:
                self.categoria[valor_hash_categoria] = categoria
                self.eventos[valor_hash_categoria][valor_hash_evento] = evento
            else:
                
        else:
            print('Categoria não encontrada!')
        


hashtable = HashTable()
print(hashtable.hashfunction('cat'))



