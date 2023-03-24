class ContaCorrente:

    def __init__(self, nome, numero, cpf, saldo, limite):
        self.nome = nome
        self.numero = numero
        self.cpf = cpf
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'Seu saldo disponivel é: R${self.saldo}')

    def deposito(self, valorx):
        self.saldo += valorx

    def pode_sacar(self, valor_saque):
        disponivel = self.saldo + self.limite
        return valor_saque <= disponivel

    def saque(self, valorx):
        if self.pode_sacar(valorx):
            self.saldo -= valorx
            print(f'vocÊ sacou R${valorx}')
        else:
            print('valor indisponivel')


cliente = ContaCorrente('Gabriel', 12345, 1111111111, 5000, 3000)
print(cliente.saque(9000))
