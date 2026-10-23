import os
os.system("cls")


valor_produto = float(input("Digite o valor do produto: "))
forma_pagamento = int(input("Digite a forma de pagamento (1 para à vista, 2 para a prazo): "))

match forma_pagamento:
    case 1:
        # Pagamento à vista: 10% de desconto
        desconto = valor_produto * 0.10
        total = valor_produto - desconto
        print("\n--- Resumo da Compra ---")
        print(f"Valor original: R$ {valor_produto:.2f}")
        print("Forma de pagamento: À vista")
        print(f"Desconto aplicado: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
        
    case 2:
        # Pagamento a prazo: até 6x sem desconto
        parcelas = int(input("Digite a quantidade de parcelas (máximo 6): "))
        
        if 1 <= parcelas <= 6:
            valor_parcela = valor_produto / parcelas
            print("\n--- Resumo da Compra ---")
            print(f"Valor original: R$ {valor_produto:.2f}")
            print("Forma de pagamento: A prazo")
            print(f"Número de parcelas: {parcelas}x")
            print(f"Valor da parcela: R$ {valor_parcela:.2f}")
            print(f"Total a pagar: R$ {valor_produto:.2f}")
        else:
            print("\nErro: A quantidade de parcelas deve ser entre 1 e 6.")
            
    case _:
        print("\nErro: Forma de pagamento inválida. Escolha 1 ou 2.")