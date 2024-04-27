intro = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

'''
deposito = 0
saque = 500
extrato = ""
limite_saques = 3

while True :
    opcao = int(input(intro))
    if opcao == 1 :
        valor = float(input("Valor do depósito: "))
        if valor > 0 :
            deposito += valor
            extrato += "Depósito: R$ {:.2f}\n".format(valor)
        else :
            print ("Valor informado inválido.")

    elif opcao == 2 :
        if limite_saques <= 0 :
            print ("Operação indisponivel. Número de saques excedido")
        else :
            valor = float(input("Informe o valor que deseja sacar: R$"))
            if valor > deposito :
                print ("Operação indisponivel. Você não tem saldo o suficiente.")
            elif valor > saque :
                print ("Operação indisponivel. O valor do saque excede o limite.")
            elif valor > 0 :
                limite_saques -= 1
                deposito -= valor
                extrato += "Saque: R$ {:.2f}\n".format(valor)
            else :
                print ("Valor da operação indisponivel.")

    elif opcao == 3 :
        print("\n{:=^40}".format("EXTRATO"))
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print("Saldo: R$ {:.2f}\n".format(deposito))
        print("="*40)

    elif opcao == 0 :
        break

    else :
        print ("Operação indisponivel.")
