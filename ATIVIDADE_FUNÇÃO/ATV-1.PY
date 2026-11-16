import os
os.system('cls')


def calcular_notas(nota1,nota2):
    resultado = nota1 +nota2
    return resultado


print('= SOLICITANDO NOTAS =')
nota1 = float(input('digite a primeira nota:'))
nota2 = float(input('digite a segunda nota:'))

# Usando a função com parametro e
# inserindo on retorno a variavel soma.
soma = calcular_notas(nota1,nota2)

print(f'soma: {soma}')

