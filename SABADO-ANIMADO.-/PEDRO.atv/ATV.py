import os
os.system('cls')

lista_series = []

while True:
    print('''
    === Top series ===
    1- cadastra series
    2- lista series
    0- sair
    ''')
    opicao = int(input('digite a opição desejada:'))

    match opicao:
        case 1:
            print('\n==cadastra series==')
            nome = input('digite o nome de uma serie:')
            if nome == '':
                print('escreva o nome de uma serie!')
            elif nome in lista_series:
                print(f'{nome} ja esta cadastrado!')
            else:
                lista_series.append(nome)
                print(f'serie {nome} cadastrada com sucesso!')

        case 2:
            print('\n==Listar todas as series==')
            if len(lista_series) == 0:
                print('estamos com falta de series no catalogo!!')
            else:
                for i, serie in enumerate(lista_series):
                    print(f'{i+1} - {serie}')
                    print(f'total de series: {len(lista_series)}                                                                    ')
        case 0:
            print('======FIM======')
            input('aperte uma tecla para continuar...')
            break
        case _:
            print('opição invalida, tente novamente!')