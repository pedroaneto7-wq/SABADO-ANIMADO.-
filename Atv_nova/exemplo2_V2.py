from dataclasses import dataclass
import os
os.system('cls')

# CRIE UMA CLASSE PARA OS DADOS DE UM CLIENTE.
@dataclass
class cliente:
    
    nome :str
    telefone : str
    email : str
    
    def mostrar_dados(self):
        print(f'nome: {self.nome}')
        print(f'telefone: {self.telefone}')
        print(f'email: {self.email}')
        print('='*30)




lista_clientes = []

print('= SOLICITANDO DADOS =')
for i in range(1):
    dados = cliente(
        nome = input('digite  seu nome:'),
        telefone = input('digite seu telefone:'),
        email= input('informe seu e-mail:')
    )
    lista_clientes.append(dados)
    
    for cliente in lista_clientes:
        cliente.mostrar_dados()