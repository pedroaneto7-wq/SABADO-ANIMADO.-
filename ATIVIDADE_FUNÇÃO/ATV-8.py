import os
os.system('cls')


def calculando_notas(lista_notas):
    resultado = sum(lista_notas) / len(lista_notas)
    return resultado


notas = []


for i in range(3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(nota)


media = calculando_notas(notas)
print(f'A média do aluno é: {media}')