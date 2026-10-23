import os
os.system("cls")

QUANTIDADE_NUMERICA = 2



print('''
Calculadora''')

numero = int(input("Digite 1° número: "))
numerow = int(input("Digite o 2° Número: "))
print()
calculo = input("Qual forma de calculo deseja? +,-,*,/")



match calculo:
    case '+':
        soma =  numero + numerow
        print(f"Sua soma é: {soma}")
    case '-':
        subtracao = numero - numerow
        print(f"Sua Subtração é: {subtracao}")
    case '*':
        multiplicacao = numero * numerow
        print(f"Sua Multiplicação é: {multiplicacao}")
    case '/':
        if numero or numerow == 0:
            print("Não é fazer esse cálculo matematico :c")
        else:
            divisao = numero / numerow
            print(f"Sua divisão é: {divisao}")
    case _:
        print("Pedido não identificado...., tente novamente!")



