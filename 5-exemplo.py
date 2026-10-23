import os
import time
os.system("cls")

numero = int(input("Digite um número para a tabuada: "))

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")
    time.sleep(1)