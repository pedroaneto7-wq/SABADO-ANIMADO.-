from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class cliente:
    nome : str
    idade : int
    telefone : str
    endereco : str
    
    def mostrar_dados(self):
        print(f'nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'endereço: {self.endereco}')
        print('='*30)
    def nome_idade(self):
        print(f'nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'='*30)
    def nome_telefone(self):
        print(f'nome: {self.nome}')
        print(f'telefone: {self.telefone}')
        print('='*30)

lista_dados = []

for i in range(2):
    dados = cliente(
        nome = input('digite o seu nome:'),
        idade = int(input('digite sua idade:')),
        telefone = input('digite seu telefone:'),
        endereco = input('digite seu endereço:')
    )
lista_dados.append(dados)

print('==== MOSTRANDO DADOS ====')
for cliente in lista_dados:
    cliente.mostrar_dados()
print('==== NOME E IDADE ====')
for cliente in lista_dados:
    cliente.nome_idade()
print('==== NOME E TELEFONE ====')
for cliente in lista_dados:
    cliente.nome_telefone()