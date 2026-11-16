import os
os.system('cls')
from datetime import date


def aniversario(ano_nascimento):
    ano_atual = date . today() . year
    idade = ano_atual - ano_nascimento
    return idade

nascimento = int(input('digite seu ano de nascimneto:'))

resultado = aniversario(nascimento)
print(f'você tem:{resultado} anos')
    