class HashTable:
    def __init__(self):
        self.tamanho_categorias = 3
        self.qtd_eventos_categoria = 3
        self.categoria = None
        self.eventos = []  
    
    def aumentar_tamanho_eventos(self):
        self.eventos.append([None] * self.qtd_eventos_categoria)
    
    def aumentar_tamanho_categoria(self):
        self.categoria = [None] * self.tamanho_categorias

    def hashfunction(self, palavra):
        valor_categoria = 0
        for letra in palavra:
            valor_categoria += ord(letra)
        valor_hash = valor_categoria%self.tamanho_categorias
        return valor_hash

    def rehashing(self, oldhash):
        return (oldhash+1)%self.tamanho_categorias

    def put(self, categoria, evento):
        categoria = categoria.upper()
        evento = evento.upper()
        valor_hash_categoria = self.hashfunction(categoria)
        valor_hash_evento = self.hashfunction(evento)
        # verifica se a categoria já existe
        if categoria in self.categoria:
            # Verifica se o slot da categoria 
            if self.eventos[valor_hash_categoria] == categoria:
                # verifica se o slot do evento está vazio
                if self.eventos[valor_hash_categoria][valor_hash_evento] == None:
                    self.eventos[valor_hash_categoria][valor_hash_evento] = evento
                # recalcula o hash do evento
                else:
                    novo_hash_evento = self.rehashing(valor_hash_evento)
                    self.eventos[valor_hash_categoria][novo_hash_evento] = evento

        # executa caso a categoria não exista
        else:
            # Verifica se o slot da categoria está vazio
            if self.categoria[valor_hash_categoria] == None:
                self.categoria[valor_hash_categoria] = categoria
                # Verifica se o slot do evento está vazio
                if self.eventos[valor_hash_categoria][valor_hash_evento] == None:
                    self.eventos[valor_hash_categoria][valor_hash_evento] = evento
                # recalcula o rehash do evento
                else:
                    novo_hash_evento = self.rehashing(valor_hash_evento)
                    self.eventos[valor_hash_categoria][novo_hash_evento] = evento
            # executa caso o slot nao esteja vazio
            else:
                # calcula um novo hash para a categoria
                novo_hash_categoria = self.rehashing(valor_hash_categoria)
                self.categoria[novo_hash_categoria] = categoria
                # verifica se o slot para o evento está vazio
                if self.eventos[valor_hash_categoria][valor_hash_evento] == None:
                    self.eventos[valor_hash_categoria][valor_hash_evento] = evento
                # execute caso o slot nao esteja vazio
                else:
                    # calcula um novo hash
                    novo_hash_evento = self.rehashing(valor_hash_evento)
                    self.eventos[valor_hash_categoria][novo_hash_evento] = evento

           

hashtable = HashTable()
hashtable.put('Festa', 'Balada')
hashtable.put('Apresentacao', 'Palestra')
hashtable.put('Venda', 'Venda Livros')
print(hashtable.categoria)
print(hashtable.eventos)



