import moeda as m

n = float(input('Digite um valor: '))
print(f'Metade do valor: {m.metade(n, True)}')
print(f'Dobro do valor: {m.dobro(n, True)}')
print(f'Valor diminuido (10%): {m.diminuir(n, True)}')
print(f'Valor aumentado (10%): {m.aumentar(n, True)}')