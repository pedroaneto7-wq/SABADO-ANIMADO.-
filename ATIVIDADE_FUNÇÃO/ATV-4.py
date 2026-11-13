import os
os.system
def somar(num1,num2):
    return num1 + num2


def subtrair(num1,num2 ):
    return num1 - num2


def multiplicar(num1,num2 ):
  return num1 * num2


def dividir( num1,num2):
    if num2 == 0:
        return "Erro: divisão por zero"
    return num1 / num2


print('= SOLICITANDO DADOS =')
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Soma:", somar(num1, num2))
print("Subtração:", subtrair(num1, num2))
print("Multiplicação:", multiplicar(num1, num2))
print("Divisão:", dividir(num1, num2))