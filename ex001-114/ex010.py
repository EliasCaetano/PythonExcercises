# Assumimos que R$ 6,00 = U$ 1,00
saldors = float(input("Digite seu saldo atual em real: R$ "))
saldoeur = saldors/6
print('Considerando o atual valor do Euro, com seu saldo atual de R$ {} é possível comprar EUR {}'.format(saldors,saldoeur))

