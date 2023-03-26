import clientes

while True:
    print('****************** ')
    print('*   GAMER BANK   *')
    print('******************')
    print('Olá, bem vindo ao Gamer Bank!')
    print('Antes de continuar, você deve fazer login em sua conta')
    autenticacao = input('Informe o seu CPF: ')
    for conta in clientes.contas_correntes:
        if conta._ContaCorrente__cpf == autenticacao:
            print(f'Seja bem vindo, {conta.nome}. O que deseja fazer agora?')


            opt = input('********************************\n'
                        '1 - Consultar seu extrato\n'
                        '2 - Efetuar um deposito\n'
                        '3 - Efetuar um saque\n'
                        '4 - Fazer uma transferencia pix\n'
                        '5 - Sair\n'
                        '********************************\n')
            if opt == '1':
                print(f"\n--- Cliente: {conta.nome} ---")
                print(conta.extrato())
                exit()
            elif opt == '2':
                valor_deposito = float(input('Digite o valor que deseja depositar: '))
                conta.deposito(valor_deposito)
                print(f'Depósito efetuado com sucesso. Seu novo saldo é: R${conta._ContaCorrente__saldo:.2f}')
                exit()
            elif opt == '3':
                valor_saque = float(input('Digite o valor que deseja sacar: '))
                resultado_saque = conta.saque(valor_saque)
                print(resultado_saque)
                exit()
            elif opt == '4':
                valor_transferencia = float(input('Digite o valor da transferência: '))
                cpf_destino = input('Digite o CPF do destinatário: ')
                destinatario_encontrado = False
                for titular in clientes.titulares_correntistas.values():
                    if titular['cpf'] == cpf_destino:
                        destinatario_encontrado = True
                        nome = titular['nome']
                        if conta.pode_sacar(valor_transferencia):
                            resultado_transferencia = conta.transferencia_pix(valor_transferencia, cpf_destino)
                            print(f'Você transferiu R${valor_transferencia} para {titular["nome"]}')
                            print(conta.extrato())
                            exit()
                        else:
                            print('Saldo insuficiente para realizar essa operação')
                            print(conta.extrato())
                            exit()
                if not destinatario_encontrado:
                    print('Destinatário não encontrado')
            elif opt == '5':
                exit()
            else:
                print('Opção inválida')
            exit()

    else:
        print('Cliente não encontrado em nosso sistema')
        break



