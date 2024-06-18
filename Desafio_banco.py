menu = """
      =================== Menu ===================
    [s] Sacar
    [d] Depositar
    [e] Extrato
    [q] Sair
      ============================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "s":
        valor = float(input("Informe o valor para saque:"))
    
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
                print("Realizando saque ...")
                print("Operação falhou! Voce não tem saldo suficiente")
                print("Obrigado por ser nosso cliente, tenha um bom dia.")

        elif excedeu_limite:
                print("Realizando saque ...")
                print("Operação falhou! O valor do saque excede o limite.")
                print("Obrigado por ser nosso cliente, tenha um bom dia.")
        
        elif excedeu_saques:
                print("Realizando saque ...")
                print("Operação falhou! Número máximo de saque excedido!")
                print("Obrigado por ser nosso cliente, tenha um bom dia.")
        
        elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Realizando saque ...")
                print("Saque realizado. Retire o cartão da leitora.")
                print(f'Seu valor atual em conta é de R$ {saldo}')
                print("Obrigado por ser nosso cliente, tenha um bom dia.")

    if opcao == "d":
                valor = float(input("Informe o valor para depósito:"))

                if valor > 0:
                        saldo += valor
                        extrato += f"Depósito: R$ {valor:.2f}\n"
                        print("Realizando deposito ...")
                        print(f"Seu saldo atual da conta é de R$ {saldo}")
                        print("Obrigado por ser nosso cliente, tenha um bom dia.")

                else:
                        print("Operação falhou! O valor informado é inválido")

    if opcao == "e":
                print("\n$_____EXTRATO_____$")
                print("Não foram realizadas movimentações." if not extrato else extrato)
                print(f"Seu saldo atual da conta é de R$ {saldo:.2f}")
                print("______________________")

    elif opcao == "q":
            break

else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")