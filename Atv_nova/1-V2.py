from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class cliente:
    
    # Nome da variavel : tipo da variavel
    nome = str
    idade = int



# SOLICITANDO DADOS DE UM CLIENTE
cliente = cliente('marta',30)

# SOLICITANDO DADOS DE OUTRO CLIENTE
cliente2 = cliente( 'josé',40)
idade = 40


print(f'nome: {cliente.nome}')
print(f'idade: {cliente.idade}')

print(f'nome: {cliente2.nome}')
print(f'idade: {cliente2.idade}')