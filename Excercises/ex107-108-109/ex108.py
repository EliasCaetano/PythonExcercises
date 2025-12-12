import moeda as m

n = float(input('Digite um valor: R$ '))
print(f'Valor da metade: {m.moeda(m.metade(n))}')
print(f'Valor do dobro: {m.moeda(m.dobro(n))}')
print(f'Valor diminuido (10%): {m.moeda(m.diminuir(n))}')
print(f'Valor aumentado (10%): {m.moeda(m.aumentar(n))}')
