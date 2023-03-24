import clientes
from main import ContaCorrente

print(clientes.cliente.transferencia_pix(500, clientes.cliente2,
                                         clientes.cliente2.nome))  # Transferindo para a Conta do Felipe
print(clientes.cliente.extrato())  # Mostrando o saldo
print(clientes.cliente.saque(450))  # Sacando 450
print(clientes.cliente.extrato())  # Mostrando o saldo
