import clientes
import contaCorrente


def login():
    autenticacao = input('Informe o seu CPF: ')
    conta = contaCorrente.busca_cliente_por_cpf(autenticacao)
    if conta is None:
        print('Cliente não encontrado em nosso sistema')
        return None
    else:
        print(f'Seja bem vindo, {conta.nome}!')
        return conta


def consultar_extrato(conta):
    print(f"\n--- Cliente: {conta.nome} ---")
    print(conta.extrato())


def efetuar_deposito(conta):
    valor_deposito = float(input('Digite o valor que deseja depositar: '))
    conta.deposito(valor_deposito)
    print(f'Depósito efetuado com sucesso. Seu novo saldo é: R${conta.saldo:.2f}')


def efetuar_saque(conta):
    valor_saque = float(input('Digite o valor que deseja sacar: '))
    resultado_saque = conta.saque(valor_saque)
    if resultado_saque == 'Saque efetuado com sucesso':
        print(f'{resultado_saque}. Seu novo saldo é: R${conta.saldo:.2f}')
    else:
        print(resultado_saque)


def efetuar_transferencia(conta):
    valor_transferencia = float(input('Digite o valor da transferência: '))
    cpf_destino = input('Digite o CPF do destinatário: ')
    destinatario = contaCorrente.busca_cliente_por_cpf(cpf_destino)
    if destinatario is None:
        print('Destinatário não encontrado')
        return
    if conta.pode_sacar(valor_transferencia):
        resultado_transferencia = conta.transferencia_pix(valor_transferencia, cpf_destino)
        print(f'Você transferiu R${valor_transferencia} para {destinatario.nome}')
        print(conta.extrato())
    else:
        print('Saldo insuficiente para realizar essa operação')
        print(conta.extrato())


def menu():
    print('****************** ')
    print('*   GAMER BANK   *')
    print('******************')
    print('Olá, bem vindo ao Gamer Bank!')
    print('Antes de continuar, você deve fazer login em sua conta')
    conta = login()
    if conta is None:
        return
    while True:
        opt = input('********************************\n'
                    '1 - Consultar seu extrato\n'
                    '2 - Efetuar um deposito\n'
                    '3 - Efetuar um saque\n'
                    '4 - Fazer uma transferencia pix\n'
                    '5 - Sair\n'
                    '********************************\n')
        try:
            opt = int(opt)
        except ValueError:
            print('Opção inválida. Digite um número entre 1 e 5.')
            continue
        if opt == 1:
            consultar_extrato(conta)
        elif opt == 2:
            efetuar_deposito(conta)
        elif opt == 3:
            efetuar_saque(conta)
        elif opt == 4:
            efetuar_transferencia(conta)
        elif opt == 5:
            print('Obrigado por usar o Gamer Bank!')
            break
        else:
            print('Opção inválida. Digite um número entre 1 e 5.')
            continue
