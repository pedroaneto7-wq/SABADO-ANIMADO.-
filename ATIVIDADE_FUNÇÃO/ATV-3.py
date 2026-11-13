import os
os.system('cls')

def verificar_numero(numero):
    if numero > 0:
        return 'positivo'
    elif numero < 0:
        return 'negativo'
    else:
        return 'zero (neutro)'

print(verificar_numero(10))
print(verificar_numero(-5))

