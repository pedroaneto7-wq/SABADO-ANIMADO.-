import os
os.system('cls')





def mostrar_saldo(saldo):
    print(f"Saldo na conta: {saldo}")

def extrato(vetor_saldo):
    if not vetor_saldo:
        print("Nada foi Modificado!")
    else:
        for item in vetor_saldo:
            print(item)

def depositando(saldo, vetor_saldo):
    valor = float(input("Quanto deseja depositar?: ").replace(",", "."))
    if valor <= 0:
        print("Erro!")
        return saldo
    saldo += valor
    vetor_saldo.append(f"Valor depositado + R$ {valor:.2f}")
    print(f"Deposito de {valor:.2f}")
    return saldo


def sacando (saldo, vetor_saldo):
    sacar = float(input("Digite o quanto você deseja Retirar: ").replace(",", "."))
    if  sacar > saldo:
        print("Você não possue esse valor no saldo")
    elif sacar <= 0:
        print("Não é possivel retirar números negativos! ")
    else:
        saldo -= sacar
        vetor_saldo.append(f"Valor removido - R${sacar:.2f}")
        print(f"Saque de {sacar:.2f} Feito com sucesso!")
        return saldo

saldo = 0
vetor_saldo = []
 
while True:
    os.system('cls')
    print('''
1 - Ver saldo
2 - Depositar
3 - Sacar
4 - Ver extrato
0 - Sair
''')
    opcao = int(input('digite a sua opção: '))
    match opcao:
        case 1:
            mostrar_saldo(saldo)
        case 2:
            saldo = depositando(saldo, vetor_saldo)
        case 3:
            saldo = sacando(saldo, vetor_saldo)
        case 4:
            extrato(vetor_saldo)
        case 0:
            print("Obrigado por vir! \nSaindo...")
            break
        case _:
            
            print('oppição invalida...')
    input('pressione para continuar...')