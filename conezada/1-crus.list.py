import os

#lista de produtos.
lista_produtos = []

while True:
    input("\nPressione uma telca para continuar...")
    #limpar o terminal
    os.system("cls")
    print('''
1 - Cadastra produto
2 - Lista produtos
0 - sair
''')
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print('\n == CADASTRA UM PRODUTO ==')
            #STRIP() retirar o espaço
            #upper ()todas as letras em maiusculas
            nome = input("Nome do novo produto: ").strip().upper()
            if nome == '':
                print('O nome não pode ficar vazio.')
            elif nome in lista_produtos:
                print(f"{nome} já existe no cadastro.")
            else:
            #.apeend(nome) adiciona o nome do produto na lista
                lista_produtos.append(nome)
                print("Produto Cadastrado com sucesso!")
            input("Pressione uma telca para continuar...")

        case 2:
            print("\n== LISTAR TODOS OS PRODUTOS ==")
            if len(lista_produtos) == 0:
                print(" O estoque está vazio")
            else:
                for i, produto in enumerate(lista_produtos):
                    print(f"{i+1}, {produto}")
            #len(lista de produto ) mostra a quantidade de produtos na lista
                    print(f"Total de produtor: {len(lista_produtos)}")
            input("\nPressione uma tecla para continuar")

        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção invalida! ")
            input("\nPressione uma telca para continuar...")