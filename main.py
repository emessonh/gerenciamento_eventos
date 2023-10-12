from estruturas.hash_table import * 
from menus import *

while True:
    opcao = menuInicial()
    if opcao == 1:
        evento = menuInserirEvento()
        print('Evento inserido com sucesso!')
    elif opcao == 2:
        evento = menuRemoverEvento()
        print('Evento Removido com sucesso!')
    elif opcao == 3:
        categoria = listarEventosCat()
        print('Categoria: ')
        print('Eventos: ')
    elif opcao == 4:
        categoria = listarCategorias()
        print('Categorias disponíveis: ')
    elif opcao == 5:
        print('Finalizando sistema...')
        break
    else:
        print('Opção inválida!')