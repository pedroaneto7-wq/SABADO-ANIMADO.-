from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    
    # Nome da variavel : tipo da variavel
    nome : str
    idade : int
    altura : float
    peso : float

lista_clientes = []
# SOLICITANDO DADOS DE UM CLIENTE

for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('digite o nome do cliente:'),
        idade = int(input('digite a idade do cliente:')),
        altura = float(input('digite sua altura:')),
        peso = float(input('digite seu peso:'))
    )
    lista_clientes.append(dados_do_cliente)
    
for cliente in lista_clientes:
    print(f'nome: {cliente.nome}')
    print(f'idade: {cliente.idade}')
    print(f'altura: {cliente.altura}')
    print(f'peso: {cliente.peso}')
    print('='*15)
