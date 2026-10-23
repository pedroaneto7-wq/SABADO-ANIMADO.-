import os
os.system('cls')
total = 0

produto = str(input('digite qual é o seu produto:'))
preço = float(input('digite o valor dop seu produto'))
quantedade = int(input('digite a quante dade de produtos:'))
total = quantedade * preço

if quantedade == 5:
    total / 0.02
elif quantedade <= 6:
    total / 0.05
    
    print(f'produto {produto}')
    print(f'preço {preço}')
    print(f'quantedade {quantedade}')
    print(f'total {total}')
    
    


