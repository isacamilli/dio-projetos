from time import sleep
import textwrap

def menu():

    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tNovo usuário
    [6]\tListar contas
    [0]\tSair
    =>  """
    return input(menu)


def depositar(deposito, valor, extrato, /):
    if valor > 0 :
            deposito += valor
            extrato += "Depósito: R$ {:.2f}\n".format(valor)
            print ("Depósito realizado com sucesso!")
    else :
        print ("Valor informado inválido.")

    return deposito, extrato


def sacar(*, deposito, valor, extrato, limite, limite_saques):
    if limite_saques <= 0 :
            print ("Operação indisponivel. Número de saques excedido")
    else :
        if valor > deposito :
            print ("Operação indisponivel. Você não tem saldo o suficiente.")
        elif valor > limite :
            print ("Operação indisponivel. O valor do saque excede o limite.")
        elif valor > 0 :
            limite_saques -= 1
            deposito -= valor
            extrato += "Saque: R$ {:.2f}\n".format(valor)
            print ("Saque reaizado com sucesso")
        else :
            print ("Valor da operação indisponivel.")

    return deposito, extrato


def exibir_extrato(deposito, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {deposito:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nERRO: Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado. Obrigatório criar")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    AGENCIA = "0001"

    deposito = 0
    limite = 500
    extrato = ""
    limite_saques = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        sleep(1)
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$"))

            deposito, extrato = depositar(deposito, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor que deseja sacar: R$"))

            saldo, extrato = sacar(
                deposito=deposito,
                valor=valor,
                extrato=extrato,
                limite=limite,
                limite_saques=limite_saques,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
