import criaConta
import pickle

class ContaCorrente:
    # Método construtor que inicializa os atributos do objeto
    def __init__(self, nome, numero, cpf, saldo, limite):
        self.__nome = nome
        self.__numero = numero
        self.__cpf = cpf
        self.__saldo = saldo
        self.__limite = limite  # Um valor que o banco te oferece

def consultar_extrato(conta):
    print(f"\n--- Cliente: {conta.nome} ---")
    print(f'Seu saldo disponivel é: R${conta.saldo}')


def efetuar_deposito(conta):
    valor_deposito = float(input('Digite o valor que deseja depositar: '))
    conta.deposito(valor_deposito)
    print(
        f'Depósito efetuado com sucesso. Seu novo saldo é: R${conta.saldo:.2f}')


def pode_sacar(conta):
    # Método que verifica se é possível realizar um saque
    disponivel = conta.saldo + conta.saldo


def efetuar_saque(conta):
    valor_saque = float(input('Digite o valor que deseja sacar: '))
    if conta.saldo >= valor_saque:
        resultado = conta.saldo - valor_saque
        print(f'Saque no valor de R${valor_saque} realizado. Seu novo saldo é: R${resultado:.2f}')
    else:
        print('Saldo insuficiente para realizar esse saque.')


def efetuar_transferencia(conta):
    valor_transferencia = float(input('Digite o valor da transferência: '))
    cpf_destino = input('Digite o CPF do destinatário: ')
    destinatario = busca_cliente_por_cpf(cpf_destino)
    if destinatario is None:
        print('CPF do destinatário não encontrado.')
    elif valor_transferencia > conta.saldo + conta.limite:
        print('Saldo insuficiente para realizar essa transferência.')
    else:
        conta.saldo -= valor_transferencia
        # destinatario.saldo += valor_transferencia
        print(f'Transferência no valor de R${valor_transferencia:.2f} realizada com sucesso.')


contas_correspondentes = []


def busca_cliente_por_cpf(autenticacao):
    with open('contas_correntes.pkl', 'rb') as f:
        contas_correntes_salvas = pickle.load(f)
    # Função que recebe um CPF e retorna a conta corrente correspondente
    contas_correspondentes = []
    # Função que recebe um CPF e retorna a conta corrente correspondente
    for conta in contas_correntes_salvas:
        if conta.cpf == autenticacao:
            contas_correspondentes.append(conta)
    return contas_correspondentes


def login():
    autenticacao = input('Informe o seu CPF: ')
    contas_correspondentes = busca_cliente_por_cpf(autenticacao)
    if not contas_correspondentes:
        print('Cliente não encontrado em nosso sistema')
        return None
    else:
        if len(contas_correspondentes) > 1:
            print('Mais de uma conta encontrada para o CPF informado, por favor entre em contato com o suporte.')
            return None
        conta = contas_correspondentes[0]
        print(f'Seja bem vindo, {conta.nome}!')
        return conta


def menu():
    print('****************** ')
    print('*   GAMER BANK   *')
    print('******************')
    print('Olá, bem vindo ao Gamer Bank!')
    print('Antes de continuar, você deve escolher uma das opções abaixo.')
    while True:
        opt = input('********************************\n'
                    '1 - Criar Conta\n'
                    '2 - Acessar sua conta\n'
                    '********************************\n')
        opt = int(opt)
        if opt == 1:
            criaConta.criar_conta()
        elif opt == 2:
            conta = login()
            if conta is None:
                print('Não foi possível fazer login. Tente novamente.')
                continue
            else:
                option_conta = int(input('********************************\n'
                                         '1 - Consultar seu extrato\n'
                                         '2 - Efetuar um deposito\n'
                                         '3 - Efetuar um saque\n'
                                         '4 - Fazer uma transferencia pix\n'
                                         '5 - Sair\n'
                                         '********************************\n'))
                option_conta = int(option_conta)
                if option_conta == 1:
                    consultar_extrato(conta)
                elif option_conta == 2:
                    efetuar_deposito(conta)
                elif option_conta == 3:
                    efetuar_saque(conta)
                    print('Obrigado por usar o Gamer Bank!')
                    break
                elif option_conta == 4:
                    efetuar_transferencia(conta)
                elif option_conta == 5:
                    break
                elif option_conta not in [5, 4, 3, 2, 1]:
                    print('invalido.')
                    continue
