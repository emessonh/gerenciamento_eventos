from estruturas.hash_table import *
from menus import *

hashtable = HashTable()
while True:
    opcao = menuInicial()
    if opcao == 1:
        menuInserirEvento(hashtable)
    elif opcao == 2:
        evento = menuRemoverEvento()
        print('Evento Removido com sucesso!')
    elif opcao == 3:
        listarEventosCat(hashtable)
    elif opcao == 4:
        # categoria = listarCategorias()
        print('Categorias disponíveis: ')
    elif opcao == 5:
        print('Finalizando sistema...')
        break
    else:
        print('Opção inválida!')