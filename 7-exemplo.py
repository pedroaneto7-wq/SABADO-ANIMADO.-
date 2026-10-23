import os
os.system("cls")

notas = []
QUANTIDADE_NUMERICA = 3

for i in range(QUANTIDADE_NUMERICA):
    nota = float(input(f"Digite a {i + 1 }° nota:"))
    notas.append(nota)

while nota < 0 or nota > 10:
    print('Nota invalida! Digite uma nota entre 1 e 10')
    nota = float(input(f"Digite a {i + 1}° nota: "))


media = sum(notas) / QUANTIDADE_NUMERICA
print(f"\n Sua média foi: {media}")
if media >= 7:
        print("aprovado")
elif media >= 5:
        print("Recuperação")
elif media <= 5:
        print("Reprovado")