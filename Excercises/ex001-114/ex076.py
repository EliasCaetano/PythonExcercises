produtos = ('Caneta', 1.50, 'Lápis', 1, 'Caderno', 5.75, 'Livro', 9.99)

print('-' * 30)
print('LISTA DE PRODUTOS'.center(30))
print('-' * 30)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<23}', end='')
    else:
        print(f'R${produtos[pos]:>5.2f}')