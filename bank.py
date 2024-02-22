menu = """
========= MENU =========

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

========================
"""

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = str(input(menu))

    if opcao == "d":

        valor = float(input("Informe o valor do depósito: \n"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso!")
        
        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "s":
        
        valor = float(input("Informe o valor do saque: \n"))

        if valor <= limite:
            if numero_saques < LIMITE_SAQUES:
                    if limite >= valor <= saldo:
                        saldo -= valor
                        numero_saques += 1
                        extrato += f"Saque: R$ {valor:.2f}\n"
                        print(f"Saque realizado com sucesso!")
                    else:
                        print(f"Falha na operação! Você não possui o saldo suficiente.")
            else:
                print(f"Falha na operação! Você excedeu o máximo de saques.")
        else:
            print(f"Falha na operação! Você excedeu o valor limite de saque.") 

    elif opcao == "e":
        print("=============== EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")