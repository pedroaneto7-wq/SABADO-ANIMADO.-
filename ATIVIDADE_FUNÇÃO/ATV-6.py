import os
os.system('cls')

def inflacionar_preco(preco):
    if preco < 100:
        novo_preco = preco * 1.10
    else:
        novo_preco = preco * 1.20
    return novo_preco

# Programa principal
valor_produto = float(input("Digite o preço do produto: R$ "))
preco_final = inflacionar_preco(valor_produto)
print(f"O novo preço inflacionado é: R$ {preco_final:.2f}")
print(f"O novo preço inflacionado é: R$ {preco_final:.2f}")