while True:
    try:
        n = int(input('Digite um número para ver sua tabuada (nº negativo para encerrar): '))
    except ValueError:
        print('Insira um número válido!')
        continue

    if n < 0:
        break

    for i in range(1, 11):
        print(f'{i} X {n} = {i * n}')