from eventos import Evento

evento = Evento()

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

def menuInserirEvento():
    print('====================================')
    print('Inserindo Evento:')
    categoria = input('Digite a categoria do evento > ')
    nome_evento = input('Digite o nome do evento > ')
    descricao = input('Descreva-o rapidamente > ')
    print('====================================')
    evento.insertiEvento(categoria, nome_evento, descricao)
    return evento

def menuRemoverEvento():
    print('===================================')
    print('Removendo evento:')
    categoria = input('Digite a categoria do evento > ')
    nome_evento = input('Digite o nome do evento > ')
    print('===================================')
    return categoria, nome_evento

def listarEventosCat():
    print('===================================')
    print('Listagem de eventos por categoria:')
    getEvento= evento.get(categoria, evento)
    print(getEvento)
    categoria = input('Digite a categoria > ')
    print('===================================')
    return categoria

def listarCategorias():
    print('==================================')
    print('Listagem de categorias:')
    listaCategoria = evento.listarCategorias()
    print(listaCategoria)
    categoria = input('Digite a categoria > ')
    print('==================================')
    return categoria