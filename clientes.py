from main import ContaCorrente

titulares_correntistas = {
    'Diego Corredeira': {'nome': 'Diego Corredeira', 'numero': 13221335, 'cpf': '91506736025', 'saldo': 5000,
                         'limite': 300},
    'Gabriel Felipe': {'nome': 'Gabriel Felipe', 'numero': 2697688, 'cpf': '70591397021', 'saldo': 5000, 'limite': 300},
    'Konos Adriano': {'nome': 'Konos Adriano', 'numero': 657655, 'cpf': '91143545001', 'saldo': 500, 'limite': 100}
}
contas_correntes = []
# iterando pelos clientes
for titular in titulares_correntistas.values():
    conta = ContaCorrente(titular['nome'], titular['numero'], titular['cpf'], titular['saldo'],
                          titular['limite'])
    contas_correntes.append(conta)
