import os
os.system('cls')


def calculando_notas(lista_notas):
    return sum(lista_notas) / len(lista_notas)
    
def mostrar_resultado(media,lista_notas):
    for nota in lista_notas:
        print(f'nota: {nota}')
    print(f'media: {media}')

lista_notas = []


for i in range(3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    lista_notas.append(nota)


media = calculando_notas(lista_notas)
mostrar_resultado(media,lista_notas)