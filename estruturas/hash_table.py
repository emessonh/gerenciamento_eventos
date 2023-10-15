import sys
sys.path.append('C:\Projetos\Estrutura_dados\gerenciamento_eventos')
from evento import *

class HashTable:
    def __init__(self):
        self.tamanho_categorias = 0
        self.qtd_eventos_categoria = 0
        self.categoria = [None] 
        self.eventos = [[None]] 
    
    def tamanhoCateg(self):
        return self.tamanho_categorias
    
    def tamanhoEventos(self):
        return self.qtd_eventos_categoria

    def aumentar_tamanho_eventos(self):
        for c in range(0, self.tamanho_categorias):
            for i in range(0, self.qtd_eventos_categoria):
                self.eventos[c].append(None) 
    
    def aumentar_tamanho_categoria(self):
        for i in range(0, self.tamanho_categorias):
            self.categoria.append(None) 
        for c in range(0, self.tamanho_categorias):
            self.eventos.append([None]*len(self.eventos[0]))

    def hashfunction(self, palavra):
        valor_categoria = 0
        for letra in palavra:
            valor_categoria += ord(letra)
        valor_hash = valor_categoria%len(self.categoria)
        return valor_hash

    def rehashing(self, oldhash):
        return (oldhash+1)%len(self.categoria)

    def put(self, categoria_evento, nome_evento, descricao_evento):
        categoria = categoria_evento.upper()
        nome_evento = nome_evento.upper()
        valor_hash_categoria = self.hashfunction(categoria)
        evento = Evento(nome_evento, descricao_evento)
        evento_adic = False
        # verifica se a categoria já existe
        if categoria in self.categoria:
            # verifica se o evento já existe
            for evento in self.eventos[valor_hash_categoria]:
                if evento != None and evento.nome == nome_evento:
                    print('Evento já cadastrado!')
                    evento_adic = False
                    return False
            # verifica o tamanho atual da lista de eventos
            if self.qtd_eventos_categoria*0.7 >= len(self.eventos[valor_hash_categoria])*0.7:
                self.aumentar_tamanho_eventos()
            if self.qtd_eventos_categoria*0.7 < len(self.eventos[valor_hash_categoria])*0.7:
                # Verifica se é o slot da categoria 
                if self.categoria[valor_hash_categoria] == categoria:
                    # verifica se o slot do evento está vazio
                    for i in range(0, len(self.eventos[valor_hash_categoria])):
                        if self.eventos[valor_hash_categoria][i] == None:
                            self.eventos[valor_hash_categoria][i] = evento
                            self.qtd_eventos_categoria += 1
                            evento_adic = True
                            break
                # executa caso o slot nao seja o da categoria
                else:
                    # calcula um novo hash para a categoria
                    novo_hash_categoria = self.rehashing(valor_hash_categoria)
                    if self.categoria[novo_hash_categoria] == categoria:
                    # verifica se o slot para o evento está vazio
                        for i in range(0, len(self.eventos[novo_hash_categoria])):
                            if self.eventos[novo_hash_categoria][i] == None:
                                self.eventos[novo_hash_categoria][i] = evento
                                evento_adic = True
                                self.qtd_eventos_categoria += 1
                                break

        # executa caso a categoria não exista
        else:
            # Verifica se o slot da categoria está vazio
            if self.tamanho_categorias*0.7 >= len(self.categoria)*0.7:
                self.aumentar_tamanho_categoria()
            if self.tamanhoCateg()*0.7 < len(self.categoria):
                if self.categoria[valor_hash_categoria] == None:
                    self.categoria[valor_hash_categoria] = categoria
                    self.tamanho_categorias += 1
                    for i in range(0, len(self.eventos[valor_hash_categoria])):
                        if self.eventos[valor_hash_categoria][i] == None:
                            self.eventos[valor_hash_categoria][i] = evento
                            self.qtd_eventos_categoria += 1
                            evento_adic = True
                            break
                # executa caso o slot nao esteja vazio
                else:
                    # procura um slot vazio na lista de categoria
                    for i in range(0, len(self.categoria)):
                        # calcula um novo hash para a categoria
                        novo_hash_categoria = self.rehashing(valor_hash_categoria)
                        if self.categoria[novo_hash_categoria] == None:
                            self.categoria[novo_hash_categoria] = categoria
                            self.tamanho_categorias += 1
                            # verifica se o slot para o evento está vazio
                            for i in range(0, len(self.eventos[novo_hash_categoria])):
                                if self.eventos[novo_hash_categoria][i] == None:
                                    self.eventos[novo_hash_categoria][i] = evento
                                    self.qtd_eventos_categoria += 1
                                    evento_adic = True
                                    break
                            # para a execucao ao achar uma posicao vazia de categoria 
                            break
                        valor_hash_categoria = novo_hash_categoria
        # retorna se o evento foi adicionado com sucesso
        return evento_adic
    
    def getEventosByCat(self, categoria):
        categoria = categoria.upper()
        eventos = []
        valor_hash_categoria = self.hashfunction(categoria)
        if self.tamanho_categorias == 0:
            return []
        elif self.categoria[valor_hash_categoria] == categoria:
            for i in range(0, len(self.eventos[valor_hash_categoria])):
                if self.eventos[valor_hash_categoria][i] != None:
                    eventos.append(self.eventos[valor_hash_categoria][i])
            return eventos
        else:
            for i in range(0, len(self.eventos[0])):
                novo_hash_categoria = self.rehashing(valor_hash_categoria)
                if self.categoria[novo_hash_categoria] == categoria:
                    for i in range(0, len(self.eventos[novo_hash_categoria])):
                        if self.eventos[novo_hash_categoria][i] != None:
                            eventos.append(self.eventos[novo_hash_categoria][i]) 
                    return eventos
                valor_hash_categoria = novo_hash_categoria
        return [False]
        
    def listarCategorias(self):
        for i in range(0, len(self.categoria)):
            if self.categoria[i] != None:
                print(self.categoria[i])

    def getCategoria(self, categoria):
        categoria = categoria.upper()
        valor_hash_categoria = self.hashfunction(categoria)
        if self.categoria[valor_hash_categoria] == categoria:
            return self.categoria[valor_hash_categoria]
        else:
            novo_hash_categoria = self.rehashing(valor_hash_categoria)
            return self.categoria[novo_hash_categoria]
        return None
    
    def remove(self,categoria,nome_evento):
        categoria = categoria.upper()
        nome_evento = nome_evento.upper()
        # Verifica qual o valor da categoria
        valor_hash_categoria = self.hashfunction(categoria)  
        if self.categoria[valor_hash_categoria] == categoria:
            # faz uma iteracao na lista de eventos da categoria
            for i in range(0, len(self.eventos[valor_hash_categoria])):
                if self.eventos[valor_hash_categoria][i] != None:
                    if self.eventos[valor_hash_categoria][i].getNome() == nome_evento:
                        self.eventos[valor_hash_categoria][i] = None
                        self.qtd_eventos_categoria -= 1
                        return True
        else:
            for i in range(0, len(self.eventos[0])):
                # Verifica qual o valor da categoria com o rehashing, novo calculo de hash
                novo_hash_categoria = self.rehashing(valor_hash_categoria)
                if self.categoria[novo_hash_categoria] == categoria:
                    for i in range(0, len(self.eventos[novo_hash_categoria])):
                        if self.eventos[novo_hash_categoria][i] != None:
                            if self.eventos[novo_hash_categoria][i].getNome() == nome_evento:
                                self.eventos[novo_hash_categoria][i] = None
                                self.qtd_eventos_categoria -= 1
                                return True
                valor_hash_categoria = novo_hash_categoria
        return False
    
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



