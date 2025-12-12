print('Números pares que estão no intervalo entre 1 e 50')
for i in range(1,51,1):
    if i % 2 == 0:
        if i == 50:
            print(i, end='.')
        else:
            print(i, end=', ')
