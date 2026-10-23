import os
os.system('cls')

import os
os.system('cls')

soma_salario = 0
contador_pessoas = 0
maior_idade = 0
menor_idade = 999
mulheres_5K = 0


while True:
    os.system('cls')
    print('''
=== MENU ===
1- adicionar pessoas
2- exibir resultados
3- sair
''')
    opcao = int(input('digite a opição desejada:'))

    match opcao:
        case 1:
            print('=== CADASTRO ===')
            idade = int(input('digite sua idade'))
            sexo = input('digite o sexo (M/F): ').upper()
            salario = float(input('digite seu salario'))

            soma_salario += salario
            contador_pessoas += 1
            maior_idade = max('idade, maior_idade')
            menor_idade = min('idade, menor_idade')

            if sexo == "F" and salario >= 5000:
                mulher_5k += 1

                print('pessoas adicionadas com sucesso')
                input('aperte qualquer butão para continuar')
        case 2:
            if contador_pessoas == 0:
                print('\nNenhuma pessoas cadastrada. \n')
            else:
                media_salario = soma_salario / contador_pessoas


        
                print('\n=== RESULTADOS DA PESQUISA ===')
                print(f'Média de salário do grupo: R$ {media_salario}')
                print(f'Maior idade: {maior_idade}')
                print(f'Menor idade: {menor_idade}')
                print(f'Mulheres com salário a partir de R$ 5.000,00: {mulher_5k}')
                input('Pressione uma tecla para continuar...')
            input('Pressione uma tecla para continuar...')
        case 3:
            print('\nEncerrando o programa.')
            break
        case _:
            print('\nOpção inválida! \n')
            input('Pressione uma tecla para continuar...')