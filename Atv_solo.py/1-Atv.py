import os






lista_serie = []

while True:
    input("\nPressione uma telca para continuar...")
    #limpar o terminal
    os.system("cls")
    print('''
1 - Cadastra series favoritas
2 - Lista series 
0 - sair
''')
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print('\n == CADASTRA UMA SERIE ==')
            #STRIP() retirar o espaço
            #upper ()todas as letras em maiusculas
            nome = input("Nome de uma nova serie: ").strip().upper()
            if nome == '':
                print('O nome não pode ficar vazio.')
            elif nome in lista_serie:
                print(f"{nome} já existe no cadastro.")
            else:
            #.apeend(nome) adiciona o nome do produto na lista
                lista_serie.append(nome)
                print("Produto Cadastrado com sucesso!")
            input("Pressione uma telca para continuar...")

        case 2:
            print("\n== LISTAR SERIES ==")
            if len(lista_serie) == 0:
                print(" O estoque está vazio")
            else:
                for i, produto in enumerate(lista_serie):
                    print(f"{i+1}, {produto}")
            #len(lista de produto ) mostra a quantidade de produtos na lista
                    print(f"Total de produtor: {len(lista_serie)}")
            input("\nPressione uma tecla para continuar")

        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção invalida! ")
            input("\nPressione uma telca para continuar...")