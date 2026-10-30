import os
os.system('cls')


lista_produtos = []

while True:
    print('''
          === Mercadinho ===
          1- cadastrar
          2-listar todos os produtos
          3-atualizar propdutos
          4-remover produtos
          5-buscar produtos
          0-sair
          ''')
    
    opicao = int(input('escolha uma opição '))
    
    match opicao:
        case 1:
            print('===cadastra produto===')
            nome_produto = input('digite o nome do produto:').strip().upper()
            if nome_produto == '':
                print('nome do produto deve ser incerido...')
            elif nome_produto in lista_produtos:
                print('produto já cadastrado')
            else:
                lista_produtos.append(nome_produto)
                
        case 2:
            print('== produtos no estoque ==')
            for produto in lista_produtos:
                print(f'- {produto}')
            print(f'Total: {len(lista_produtos)}')
            
        case 3:
            print('=== atualizar produto ===')
            nome = input('qual produto deseja atualizar?')
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input('novo nome: ')
                lista_produtos [posicao] = novo
                print('produto alterado com sucesso!')
            else:
                print('produto não encontarado.')
                
        case 4:
            print('=== atualizar produto ===')
            nome = input('qual produto deseja atualizar?')
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print('produto alterado com sucesso!')
            else:
                print('produto não encontarado.')
            print('=== atualizar produto ===')
            
        case 5:
            print('\n== encontrar produto ==')
            nome = input('qual produto deseja buscar? ')
            if nome in lista_produtos:
                print('produto encontardo!')
            else:
                print('este produto não está no estoque.')
        case 0:
            print('saindo do programa')
            break
        case _:
            print('opição invalida')
            
    input('precione uma tecla para continuar...')