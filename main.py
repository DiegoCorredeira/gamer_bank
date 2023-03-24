# nome do titular, numero da conta, cpf, saldo, limite disponivel
#
# extrato, deposito, saque, transferencia - pix,


class ContaCorrente:
    def __init__(self, nome, numero, cpf, saldo, limite):  # Atributos do objeto
        self.__nome = nome
        self.__numero = numero
        self.__cpf = cpf
        self.__saldo = saldo
        self.__limite = limite  # Um valor que o banco te oferece

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def extrato(self):
        return f'Seu saldo disponivel é: R${self.__saldo}'

    def deposito(self, valorx):
        self.__saldo += valorx

    def pode_sacar(self, valor_saque):
        disponivel = self.__saldo + self.__limite
        return valor_saque <= disponivel  # Retorno booleano

    def saque(self, valorx):
        if self.pode_sacar(valorx):
            self.__saldo -= valorx
            return f'Você sacou R${valorx} e seu saldo atual é de R${self.__saldo}'
        else:
            return 'Valor indisponivel'

    def transferencia_pix(self, valorx, destino):
        if self.pode_sacar(valorx):
            self.saque(valorx)
            destino.deposito(valorx)
        else:
            return 'Seu saldo é insuficiente para realizar essa transação'
        return f'Você fez uma transferencia pix. {self.nome}'


cliente = ContaCorrente('Diego', 123456, 11111111111, 5000, 3000)
cliente2 = ContaCorrente('Felipe', 1234567, 1893739430, 900, 5000)

print(cliente.transferencia_pix(5000, cliente2))  # Transferindo para a conta2
print(cliente2.extrato())  # Extrato da conta2
print(cliente.extrato())  # Extrato da conta2
