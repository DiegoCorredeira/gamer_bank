"""
Proximos passos:
- Retornar CPF formatado
- Adicionar sistema de data no extrato
- Criar conta poupança onde rende um valor a cada x tempo
- Utilizar o dot env para algo só para praticar
- Adicionar mais clientes
"""
import clientes


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

    def transferencia_pix(self, valorx, destino_cpf):
        for titular in clientes.titulares.values():
            if titular['cpf'] == destino_cpf:
                destinatario = titular['nome']
                break
        else:
            return 'Destinatário não encontrado'

        if self.pode_sacar(valorx):
            self.saque(valorx)
            destino = None
            for conta in clientes.contas:
                if conta._ContaCorrente__cpf == destino_cpf:
                    destino = conta
                    break
            if destino:
                destino.deposito(valorx)
                return f'Você fez uma transferencia pix no valor de R${valorx} para {destinatario}'
            else:
                return 'Erro ao localizar a conta do destinatário'
        else:
            return 'Saldo insuficiente para realizar essa operação'


def busca_cliente_por_cpf(autenticacao):
    for conta in clientes.contas_correntes:
        if conta._ContaCorrente__cpf == autenticacao:
            return conta
    return None
