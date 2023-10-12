class HashTable:
    def __init__(self):
        self.tamanho_categorias = 1
        self.qtd_eventos_categoria = 1
        self.categoria = [None] 
        self.eventos = [[None]] 
    
    def aumentar_tamanho_eventos(self):
        self.qtd_eventos_categoria = self.qtd_eventos_categoria*2
        for c in range(0, self.tamanho_categorias):
            for i in range(0, self.qtd_eventos_categoria//2):
                self.eventos[c].append(None) 
    
    def aumentar_tamanho_categoria(self):
        self.tamanho_categorias = self.tamanho_categorias*2
        for i in range(0, self.tamanho_categorias//2):
            self.categoria.append(None) 
        for c in range(0, self.tamanho_categorias//2):
            self.eventos.append([None]*((self.qtd_eventos_categoria*2)//2))

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
        # verifica se a categoria já existe
        if categoria in self.categoria:
            # Verifica se o slot da categoria 
            if self.categoria[valor_hash_categoria] == categoria:
                # verifica se o slot do evento está vazio
                for i in range(0, len(self.eventos[valor_hash_categoria])):
                    if self.eventos[valor_hash_categoria][i] == None:
                        self.eventos[valor_hash_categoria][i] = evento
                        break
            # executa caso o slot nao seja o da categoria
            else:
                # calcula um novo hash para a categoria
                novo_hash_categoria = self.rehashing(valor_hash_categoria)
                # verifica se o slot para o evento está vazio
                for i in range(0, len(self.eventos[novo_hash_categoria])):
                    if self.eventos[novo_hash_categoria][i] == None:
                        self.eventos[novo_hash_categoria][i] = evento
                        break

        # executa caso a categoria não exista
        else:
            # Verifica se o slot da categoria está vazio
            if self.categoria[valor_hash_categoria] == None:
                self.categoria[valor_hash_categoria] = categoria
                for i in range(0, len(self.eventos[valor_hash_categoria])):
                    if self.eventos[valor_hash_categoria][i] == None:
                        self.eventos[valor_hash_categoria][i] = evento
                        break
            # executa caso o slot nao esteja vazio
            else:
                # calcula um novo hash para a categoria
                novo_hash_categoria = self.rehashing(valor_hash_categoria)
                self.categoria[novo_hash_categoria] = categoria
                # verifica se o slot para o evento está vazio
                for i in range(0, len(self.eventos[novo_hash_categoria])):
                    if self.eventos[novo_hash_categoria][i] == None:
                        self.eventos[novo_hash_categoria][i] = evento
                        break
    
    def remove(self, categoria, evento):
        categoria = categoria.upper()
        evento = evento.upper()
        valor_hash_categoria = self.hashfunction(categoria)
        if self.categoria[valor_hash_categoria] == categoria:
            for i in range(0, len(self.eventos[valor_hash_categoria])):
                if self.eventos[valor_hash_categoria][i] == evento:
                    self.eventos[valor_hash_categoria][i] = None
                    break
        else:
            novo_hash_categoria = self.rehashing(valor_hash_categoria)
            for i in range(0, len(self.eventos[novo_hash_categoria])):
                if self.eventos[novo_hash_categoria][i] == evento:
                    self.eventos[novo_hash_categoria][i] = None
                    break

# hashtable = HashTable()
# hashtable.put('Festa', 'Balada')
# hashtable.aumentar_tamanho_categoria()
# hashtable.aumentar_tamanho_eventos()
# hashtable.put('festa', 'Casamento')
# hashtable.put('Tecnologia', 'palestra')
# hashtable.aumentar_tamanho_eventos()
# hashtable.remove('festa', 'balada')
# hashtable.remove('tecnologia', 'PALESTRA')
# # hashtable.aumentar_tamanho_categoria()
# print(hashtable.categoria)
# print(hashtable.eventos)



