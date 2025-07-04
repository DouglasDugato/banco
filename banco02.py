import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [NC]\tNova Conta
    [LC]\tListar contas
    [NU]\tNovo usuário
    [Q]\tSair
    ======================================
    
    Escolha =>   """
    return input(textwrap.dedent(menu)).lower()

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print('Depósito feito com sucesso!!')
        print(f'Saldo após depósito: R$ {saldo:.2f}')
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato  

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        print(f'Saldo atual: R$ {saldo:.2f}')
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print('Saque efetuado com sucesso.')
        print(f'Saldo após saque: R$ {saldo:.2f}')
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def criar_usuarios(usuarios):
    cpf = input("Informe o seu CPF (SOMENTE NÚMEROS): ")
    if filtrar_usuarios(cpf, usuarios):
        print("\nUsuário já existente!")
        return

    nome = input("Informe o seu nome: ")
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input("Informe o endereço (logradouro, bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print(f"Usuário criado com sucesso. Seja bem-vindo(a), {nome}!")

def criar_conta(numero_conta, agencia, usuarios):
    cpf = input('Insira seu CPF (Somente Números): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }

    print('Usuário não encontrado.')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\  
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
"""
        print("=" * 100)
        print(textwrap.dedent(linha))

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuarios(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(numero_conta, AGENCIA, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
