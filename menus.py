from estruturas.hash_table import *

def menuInicial():
    print('=====================================')
    print('Escolha uma das opções:')
    print('1 - Inserir evento;')
    print('2 - Remover evento;')
    print('3 - Listar eventos por categoria;')
    print('4 - Listar categorias disponíveis;')
    print('5 - Sair;')
    print('=====================================')
    opcao = int(input('> '))
    return opcao

def menuInserirEvento(hashtable):
    print('====================================')
    print('Inserindo Evento:')
    categoria = input('Digite a categoria do evento > ')
    nome_evento = input('Digite o nome do evento > ')
    descricao = input('Descreva-o rapidamente > ')
    print('====================================')
    evento_adic = hashtable.put(categoria, nome_evento, descricao)
    if evento_adic == True:
        print("O evento inserido com sucesso!")
    else:
        print("Falha ao inserir o evento!")

def menuRemoverEvento(hashtable):
    print('====================================')
    print('Removendo Evento:')
    categoria = input('Digite a categoria do evento > ')
    nome_evento = input('Digite o nome do evento > ')
    print('====================================')
    evento_remov = hashtable.remove(categoria, nome_evento)
    print(evento_remov)
    if evento_remov == True:
        print("O evento removido com sucesso!")
    else:
        print("Falha ao remover o evento!")

def listarEventosCat(hashtable):
    categoria = input('Digite a categoria > ')
    print('===================================')
    eventos = hashtable.getEventosByCat(categoria)
    if len(eventos) > 0:
        if eventos[0] == False:
            print('Categoria não encontrada!')
        else:
            print('Listagem de eventos por categoria:')
            cont = 0
            for evento in eventos:
                cont += 1
                print()
                print(f'{cont} - {evento.getNome()}')
                print(f'{cont}.1 - {evento.getDescricao()}')
    else:
        print('Não há eventos cadastrados!')
    print('===================================')
    return categoria

def listarCategorias(hashtable):
    print('===================================')
    print('Listagem de categorias:')
    categorias = hashtable.listarCategorias()
    print('===================================')
    return categorias