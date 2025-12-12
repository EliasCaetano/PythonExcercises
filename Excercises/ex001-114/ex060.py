while True:
    try:
        n = int(input('Digite um número para ver seu fatorial: '))
    except ValueError:
        print('Insira um valor válido!')
        continue

    fat = 1

    for i in range(1, n+1):
        fat *= i
        print(f'{i} X {n}')

    print(f'O fatorial de {n} é {fat}')
    break