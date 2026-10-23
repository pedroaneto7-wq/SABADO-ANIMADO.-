import os
import time
os.system('cls')
contador = 0

while True:
    logi = str(input('login:'))
    senha = str(input('senha:'))
    
    if logi =='pda2230' and senha == 'pn3022':
        print('analizando login e senha...')
        
        time.sleep(1.2)
        print()
        print('seja bem vindo')
        break
    else:
        contador =+ 1
        if contador == 3:
            break
        print('\n login ou senha incorretos, tentar novamente!')
        input('pressione para continuar....')
        os.system('cls')
