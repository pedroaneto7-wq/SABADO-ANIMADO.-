import os
os.system('cls')

def metros_para_centimetros(metros):
  return metros * 100


# Solicitando o valor ao utilizador
valor_metros = float(input("Digite o valor em metros: "))

# Chamando a função e exibindo o resultado
resultado = metros_para_centimetros(valor_metros)
print(f"{valor_metros} m equivale a {resultado} cm.")