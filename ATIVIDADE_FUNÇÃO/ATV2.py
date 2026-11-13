import os
os.system('cls')

def par_ou_impar(numero):
    if numero % 2 == 0:
        print('é par')
    else:
        print('é impar')

numero = int(input('digite o numero:'))

par_ou_impar(numero)