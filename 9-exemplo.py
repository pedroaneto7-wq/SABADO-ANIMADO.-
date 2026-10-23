import os
os.system('cls')

feijao_da_vovo = 150
acai = 20
Xbanana = 2.50
churros = 999
hakuna_matata = 6767

while True:
    print('''
====== SENAI SHOP ======
1 - feijão da vovó R$ 150
2 - Açai R$ 20
3 - xbanana R$ 2,50
4 - CHURROS R$ 999
5 - hakuna matata R$ 6767''')
    numero = input("Escolha o número do produto: ")
    if numero == "1":
        print(f"Opção escolhida, feijãodavovó R${feijao_da_vovo}")
        break
    elif numero == "2":
        print(f"opção escolhida, açai R${acai}")
        break
    elif numero == "3":
        print(f"opção escolhida, Xbanana R${Xbanana}")
        break
    elif numero == "4":
        print(f"opção escolhida, churros R${churros}")
        break
    elif numero == "5":
        print(f"opção escolhida, hakuna matata R${hakuna_matata}")
        break
    else:
        print(f"Não vendemos esse produto")
        print("tente novamente")
        input("Pressione para continuar..")
        os.system("cls")