import os

veto_alimento = []
veto_dinheiro = []

picanha = 25


while True:
    os.system("CLS")
    print('''
===== TUNG TUNG TUNG SAHUR ====
1 - Picanha        | 25,00R$
2 - Lasanha        | 20,00 R$
3 - Strongonoff    | 18,00 R$
4 - Bife Acebolado | 15,00 R$
5 - Pão com ovo    | 5,00 R$
0 - Sair ''')

    opicao = int(input("Qual deseja? "))
    match opicao:
        case 1:
            print("Prato selecionado: Picanha \n Valor 25:00 R$")
            prato = "Picanha"
            valor = 25
        case 2:
            print('prato selecionado: lasanha \n Valor 20:00 R$')
            prato = "lasanha"
            Valor = 20
        case 3:
            print("Prato selecionado: Strogonoff\n Valor 18:00 R$")
            prato = "Strogonoff"
            Valor = 18
        case 4:
            print("prato selecionado: Bife Acebolado\n Valor 15:00 R$")
            prato = "Bife Acebolado"
            Valor = 15
        case 5:
            print("prato selecionado: Pão com ovo\n Valor 5:00 R$")
            Prato = "Pão com ovo"
            Valor = 5
        case 0:
            print("==== Saindo do programa ===")
            break
        case _:
            print("A ordem que foi selecionada não existe no nosso sistema!")
    input("Pressione para continuar.... ")
    if opicao >= 1 and opicao <= 5:
        veto_alimento.append()
        veto_dinheiro.append()

    deseja_continuar = True
    while True:
        resposta = (input("Deseja pedir mais algum prato? (S/N): ").strip().upper())
        if resposta == "S":
            break
        elif resposta == "N":
            deseja_continuar = False
            break
        else:
            print("Opção inválida. Tente novamente.")

    if not deseja_continuar:
        break

nome = input('Nome para retirada: ')

os.system('cls || clear')

if sum(veto_dinheiro) == 0:
    print('Nenhum prato foi pedido.')
else:
    print('=== PEDIDO ===')
    print(f'Nome para retirada: {nome}')
    for i in range(len(veto_dinheiro)):
        print(f'{veto_alimento[i]} ..... R${veto_dinheiro[i]:.2f}')
    print('---------------')
    valor_total = sum(veto_dinheiro)
    print(f'Valor total: R${valor_total:.2f}')