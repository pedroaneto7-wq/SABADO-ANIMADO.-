import os
os.system('cls')

def inflacionar_preco(preco):
    if preco < 100:
        resultado = preco * 1.20
    else:
        resultado = preco * 1.10
    return resultado

# Programa principal
valor_produto = float(input("Digite o preço do produto: R$ "))
preco_final = inflacionar_preco(valor_produto)
print(f"O novo preço inflacionado é: R$ {preco_final}")
print(f"O novo preço inflacionado é: R$ {preco_final}")