saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print('Ola, seja bem vindo ao nosso banco')
    ver = str(input('''

Deseja fazer que operação?
[S] Ver Saldo
[D] Fazer Deposito
[R] Fazer Saque
[E] Extrato                     
[N] Nenhuma Opção   
                                                                                     

Opção: ''')).lower()
    if ver == 's':
        print(f'O seu saldo é R${saldo:.2f}')

    elif ver == 'd':
        deposito = float(input('Informe o valor do deposito: '))
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print(f'Saldo disponivel após deposito R$ {saldo:.2f}')

    elif ver == 'r':
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
         
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f'Saldo após saque R$ {saldo:.2f}')
        
    elif ver == 'e':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    else:
        print("Operação falhou! O valor informado é inválido.")
 
            
        
    if ver == 'n':
        print('Obrigado por usar nosso Banco')
        break

    prosseguir = str(input('Deseja fazer algo a mais? [S/N]: ')).lower()
    if prosseguir == 'n':
        print('Obrigado por usar nosso Banco')
        break
