import os
os.system('cls')


renda_mensal = float(input("Digite a renda mensal do cliente (R$): "))
valor_emprestimo = float(input("Digite o valor do empréstimo (R$): "))
numero_prestacoes = int(input("Digite o número de prestações: "))

# Cálculo da prestação
prestacao = valor_emprestimo / numero_prestacoes


limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30


print(f"\nValor da prestação mensal: R$ {prestacao:.2f}")


if valor_emprestimo <= limite_emprestimo and prestacao <= limite_prestacao:
    print("Resultado: CRÉDITO APROVADO")
else:
    print("Resultado: CRÉDITO NEGADO")