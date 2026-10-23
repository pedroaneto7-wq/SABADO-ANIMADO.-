import os
os.system("cls")

TENTATIVAS = 3


login_salva = input("Digite seu login: ")
senha_salva = input("Digite sua senha: ")

for i in range(TENTATIVAS):
    while True:
        login = input("Digite seu Login: ")
        senha = input("Digite sua senha: ")
        if login == login_salva and senha == senha_salva:
            print("\n seja bem-vindo(a)")
            break
        else:
            print("\n login ou senha incorreta, tente novamente!")
            input("Pressione para continuar....")
            os.system("cls")



