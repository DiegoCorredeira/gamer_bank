"""
Proximos passos:
- Fazer busca sobre o cliente pelo CPF
- Fazer busca pelo cliente pelo número da conta
- Retornar CPF formatado
- Adicionar sistema de data no extrato
- Criar conta poupança onde rende um valor a cada x tempo
- Utilizar o dot env para algo só para praticar
- Criar sistema de senha da conta
- Menu interativo para acesso

"""


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

    def transferencia_pix(self, valorx, destino, nome):
        if self.pode_sacar(valorx):
            self.saque(valorx)
            destino.deposito(valorx)
            destino = nome
            return f'Você fez uma transferencia pix no valor de R${valorx} para {destino}'
        else:
            return 'Seu saldo é insuficiente para realizar essa transação'
