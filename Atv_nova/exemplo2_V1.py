from dataclasses import dataclass
import os
os.system('cls')

# CRIE UMA CLASSE PARA OS DADOS DE UM CLIENTE.
@dataclass
class cliente:
    
    nome :str
    telefone : str
    email : str
    
lista_clientes = []

for i in range(1):
    dados_do_cliente = cliente(
        nome = input('digite  seu nome:'),
        telefone = input('digite seu telefone:'),
        email= input('informe seu e-mail:')
    )
    lista_clientes.append(dados_do_cliente)
    
    for cliente in lista_clientes:
        print(f'nome: {cliente.nome}')
        print(f'telefone: {cliente.telefone}')
        print(f'email: {cliente.email}')
        print('='*15)