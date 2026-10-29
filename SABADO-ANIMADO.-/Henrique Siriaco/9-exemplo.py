import os
os.system("cls")

total = 0
continuar = "s"

while continuar == "s":
    print("\n===== CARDÁPIO =====")
    print("1 - Picanha - R$ 25,00")
    print("2 - Lasanha - R$ 20,00")
    print("3 - Strogonoff - R$ 18,00")
    print("4 - Bife Acebolado - R$ 15,00")
    print("5 - Pão com ovo - R$ 5,00")

    codigo = int(input("Escolha o código do prato: "))

    if codigo == 1:
        total += 25
    elif codigo == 2:
        total += 20
    elif codigo == 3:
        total += 18
    elif codigo == 4:
        total += 15
    elif codigo == 5:
        total += 5
    else:
        print("Código inválido!")

    if codigo >= 1 and codigo <= 5:
        print("Total parcial: R$", total)

    continuar = input("Deseja escolher outro prato? (s/n): ").lower()

print("Valor total a pagar: R$", total)