import os
os.system('cls')

import os
os.system('cls')

soma_pares = 0
contador_pares=0
soma_geral=0
contador_geral=0
contador_impares=0

while True:
    numero=int(input('digite seu numero:'))
    if numero == 0:
        break
    soma_geral += 1
    if numero % 2 == 0:
        contador_pares += 1
        soma_pares += numero
    else:
        contador_impares += 1
        print(f'quantidadade de numeros pares: {contador_pares}')
        print(f'quantidadade de numeros impares: {contador_impares}')
    if contador_pares > 0:
        media_pares = soma_pares / contador_pares
        print(f'media dos numeros pares: {media_pares}')

    else:
        print('sem valor')
    if contador_geral >0:
        media_geral = soma_geral / contador_geral
        print(f'media geral: {media_geral}')
    else:
        print('sem valor')

        