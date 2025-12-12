import moeda as m

n = int(input('Digite um valor: '))
print(f'Valor com 10% acrescidos: {m.aumentar(n):8.2f}')
print(f'Valor com 10% descontados: {m.diminuir(n):8.2f}')
print(f'Metade do valor: {m.metade(n):8.2f}')
print(f'Dobro do valor: {m.dobro(n):8.2f}')
