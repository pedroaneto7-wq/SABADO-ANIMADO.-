import os
os.system('cls')

lista_produtos = []


while True:

    print('''
=== Mercadinho===
1-cadastra produtos
2-lista produtos
0-sair
''')
    opicao = int(input('digite a opição desejada:'))


    match opicao:
        case 1:
            print('\n==Cadastra produto==')
        
            nome = input('digite o nome do novo produto:')
            if nome == '':
                print('ecreve o nome do produto!')
            elif nome in lista_produtos:
                print(f'{nome} ja esta cadastrado!')
            else:

                lista_produtos.append(nome)
            print(f'produto {nome} cadastrado com sucesso!')

        case 2:
            print('\n==Listar todos os produtos==')
            if len(lista_produtos) == 0:
                print('estamos sem produtos!!')

            else:
                for i, produto in enumerate(lista_produtos):
                    print(f'{i+1} - {produto}')

            print(f'total de produtos: {len(lista_produtos)}')
            
        case 0:
            print('Fim....')
            input('aperte uma tecla para continuar...')
            break
        case _:
            print('opição invalida, tente novamente!')
            input('aperte uma tecla para continuar...')