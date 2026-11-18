import os
os.system('cls || clear')

def autenticar(matricula, senha):
    matricula_valida = "6767"
    senha_valida = "roblox"
    return matricula.strip() == matricula_valida and senha.strip() == senha_valida

def calcular_inss(salario_base):
    desconto = 0.0
    if salario_base > 0:
        faixa1 = min(salario_base, 1621.00)
        desconto += faixa1 * 0.075

    if salario_base > 1621.00:
        faixa2 = min(salario_base, 2902.84) - 1621.00
        desconto += faixa2 * 0.09
    
    if salario_base > 2902.84:
        faixa3 = min(salario_base, 4354.27) - 2902.84
        desconto += faixa3 * 0.12

    if salario_base > 4354.27:
        faixa4 = min(salario_base, 8475.55) - 4354.27
        desconto += faixa4 * 0.14
    return min(desconto, 988.10)

def calcular_irrf(salario_base, inss, dependentes):
    base = salario_base - inss - (189.59 * dependentes)
    if base <= 2428.80:
        imposto = 0.0
    elif base <= 2826.65:
        imposto = (base * 0.075) - 182.16
    elif base <= 3751.05:
        imposto = (base * 0.15) - 394.16
    elif base <= 4664.68:
        imposto = (base * 0.225) - 675.49
    else:
        imposto = (base * 0.275) - 908.73

    imposto = max(0.0, imposto)

    if salario_base <= 5000.00:
        imposto_final = 0.0
    elif salario_base <= 7350.00:
        reducao = 978.62 - (0.133145 * salario_base)
        imposto_final = imposto - reducao
    else:
        imposto_final = imposto

    return max(0.0, imposto_final)

def calcular_vt(salario_base, opcao_vt):
    if opcao_vt.strip().lower() == "s":
        return salario_base * 0.06
    return 0.0

def calcular_vr(valor_vr):
    return valor_vr * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00

def mostrar_contracheque(matricula, salario_base, opcao_vt, valor_vr, inss, irrf, desconto_vt, desconto_vr, desconto_saude):
    total_descontos = inss + irrf + desconto_vt + desconto_vr + desconto_saude
    salario_liquido = salario_base - total_descontos
    vt_texto = "Sim" if opcao_vt == "s" else "Não"

    print("\n" + "=" * 45)
    print(f"CONTRACHEQUE • MATRÍCULA {matricula}")
    print("=" * 45)
    print(f"Benefícios: VT ({vt_texto}) | VR (R$ {valor_vr:.2f})")
    print("-" * 45)
    print(f"Salário base              R$ {salario_base:10.2f}")
    print("-" * 45)
    print(f"(-) INSS                  R$ {inss:10.2f}")
    print(f"(-) IRRF                  R$ {irrf:10.2f}")
    print(f"(-) Vale-transporte       R$ {desconto_vt:10.2f}")
    print(f"(-) Vale-refeição         R$ {desconto_vr:10.2f}")
    print(f"(-) Plano de saúde        R$ {desconto_saude:10.2f}")
    print("-" * 45)
    print(f"Total de descontos        R$ {total_descontos:10.2f}")
    print(f"SALÁRIO LÍQUIDO           R$ {salario_liquido:10.2f}")
    print("=" * 45 + "\n")

def ler_dados_funcionario():
    while True:
        try:
            salario = float(input("Salário base (R$): ").replace(",", "."))
            if salario > 0:
                break
            print("Erro: O salário deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

    while True:
        vt = input("Vale-transporte (s/n): ").strip().lower()
        if vt in ("s", "n"):
            break
        print("Erro: Responda apenas com 's' ou 'n'.")

    while True:
        try:
            vr = float(
                input("Valor do Vale-refeição pago pela empresa (R$): ").replace(
                    ",", "."
                )
            )
            if vr >= 0:
                break
            print("Erro: O valor do VR não pode ser negativo.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

    while True:
        try:
            dependentes = int(input("Quantidade de dependentes: "))
            if dependentes >= 0:
                break
            print("Erro: O número de dependentes não pode ser negativo.")
        except ValueError:
            print("Erro: Digite um número inteiro.")

    return salario, vt, vr, dependentes

def main():
    print("=== DENDÊSOFT • FOLHA DE PAGAMENTO ===")

    while True:
        matricula = input("Matrícula (padrão: 1234): ")
        senha = input("Senha (padrão: admin): ")
        if autenticar(matricula, senha):
            print("Acesso liberado!\n")
            break
        print("Matrícula ou senha incorreta. Tente novamente.\n")

    salario_base, opcao_vt, valor_vr, dependentes = ler_dados_funcionario()

    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, inss, dependentes)
    desconto_vt = calcular_vt(salario_base, opcao_vt)
    desconto_vr = calcular_vr(valor_vr)
    desconto_saude = calcular_plano_saude(dependentes)

    mostrar_contracheque(
        matricula.strip(),
        salario_base,
        opcao_vt,
        valor_vr,
        inss,
        irrf,
        desconto_vt,
        desconto_vr,
        desconto_saude,
    )


if __name__ == "__main__":
    main()