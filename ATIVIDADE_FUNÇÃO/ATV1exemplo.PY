import os
os.system('cls')


def calcular_notas(nota1,nota2):
    resultado = (nota1 +nota2) / 2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        resultado = 'aprovado'
    else:
        resultado = 'reprovado'
    return resultado


print('= SOLICITANDO NOTAS =')
nota1 = float(input('digite a primeira nota:'))
nota2 = float(input('digite a segunda nota:'))

# Usando a função com parametro e
# inserindo on retorno a variavel soma.
media = calcular_notas(nota1,nota2)
situacao = verificar_resultado(media)



print(f'media: {media}')
print(f'Resultado:{situacao}')

