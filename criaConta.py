from random import randint
import pickle
class ContaCorrente:
    def __init__(self, nome, numero, cpf, saldo, limite=1000.0):
        self.nome = nome
        self.numero = numero
        self.cpf = cpf
        self.saldo = saldo
        self.limite = limite

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo + self.limite < valor:
            return False
        else:
            self.saldo -= valor
            return True


contas_correntes = []


def criar_conta():
    while True:
        nome = input('Nome: ')
        cpf = input('CPF: ')
        numero = randint(100000, 999999)
        saldo = float(input('Saldo: R$'))
        limite = float(input('Limite: R$'))

        conta = ContaCorrente(nome, numero, cpf, saldo, limite)
        contas_correntes.append(conta)

        opcao = input('Deseja criar outra conta? (s/n) ')
        if opcao.lower() != 's':
            break

    # salvar contas correntes em um arquivo
    with open('contas_correntes.pkl', 'wb') as f:
        pickle.dump(contas_correntes, f)

    # carregar contas correntes de um arquivo
    with open('contas_correntes.pkl', 'rb') as f:
        contas_correntes_salvas = pickle.load(f)

    # exibir contas correntes carregadas do arquivo
    for conta in contas_correntes_salvas:
        print(f"Nome: {conta.nome} | Número da Conta: {conta.numero}| CPF: {conta.cpf} | Saldo: R${conta.saldo:.2f} | Limite: R${conta.limite:.2f}")
