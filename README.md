# Gamer Bank


A classe ContaCorrente é responsável por gerenciar as informações e operações de uma conta corrente em um banco.<br>
# Atributos: <br>
nome: string que representa o nome do titular da conta. <br>
numero: int que representa o número da conta. <br>
cpf: int que representa o CPF do titular da conta.<br>
saldo: float que representa o saldo atual da conta.<br>
limite: float que representa o limite de crédito disponível na conta.

# Métodos
  - __ init __(self, nome, numero, cpf, saldo, limite): construtor da classe, que recebe os valores iniciais dos atributos da conta.
  - extrato(self) -> str: método que retorna uma string contendo o saldo disponível na conta.
  - deposito(self, valorx): método que recebe um valor em float e realiza o depósito na conta, atualizando o saldo.
  - pode_sacar(self, valor_saque) -> bool: método que recebe um valor em float e verifica se é possível realizar o saque com base no saldo e no limite disponíveis na conta.
  - saque(self, valorx) -> str: método que recebe um valor em float e realiza o saque na conta, atualizando o saldo. Retorna uma string informando se a operação foi realizada com sucesso ou se o valor solicitado é maior que o limite disponível na conta.
  - transferencia_pix(self, valorx, destino, nome) -> str: método que recebe um valor em float, uma conta de destino e um nome de destinatário e realiza uma transferência via Pix entre as contas. Verifica se é possível realizar a transação e atualiza os saldos das contas envolvidas. Retorna uma string informando se a operação foi realizada com sucesso ou se o valor solicitado é maior que o limite disponível na conta.

# Próximos Passos
 - Fazer busca sobre o cliente pelo CPF: implementar um método que busque e retorne informações sobre um cliente a partir do seu CPF.
 - Fazer busca pelo cliente pelo número da conta: implementar um método que busque e retorne informações sobre um cliente a partir do número da sua conta.
 - Retornar CPF formatado: implementar um método que formate o CPF do cliente com pontos e traços.
 - Adicionar sistema de data no extrato: adicionar informações de data e hora nas operações de depósito, saque e transferência.
 - Criar conta poupança onde rende um valor a cada x tempo: implementar uma nova classe de conta que rende juros e atualiza o saldo periodicamente.
 - Utilizar o dotenv: usar a biblioteca dotenv para armazenar informações sensíveis, como senhas e chaves de acesso, em variáveis de ambiente.
 - Criar sistema de senha da conta: adicionar um sistema de senha para acessar a conta.
 - Menu interativo para acesso: criar um menu interativo que permita ao usuário realizar as operações disponíveis na conta.
    
# Repositório em manutenção

Este repositório está em manutenção e será atualizado em breve. Pedimos desculpas pelo transtorno e agradecemos pela compreensão.
